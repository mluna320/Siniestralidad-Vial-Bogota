"""Prueba ejecutable sin Streamlit (requiere pandas/numpy/plotly)."""
from pathlib import Path
import sys
from plotly.graph_objs import Figure

sys.path.insert(0, str(Path(__file__).resolve().parent / 'app'))
from informe import cargar, construir

class LienzoPrueba:
    def __init__(self): self.figuras=[]
    def html(self, s): assert isinstance(s,str)
    def fig(self, f, config=None):
        assert isinstance(f, Figure)
        f.to_plotly_json()
        self.figuras.append(f)
    def fila(self, izq, der, proporcion=(7,5)):
        for e in izq+der:
            if isinstance(e, str): self.html(e)
            else: self.fig(e)
    def cerrar(self): pass

v, serie = cargar()
assert not v.empty and not serie.empty, 'Datos vacíos'
assert {'anio','estado','hora','actor','localidad'} <= set(v.columns)
assert {'anio','siniestros_con_victimas'} <= set(serie.columns)
assert serie.anio.min() == 2015 and serie.anio.max() == 2025
lienzo = LienzoPrueba()
construir(lienzo,(v,serie))
assert len(lienzo.figuras) == 6, f'Esperados 6 gráficos, encontrados {len(lienzo.figuras)}'
print('OK: datos leídos, 6 figuras Plotly construidas y serializadas.')
