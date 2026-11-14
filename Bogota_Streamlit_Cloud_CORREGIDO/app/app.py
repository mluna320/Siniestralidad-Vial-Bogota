"""Informe: siniestralidad vial en Bogotá 2015-2025 (Streamlit).

Ejecutar:  streamlit run app.py
El contenido está en informe.py; exportar_html.py genera la misma versión como informe.html.
"""
import streamlit as st

from comun import CSS, CSS_NARRATIVA, LienzoStreamlit
from informe import cargar, construir

st.set_page_config(page_title="Siniestralidad vial en Bogotá", page_icon="📊", layout="wide", initial_sidebar_state="collapsed")
st.markdown(CSS + CSS_NARRATIVA, unsafe_allow_html=True)
construir(LienzoStreamlit(), st.cache_data(cargar)())
