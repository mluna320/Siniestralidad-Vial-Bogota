"""Informe narrativo que COMPLEMENTA el Power BI de siniestralidad vial de Bogotá.

Fuente primaria: las mismas bases oficiales de Anuarios que alimentan el tablero:
 - siniestros.csv.gz (Power BI) -> siniestros_con_victimas_anual.csv (agregado verificable)
 - actor_vial.csv.gz (Power BI) -> victimas_anuario.csv.gz (registro depurado del informe anterior)
No se incluyen datos simulados. La mortalidad se define a 30 días.
"""
from pathlib import Path
import pandas as pd
import plotly.graph_objects as go
from comun import (ACENTO, NAVY, NAVY2, GRIS1, GRIS2, SUAVE, TEXTO, estilo,
                   h_barra, h_lamina, h_graf_titulo, h_panel, h_resumen)

D = Path(__file__).resolve().parent / 'datos'
FUENTE = 'Fuente: Anuarios de Siniestralidad Vial 2024 y 2025 · Secretaría Distrital de Movilidad · fallecimiento a 30 días.'
ANIOS = list(range(2015, 2026))
FRANJAS = ['Madrugada (0–5 h)', 'Mañana (6–11 h)', 'Tarde (12–17 h)', 'Noche (18–23 h)']


def es(n, dec=0):
    return f'{n:,.{dec}f}'.replace(',', 'X').replace('.', ',').replace('X', '.')


def pc(n, dec=1):
    return f'{n * 100:.{dec}f}'.replace('.', ',') + '%'


def pp(a, b):
    return f'{(a-b)*100:+.1f}'.replace('.', ',') + ' pp'


def cargar():
    v = pd.read_csv(D / 'victimas_anuario.csv.gz', parse_dates=['fecha'])
    annual = pd.read_csv(D / 'siniestros_con_victimas_anual.csv')
    v['franja'] = pd.cut(v.hora, [-1, 5, 11, 17, 23], labels=FRANJAS)
    v['noche'] = (v.hora <= 5) | (v.hora >= 18)
    return v, annual


def desc(t):
    return f'<div class="conector"><div><b>{t[0]}</b><p>{t[1]}</p></div></div>'



def base_linea(anios, values, nombre, color=NAVY, altura=385, highlight_year=2025, is_pct=False):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=anios, y=values, name=nombre, mode='lines+markers',
                             line=dict(color=color, width=3), marker=dict(size=8, color=color),
                             hovertemplate='%{x}: %{y:,.1f}' + ('%' if is_pct else '') + '<extra></extra>'))
    idx = list(anios).index(highlight_year)
    fig.add_trace(go.Scatter(x=[highlight_year], y=[list(values)[idx]], mode='markers', showlegend=False,
                             marker=dict(size=13, color=ACENTO, line=dict(color='white',width=2)), hoverinfo='skip'))
    fig.update_xaxes(dtick=1, tickangle=0, range=[2014.7, 2025.3])
    fig.update_yaxes(tickformat='.0f', rangemode='tozero')
    return estilo(fig, altura)


def construir(L, datos=None):
    v, san = cargar() if datos is None else datos
    años = ANIOS
    mu = v[v.estado == 'Fallecido'].copy()
    he = v[v.estado == 'Herido'].copy()
    fatal = mu.groupby('anio').size().reindex(años)
    heridos = he.groupby('anio').size().reindex(años)
    eventos = san.set_index('anio').siniestros_con_victimas.reindex(años)
    moto = mu[mu.actor == 'Motociclista'].groupby('anio').size().reindex(años, fill_value=0)
    peat = mu[mu.actor == 'Peatón'].groupby('anio').size().reindex(años, fill_value=0)
    motop = moto / fatal
    peatp = peat / fatal
    años_rec = (2021, 2025)
    rec = v[v.anio.between(*años_rec)]
    f_rec = rec[rec.estado == 'Fallecido']
    fr = pd.crosstab(rec.franja, rec.estado).reindex(FRANJAS)
    fr['pct'] = fr.Fallecido / fr.sum(axis=1) * 100
    noche = rec[rec.noche]
    dia = rec[~rec.noche]
    pn = (noche.estado == 'Fallecido').sum() / len(noche)
    pdia = (dia.estado == 'Fallecido').sum() / len(dia)
    muerte_noche = f_rec.noche.mean()
    mu_loc = f_rec[f_rec.localidad != 'Sin información'].localidad.value_counts()
    top5 = mu_loc.head(5).sum() / len(f_rec)
    m_rec = f_rec[f_rec.actor == 'Motociclista']
    cr_orden = m_rec.localidad.value_counts().head(10).index
    cr = pd.crosstab(m_rec.localidad, m_rec.franja).reindex(index=cr_orden, columns=FRANJAS, fill_value=0)
    maxcell = cr.stack().idxmax()
    maxvalue = int(cr.stack().max())
    tres = m_rec[m_rec.noche].localidad.value_counts().head(3)
    vari_ev = eventos.loc[2025] / eventos.loc[2024] - 1
    vari_fa = fatal.loc[2025] / fatal.loc[2024] - 1

    L.html(h_barra([('inicio','Inicio'), ('pregunta','El problema'), ('evolucion','Evolución'), ('actores','Actores'),
                    ('horas','Franjas'), ('localidades','Localidades'), ('cruce','Cruce'),
                    ('cierre','Cierre')]))

    # 00 Portada: abrir con una cifra y una distinción decisiva.
    L.html('<div id="inicio"></div>')
    L.html(f'<div class="hero2"><div>'
           '<div class="meta">Bogotá · Siniestralidad vial · 2015–2025</div>'
           '<h1>La siniestralidad vial no se entiende con una sola cifra.</h1>'
           '<div class="golpe">En 2025 disminuyeron los siniestros, pero las muertes apenas cambiaron.</div>'
           '</div><div class="gran">'
           f'<div class="num">{es(int(eventos.loc[2025]))}</div>'
           '<div class="txt">siniestros con víctimas registrados en 2025</div>'
           f'<div class="sub">Ese año fallecieron <b>{es(int(fatal.loc[2025]))} personas</b>. '
           'Un siniestro puede causar varias víctimas.</div>'
           '</div></div>')

    # 01 Contexto y pregunta analítica.
    L.html(h_lamina('pregunta','01 · Contexto y problemática',
                    'Una cifra global no muestra a quiénes afecta la siniestralidad.',
                    'En Bogotá, los siniestros viales con víctimas comprometen la vida y la integridad de las personas. '
                    'Comprenderlos exige distinguir la evolución de los hechos y su distribución entre grupos, horarios y localidades.'))
    L.html('<div class="obj-g"><small>La pregunta de fondo</small>'
           '<p>¿Cómo ha evolucionado la siniestralidad vial con víctimas en Bogotá entre 2015 y 2025, '
           'y qué patrones temporales, territoriales y por actor vial permiten identificar diferencias relevantes para su seguimiento?</p>'
           '</div>')

    # 02 Evolución: eventos y consecuencias mortales, sin igualarlos.
    L.html(h_lamina('evolucion','02 · Evolución temporal',
                    'La reducción de siniestros no fue equivalente a la de fallecimientos.',
                    f'Entre 2024 y 2025, los siniestros con víctimas disminuyeron {pc(abs(vari_ev))}; '
                    f'los fallecimientos, apenas {pc(abs(vari_fa))}.'))
    fig1 = base_linea(años, eventos.values, 'Siniestros con víctimas', NAVY, 375)
    fig1.data[0].customdata = [es(int(val)) for val in eventos.values]
    fig1.data[0].hovertemplate = '%{x}: %{customdata} siniestros con víctimas<extra></extra>'
    fig1.add_annotation(x=2020,y=eventos.loc[2020],text='2020 · mínimo de la serie',showarrow=True,
                        ax=8, ay=-52,arrowcolor=GRIS1,font=dict(color=SUAVE,size=11))
    L.fila([h_graf_titulo('Siniestros con personas heridas o fallecidas, por año',
                           'Cantidad de siniestros distintos · 2015–2025'),fig1,
            ],
           [h_panel([('El periodo completo',
                      f'De {es(int(eventos.loc[2015]))} siniestros en 2015 a {es(int(eventos.loc[2025]))} en 2025.'),
                     ('El contraste entre años',
                      f'En 2020 se registraron {es(int(eventos.loc[2020]))} eventos, frente a '
                      f'{es(int(eventos.loc[2024]))} en 2024.')],
                    titulo='Lo que revela la serie', acento=2)],(7,5))

    fig2=base_linea(años,fatal.values,'Fallecidos',ACENTO,370)
    fig2.update_traces(hovertemplate='%{x}: %{y:,.0f} fallecidos<extra></extra>',selector=dict(mode='lines+markers'))
    L.fila([h_graf_titulo('Personas fallecidas en siniestros viales, por año',
                           'Fallecidos a 30 días · una persona no equivale a un siniestro'),fig2,
            ],
           [h_panel([('Las muertes en perspectiva',
                      f'{es(int(fatal.loc[2015]))} personas fallecidas en 2015 y {es(int(fatal.loc[2025]))} en 2025.'),
                     ('Los lesionados también disminuyeron',
                      f'De {es(int(heridos.loc[2024]))} en 2024 a {es(int(heridos.loc[2025]))} en 2025.')],
                    titulo='Las consecuencias',acento=1)],(7,5))
    # 03 Usuarios viales: evolución de la participación de quienes fallecen.
    L.html(h_lamina('actores','03 · ¿Quiénes son las víctimas?',
                    'Los motociclistas pasaron a ser el grupo con más personas fallecidas.',
                    f'Su participación entre las muertes aumentó de {pc(motop.loc[2015])} a '
                    f'{pc(motop.loc[2025])} entre 2015 y 2025.'))
    fig3=go.Figure()
    for nombre, serie, color in [('Motociclistas',motop,NAVY),('Peatones',peatp,GRIS1)]:
        fig3.add_trace(go.Scatter(x=años,y=serie.values*100,name=nombre,mode='lines+markers',
                                 marker=dict(size=8),line=dict(color=color,width=3),
                                 customdata=[es(float(val),1) for val in serie.values * 100],
                                 hovertemplate=nombre + ' · %{x}: %{customdata}%<extra></extra>'))
    fig3.add_trace(go.Scatter(x=[2025],y=[motop.loc[2025]*100],mode='markers',showlegend=False,
                             marker=dict(color=ACENTO,size=14,line=dict(color='#FFFFFF',width=2)),hoverinfo='skip'))
    fig3.update_layout(legend=dict(orientation='h',x=0,y=1.13))
    fig3.update_xaxes(dtick=1)
    fig3.update_yaxes(rangemode='tozero', ticksuffix='%', range=[0,60])
    L.fila([h_graf_titulo('Composición de las personas fallecidas: motociclistas y peatones',
                           '% del total de fallecidos de cada año · las dos categorías principales'),
            estilo(fig3,410,leyenda=True),
            ],
           [h_panel([('Motociclistas',
                      f'De {es(int(moto.loc[2015]))} fallecidos en 2015 a {es(int(moto.loc[2025]))} en 2025.'),
                     ('Peatones',
                      f'De {es(int(peat.loc[2015]))} a {es(int(peat.loc[2025]))} muertes; '
                      f'su participación pasó de {pc(peatp.loc[2015])} a {pc(peatp.loc[2025])}.'),
                     ('Una diferencia importante',
                      'La participación entre fallecidos no mide el riesgo individual sin datos de exposición.')],
                    titulo='Cómo cambió el perfil',acento=1)],(7,5))
    # 04 Horario: comparar fallecidos por cada 100 víctimas registradas.
    L.html(h_lamina('horas','04 · ¿Cuándo ocurre?',
                    'La madrugada presenta la mayor proporción de fallecidos entre las víctimas registradas.',
                    f'Entre 2021 y 2025, el {pc(muerte_noche)} de las muertes ocurrió '
                    'entre las 18:00 y las 05:59.'))
    fig4=go.Figure(go.Bar(x=[f.replace(' (', '<br>(') for f in FRANJAS],y=fr.pct.values,
                          marker=dict(color=[ACENTO,NAVY2,NAVY2,ACENTO],line=dict(color='#FFFFFF',width=.6)),
                          text=[es(x,2) for x in fr.pct],textposition='outside',textfont=dict(color=TEXTO,size=13),
                          customdata=[[es(fr.loc[f, 'pct'],2), es(int(fr.loc[f, 'Fallecido'])),
                                       es(int(fr.loc[f, 'Herido']))] for f in FRANJAS],
                          hovertemplate='%{x}<br>%{customdata[0]} fallecidos por cada 100 víctimas<br>'
                                        '%{customdata[1]} fallecidos · %{customdata[2]} heridos<extra></extra>'))
    fig4.update_yaxes(range=[0,fr.pct.max()*1.30],showticklabels=True)
    fig4.update_xaxes(tickangle=0)
    L.fila([h_graf_titulo('Fallecidos por cada 100 víctimas, según franja horaria',
                           'Periodo 2021–2025 · naranja = 18:00 a 05:59 · azul = 06:00 a 17:59'),
            estilo(fig4,410),
            ],
           [h_panel([('La madrugada frente a la mañana',
                      f'{es(fr.loc[FRANJAS[0],"pct"],2)} frente a '
                      f'{es(fr.loc[FRANJAS[1],"pct"],2)} fallecidos por cada 100 víctimas.'),
                     ('La noche frente al día',
                      f'{es(pn*100,2)} frente a {es(pdia*100,2)} fallecidos por cada 100 víctimas.'),
                     ('Alcance del indicador',
                      'Compara la gravedad entre las víctimas registradas, no el riesgo por viaje ni sus causas.')],
                    titulo='Diferencias por horario',acento=1)],(7,5))
    # 05 Territorio: concentración de muertes, sin confundir conteos y tasas.
    L.html(h_lamina('localidades','05 · ¿Dónde ocurre?',
                    'Las muertes se concentran en un grupo de localidades.',
                    f'{", ".join(mu_loc.head(5).index[:-1])} y {mu_loc.head(5).index[-1]} '
                    f'reunieron {es(int(mu_loc.head(5).sum()))} de {es(int(len(f_rec)))} fallecimientos '
                    f'({pc(top5)}) durante 2021–2025.'))
    top = mu_loc.head(10).sort_values()
    fig5=go.Figure(go.Bar(y=top.index,x=top.values,orientation='h',
                          marker=dict(color=[ACENTO if l in mu_loc.head(5).index else GRIS2 for l in top.index]),
                          text=[es(x) for x in top.values],textposition='outside',
                          textfont=dict(color=TEXTO,size=12),cliponaxis=False,
                          hovertemplate='%{y}: %{x} fallecidos · 2021–2025<extra></extra>'))
    fig5.update_xaxes(range=[0,top.max()*1.21],tickformat=',d')
    fig5.update_yaxes(tickfont=dict(size=12,color=TEXTO))
    loc25=mu[mu.anio==2025].localidad.value_counts()
    L.fila([h_graf_titulo('Las diez localidades con más personas fallecidas',
                           'Conteos acumulados · 2021–2025 · naranja = cinco primeras'),
            estilo(fig5,440),
            ],
           [h_panel([('El patrón cambia según el año',
                      f'En 2025 encabezaron {loc25.index[0]} ({loc25.iloc[0]}) y '
                      f'{loc25.index[1]} ({loc25.iloc[1]}); en el acumulado 2021–2025 lidera {mu_loc.index[0]}.'),
                     ('Qué permiten concluir los conteos',
                      'Indican concentración de fallecimientos, pero no riesgo ajustado por circulación.')],
                    titulo='La distribución territorial',acento=1)],(7,5))
    # 06 Intersección: actores, localidades y horarios simultáneamente.
    L.html(h_lamina('cruce','06 · Las diferencias se combinan',
                    'Al cruzar actor vial, territorio y horario aparecen concentraciones específicas.',
                    f'En {maxcell[0]}, durante la {maxcell[1].lower()}, '
                    f'fallecieron {maxvalue} motociclistas entre 2021 y 2025.'))
    htitle=[x.replace(' (','<br>(') for x in FRANJAS]
    fig6=go.Figure(go.Heatmap(z=cr.values,x=htitle,y=cr.index,
                              colorscale=[[0,'#F4F6F9'],[.5,'#F2B880'],[1,ACENTO]],
                              zmin=0,zmax=maxvalue,showscale=False,xgap=3,ygap=3,
                              text=cr.values,texttemplate='%{text}',textfont=dict(color=NAVY,size=12),
                              hovertemplate='%{y}<br>%{x}: %{z} motociclistas fallecidos<extra></extra>'))
    fig6.update_xaxes(side='top',tickfont=dict(color=TEXTO,size=12))
    fig6.update_yaxes(autorange='reversed',tickfont=dict(color=TEXTO,size=12))
    L.fila([h_graf_titulo('Motociclistas fallecidos por localidad y franja horaria',
                           '2021–2025 · diez localidades principales · más naranja = mayor recuento'),
            estilo(fig6,500),
            ],
           [h_panel([('La noche entre motociclistas',
                      f'{es(int(m_rec.noche.sum()))} de {es(len(m_rec))} muertes de motociclistas '
                      f'ocurrieron de noche ({pc(m_rec.noche.mean())}).'),
                     ('Concentración por localidad',
                      f'En ese horario destacan {", ".join(tres.index)} por sus recuentos acumulados.')],
                    titulo='El patrón combinado',acento=1)],(7,5))

    # 07 Síntesis que interpreta sin volver a enumerar cifras.
    L.html(h_lamina('cierre','07 · Conclusiones',
                    'La evolución, los actores y el territorio revelan distintas dimensiones del problema.'))
    L.html(h_resumen([
      ('La mejora fue desigual',
       'De 2024 a 2025, los siniestros disminuyeron mucho más que los fallecimientos.'),
      ('Cambió el grupo más afectado',
       'Los motociclistas superaron a los peatones en número de muertes registradas.'),
      ('Las diferencias se superponen',
       'Horario y localidad permiten reconocer concentraciones de víctimas fatales entre motociclistas.')],
      titulo='Lo que muestran los datos',acento=3))
    L.html('<div class="report-foot"><b>Fuente y alcance.</b> '
           'Anuarios de Siniestralidad Vial 2024 y 2025, Secretaría Distrital de Movilidad. '
           'Serie anual 2015–2025; desagregaciones por actor, horario y localidad: 2021–2025. '
           'Fallecimientos a 30 días. Los conteos no están ajustados por exposición; '
           'los cambios de movilidad de 2020 afectan la comparación temporal.</div>')
    L.cerrar()
