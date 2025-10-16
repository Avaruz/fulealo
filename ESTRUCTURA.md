# Estructura del Proyecto - FuleAlo

## 📁 Archivos y Directorios

```
fulealo/
├── scrapper.py                    # Script principal
├── config_ubicaciones.py          # ⚠️ PRIVADO: Tus ubicaciones personales (no en git)
├── config_ubicaciones.example.py  # 📋 Plantilla: Ejemplo de configuración
├── requirements.txt               # 📦 Dependencias del proyecto
├── .gitignore                     # 🚫 Archivos ignorados por Git
├── README.md                      # 📖 Documentación principal
├── GUIA_RAPIDA.md                 # 📖 Guía rápida de uso
├── ESTRUCTURA.md                  # 📖 Este archivo
└── .venv/                         # 🐍 Entorno virtual (local, no en git)
```

## 📄 Descripción de Archivos

### `scrapper.py` (Principal)
- Script principal del proyecto
- Importa ubicaciones desde `config_ubicaciones.py`
- Ejecuta el scraping de gasolineras

**Uso:**
```bash
python scrapper.py --geoloc_name cedis --max_distancia 5
```

### `config_ubicaciones.py` (Privado)
- ⚠️ **NO se sube a Git** (está en `.gitignore`)
- Contiene tus ubicaciones personales
- Cada usuario configura el suyo

**Cómo crear:**
```bash
cp config_ubicaciones.example.py config_ubicaciones.py
```

**Ejemplo:**
```python
UBICACIONES = {
    'cedis': [-17.672590, -63.147228],
    'moldes': [-17.7892227, -63.1876608],
    'casa': [-17.707494, -63.184554],
    'centro': [-17.783327, -63.182140]
}
```

### `config_ubicaciones.example.py` (Plantilla)
- 📋 Ejemplo de cómo configurar ubicaciones
- Se sube a Git para que otros vean el formato
- Los usuarios crean su `config_ubicaciones.py` basándose en esto

### `requirements.txt`
- 📦 Lista de dependencias del proyecto
- Instalación: `pip install -r requirements.txt`

**Contenido:**
```
playwright==1.48.2
beautifulsoup4==4.12.3
requests==2.32.5
```

### `.gitignore`
- 🚫 Especifica qué archivos ignorar en Git
- Incluye:
  - `config_ubicaciones.py` (privado)
  - `__pycache__/` (compilados)
  - `.venv/` (entorno virtual)
  - Archivos temporales de debug

### Documentación

#### `README.md`
- 📖 Documentación principal y completa
- Instalación, uso, ejemplos, configuración

#### `GUIA_RAPIDA.md`
- ⚡ Guía de referencia rápida
- Ejemplos de comandos más usados

#### `ESTRUCTURA.md`
- 📋 Este archivo: explicación de la estructura

## 🔐 Privacidad y Seguridad

### ¿Por qué `config_ubicaciones.py` es privado?

1. **Protege tus direcciones:** No compartes ubicaciones personales en Git
2. **Seguridad:** Cada usuario tiene sus propias coordenadas
3. **Privacidad:** Solo tu máquina local ve el archivo

### Flujo de Trabajo

```
Usuario 1 (GitHub)
├── clone repositorio
├── cp config_ubicaciones.example.py → config_ubicaciones.py
├── edita con sus ubicaciones
└── usa el script (sin subir direcciones)

Usuario 2 (GitHub)  
├── clone repositorio
├── cp config_ubicaciones.example.py → config_ubicaciones.py
├── edita con sus ubicaciones
└── usa el script (sin subir direcciones)

GitHub (Repositorio Público)
├── scrapper.py ✅
├── config_ubicaciones.example.py ✅
├── config_ubicaciones.py ❌ (IGNORADO)
└── ...
```

## 🚀 Primeros Pasos

### 1. Instalación Inicial
```bash
# Clonar
git clone <repo>
cd fulealo

# Entorno virtual
python -m venv venv
source venv/Scripts/activate

# Dependencias
pip install -r requirements.txt
playwright install chromium
```

### 2. Configurar Ubicaciones
```bash
cp config_ubicaciones.example.py config_ubicaciones.py
# Editar config_ubicaciones.py con tus ubicaciones
```

### 3. Usar el Script
```bash
python scrapper.py --geoloc_name cedis --max_distancia 10
```

## 📝 Agregar Ubicaciones Nuevas

1. Abre `config_ubicaciones.py`
2. Obtén coordenadas de Google Maps (click derecho)
3. Agrega una nueva entrada:

```python
UBICACIONES = {
    'cedis': [-17.672590, -63.147228],
    'moldes': [-17.7892227, -63.1876608],
    'trabajo': [-17.750000, -63.190000],  # ← Nueva ubicación
}
```

4. Guarda y usa: `python scrapper.py --geoloc_name trabajo`

## 🔄 Ciclo de Vida del Archivo

```
config_ubicaciones.example.py (en Git)
           ↓
Copia local
           ↓
config_ubicaciones.py (NO en Git)
           ↓
Personalización con tus datos
           ↓
Uso exclusivo en tu máquina
```

## ✅ Checklist

- [ ] Cloné el repositorio
- [ ] Instalé las dependencias (`pip install -r requirements.txt`)
- [ ] Instalé Playwright (`playwright install chromium`)
- [ ] Copié `config_ubicaciones.example.py` a `config_ubicaciones.py`
- [ ] Personalicé mis ubicaciones
- [ ] Probé el script (`python scrapper.py --help`)

¡Listo para usar! 🎉
