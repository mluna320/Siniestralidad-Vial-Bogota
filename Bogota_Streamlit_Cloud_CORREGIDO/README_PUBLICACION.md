# Siniestralidad vial de Bogotá (2015–2025) · Streamlit Cloud

## Qué causó el error
El traceback identificó `ModuleNotFoundError` durante la importación de `plotly.graph_objects` desde `app/informe.py`.
El ZIP anterior **sí** tenía `requirements.txt`, pero la aplicación fue publicada desde la ruta `Paquete_Bogota_2026_REPARADO/app/app.py` dentro del repositorio; Streamlit busca las dependencias **junto al archivo principal o en la raíz del repositorio**. El `requirements.txt` estaba en `Paquete_Bogota_2026_REPARADO/`, que no coincide con ninguno de esos dos lugares.

## Opción recomendada: cargar este paquete como raíz del repositorio
1. Descomprimir `Bogota_Streamlit_Cloud_CORREGIDO.zip`.
2. En GitHub, subir **los archivos que están dentro de la carpeta**, no la carpeta contenedora. La raíz del repositorio debe mostrar `streamlit_app.py`, `requirements.txt`, `app/`, `.streamlit/`.
3. En Streamlit Community Cloud seleccionar ese repositorio, rama correspondiente y archivo principal **`streamlit_app.py`** (también funciona `app/app.py`).
4. Elegir Python **3.12 o 3.13** si la configuración de despliegue lo solicita.
5. Volver a desplegar. Si ya había un despliegue, hacer commit/push de los cambios; si persiste el error tras actualizar dependencias, reiniciar la app desde Manage app.

## Opción sin reorganizar el repositorio actual
Si tu GitHub tiene el proyecto dentro de la carpeta `Paquete_Bogota_2026_REPARADO/`, **no hace falta moverlo**:
1. Copia `requirements.txt` de este paquete a `Paquete_Bogota_2026_REPARADO/app/requirements.txt` en el repositorio (al lado de `app.py`).
2. Se recomienda copiar también `.streamlit/config.toml` a `Paquete_Bogota_2026_REPARADO/app/.streamlit/config.toml` para preservar el tema en la ruta anidada.
3. Asegúrate de conservar los CSV en `Paquete_Bogota_2026_REPARADO/app/datos/`.
4. Mantén como archivo principal **`Paquete_Bogota_2026_REPARADO/app/app.py`**.
5. Haz commit/push y reinicia la app si el despliegue no se actualiza.

## Estructura esperada
```
repo/
├── streamlit_app.py                 # punto de entrada recomendado
├── requirements.txt                # dependencias si app queda en raíz
├── .streamlit/config.toml          # tema de colores
├── app/
│   ├── app.py                      # punto de entrada original
│   ├── requirements.txt            # dependencias junto al app.py
│   ├── .streamlit/config.toml      # mismo tema al desplegar app/app.py
│   ├── comun.py
│   ├── informe.py
│   ├── exportar_html.py
│   └── datos/
│       ├── siniestros_con_victimas_anual.csv
│       └── victimas_anuario.csv.gz
└── Informe_Bogota_2015_2025.html   # alternativa offline
```

## Inicio local
```bash
python -m pip install -r requirements.txt
python -m streamlit run streamlit_app.py
```
En Windows también se puede usar `ABRIR_STREAMLIT.bat`.

## Integridad
- Los archivos de datos, los cálculos, los gráficos y los colores del informe permanecen sin modificar respecto al ZIP anterior.
- Se añadieron los manifiestos de dependencias en las ubicaciones correctas, un punto de entrada alternativo, y la configuración de tema junto al punto de entrada anidado.
- Las comprobaciones automatizadas de sintaxis, lectura de datos y construcción de las seis figuras se ejecutaron localmente con los paquetes de análisis disponibles.
- No se pudo ejecutar aquí un servidor real Streamlit (la dependencia Streamlit no está instalada en este entorno y la instalación de paquetes externa está restringida). El funcionamiento final en Streamlit Community Cloud debe comprobarse tras el commit.
