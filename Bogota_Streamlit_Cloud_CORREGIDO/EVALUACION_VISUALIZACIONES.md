# Evaluación de las visualizaciones · Siniestralidad vial de Bogotá, 2015–2025

**Objeto evaluado.** Los **seis gráficos Plotly** del informe narrativo depurado (HTML y versión Streamlit); su secuencia, datos y su correspondencia con la pregunta analítica. **No** se auditan aquí todas las visualizaciones internas del archivo Power BI, porque se trata de otro artefacto. Las paletas se contrastaron con el tema original del tablero (`TemaClaro.json`).

**Criterio.** Evaluación de adecuación del dominio, abstracción, codificación visual e implementación (Munzner, 2009); expresividad y efectividad (Mackinlay, 1986); precisión de la tarea perceptual (Cleveland & McGill, 1984). La decisión de sustitución exige una ventaja objetiva, no una preferencia estética. Los destinatarios plausibles son personas que consultan la siniestralidad y responsables de seguimiento de seguridad vial; sus necesidades individuales **no** han sido verificadas con entrevistas o pruebas de usuarios.

## Resultado general

| N.º | Visualización | Tarea dominante | Diagnóstico | Decisión | Implementación |
|:--:|---|---|---|---|---|
| 1 | Siniestros con víctimas, 2015–2025 | Tendencia, extremos y comparación interanual | Línea apropiada; información sobre cifras enteras mal formateada en el *hover* y anotación que sugería una explicación causal | 🟡 **AJUSTAR** | Corregir separadores/decimales del *hover*; anotar el mínimo observado, sin atribuir causa |
| 2 | Fallecidos, 2015–2025 | Tendencia temporal y magnitud de muertes | Ejes, escala y línea consistentes con la tarea | ✅ **CONSERVAR** | Objeto gráfico intacto |
| 3 | Participación de motociclistas y peatones | Comparar dos series de porcentajes | Dos líneas son pertinentes; *hover* con decimal anglosajón en un informe en español | 🟡 **AJUSTAR** | Formato decimal español en *hover*, sin modificar trazos ni series |
| 4 | Fallecidos por 100 víctimas según franja | Comparar cuatro proporciones con base común | Barras y base cero apropiadas; rótulos largos y formato decimal del *hover* | 🟡 **AJUSTAR** | Etiquetas de categoría en dos líneas; *hover* numérico localizado |
| 5 | Diez localidades con más fallecidos | Identificar y ordenar los máximos | Ranking horizontal ordenado, base cero y valores exactos | ✅ **CONSERVAR** | Objeto gráfico intacto |
| 6 | Motociclistas fallecidos: localidad × franja | Localizar combinaciones altas en una matriz categórica | Mapa de calor pertinente, pero el significado de la intensidad cromática podía quedar implícito | 🟡 **AJUSTAR** | Aclaración de la escala cualitativa de intensidad en subtítulo; mapa de calor intacto |

**Balance: 2 gráficos conservados y 4 ajustados; 0 reemplazados.** Se mantuvieron los tipos de gráfico, las seis posiciones en la narrativa y **todas** las series y agregaciones. Tres ajustes intervienen solo textos emergentes/etiquetas; el cuarto añade una precisión semántica al subtítulo. Ningún cambio pretende demostrar un aumento perceptual medido experimentalmente.

---

## GRÁFICO 1. Siniestros con personas heridas o fallecidas, por año

### 1. Propósito

**Pregunta:** ¿cómo varía anualmente la cantidad de siniestros distintos con víctimas en Bogotá entre 2015 y 2025? **Tarea:** leer tendencia, comparar años, localizar extremos. **Variables:** `anio` (temporal anual ordenado; 2015–2025) y `siniestros_con_victimas` (cuantitativa discreta de conteo). Unidad de observación presentada: **año**; medida: **siniestros distintos con al menos una víctima**, no personas. El contexto de uso plausible es comprender la evolución, no calcular tasas de exposición vial.

### 2. Evaluación teórica

- **Munzner / dominio:** pregunta adecuada a la problemática temporal. Se evita confundir un suceso con su número de víctimas. Riesgo de dominio: leer una reducción de eventos como una reducción equivalente de su gravedad.
- **Munzner / abstracción:** datos temporales agregados por año; operación de serie temporal, extremos y cambios interanuales. La agregación anual responde la pregunta sobre evolución, pero no estacionalidad o tasas por viaje.
- **Munzner / codificación/interacción:** línea con puntos sobre ejes rectilíneos; orden cronológico continuo y línea azul del tema original. Permite comparar posiciones en una escala común. El punto destacado de 2025 respeta el foco narrativo. El *hover* original mostraba décimas inexistentes en un conteo entero (`11,573.0` para 11.573).
- **Munzner / algoritmo:** se contrastó cada punto contra los once valores del CSV anual conservado, y la igualdad se mantuvo tras el ajuste. La anotación original “2020 · cambio de movilidad” mezclaba observación del gráfico con una explicación que el gráfico aislado no verifica.
- **Mackinlay:** expresividad correcta en la geometría de la línea; defecto puntual de expresividad en el *hover* y en la atribución del comentario. Efectividad alta para cambios por año; un gráfico de barras exigiría comparar longitudes y sería menos natural para continuidad temporal.
- **Cleveland & McGill:** la lectura cuantitativa procede por **posición sobre una escala común**. No exige juzgar sectores, áreas o volumen. La pendiente ayuda a la dirección temporal, no sustituye los valores.

### 3. Diagnóstico

**Fortalezas:** escala temporal legible, 2020 claramente diferenciable, unidad expresada en el título. **Debilidades:** decimal falso y separadores anglosajones del dato flotante en el *hover*; anotación causal no sustentada por esa serie. **Riesgo:** inferir una explicación de la caída de 2020 sin evidencia de movilidad o exposición.

### 4. Alternativas

**Actual:** línea de puntos y anotación. **Alternativa considerada:** columnas por año. **Comparación:** las columnas facilitan magnitudes absolutas contra cero, pero agregan once barras y no mejoran la lectura del patrón longitudinal; por tanto, **no se justifica reemplazar**.

### 5. Decisión final

🟡 **AJUSTAR.** Se conserva el gráfico de líneas y sus valores; se corrigen solamente metadatos de lectura y anotación. Fundamento: exactitud semántica (Mackinlay) sin perder posición común (Cleveland & McGill).

### 6. Implementación y verificación

Se cambió el *hover* a **“2025: 11.573 siniestros con víctimas”** (sin décimas) y la anotación a **“2020 · mínimo de la serie”**, afirmación comprobada contra la propia serie. La secuencia anual y sus valores permanecen idénticos. La comparación con fuente conservada arrojó 11.255 en 2015, 8.936 en 2020 y 11.573 en 2025.

---

## GRÁFICO 2. Personas fallecidas en siniestros viales, por año

### 1. Propósito

**Pregunta:** ¿cómo evolucionan los fallecimientos por siniestros viales entre 2015 y 2025 y qué contraste ofrecen frente a los eventos? **Tarea:** seguir tendencia, detectar máximos y mínimos, contrastar años. **Variables:** `anio` (temporal anual), `estado = Fallecido` (filtro nominal), y cantidad de personas fallecidas (cuantitativa discreta). La definición operativa es **fallecimiento a 30 días**.

### 2. Evaluación teórica

- **Munzner / dominio:** el indicador es central para integridad y vida; complementa el conteo de eventos sin confundir sus denominadores.
- **Munzner / abstracción:** conteo anual de filas de víctimas fatales. Se preserva la diferenciación entre personas y siniestros. Riesgo del dominio: tratar la serie de muertes como tasa de mortalidad por trayecto sin información de exposición.
- **Munzner / codificación/interacción:** línea naranja con puntos, años en el eje horizontal, eje vertical desde cero y *hover* de enteros. La naranja conserva su papel de énfasis narrativo.
- **Munzner / implementación:** se verificó identidad de la representación exportada **antes y después** del proceso. Los valores fueron recomputados desde los registros de víctimas.
- **Mackinlay:** expresividad y efectividad adecuadas: una variable temporal y otra cuantitativa, con escala común dentro de la gráfica. La separación visual respecto de la serie de eventos evita imponer una falsa equivalencia de magnitud.
- **Cleveland & McGill:** comparación por posición sobre eje común; la línea es pertinente para continuidad temporal y no emplea codificaciones menos precisas.

### 3. Diagnóstico

**Fortalezas:** compara cambios de año en año con escala explícita, semántica de unidad correcta. **Debilidades:** no puede responder por sí sola a la pregunta de riesgo por viaje; comparaciones porcentuales con siniestros requieren leer ambos gráficos o calcular variaciones, no comparar sus alturas directamente. **Riesgo:** atribuir las variaciones a políticas concretas sin análisis causal.

### 4. Alternativas

**Actual:** línea única. **Alternativa considerada:** barras verticales o doble eje junto con siniestros. Las barras no aportan ventaja clara para tendencia; un doble eje puede confundir escalas y exagerar o amortiguar correlaciones. No conviene reemplazar.

### 5. Decisión final

✅ **CONSERVAR**, sin modificar datos, geometría, etiquetas, colores ni configuración Plotly.

### 6. Implementación y verificación

No se hizo ninguna modificación. Se verificó que el objeto gráfico completo (trazas y configuración de ejes) coincide exactamente con el original y que se reproduce el conteo derivado de `estado = Fallecido` por año: 530 fallecidos en 2015 y 562 en 2025.

---

## GRÁFICO 3. Participación entre fallecidos: motociclistas y peatones

### 1. Propósito

**Pregunta:** ¿cómo cambió la participación relativa de motociclistas y peatones entre las personas fallecidas? **Tarea:** comparar tendencias de dos grupos y localizar la inversión en su posición relativa. **Variables:** `anio` (temporal), `actor` (nominal; dos categorías elegidas), `estado` (nominal, filtro “Fallecido”) y proporción anual `fallecidos_actor / fallecidos_total × 100` (cuantitativa porcentual).

### 2. Evaluación teórica

- **Munzner / dominio:** relevante para conocer qué grupos componen los fallecimientos; **no** estima probabilidades individuales de muerte.
- **Munzner / abstracción:** el denominador es el total anual de fallecidos de todos los actores; se muestran únicamente dos categorías seleccionadas. Son **dos participaciones parciales**, no el 100 % de la composición; así lo indica el subtítulo. Se comprobó la fórmula sobre los registros.
- **Munzner / codificación/interacción:** dos líneas por año, colores azul y gris, leyenda explícita, eje porcentual de 0 a 60 y foco naranja al punto final de motociclistas. Las dos curvas comparten escala y la codificación de categorías es inequívoca. El *hover* previo representaba decimales con punto mientras el informe utiliza coma.
- **Munzner / implementación:** las dos series se contrastaron contra conteos de actores y totales anuales; no se alteraron valores, escala, puntos ni líneas.
- **Mackinlay:** expresividad correcta para las dos participaciones descritas. Si el objetivo fuese **composición exhaustiva**, harían falta otras categorías y sería otra pregunta; no es motivo para sustituir la comparación de dos grupos. La efectividad de líneas es alta al comparar tendencias.
- **Cleveland & McGill:** posición vertical común; se percibe tanto variación de cada serie como diferencia entre ambas en un año. No se requiere comparar áreas apiladas.

### 3. Diagnóstico

**Fortalezas:** diferencias de trayectoria legibles; evita confundir magnitudes absolutas con participación. **Debilidad:** detalle de localización numérica en *hover*. **Riesgo:** interpretar “45,4 % de fallecidos” como “45,4 % de motociclistas muere”; el gráfico no mide eso.

### 4. Alternativas

**Actual:** dos líneas. **Alternativa considerada:** área apilada o barra 100 % apilada por año con todos los actores. La alternativa serviría para composición completa, pero obligaría a una tarea distinta y haría más difícil comparar con precisión dos series específicas. No es superior para la pregunta vigente.

### 5. Decisión final

🟡 **AJUSTAR** únicamente la lectura del *hover* en español. No se reemplaza ni se altera el diseño visual.

### 6. Implementación y verificación

Los valores emergentes ahora presentan **45,4 %** en lugar de **45.4 %**. Se comprobó la identidad de las series originales y de los estilos. En 2015, motociclistas ≈30,8 % y peatones ≈48,5 %; en 2025, ≈45,4 % y ≈39,1 %, respectivamente.

---

## GRÁFICO 4. Fallecidos por cada 100 víctimas, según franja horaria

### 1. Propósito

**Pregunta:** ¿en qué franjas horarias hay una mayor proporción de fallecidos entre las víctimas registradas? **Tarea:** comparar magnitudes entre cuatro categorías; identificar el máximo y los contrastes día/noche. **Variables:** `hora` (hora temporal discreta, convertida en cuatro intervalos ordenados), `estado` (nominal: Herido/Fallecido), y `100 × Fallecido / (Fallecido + Herido)` (cuantitativa continua derivada, expresada por 100 víctimas). Periodo: 2021–2025.

### 2. Evaluación teórica

- **Munzner / dominio:** la pregunta de **gravedad observada entre víctimas** está bien operacionalizada. La cifra no estima riesgo de accidente por hora ni por desplazamiento.
- **Munzner / abstracción:** recodificación de horas en madrugada 0–5, mañana 6–11, tarde 12–17 y noche 18–23. El denominador contiene las víctimas registradas, no los viajes. El orden de los intervalos es cronológico. Se verificó que no faltan horas fuera de 0–23 en el registro usado.
- **Munzner / codificación/interacción:** cuatro barras desde cero en escala común; naranja para dos intervalos 18–05, azul para 06–17. Etiquetas numéricas precisas sobre cada barra. El eje de categorías original colocaba nombres largos en una sola línea, vulnerables a compresión del ancho disponible; el *hover* usaba punto decimal.
- **Munzner / implementación:** se recalculó cada proporción por `crosstab(franja, estado)`. La altura de cada barra y su color no cambian.
- **Mackinlay:** las barras son expresivas y efectivas para cuatro proporciones que comparten unidad. Un gráfico de líneas podría sugerir interpolación continua entre cuatro intervalos amplios que los datos agregados no permiten. Un gráfico circular sería menos preciso para comparar estas cuatro razones.
- **Cleveland & McGill:** longitud y extremos de barras alineados a un origen común facilitan comparación. Los valores anotados mejoran la lectura exacta, sin obligar a juzgar ángulos o áreas.

### 3. Diagnóstico

**Fortalezas:** unidad común, orden temporal, eje vertical con cero, texto numérico y color con función semántica clara. **Debilidades:** rótulos de categorías extensos; pequeñas inconsistencias de notación decimal. **Riesgo:** interpretar 5,06 como una tasa de accidentes entre toda la movilidad; en realidad corresponde a fallecidos entre víctimas.

### 4. Alternativas

**Actual:** cuatro barras verticales. **Alternativa considerada:** cuatro puntos en escala horizontal común, o barras horizontales. En pantallas angostas una disposición horizontal puede ser útil, pero las barras existentes son apropiadas en un informe de escritorio y reflejan el orden del día. Para este caso dividir etiquetas en dos líneas es una corrección más conservadora que sustituir la visualización.

### 5. Decisión final

🟡 **AJUSTAR** rotulación, no el tipo de gráfico. Fundamento: mantener comparaciones por longitud desde un cero compartido y disminuir el riesgo de solapamiento de categorías.

### 6. Implementación y verificación

Se presentan los nombres de franja y los rangos horarios en **dos líneas**. El *hover* usa 5,06 y registra fallecidos/heridos con formato numérico en español. Se verificaron las cuatro proporciones, sin modificar la geometría: madrugada **5,06**; mañana **1,93**; tarde **1,95**; noche **2,55** fallecidos por cada 100 víctimas.

---

## GRÁFICO 5. Diez localidades con más personas fallecidas

### 1. Propósito

**Pregunta:** ¿en qué localidades se registran más fallecidos acumulados en 2021–2025? **Tarea:** ordenar categorías, reconocer máximos, comparar volúmenes. **Variables:** `localidad` (nominal) y cantidad de personas fallecidas acumulada (cuantitativa discreta); filtro temporal 2021–2025; subconjunto de las diez localidades con más casos.

### 2. Evaluación teórica

- **Munzner / dominio:** identifica concentración territorial **en números absolutos**, útil para el seguimiento; no permite comparar riesgo ajustado por habitantes, tráfico o viajes.
- **Munzner / abstracción:** agrupación de fallecidos por localidad, ordenación descendente y selección de top 10. La selección es coherente con localizar focos de concentración; no pretende representar todas las localidades ni distribución geográfica dentro de ellas.
- **Munzner / codificación/interacción:** barras **horizontales**, inicio en cero, orden de mayor a menor leído de arriba hacia abajo, nombres completos, números encima/al final de cada barra. El naranja identifica las cinco primeras, el gris el resto. No se requiere mapa de polígonos para un ranking.
- **Munzner / implementación:** se comprobó el orden y cada cantidad contra `value_counts()` sobre víctimas fatales 2021–2025; todas las especificaciones del gráfico se conservaron iguales al original.
- **Mackinlay:** expresividad y efectividad altas: categorías nominales ↔ posición ordenada; cuantía ↔ longitud desde cero, con etiquetas exactas. Un mapa coloreado introduciría geometría y áreas de localidades que no facilitan ordenar magnitudes tan bien.
- **Cleveland & McGill:** comparación de longitudes sobre una línea de base común. La intensidad del relleno no sustituye la longitud; el color se usa solamente para destacar top 5.

### 3. Diagnóstico

**Fortalezas:** jerarquía clara, textos de localidades legibles y valores explícitos. **Debilidad:** top 10 oculta localidades de menor acumulado (decisión de alcance documentada en el título). **Riesgo:** confundir mayor número absoluto con mayor probabilidad por desplazamiento; el texto lateral advierte el alcance.

### 4. Alternativas

**Actual:** ranking horizontal. **Alternativa considerada:** mapa coroplético o gráfico de puntos. Un mapa respondería *dónde están* y relaciones de vecindad, pero no mejora la comparación exacta de cantidades y puede sobrerrepresentar localidades extensas. Un dot plot sería aceptable, no claramente superior para estos diez conteos etiquetados.

### 5. Decisión final

✅ **CONSERVAR** exactamente el gráfico existente.

### 6. Implementación y verificación

No hubo cambios. Se verificó igualdad de objeto Plotly completo, recuentos, orden y paleta. Kennedy conserva el primer puesto en el acumulado con **328** fallecidos; Engativá registra **240**.

---

## GRÁFICO 6. Motociclistas fallecidos por localidad y franja horaria

### 1. Propósito

**Pregunta:** ¿qué combinaciones de localidad y horario concentran más motociclistas fallecidos entre 2021 y 2025? **Tarea:** examinar una matriz de dos categorías, localizar celdas de valor alto y comparar recuentos específicos. **Variables:** `localidad` (nominal), `franja` (categoría ordinal temporal con cuatro intervalos), `actor = Motociclista` (filtro nominal), `estado = Fallecido` (filtro nominal) y conteo (cuantitativo discreto).

### 2. Evaluación teórica

- **Munzner / dominio:** responde directamente a la intersección de tres dimensiones relevantes. **No** informa tasas por motociclista expuesto o por flujo vehicular.
- **Munzner / abstracción:** tabla de contingencia `localidad × franja` y selección de las diez localidades con más fallecidos motociclistas. La misma escala se usa en todas las 40 celdas. La localidad se ordena por total, no por un solo intervalo.
- **Munzner / codificación/interacción:** mapa de calor de 10 × 4. La intensidad naranja indica mayor conteo y cada celda muestra su número exacto; el *hover* reproduce localidad, franja y conteo. La escala fue fija de 0 a 47, sin barra de color. El código era correcto, pero **faltaba declarar en texto la dirección de la escala** para quienes no la infieren espontáneamente.
- **Munzner / algoritmo:** se recomputó la tabla cruzada completa de 40 celdas sobre CSV y se comparó con la matriz original y revisada. Se conserva el arreglo, los límites 0–47 y la lógica de color.
- **Mackinlay:** la intensidad cromática es menos efectiva para diferencias exactas, pero aquí permite **buscar concentraciones** en muchos cruces sin desplegar 40 barras. Las etiquetas numéricas compensan la precisión perceptual limitada del color. La matriz no introduce geografía inexistente: no es un mapa espacial.
- **Cleveland & McGill:** para magnitudes individuales, el color es menos preciso que la posición; sin embargo, una matriz con números dentro de celdas es adecuada a la tarea de *detección visual* y búsqueda por dos categorías. Reemplazar por 40 barras o un gráfico de puntos dificultaría el cruce de dimensiones. Se reservan los números para comparación exacta.

### 3. Diagnóstico

**Fortalezas:** todos los cruces en una vista, lectura explícita por celda, escala cromática monotónica, alto contraste de texto oscuro sobre fondo naranja. **Debilidad:** la escala de intensidad carece de leyenda y su dirección no se explicitaba en el subtítulo. **Riesgo:** confundir altos conteos con un mayor riesgo ajustado o interpretar el color como una clase nominal de riesgo.

### 4. Alternativas

**Actual:** mapa de calor anotado. **Alternativa considerada:** barras agrupadas localidad × horario o *small multiples*. Estas mejorarían la comparación exacta de un subconjunto de celdas, pero multiplicarían ejes y dificultarían identificar rápidamente concentraciones en 40 intersecciones. La matriz anotada conserva un equilibrio adecuado para detectar patrones y leer cantidades exactas.

### 5. Decisión final

🟡 **AJUSTAR** exclusivamente el subtítulo: aclarar “**más naranja = mayor recuento**”. No se agrega una leyenda que reduzca el área útil ni se reemplaza el mapa de calor.

### 6. Implementación y verificación

La matriz, el orden de localidades, los textos, el mapa de colores y los intervalos son **idénticos** al original; se modificó solo el subtítulo. Se verificó que Kennedy × madrugada presenta **47** motociclistas fallecidos y que las 40 celdas coinciden con el archivo fuente.

---

## Comprobaciones transversales y límites de validez

**Revisión de fuentes y operaciones.** Se leyó el agregado de siniestros con víctimas (`siniestros_con_victimas_anual.csv`) y el registro de víctimas (`victimas_anuario.csv.gz`), ambos provenientes de la entrega anterior. Se reprodujeron por separado las seis construcciones de datos: 11 valores anuales de siniestros, 11 de fallecidos, dos series de participación, cuatro razones por franja, diez recuentos de localidades y 40 cruces localidad–horario. Los resultados numéricos y las escalas de los seis gráficos nuevos son los mismos. El tramo desagregado de 2021–2025 contiene **107.755 registros de víctimas**, de los cuales **2.667 son fallecidos**. Esto constituye una **verificación interna frente a las bases entregadas**, no una auditoría externa independiente frente a publicaciones del Observatorio de Movilidad.

**Conservación estricta.** Las representaciones **2, 5 y 6** mantienen exactamente sus objetos Plotly de trazas y diseño, comprobado mediante comparación estructural. En el n.º 6 solo cambió un subtítulo HTML externo al gráfico. Las representaciones 1, 3 y 4 conservan todas las magnitudes, colores y tipos: cambian anotación o formato de lectura. Se mantuvo la paleta original: naranja `#E8772E`, azul `#16213A` y grises del tema de Power BI; el naranja conserva su función de énfasis.

**Interactividad y rendimiento.** Las seis visualizaciones se exportaron como Plotly con *hover* y configuración responsiva. El HTML conserva Plotly embebido y puede abrirse sin instalaciones ni dependencia de servidores externos. La inspección estática confirmó seis gráficos, cero scripts remotos y la preservación de sus valores. **En esta sesión no se completó una prueba de renderizado en navegador automatizado** porque el entorno bloqueó el acceso automatizado a las páginas locales (`ERR_BLOCKED_BY_ADMINISTRATOR`); por ello la lectura visual final en Chrome/Edge —especialmente a 550 px de ancho y en pantalla de proyección— queda **pendiente de comprobación directa**, y no se afirma que los solapamientos se hayan medido empíricamente.

**Validación con usuarios pendiente.** Para contrastar efectividad real, sugerimos una pequeña prueba de tareas con lectoras/es representativos: encontrar el mínimo anual, comparar porcentajes de actores en 2025, identificar la franja de mayor gravedad y localizar la celda más alta de motociclistas. Registrar exactitud, tiempo y errores de interpretación antes de atribuir una mejora empírica. Para probar el **dominio**, validar con los responsables de movilidad que las preguntas y el denominador de cada indicador corresponden a su necesidad de decisión.

**Conclusión de diseño.** Ninguna visualización requiere sustitución. Las mejores correcciones son pequeñas, reversibles y orientadas a fidelidad de lectura; conservar los tipos actuales ofrece una mejor relación entre precisión, continuidad narrativa y carga cognitiva que un rediseño general.

## Referencias

- Munzner, T. (2009). *A nested model for visualization design and validation*. *IEEE Transactions on Visualization and Computer Graphics, 15*(6), 921–928. https://doi.org/10.1109/TVCG.2009.111
- Mackinlay, J. (1986). *Automating the design of graphical presentations of relational information*. *ACM Transactions on Graphics, 5*(2), 110–141. https://doi.org/10.1145/22949.22950
- Cleveland, W. S., & McGill, R. (1984). *Graphical perception: Theory, experimentation, and application to the development of graphical methods*. *Journal of the American Statistical Association, 79*(387), 531–554. https://doi.org/10.1080/01621459.1984.10478080
