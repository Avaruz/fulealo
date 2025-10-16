# Guía Rápida de Uso - Scrapper FuleAlo

## Formas de Uso

### 1. Modo Interactivo (con menú)
```bash
python scrapper.py
```
El script te mostrará un menú para elegir la ubicación.

### 2. Usando Ubicaciones Preconfiguradas

#### Cedis
```bash
python scrapper.py --geoloc_name cedis
```

#### Moldes
```bash
python scrapper.py --geoloc_name moldes
```

#### Casa
```bash
python scrapper.py --geoloc_name casa
```

#### Centro (Plaza 24 de Septiembre)
```bash
python scrapper.py --geoloc_name centro
```

### 3. Ubicación Personalizada (Custom)
```bash
python scrapper.py --geoloc_name custom --lat -17.783327 --lon -63.182140
```

### 4. Con Filtros

#### Filtrar por distancia (máximo 5 km)
```bash
python scrapper.py --geoloc_name cedis --max_distancia 5
```

#### Filtrar por saldo mínimo (mínimo 20%)
```bash
python scrapper.py --geoloc_name casa --min_saldo 20
```

#### Combinar ambos filtros
```bash
python scrapper.py --geoloc_name moldes --max_distancia 8 --min_saldo 15
```

### 5. Modo Silencioso
```bash
python scrapper.py --silencioso --max_distancia 10
```
Usa la ubicación "Centro" por defecto sin preguntar.

## Validaciones

❌ **Error si la ubicación no existe:**
```bash
python scrapper.py --geoloc_name invalida
# Error: 'invalida' no es una ubicación válida
# Ubicaciones disponibles: cedis, moldes, casa, centro, custom
```

❌ **Error si falta lat o lon con custom:**
```bash
python scrapper.py --geoloc_name custom --lat -17.783327
# Error: Para usar 'custom' debe proporcionar --lat y --lon
```

## Ubicaciones Configuradas

| Nombre | Latitud | Longitud |
|--------|---------|----------|
| Cedis  | -17.672590 | -63.147228 |
| Moldes | -17.7892227 | -63.1876608 |
| Casa   | -17.707494 | -63.184554 |
| Centro | -17.783327 | -63.182140 |

## Ejemplos Prácticos

### Buscar gasolineras cerca de Cedis con buen saldo
```bash
python scrapper.py --geoloc_name cedis --max_distancia 5 --min_saldo 30
```

### Buscar gasolineras cerca de Casa
```bash
python scrapper.py --geoloc_name casa --max_distancia 10
```

### Usar ubicación del aeropuerto (custom)
```bash
python scrapper.py --geoloc_name custom --lat -17.644444 --lon -63.135556 --max_distancia 15
```

## Ver Ayuda
```bash
python scrapper.py --help
```
