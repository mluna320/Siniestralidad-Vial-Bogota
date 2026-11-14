"""Punto de entrada alternativo para Streamlit Community Cloud.

En GitHub, seleccionar este archivo o app/app.py como main file.
Los dos llevan al mismo informe y datos.
"""
from pathlib import Path
import runpy
import sys

ROOT = Path(__file__).resolve().parent
APP_DIR = ROOT / "app"
sys.path.insert(0, str(APP_DIR))
runpy.run_path(str(APP_DIR / "app.py"), run_name="__main__")
