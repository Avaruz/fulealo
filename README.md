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
    'ubi1': [-17.2332, -63.2323],
    'ubi2': [-17.27892227, -63.1834442],
    'ubi13': [-17.70722494, -63.39993],
    'defecto': [-17.7833327, -63.182140]
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
  ubi1: -17.67259, -63.14337228
  ubi2: -17.7892227, -63.322323
  ubi3: -17.707494, -63.232323
  defecto: -17.783327, -63.1833214

¿Qué ubicación deseas usar?
  1. Ubi1
  2. Ubi2
  3. Ubi3
  4. Defecto
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
# Usar ubicación Ubi1
python scrapper.py --geoloc_name ubi1

# Usar ubicación Ubi3
python scrapper.py --geoloc_name ubi3

# Usar ubicación Ubi2
python scrapper.py --geoloc_name ubi2

# Usar ubicación Defecto
python scrapper.py --geoloc_name defecto
```

### Usando Coordenadas Personalizadas

Para usar coordenadas personalizadas, usa `--geoloc_name custom` junto con `--lat` y `--lon`:

```bash
python scrapper.py --geoloc_name custom --lat -17.783327 --lon -63.182140
```

### Filtrar por Distancia

Mostrar solo gasolineras a menos de 5 km desde Ubi1:

```bash
python scrapper.py --geoloc_name ubi1 --max_distancia 5
```

### Filtrar por Saldo Mínimo

```bash
Mostrar solo gasolineras con al menos 20% de saldo desde Ubi3:

```bash
python scrapper.py --geoloc_name ubi3 --min_saldo 20
```

### Combinando Filtros

Ubicación Custom + máximo 10 km + mínimo 15% de saldo:

```bash
python scrapper.py --geoloc_name custom --lat -17.672590 --lon -63.147228 --max_distancia 10 --min_saldo 15
```

Ubicación Ubi2 + máximo 8 km + mínimo 10% de saldo:

```bash
python scrapper.py --geoloc_name ubi2 --max_distancia 8 --min_saldo 10
```

## Ubicaciones Preconfiguradas

| Nombre | Latitud | Longitud | Descripción |
|--------|---------|----------|-------------|
| Ubi1  | -17.672590 | -63.14337228 | Zona Ubi1 |
| Ubi2 | -17.7892227 | -63.322323 | Zona Ubi2 |
| Ubi3   | -17.707494 | -63.232323 | Ubicación Ubi3 |
| Defecto | -17.783327 | -63.1833214 | Plaza 24 de Septiembre |

## Parámetros Disponibles

| Parámetro | Tipo | Descripción | Ejemplo |
|-----------|------|-------------|---------|
| `--geoloc_name` | string | Nombre de ubicación: ubi1, ubi2, ubi3, defecto, o custom | `--geoloc_name ubi1` |
| `--lat` | float | Latitud (solo si geoloc_name=custom) | `--lat -17.783327` |
| `--lon` | float | Longitud (solo si geoloc_name=custom) | `--lon -63.182140` |
| `--max_distancia` | float | Distancia máxima en kilómetros | `--max_distancia 5` |
| `--min_saldo` | float | Saldo mínimo de combustible en % | `--min_saldo 10` |
| `--silencioso` | flag | No preguntar, usar Defecto por defecto | `--silencioso` |

## Validaciones

El script valida automáticamente:
- ✅ El nombre de ubicación debe estar en: `ubi1`, `ubi2`, `ubi3`, `defecto`, o `custom`
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
