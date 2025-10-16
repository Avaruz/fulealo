from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time
import argparse
from config_ubicaciones import UBICACIONES

url = "https://fulealo.com/"

def seleccionar_ubicacion(geoloc_name=None, lat=None, lon=None):
    """Selecciona la ubicación ya sea de parámetros o preguntando al usuario"""
    
    # Si viene de parámetros de línea de comando
    if geoloc_name:
        geoloc_lower = geoloc_name.lower()
        
        # Validar que el nombre esté en las ubicaciones configuradas o sea 'custom'
        if geoloc_lower in UBICACIONES:
            coords = UBICACIONES[geoloc_lower]
            print(f"\n✓ Usando ubicación: {geoloc_lower.capitalize()}")
            return coords[0], coords[1]
        elif geoloc_lower == 'custom':
            if lat is None or lon is None:
                print("Error: Para usar 'custom' debe proporcionar --lat y --lon")
                print("Ejemplo: --geoloc_name custom --lat -17.783327 --lon -63.182140")
                exit(1)
            try:
                latitude = float(lat)
                longitude = float(lon)
                print(f"\n✓ Usando ubicación personalizada: {latitude}, {longitude}")
                return latitude, longitude
            except ValueError:
                print("Error: lat y lon deben ser números válidos")
                exit(1)
        else:
            print(f"Error: '{geoloc_name}' no es una ubicación válida")
            print(f"Ubicaciones disponibles: {', '.join(UBICACIONES.keys())}, custom")
            exit(1)
    
    # Modo interactivo
    print("\n=== UBICACIONES DISPONIBLES ===")
    for nombre_loc, coords in UBICACIONES.items():
        print(f"  {nombre_loc.capitalize()}: {coords[0]}, {coords[1]}")
    
    print("\n¿Qué ubicación deseas usar?")
    for i, nombre_loc in enumerate(UBICACIONES.keys(), 1):
        print(f"  {i}. {nombre_loc.capitalize()}")
    print(f"  {len(UBICACIONES)+1}. Custom (ingresar coordenadas personalizadas)")
    
    try:
        opcion = int(input("\nSelecciona una opción: "))
        
        if opcion <= len(UBICACIONES):
            nombre_ubicacion = list(UBICACIONES.keys())[opcion-1]
            coords = UBICACIONES[nombre_ubicacion]
            print(f"\n✓ Usando ubicación: {nombre_ubicacion.capitalize()}")
            return coords[0], coords[1]
        elif opcion == len(UBICACIONES) + 1:
            latitude = float(input("Ingresa la latitud: "))
            longitude = float(input("Ingresa la longitud: "))
            print(f"\n✓ Usando ubicación personalizada: {latitude}, {longitude}")
            return latitude, longitude
        else:
            print("Opción inválida")
            exit(1)
    except (ValueError, KeyboardInterrupt):
        print("\nOperación cancelada")
        exit(1)

# Configurar argumentos de línea de comando
parser = argparse.ArgumentParser(description='Scrapper de gasolineras FuleAlo')
parser.add_argument('--geoloc_name', type=str, help='Nombre de ubicación: cedis, moldes, casa, centro, o custom')
parser.add_argument('--lat', type=float, help='Latitud (solo si geoloc_name=custom)')
parser.add_argument('--lon', type=float, help='Longitud (solo si geoloc_name=custom)')
parser.add_argument('--max_distancia', type=float, help='Filtrar gasolineras hasta X kilómetros de distancia')
parser.add_argument('--min_saldo', type=float, help='Filtrar gasolineras con al menos X%% de saldo')
parser.add_argument('--silencioso', action='store_true', help='No preguntar, usar ubicación por defecto (centro)')

args = parser.parse_args()

# Seleccionar ubicación
if args.silencioso and not args.geoloc_name:
    LATITUDE, LONGITUDE = UBICACIONES['centro']
    print("Usando ubicación por defecto: Centro")
else:
    LATITUDE, LONGITUDE = seleccionar_ubicacion(args.geoloc_name, args.lat, args.lon)

# Usar Playwright para obtener el contenido renderizado
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    # Configurar contexto con geolocalización
    context = browser.new_context(
        geolocation={"latitude": LATITUDE, "longitude": LONGITUDE},
        permissions=["geolocation"]
    )
    page = context.new_page()
    page.goto(url)
    
    # Esperar a que el contenido inicial se cargue
    time.sleep(3)
    
    # Hacer scroll hacia abajo varias veces para cargar todo el contenido
    previous_height = 0
    for _ in range(10):  # Intentar hacer scroll 10 veces
        # Hacer scroll hasta el final de la página
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1)  # Esperar a que cargue el contenido
        
        # Verificar si llegamos al final (no hay más contenido nuevo)
        current_height = page.evaluate("document.body.scrollHeight")
        if current_height == previous_height:
            break
        previous_height = current_height
    
    # Obtener el HTML completo después de que JavaScript lo haya renderizado
    html_content = page.content()
    browser.close()

soup = BeautifulSoup(html_content, "html.parser")

# El patrón es: nombre de la estación, seguido por bloques con los saldos
results = []
blocks = soup.get_text(separator='\n').split('\n')

i = 0
while i < len(blocks):
    # Detectar el nombre de la gasolinera: termina con '- BioPetrol' o '- Genex' o ' - URBARI'
    if ('- BioPetrol' in blocks[i] or '- Genex' in blocks[i] or ' - URBARI' in blocks[i]):
        nombre = blocks[i].strip()
        i += 1
        saldos = {}
        distancia = None
        
        while i < len(blocks) and not blocks[i].strip().endswith('- BioPetrol') and not blocks[i].strip().endswith('- Genex') and not blocks[i].strip().endswith(' - URBARI'):
            # Buscar distancia (formato: "X.X Km" o "X Km")
            if 'Km' in blocks[i] or 'km' in blocks[i]:
                distancia = blocks[i].strip()
            # Buscar tipo y saldo
            elif 'ESPECIAL' in blocks[i]:
                saldo_especial = blocks[i-1].strip()
                saldos['ESPECIAL'] = saldo_especial
            elif 'PREMIUM' in blocks[i]:
                saldo_premium = blocks[i-1].strip()
                saldos['PREMIUM'] = saldo_premium
            i += 1
        
        results.append({
            'gasolinera': nombre, 
            'distancia': distancia,
            'saldos': saldos
        })
    else:
        i += 1

# Mostrar resultados
print(f"\n{'='*70}")
print(f"📍 Ubicación configurada: {LATITUDE}, {LONGITUDE}")
print(f"🔍 Filtros aplicados:")
if args.max_distancia:
    print(f"   - Distancia máxima: {args.max_distancia} km")
if args.min_saldo:
    print(f"   - Saldo mínimo: {args.min_saldo}%")
print(f"{'='*70}")

# Aplicar filtros
resultados_filtrados = []
for item in results:
    # Filtro de distancia
    if args.max_distancia and item['distancia']:
        try:
            distancia_num = float(item['distancia'].replace('Km', '').replace('km', '').strip())
            if distancia_num > args.max_distancia:
                continue
        except:
            pass
    
    # Filtro de saldo mínimo
    if args.min_saldo:
        tiene_saldo_suficiente = False
        for saldo_str in item['saldos'].values():
            try:
                saldo_num = float(saldo_str.replace('%', '').strip())
                if saldo_num >= args.min_saldo:
                    tiene_saldo_suficiente = True
                    break
            except:
                pass
        if not tiene_saldo_suficiente:
            continue
    
    resultados_filtrados.append(item)

print(f"\n📊 Total de gasolineras encontradas: {len(results)}")
print(f"✅ Gasolineras después de filtros: {len(resultados_filtrados)}\n")

if not resultados_filtrados:
    print("⚠️  No se encontraron gasolineras con los filtros especificados")
else:
    for item in resultados_filtrados:
        print(f"\n{'─'*70}")
        print(f"🏪 {item['gasolinera']}")
        if item['distancia']:
            print(f"   📍 Distancia: {item['distancia']}")
        for tipo, saldo in item['saldos'].items():
            # Colorear según el nivel de saldo
            try:
                saldo_num = float(saldo.replace('%', '').strip())
                if saldo_num == 0:
                    emoji = "⚫"  # Sin combustible
                elif saldo_num < 10:
                    emoji = "🔴"  # Bajo
                elif saldo_num < 30:
                    emoji = "🟡"  # Medio
                else:
                    emoji = "🟢"  # Alto
            except:
                emoji = "⛽"
            
            print(f"   {emoji} {tipo}: {saldo}")
    print(f"\n{'='*70}")
