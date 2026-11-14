"""Genera informe.html: el mismo informe en un solo archivo que se abre con doble clic (sin Python)."""
from pathlib import Path

from comun import LienzoHTML
from informe import construir

L = LienzoHTML()
construir(L)
salida = Path(__file__).resolve().parent / "informe.html"
salida.write_text(L.documento("Siniestralidad vial en Bogotá"), encoding="utf-8")
print("ok", salida, round(salida.stat().st_size / 1e6, 1), "MB")
