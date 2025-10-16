# Guía para Nuevos Colaboradores 👋

## Primeros Pasos

### 1. Clonar el Repositorio
```bash
git clone <URL-del-repositorio>
cd fulealo
```

### 2. Configurar el Entorno

#### Windows (PowerShell)
```powershell
python -m venv venv
.\.venv\Scripts\Activate.ps1
```

#### Mac/Linux (Bash)
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
playwright install chromium
```

### 4. Configurar Ubicaciones Personales
```bash
cp config_ubicaciones.example.py config_ubicaciones.py
```

Abre `config_ubicaciones.py` y personaliza con tus ubicaciones:
```python
UBICACIONES = {
    'tu_ubicacion_1': [latitud, longitud],
    'tu_ubicacion_2': [latitud, longitud],
    # ...
}
```

## ⚠️ IMPORTANTE: No subas `config_ubicaciones.py`

El archivo `config_ubicaciones.py` está en `.gitignore` por razones de **seguridad y privacidad**.

✅ **Bien:** Personalizas el archivo localmente, Git no lo ve
❌ **Mal:** Subes archivos con tus direcciones personales

Git solo verá:
- `config_ubicaciones.example.py` (plantilla, seguro)
- No verá: `config_ubicaciones.py` (tus datos privados)

## Primeras Pruebas

### Probar el Script
```bash
python scrapper.py --help
```

### Usar una ubicación preconfigurada
```bash
python scrapper.py --geoloc_name <ubicacion> --max_distancia 10
```

### Ver todas las ubicaciones disponibles
```bash
python scrapper.py
```
Te mostrará un menú interactivo.

## Estructura del Proyecto

```
fulealo/
├── scrapper.py                 # Script principal
├── config_ubicaciones.py       # 🔐 Privado (tuyo, no en git)
├── config_ubicaciones.example.py # 📋 Público (ejemplo)
├── requirements.txt            # Dependencias
├── .gitignore                  # Archivos ignorados
├── README.md                   # Documentación
├── GUIA_RAPIDA.md             # Guía de referencia
└── ESTRUCTURA.md              # Explicación de archivos
```

## Flujo de Trabajo

### Crear una Rama para Cambios
```bash
git checkout -b mi-nueva-feature
```

### Hacer Cambios
Edita los archivos que necesites (excepto `config_ubicaciones.py`).

### Hacer Commit
```bash
git add .
git commit -m "Descripción de los cambios"
```

### Push y Pull Request
```bash
git push origin mi-nueva-feature
```

**Nota:** Git automáticamente ignorará `config_ubicaciones.py` 🔐

## Troubleshooting

### Error: "ModuleNotFoundError: No module named 'config_ubicaciones'"
**Solución:**
```bash
cp config_ubicaciones.example.py config_ubicaciones.py
```

### Error: "Playwright not found"
**Solución:**
```bash
playwright install chromium
```

### Error: "Module not found: beautifulsoup4"
**Solución:**
```bash
pip install -r requirements.txt
```

## Preguntas Comunes

### ¿Puedo cambiar mis ubicaciones?
✅ Sí, edita `config_ubicaciones.py` libremente. No se subirá a Git.

### ¿Debo compartir mis ubicaciones en Git?
❌ No. Están protegidas por `.gitignore`.

### ¿Cómo agrego nuevas ubicaciones?
1. Abre `config_ubicaciones.py`
2. Agrega una nueva entrada
3. Usa: `python scrapper.py --geoloc_name tu_nueva_ubicacion`

### ¿Puedo contribuir con nuevas características?
✅ Sí, crea un issue o pull request. Consulta con los mantenedores primero.

## Recursos Útiles

- 📖 [README.md](README.md) - Documentación completa
- ⚡ [GUIA_RAPIDA.md](GUIA_RAPIDA.md) - Ejemplos rápidos
- 📋 [ESTRUCTURA.md](ESTRUCTURA.md) - Explicación de archivos

## Contacto

Si tienes dudas, abre un issue en el repositorio.

¡Bienvenido! 🎉
