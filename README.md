# Scrapper FuleAlo 🚗⛽

Script para obtener información en tiempo real de disponibilidad de combustible en gasolineras de Santa Cruz, Bolivia.

## Características

- 🌍 Ubicaciones configurables
- 📍 Soporte para coordenadas personalizadas
- 📏 Filtro por distancia máxima
- ⛽ Filtro por saldo mínimo de combustible
- 🎨 Indicadores visuales de nivel de combustible
- 🔄 Actualización en tiempo real desde fulealo.com
- 🔐 Configuración privada (no incluida en git)

## Instalación

### 1. Clonar el repositorio
```bash
git clone <tu-repo>
cd fulealo
```

### 2. Crear entorno virtual
```bash
python -m venv venv
source venv/Scripts/activate  # En Windows
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
playwright install chromium
```

### 4. Configurar ubicaciones
Copia el archivo de ejemplo y personalízalo:
```bash
cp config_ubicaciones.example.py config_ubicaciones.py
```

Edita `config_ubicaciones.py` con tus ubicaciones:
```python
UBICACIONES = {
    'cedis': [-17.672590, -63.147228],
    'moldes': [-17.7892227, -63.1876608],
    'casa': [-17.707494, -63.184554],
    'centro': [-17.783327, -63.182140]
}
```

## Configuración

### Archivo `config_ubicaciones.py`
Este archivo contiene tus ubicaciones personalizadas y **NO se subirá a Git** (está en `.gitignore`).

**¿Por qué es privado?**
- 🔐 Protege tus direcciones personales
- 🚫 Evita que se compartan ubicaciones privadas en el repositorio
- ✅ Cada usuario puede tener sus propias ubicaciones

**Cómo configurar:**
1. Copia `config_ubicaciones.example.py` a `config_ubicaciones.py`
2. Abre `config_ubicaciones.py` y personaliza tus ubicaciones
3. El archivo es ignorado por Git, solo tu máquina lo puede ver

## Requisitos

```bash
pip install -r requirements.txt
```

## Uso

### Modo Interactivo (con menú)

```bash
python scrapper.py
```

Te preguntará qué ubicación deseas usar:
```
=== UBICACIONES DISPONIBLES ===
  Cedis: -17.67259, -63.147228
  Moldes: -17.7892227, -63.1876608
  Casa: -17.707494, -63.184554
  Centro: -17.783327, -63.18214

¿Qué ubicación deseas usar?
  1. Cedis
  2. Moldes
  3. Casa
  4. Centro
  5. Ingresar coordenadas personalizadas

Selecciona una opción:
```

### Modo Silencioso (sin preguntas)

Usa la ubicación "Centro" por defecto:

```bash
python scrapper.py --silencioso
```

### Usando Ubicaciones Preconfiguradas

```bash
# Usar ubicación Cedis
python scrapper.py --geoloc_name cedis

# Usar ubicación Casa
python scrapper.py --geoloc_name casa

# Usar ubicación Moldes
python scrapper.py --geoloc_name moldes

# Usar ubicación Centro
python scrapper.py --geoloc_name centro
```

### Usando Coordenadas Personalizadas

Para usar coordenadas personalizadas, usa `--geoloc_name custom` junto con `--lat` y `--lon`:

```bash
python scrapper.py --geoloc_name custom --lat -17.783327 --lon -63.182140
```

### Filtrar por Distancia

Mostrar solo gasolineras a menos de 5 km desde Cedis:

```bash
python scrapper.py --geoloc_name cedis --max_distancia 5
```

### Filtrar por Saldo Mínimo

Mostrar solo gasolineras con al menos 20% de saldo desde Casa:

```bash
python scrapper.py --geoloc_name casa --min_saldo 20
```

### Combinando Filtros

Ubicación Custom + máximo 10 km + mínimo 15% de saldo:

```bash
python scrapper.py --geoloc_name custom --lat -17.672590 --lon -63.147228 --max_distancia 10 --min_saldo 15
```

Ubicación Moldes + máximo 8 km + mínimo 10% de saldo:

```bash
python scrapper.py --geoloc_name moldes --max_distancia 8 --min_saldo 10
```

## Ubicaciones Preconfiguradas

| Nombre | Latitud | Longitud | Descripción |
|--------|---------|----------|-------------|
| Cedis  | -17.672590 | -63.147228 | Zona Cedis |
| Moldes | -17.7892227 | -63.1876608 | Zona Moldes |
| Casa   | -17.707494 | -63.184554 | Ubicación Casa |
| Centro | -17.783327 | -63.182140 | Plaza 24 de Septiembre |

## Parámetros Disponibles

| Parámetro | Tipo | Descripción | Ejemplo |
|-----------|------|-------------|---------|
| `--geoloc_name` | string | Nombre de ubicación: cedis, moldes, casa, centro, o custom | `--geoloc_name cedis` |
| `--lat` | float | Latitud (solo si geoloc_name=custom) | `--lat -17.783327` |
| `--lon` | float | Longitud (solo si geoloc_name=custom) | `--lon -63.182140` |
| `--max_distancia` | float | Distancia máxima en kilómetros | `--max_distancia 5` |
| `--min_saldo` | float | Saldo mínimo de combustible en % | `--min_saldo 10` |
| `--silencioso` | flag | No preguntar, usar Centro por defecto | `--silencioso` |

## Validaciones

El script valida automáticamente:
- ✅ El nombre de ubicación debe estar en: `cedis`, `moldes`, `casa`, `centro`, o `custom`
- ✅ Si usas `custom`, debes proporcionar `--lat` y `--lon`
- ✅ Los valores de lat/lon deben ser números válidos
- ✅ Muestra mensajes de error claros si algo está mal

## Indicadores de Nivel

- 🟢 **Verde**: 30% o más (buena disponibilidad)
- 🟡 **Amarillo**: 10% - 29% (disponibilidad media)
- 🔴 **Rojo**: 1% - 9% (disponibilidad baja)
- ⚫ **Negro**: 0% (sin combustible)

## Ejemplos de Salida

```
======================================================================
📍 Ubicación configurada: -17.783327, -63.18214
🔍 Filtros aplicados:
   - Distancia máxima: 5.0 km
   - Saldo mínimo: 10.0%
======================================================================

📊 Total de gasolineras encontradas: 30
✅ Gasolineras después de filtros: 8

──────────────────────────────────────────────────────────────────────
🏪 SUR CENTRAL - BioPetrol
   📍 Distancia: 1.9 Km
   🟡 ESPECIAL: 29 %
   ⚫ PREMIUM: 0 %

──────────────────────────────────────────────────────────────────────
🏪 GENEX II - Genex
   📍 Distancia: 1.9 Km
   🟢 ESPECIAL: 58 %
```

## Cómo Obtener Coordenadas

1. Abre Google Maps
2. Haz clic derecho en la ubicación deseada
3. Selecciona las coordenadas que aparecen (se copian automáticamente)
4. Formato: `-17.783327, -63.182140`

## Notas

- El script simula una ubicación para obtener distancias calculadas
- Los datos se obtienen en tiempo real de fulealo.com
- Las gasolineras están ordenadas por distancia (más cercanas primero)
- El proceso tarda ~10-15 segundos debido al renderizado de JavaScript

## Licencia

MIT
