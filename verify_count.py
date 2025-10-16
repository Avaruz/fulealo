from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time

url = "https://fulealo.com/"

# Usar Playwright para obtener el contenido renderizado
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(url)
    
    # Esperar a que el contenido inicial se cargue
    time.sleep(3)
    
    # Hacer scroll hacia abajo varias veces para cargar todo el contenido
    previous_height = 0
    for _ in range(10):
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1)
        current_height = page.evaluate("document.body.scrollHeight")
        if current_height == previous_height:
            break
        previous_height = current_height
    
    html_content = page.content()
    browser.close()

soup = BeautifulSoup(html_content, "html.parser")

# El patrón es: nombre de la estación, seguido por bloques con los saldos
results = []
blocks = soup.get_text(separator='\n').split('\n')

i = 0
while i < len(blocks):
    if ('- BioPetrol' in blocks[i] or '- Genex' in blocks[i] or ' - URBARI' in blocks[i]):
        nombre = blocks[i].strip()
        i += 1
        saldos = {}
        while i < len(blocks) and not blocks[i].strip().endswith('- BioPetrol') and not blocks[i].strip().endswith('- Genex') and not blocks[i].strip().endswith(' - URBARI'):
            if 'ESPECIAL' in blocks[i]:
                saldo_especial = blocks[i-1].strip()
                saldos['ESPECIAL'] = saldo_especial
            elif 'PREMIUM' in blocks[i]:
                saldo_premium = blocks[i-1].strip()
                saldos['PREMIUM'] = saldo_premium
            i += 1
        results.append({'gasolinera': nombre, 'saldos': saldos})
    else:
        i += 1

# Mostrar resultados con conteo
print(f"=== Total de gasolineras encontradas: {len(results)} ===\n")

biopetrol = [r for r in results if 'BioPetrol' in r['gasolinera']]
genex = [r for r in results if 'Genex' in r['gasolinera']]
urbari = [r for r in results if 'URBARI' in r['gasolinera']]

print(f"BioPetrol: {len(biopetrol)}")
print(f"Genex: {len(genex)}")
print(f"URBARI: {len(urbari)}")
print(f"\n{'='*50}\n")

for item in results:
    print(item['gasolinera'])
    for tipo, saldo in item['saldos'].items():
        print(f"  {tipo}: {saldo}")
