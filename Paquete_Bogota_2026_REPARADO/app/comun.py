"""Sistema visual del informe ejecutivo (estilo consultoría): láminas a todo el ancho, título de acción,
gráfico a la izquierda y panel de hallazgos numerados a la derecha. Riel de navegación fijo a la izquierda.
"""

NAVY, NAVY2 = "#16213A", "#24314F"
ACENTO = "#E8772E"       # mismo naranja del dashboard: foco analítico, no categoría decorativa
TEXTO, SUAVE, TENUE = "#1D2939", "#667085", "#98A2B3"
GRIS1, GRIS2, GRIS3 = "#8C9BB0", "#C5CDD8", "#E4E7EC"
BORDE = "#E4E7EC"
VERDE = "#079455"
CFG = {"displayModeBar": False, "responsive": True}

CSS = """
<style>

html, body, [class*="css"], .stMarkdown, .stMarkdown p, button, input, select, td, th {font-family:'Segoe UI', sans-serif !important;}
.accion, .portada h1, .panel .ph, .item b, .stat .v, .stat b, .cifra .v, .reco b, .cierre b, .barra .marca, .resumen .t, .resumen h3 {
  font-family:'Segoe UI', sans-serif !important;}
section[data-testid="stSidebar"], [data-testid="stSidebarCollapsedControl"], [data-testid="collapsedControl"] {display:none !important;}
header[data-testid="stHeader"] {display:none;}
.stApp {background:#FFFFFF;}
html, [data-testid="stMain"], [data-testid="stAppViewContainer"], .main {scroll-behavior:smooth;}
.block-container {max-width:100% !important; padding:4.6rem clamp(1.2rem, 5vw, 6rem) 5rem clamp(1.2rem, 5vw, 6rem) !important;}

/* barra superior fija: secciones con nombre + progreso de lectura */
.barra {position:fixed; top:0; left:0; right:0; height:56px; z-index:999; display:flex; align-items:center; gap:1.6rem;
        padding:0 clamp(1.2rem, 5vw, 6rem); background:rgba(255,255,255,.88); backdrop-filter:blur(10px);
        -webkit-backdrop-filter:blur(10px); border-bottom:1px solid #EEF0F3;}
.barra .marca {font-weight:700; font-size:.92rem; color:#16213A; white-space:nowrap;}
.barra .marca span {color:#E8772E;}
.barra nav {display:flex; gap:.2rem; margin-left:auto; overflow-x:auto; scrollbar-width:none;}
.barra nav a {color:#667085 !important; text-decoration:none !important; font-size:.82rem; font-weight:600; padding:.4rem .7rem;
              border-radius:999px; white-space:nowrap; transition:background .2s, color .2s;}
.barra nav a:hover {background:#FFF1E6; color:#C4561A !important;}
.progreso {position:fixed; top:56px; left:0; right:0; height:3px; z-index:999; background:#E8772E; transform-origin:0 50%;
           transform:scaleX(0); transition:transform .12s linear;}

/* transiciones al bajar: el script de efectos() marca cada bloque con .rv y le agrega .visto al entrar en pantalla.
   Sin script, nada queda oculto. */
.rv {opacity:0; transform:translateY(42px); transition:opacity .9s cubic-bezier(.2,.7,.2,1), transform .9s cubic-bezier(.2,.7,.2,1);}
.rv.izq {transform:translateX(-46px);}
.rv.der {transform:translateX(46px);}
.rv.visto {opacity:1; transform:none;}
@keyframes subir {from {opacity:0; transform:translateY(24px);} to {opacity:1; transform:none;}}
.portada > * {animation:subir .9s cubic-bezier(.2,.7,.2,1) both;}
.portada .meta {animation-delay:.05s;} .portada h1 {animation-delay:.15s;} .portada .preg {animation-delay:.3s;} .portada .cifras {animation-delay:.45s;}
.stat, .reco > div, .panel {transition:transform .25s ease, box-shadow .25s ease;}
.stat:hover, .reco > div:hover {transform:translateY(-4px); box-shadow:0 14px 30px rgba(15,35,65,.10);}

/* lámina */
.lamina {margin-top:clamp(3.5rem, 9vh, 7rem); padding-top:2.4rem; border-top:1px solid #E4E7EC; scroll-margin-top:72px;}
.kicker {color:#E8772E; font-weight:700; letter-spacing:.16em; font-size:.74rem; text-transform:uppercase;}
.accion {font-size:clamp(1.5rem, 2.3vw, 2.25rem); line-height:1.22; font-weight:600; color:#16213A; margin:.55rem 0 .5rem 0;
         letter-spacing:-.01em; max-width:1150px;}
.bajada {color:#667085; font-size:clamp(.95rem, 1.1vw, 1.08rem); max-width:1000px; margin:0 0 1.2rem 0; line-height:1.5;}
.graf-t {color:#1D2939; font-weight:700; font-size:.98rem; margin:.2rem 0 0 0;}
.graf-s {color:#667085; font-size:.84rem; margin:0 0 .2rem 0;}
.fuente {color:#98A2B3; font-size:.74rem; margin-top:.1rem;}

/* portada */
.portada {min-height:calc(100vh - 110px); display:flex; flex-direction:column; justify-content:center; padding:2rem 0 1rem 0;}
.portada .meta {color:#E8772E; font-weight:700; letter-spacing:.16em; font-size:.76rem; text-transform:uppercase;}
.portada h1 {font-size:clamp(2.3rem, 4.6vw, 4.2rem); line-height:1.08; font-weight:700; color:#16213A; margin:.9rem 0 1.2rem 0;
             letter-spacing:-.02em; max-width:1100px;}
.portada .preg {font-size:clamp(1.05rem, 1.45vw, 1.35rem); color:#344054; line-height:1.55; max-width:820px; border-left:4px solid #E8772E;
                padding-left:1.1rem; margin:0 0 2.6rem 0;}
.cifras {display:grid; grid-template-columns:repeat(4, minmax(0,1fr)); gap:2rem; max-width:1250px; padding-top:1.8rem; border-top:1px solid #E4E7EC;}
.cifra .v {font-size:clamp(2.1rem, 3.4vw, 3.2rem); font-weight:700; color:#16213A; line-height:1; letter-spacing:-.02em;}
.cifra .v.ac {color:#E8772E;}
.cifra .l {color:#667085; font-size:.9rem; margin-top:.5rem; line-height:1.45;}
.bajar {margin-top:2.6rem; color:#98A2B3; font-size:.8rem; letter-spacing:.12em; text-transform:uppercase;}
.bajar i {display:inline-block; margin-left:.5rem; font-style:normal; animation:rebote 1.6s ease-in-out infinite;}
@keyframes rebote {0%,100% {transform:translateY(0);} 50% {transform:translateY(6px);}}

/* portada de impacto */
.hero2 {display:grid; grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr); gap:clamp(1.5rem,4vw,4rem);
        align-items:center; padding:1.6rem 0 1.4rem 0;}
.hero2 .meta {color:#E8772E; font-weight:700; letter-spacing:.16em; font-size:.76rem; text-transform:uppercase;}
.hero2 h1 {font-family:'Segoe UI',sans-serif !important; font-size:clamp(2rem, 3.6vw, 3.3rem); line-height:1.1; font-weight:700; color:#16213A;
           margin:.9rem 0 1.2rem 0; letter-spacing:-.02em;}
.hero2 h1 .ac {color:#E8772E;}
.hero2 .golpe {font-family:'Segoe UI',sans-serif !important; font-size:clamp(1.2rem,2vw,1.75rem); font-weight:600; color:#E8772E;
               margin:-.2rem 0 1.4rem 0; letter-spacing:-.01em;}
.hero2 .preg {font-size:clamp(1.02rem, 1.35vw, 1.28rem); color:#344054; line-height:1.55; border-left:4px solid #E8772E; padding-left:1.1rem; margin:0;}
.gran {background:#16213A; border-radius:22px; padding:clamp(1.6rem,3vw,2.8rem); color:#fff; position:relative; overflow:hidden;}
.gran::after {content:""; position:absolute; right:-60px; top:-60px; width:220px; height:220px; border-radius:50%;
              border:34px solid rgba(232,119,46,.18);}
.gran .num {font-family:'Segoe UI',sans-serif !important; font-size:clamp(3.6rem, 8vw, 7rem); font-weight:700; line-height:.95; color:#E8772E;
            letter-spacing:-.03em;}
.gran .txt {font-size:clamp(1rem,1.4vw,1.25rem); color:#FFFFFF; margin-top:.8rem; line-height:1.4; max-width:420px;}
.gran .sub {color:#AFC0DA; font-size:.88rem; margin-top:1.2rem; padding-top:1rem; border-top:1px solid rgba(255,255,255,.14);}
.gran .sub b {color:#fff;}
.impactos {display:grid; grid-template-columns:repeat(3, minmax(0,1fr)); gap:1.2rem; margin:.5rem 0 1rem 0;}
.impacto {border:1px solid #E4E7EC; border-radius:18px; padding:1.5rem 1.6rem; background:#fff;}
.impacto small {color:#667085; font-weight:700; letter-spacing:.12em; font-size:.72rem; text-transform:uppercase;}
.impacto .v {font-family:'Segoe UI',sans-serif !important; font-size:clamp(2.2rem,3.6vw,3.2rem); font-weight:700; color:#16213A; line-height:1.05; margin:.5rem 0 .3rem 0;}
.impacto .v span {color:#E8772E;}
.impacto p {color:#475467; font-size:.9rem; margin:0 0 1.1rem 0; line-height:1.45; min-height:2.6em;}
.mini {display:grid; grid-template-columns:62px 1fr 44px; gap:.45rem .6rem; align-items:center; font-size:.78rem; color:#667085;}
.mini .pista {height:12px; background:#EEF1F5; border-radius:6px; overflow:hidden;}
.mini .pista i {display:block; height:100%; width:0; border-radius:6px; background:#C5CDD8; transition:width 1.4s cubic-bezier(.2,.7,.2,1) .35s;}
.mini .pista i.ac {background:#E8772E;} .mini .pista i.nv {background:#16213A;}
.impacto.visto .mini .pista i, .impacto:not(.rv) .mini .pista i {width:var(--w);}
.mini b {color:#16213A; text-align:right;}
.dividida {display:flex; height:14px; border-radius:7px; overflow:hidden; margin:.2rem 0 .5rem 0;}
.dividida i {display:block; height:100%; width:0; transition:width 1.4s cubic-bezier(.2,.7,.2,1) .35s;}
.impacto.visto .dividida i, .impacto:not(.rv) .dividida i {width:var(--w);}
.leyenda-m {display:flex; justify-content:space-between; font-size:.78rem; color:#667085;}
.leyenda-m b {color:#E8772E;}
.accion::after {content:""; display:block; width:0; height:3px; background:#E8772E; margin-top:.8rem; border-radius:2px;
                transition:width 1s cubic-bezier(.2,.7,.2,1) .35s;}
.lamina.visto .accion::after, .lamina:not(.rv) .accion::after {width:72px;}
@media (max-width:900px) {.hero2 {grid-template-columns:1fr; min-height:auto;} .impactos {grid-template-columns:1fr;}}

/* objetivos */
.obj-g {background:#16213A; border-radius:18px; padding:clamp(1.4rem,2.6vw,2.2rem) clamp(1.4rem,3vw,2.6rem); margin-bottom:1.2rem;}
.obj-g small {color:#E8772E; font-weight:700; letter-spacing:.14em; font-size:.74rem; text-transform:uppercase;}
.obj-g p {font-family:'Segoe UI',sans-serif !important; color:#fff; font-size:clamp(1.15rem,1.8vw,1.6rem); line-height:1.35; margin:.5rem 0 0 0;}
.obj-grid {display:grid; grid-template-columns:repeat(auto-fit, minmax(230px,1fr)); gap:1rem;}
.obj-e {border:1px solid #E4E7EC; border-radius:16px; padding:1.3rem 1.4rem; position:relative; background:#fff;}
.obj-e span {font-family:'Segoe UI',sans-serif !important; font-size:1.9rem; font-weight:700; color:#E8772E; line-height:1;}
.obj-e b {display:block; font-family:'Segoe UI',sans-serif !important; color:#16213A; font-size:1.02rem; margin:.6rem 0 .35rem 0;}
.obj-e p {color:#475467; font-size:.9rem; margin:0 0 .9rem 0; line-height:1.45;}
.obj-e em {font-style:normal; font-size:.76rem; font-weight:700; color:#24314F; background:#EEF3FA; padding:.25rem .6rem; border-radius:999px;}

/* datos y metodología */
.fuentes {display:grid; grid-template-columns:repeat(2, minmax(0,1fr)); gap:1rem;}
.fd {border:1px solid #E4E7EC; border-radius:16px; padding:1.2rem 1.3rem; background:#fff;}
.fd small {color:#667085; font-weight:700; letter-spacing:.1em; font-size:.7rem; text-transform:uppercase;}
.fd .c {font-family:'Segoe UI',sans-serif !important; font-size:clamp(1.6rem,2.4vw,2.1rem); font-weight:700; color:#16213A; margin:.35rem 0 .2rem 0;}
.fd p {color:#475467; font-size:.86rem; margin:0; line-height:1.45;}

/* del análisis al tablero */
.tab-grid {display:grid; grid-template-columns:repeat(auto-fit, minmax(260px,1fr)); gap:1rem; margin-top:.4rem;}
.tab-p {border-radius:16px; padding:1.4rem 1.5rem; background:#F4F6F9; border-top:4px solid #16213A;}
.tab-p.ac {border-top-color:#E8772E;}
.tab-p small {color:#667085; font-weight:700; letter-spacing:.1em; font-size:.7rem; text-transform:uppercase;}
.tab-p b {display:block; font-family:'Segoe UI',sans-serif !important; color:#16213A; font-size:1.15rem; margin:.4rem 0 .6rem 0;}
.tab-p ul {margin:0; padding-left:1.1rem; color:#475467; font-size:.88rem; line-height:1.6;}

/* resumen ejecutivo horizontal */
.resumen {background:#16213A; border-radius:18px; padding:clamp(1.6rem, 3vw, 2.6rem); margin-top:1rem;}
.resumen h3 {color:#FFFFFF !important; font-size:1.25rem !important; margin:0 0 1.6rem 0 !important; font-weight:600 !important;}
.resumen .fila {display:grid; grid-template-columns:repeat(3, minmax(0,1fr)); gap:2rem; position:relative;}
.resumen .fila::before {content:""; position:absolute; left:18px; right:18px; top:18px; height:2px; background:#24314F;}
.resumen .n {position:relative; width:38px; height:38px; border-radius:50%; background:#16213A; border:2px solid #AFC0DA; color:#fff;
             font-weight:700; display:flex; align-items:center; justify-content:center; font-size:.85rem; margin-bottom:1rem;}
.resumen .paso-r.ac .n {background:#E8772E; border-color:#E8772E;}
.resumen .t {color:#FFFFFF; font-weight:600; font-size:1.08rem; margin-bottom:.4rem;}
.resumen p {color:#C9D4E5; font-size:.93rem; line-height:1.5; margin:0;}

/* panel de hallazgos numerados */
.panel {background:#F4F6F9; border-radius:14px; padding:1.4rem 1.5rem 1.2rem 1.5rem; height:100%;}
.panel .ph {display:inline-block; background:#16213A; color:#fff; font-weight:700; font-size:.88rem; padding:.45rem 1rem;
            border-radius:8px; margin-bottom:1.1rem;}
.item {display:flex; gap:1rem; position:relative; padding-bottom:1.15rem;}
.item:not(:last-child)::before {content:""; position:absolute; left:17px; top:38px; bottom:0; width:2px; background:#D5DCE6;}
.item .n {flex:0 0 36px; height:36px; border-radius:50%; background:#16213A; color:#fff; font-weight:700; font-size:.8rem;
          display:flex; align-items:center; justify-content:center; box-shadow:0 0 0 4px #F4F6F9, 0 0 0 5px #D5DCE6;}
.item.ac .n {background:#E8772E;}
.item b {display:block; color:#16213A; font-size:1rem; margin:.35rem 0 .2rem 0;}
.item p {color:#475467; font-size:.9rem; margin:0; line-height:1.45;}

/* cifras grandes con texto (resultados) */
.stats {display:grid; grid-template-columns:repeat(auto-fit, minmax(240px, 1fr)); gap:1.2rem;}
.stat {border:1px solid #E4E7EC; border-radius:14px; padding:1.4rem 1.5rem;}
.stat .v {font-size:clamp(2.2rem, 3.4vw, 3rem); font-weight:800; color:#079455; line-height:1; letter-spacing:-.02em;}
.stat b {display:block; color:#16213A; font-size:.95rem; margin:.8rem 0 .3rem 0; text-transform:uppercase; letter-spacing:.04em;}
.stat p {color:#475467; font-size:.9rem; margin:0; line-height:1.45;}

/* recomendación */
.reco {display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:1rem; margin-top:1.4rem;}
.reco div {background:#16213A; border-radius:14px; padding:1.3rem 1.4rem; color:#fff;}
.reco small {color:#E8772E; font-weight:800; letter-spacing:.14em; font-size:.72rem;}
.reco b {display:block; font-size:1.08rem; margin:.4rem 0 .4rem 0;}
.reco p {color:#C9D4E5; font-size:.88rem; margin:0; line-height:1.45;}
.cierre {background:#F4F6F9; border-left:5px solid #E8772E; border-radius:0 14px 14px 0; padding:1.6rem 1.8rem; margin-top:1.6rem;}
.cierre b {color:#16213A; font-size:1.15rem; display:block; margin-bottom:.4rem;}
.cierre p {color:#344054; margin:0; font-size:.98rem; line-height:1.55;}
.nota {color:#98A2B3; font-size:.78rem; margin-top:2.5rem; line-height:1.5; max-width:1100px;}
[data-testid="stExpander"] {border:1px solid #E4E7EC !important; border-radius:10px !important;}
@media (max-width: 900px) {
  .barra nav {display:none;}
  .block-container {padding:4.4rem 1rem 3rem 1rem !important;}
  .cifras {grid-template-columns:1fr 1fr;}
  .resumen .fila {grid-template-columns:1fr;}
  .resumen .fila::before {display:none;}
}
@media (prefers-reduced-motion: reduce) {* {animation:none !important; transition:none !important;}}
</style>
"""


def estilo(fig, h=440, leyenda=False):
    fig.update_layout(height=h, plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
                      font=dict(color=TEXTO, family="Segoe UI, sans-serif", size=13),
                      margin=dict(l=4, r=16, t=16, b=8), showlegend=leyenda, bargap=0.28,
                      legend=dict(orientation="h", y=1.08, x=0, font=dict(color=SUAVE, size=12)),
                      hoverlabel=dict(bgcolor="#FFFFFF", bordercolor=BORDE, font_color=TEXTO))
    fig.update_xaxes(showgrid=False, linecolor=BORDE, tickfont=dict(color=SUAVE, size=12), zeroline=False, title=None)
    fig.update_yaxes(showgrid=False, tickfont=dict(color=SUAVE, size=12), zeroline=False, title=None)
    return fig


# ---------------------------------------------------------------- piezas de HTML (las usan Streamlit y la versión HTML)
def h_barra(items):
    return ('<div class="barra"><div class="marca">Seguridad vial <span>·</span> Bogotá</div><nav>' +
            "".join(f'<a href="#{ancla}">{t}</a>' for ancla, t in items) + '</nav></div><div class="progreso"></div>')


def h_resumen(items, acento=0, titulo="Conclusiones", ancla="concl"):
    html = "".join(f'<div class="paso-r{" ac" if i + 1 == acento else ""}"><div class="n">{i + 1:02d}</div>'
                   f'<div class="t">{t}</div><p>{x}</p></div>' for i, (t, x) in enumerate(items))
    return f'<div class="resumen" id="{ancla}"><h3>{titulo}</h3><div class="fila">{html}</div></div>'


def h_objetivos(pregunta, objetivos):
    tarjetas = "".join(f'<div class="obj-e"><span>{i + 1:02d}</span><b>{t}</b><p>{x}</p><em>{r}</em></div>'
                       for i, (t, x, r) in enumerate(objetivos))
    return (f'<div class="obj-g"><small>La pregunta que guía el informe</small><p>{pregunta}</p></div>'
            f'<div class="obj-grid">{tarjetas}</div>')


def h_fuentes(items):
    return '<div class="fuentes">' + "".join(
        f'<div class="fd"><small>{n}</small><div class="c">{c}</div><p>{d}</p></div>' for n, c, d in items) + "</div>"


def h_lamina(ancla, kicker, accion, bajada=""):
    return (f'<div class="lamina" id="{ancla}"><div class="kicker">{kicker}</div><div class="accion">{accion}</div>'
            f'{f"<p class=bajada>{bajada}</p>" if bajada else ""}</div>')


def h_graf_titulo(titulo, sub=""):
    return f'<p class="graf-t">{titulo}</p><p class="graf-s">{sub}</p>'


def h_fuente(txt):
    return f'<p class="fuente">{txt}</p>'


def h_panel(items, titulo="Hallazgos clave", acento=0):
    html = "".join(f'<div class="item{" ac" if i + 1 == acento else ""}"><div class="n">{i + 1:02d}</div>'
                   f'<div><b>{t}</b><p>{x}</p></div></div>' for i, (t, x) in enumerate(items))
    return f'<div class="panel"><div class="ph">{titulo}</div>{html}</div>'


# ---------------------------------------------------------------- efectos: transiciones, cifras que cuentan, progreso
JS_EFECTOS = """
<script>
(function () {
  // En Streamlit el script corre en un iframe: se usa la ventana principal. En el HTML exportado, la propia ventana.
  let W = window; try { if (window.parent && window.parent !== window && window.parent.document) W = window.parent; } catch (e) {}
  const doc = W.document;
  const main = doc.querySelector('[data-testid="stMain"]') || doc.scrollingElement;
  const origen = (main === doc.scrollingElement) ? W : main;
  function contar(el) {
    if (el.dataset.hecho) return; el.dataset.hecho = '1';
    const fin = parseFloat(el.dataset.n), dec = parseInt(el.dataset.dec || '0'), suf = el.dataset.suf || '', pre = el.dataset.pre || '';
    const t0 = W.performance.now(), dur = 1600;
    const fmt = (x) => pre + x.toLocaleString('es-CO', {minimumFractionDigits: dec, maximumFractionDigits: dec}) + suf;
    function paso(t) { const p = Math.max(0, Math.min(1, (t - t0) / dur)), e = 1 - Math.pow(1 - p, 3); el.textContent = fmt(fin * e);
                       if (p < 1) W.requestAnimationFrame(paso); }
    W.requestAnimationFrame(paso);
  }
  const ioN = new W.IntersectionObserver((es) => es.forEach((e) => { if (e.isIntersecting) { contar(e.target); ioN.unobserve(e.target); } }),
                                       {threshold: 0.4});
  function numeros() { doc.querySelectorAll('[data-n]').forEach((el) => { if (!el.dataset.obs) { el.dataset.obs = '1'; ioN.observe(el); } }); }
  const reglas = [['.lamina, .stat, .reco > div, .cierre, .resumen .paso-r, .nota, .impacto, .gran, .obj-g, .obj-e, .fd', ''],
                  ['[data-testid="stPlotlyChart"], .grafico, .graf-t', 'izq'], ['.panel', 'der'], ['.panel .item', '']];
  const io = new W.IntersectionObserver((entradas) => {
    entradas.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('visto'); io.unobserve(e.target); } });
  }, {threshold: 0.12});
  function marcar() {
    reglas.forEach(([sel, dir]) => doc.querySelectorAll(sel).forEach((el) => {
      if (el.dataset.rv) return;
      el.dataset.rv = '1';
      el.classList.add('rv'); if (dir) el.classList.add(dir);
      const hermanos = el.parentElement ? [...el.parentElement.children] : [];
      el.style.transitionDelay = (Math.max(0, hermanos.indexOf(el)) % 6) * 110 + 'ms';
      io.observe(el);
    }));
  }
  function progreso() {
    const barra = doc.querySelector('.progreso');
    if (!barra || !main) return;
    const max = main.scrollHeight - main.clientHeight;
    barra.style.transform = 'scaleX(' + (max > 0 ? main.scrollTop / max : 0) + ')';
  }
  marcar(); numeros();
  new W.MutationObserver(() => { marcar(); numeros(); }).observe(doc.body, {childList: true, subtree: true});
  if (main && !main.dataset.prog) { main.dataset.prog = '1'; origen.addEventListener('scroll', progreso, {passive: true}); }
  progreso();
})();
</script>
"""


# ---------------------------------------------------------------- lienzos: el mismo informe en Streamlit o en HTML
class LienzoStreamlit:
    """Dibuja el informe con Streamlit."""

    def __init__(self):
        import streamlit as st
        self.st = st

    def html(self, s):
        self.st.markdown(s, unsafe_allow_html=True)

    def fig(self, fig, config=None):
        self.st.plotly_chart(fig, width="stretch", config=config or CFG)

    def fila(self, izquierda, derecha, proporcion=(7, 5)):
        """izquierda / derecha: listas de piezas (texto HTML o figuras de Plotly)."""
        cols = self.st.columns(list(proporcion), gap="large")
        for col, piezas in zip(cols, (izquierda, derecha)):
            with col:
                for p in piezas:
                    self.fig(p) if not isinstance(p, str) else self.html(p)

    def cerrar(self):
        import streamlit.components.v1 as components
        components.html(JS_EFECTOS, height=0)


class LienzoHTML:
    """Arma el mismo informe como un único archivo HTML (sin servidor ni instalación)."""

    def __init__(self):
        self.partes = []

    def _fig(self, fig, config=None):
        import plotly.io as pio
        return '<div class="grafico">' + pio.to_html(fig, full_html=False, include_plotlyjs=False,
                                                       config=config or CFG) + "</div>"

    def html(self, s):
        self.partes.append(s)

    def fig(self, fig, config=None):
        self.partes.append(self._fig(fig, config))

    def fila(self, izquierda, derecha, proporcion=(7, 5)):
        celdas = ["".join(p if isinstance(p, str) else self._fig(p) for p in piezas) for piezas in (izquierda, derecha)]
        self.partes.append(f'<div class="fila-h" style="grid-template-columns:{proporcion[0]}fr {proporcion[1]}fr">'
                           f'<div>{celdas[0]}</div><div>{celdas[1]}</div></div>')

    def cerrar(self):
        pass

    def documento(self, titulo):
        import plotly.offline as po
        estilo_html = ("<style>body{margin:0;background:#fff} .contenido{padding:4.6rem clamp(1.2rem,5vw,6rem) 5rem}"
                       ".fila-h{display:grid;gap:2.5rem;align-items:start} @media(max-width:900px){.fila-h{grid-template-columns:1fr!important}}"
                       "</style>")
        return ('<!doctype html><html lang="es"><head><meta charset="utf-8">'
                '<meta name="viewport" content="width=device-width, initial-scale=1">'
                f'<title>{titulo}</title>{CSS}{CSS_NARRATIVA}{estilo_html}'
                f'<script>{po.get_plotlyjs()}</script></head><body><div class="contenido">'
                + "".join(self.partes) + f"</div>{JS_EFECTOS}</body></html>")

# Complementos específicos del informe narrativo; no modifican el tablero.
CSS_NARRATIVA = """
<style>
.conector{display:flex;gap:1.1rem;align-items:flex-start;border-left:4px solid #E8772E;background:#F4F6F9;padding:1.15rem 1.4rem;border-radius:0 12px 12px 0;margin:1rem 0 1.4rem;color:#24314F;}
.conector b{display:block;font-size:1rem;color:#16213A;margin-bottom:.25rem}.conector p{margin:0;font-size:.94rem;line-height:1.6;color:#475467}
.pills{display:flex;flex-wrap:wrap;gap:.65rem;margin:1.1rem 0 2rem}.pill{display:flex;align-items:baseline;gap:.4rem;background:#F4F6F9;border:1px solid #E4E7EC;padding:.65rem .9rem;border-radius:10px;color:#667085;font-size:.87rem}.pill b{font-size:1.1rem;color:#16213A}
.why{font-size:.85rem;color:#667085;line-height:1.6;padding:.5rem 0 .8rem}.why b{color:#24314F}
.report-foot{margin:2rem 0 .6rem;font-size:.88rem;line-height:1.7;color:#667085;max-width:1100px}.report-foot b{color:#16213A}
.kpi-table{width:100%;border-collapse:collapse;font-size:.89rem;color:#1D2939;margin:.8rem 0 1.4rem} .kpi-table th{background:#16213A;color:#fff;text-align:left;padding:.86rem .92rem;font-weight:600} .kpi-table td{border-bottom:1px solid #E4E7EC;padding:1rem .92rem;vertical-align:top;line-height:1.5} .kpi-table tr:nth-child(even) td{background:#F4F6F9}.kpi-table .key{color:#E8772E;font-weight:700;white-space:nowrap}.kpi-table .tn{font-size:.78rem;color:#667085}
.next{border:1px solid #E4E7EC;border-radius:16px;padding:1.35rem 1.7rem;background:#fff;margin:.6rem 0 1.4rem}.next b{color:#16213A;font-size:1.1rem}.next p{color:#475467;line-height:1.65;margin:.5rem 0}
details.metagraf{border-top:1px solid #E4E7EC;color:#667085;font-size:.83rem;line-height:1.6;padding:.8rem 0 1rem;margin:.4rem 0}.metagraf summary{cursor:pointer;color:#24314F;font-weight:600}.metagraf p{margin:.6rem 0 0}
@media(max-width:800px){.kpi-table{display:block;overflow-x:auto;white-space:normal}.kpi-table th,.kpi-table td{min-width:120px}}
</style>
"""
