**Estadística de la Probabilidad**

**Clase L-611**

**Tipo:** Presencial

**Días:** Sábado

**Estado:** En progreso

**Clase #1**

**Syllabus**

* 144 horas de estudio
* Plan temático:
  * Fundamentos de estadística para la analítica de datos
  * Visualización, exploración y descripción de negocios
  * Distribuciones de probabilidad discretas y continuas
  * Introducción al muestreo
  * Intervalos de confianza
  * Pruebas de hipótesis
  * Análisis de regresión
* Porcentaje de notas:
  * Fase 1: Actividad 1 - individual (13%), Actividad 2 - Grupal (12%)
  * Fase 2: Actividad 1 - individual (13%), Actividad 2 - Grupal (12%)
  * Fase 3: Actividad Final

**¿Qué es la Estadística?**

La estadística es la rama de las matemáticas que se ocupa de recopilar, organizar, analizar e interpretar datos para hacer inferencias y tomar decisiones fundamentadas. Se utiliza en diversos campos como economía, biología, sociología, e ingeniería, entre otros.

**Tipos de Estadística**

* Estadística Descriptiva: Se encarga de resumir y organizar los datos obtenidos en un estudio mediante tablas, gráficos, y medidas numéricas (promedio, mediana, moda, etc.).
* Estadística Inferencial: Permite hacer predicciones o inferencias sobre una población basándose en los datos obtenidos de una muestra. Se basa en la teoría de la probabilidad para generalizar los resultados.

**Aplicaciones de la Estadística**

* Ciencia: Para analizar datos experimentales y formular conclusiones.
* Negocios: Para predecir tendencias del mercado, evaluar el rendimiento de productos o servicios.
* Medicina: Para evaluar la eficacia de tratamientos a través de ensayos clínicos.

**Ejemplo en Python: Visualización de Datos Estadísticos**

<pre><div class="relative w-full font-sans codeblock bg-zinc-950"><div class="flex items-center justify-between w-full px-6 py-2 pr-4 bg-zinc-800 text-zinc-100"><span class="text-xs lowercase">python</span><div class="flex items-center space-x-1"><button class="inline-flex items-center justify-center rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none disabled:pointer-events-none disabled:opacity-50 shadow-none hover:text-accent-foreground h-8 w-8 p-0 hover:bg-zinc-800 focus-visible:ring-1 focus-visible:ring-slate-700 focus-visible:ring-offset-0"><svg class="h-4 w-4" width="15" height="15" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M11.8536 1.14645C11.6583 0.951184 11.3417 0.951184 11.1465 1.14645L3.71455 8.57836C3.62459 8.66832 3.55263 8.77461 3.50251 8.89155L2.04044 12.303C1.9599 12.491 2.00189 12.709 2.14646 12.8536C2.29103 12.9981 2.50905 13.0401 2.69697 12.9596L6.10847 11.4975C6.2254 11.4474 6.3317 11.3754 6.42166 11.2855L13.8536 3.85355C14.0488 3.65829 14.0488 3.34171 13.8536 3.14645L11.8536 1.14645ZM4.42166 9.28547L11.5 2.20711L12.7929 3.5L5.71455 10.5784L4.21924 11.2192L3.78081 10.7808L4.42166 9.28547Z" fill="currentColor" fill-rule="evenodd" clip-rule="evenodd"></path></svg><span class="sr-only">Edit</span></button><button class="inline-flex items-center justify-center rounded-md font-medium ring-offset-background transition-colors focus-visible:outline-none disabled:pointer-events-none disabled:opacity-50 shadow-none hover:text-accent-foreground h-8 w-8 p-0 text-xs hover:bg-zinc-800 focus-visible:ring-1 focus-visible:ring-slate-700 focus-visible:ring-offset-0"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" fill="currentColor" class="h-4 w-4"><path d="M216 32H88a8 8 0 0 0-8 8v40H40a8 8 0 0 0-8 8v128a8 8 0 0 0 8 8h128a8 8 0 0 0 8-8v-40h40a8 8 0 0 0 8-8V40a8 8 0 0 0-8-8Zm-56 176H48V96h112Zm48-48h-32V88a8 8 0 0 0-8-8H96V48h112Z"></path></svg><span class="sr-only">Copy code</span></button></div></div><div><code><span class="linenumber react-syntax-highlighter-line-number">1</span><span class="token">import</span><span> matplotlib</span><span class="token">.</span><span>pyplot </span><span class="token">as</span><span> plt
</span><span class="linenumber react-syntax-highlighter-line-number">2</span>
<span class="linenumber react-syntax-highlighter-line-number">3</span><span></span><span class="token"># Datos de ejemplo: edades de un grupo de personas</span><span>
</span><span class="linenumber react-syntax-highlighter-line-number">4</span><span>edades </span><span class="token">=</span><span></span><span class="token">[</span><span class="token">22</span><span class="token">,</span><span></span><span class="token">25</span><span class="token">,</span><span></span><span class="token">30</span><span class="token">,</span><span></span><span class="token">35</span><span class="token">,</span><span></span><span class="token">40</span><span class="token">,</span><span></span><span class="token">28</span><span class="token">,</span><span></span><span class="token">32</span><span class="token">,</span><span></span><span class="token">45</span><span class="token">,</span><span></span><span class="token">50</span><span class="token">,</span><span></span><span class="token">28</span><span class="token">,</span><span></span><span class="token">30</span><span class="token">,</span><span></span><span class="token">37</span><span class="token">]</span><span>
</span><span class="linenumber react-syntax-highlighter-line-number">5</span>
<span class="linenumber react-syntax-highlighter-line-number">6</span><span></span><span class="token"># Crear histograma para visualizar la distribución de edades</span><span>
</span><span class="linenumber react-syntax-highlighter-line-number">7</span><span>plt</span><span class="token">.</span><span>hist</span><span class="token">(</span><span>edades</span><span class="token">,</span><span> bins</span><span class="token">=</span><span class="token">5</span><span class="token">,</span><span> edgecolor</span><span class="token">=</span><span class="token">'black'</span><span class="token">)</span><span>
</span><span class="linenumber react-syntax-highlighter-line-number">8</span><span>plt</span><span class="token">.</span><span>title</span><span class="token">(</span><span class="token">'Distribución de Edades'</span><span class="token">)</span><span>
</span><span class="linenumber react-syntax-highlighter-line-number">9</span><span>plt</span><span class="token">.</span><span>xlabel</span><span class="token">(</span><span class="token">'Edades'</span><span class="token">)</span><span>
</span><span class="linenumber react-syntax-highlighter-line-number">10</span><span>plt</span><span class="token">.</span><span>ylabel</span><span class="token">(</span><span class="token">'Frecuencia'</span><span class="token">)</span><span>
</span><span class="linenumber react-syntax-highlighter-line-number">11</span><span>plt</span><span class="token">.</span><span>show</span><span class="token">(</span><span class="token">)</span></code></div></div></pre>

**Fórmulas Clave**

* Media (Promedio): `x̄ = ∑(x_i) / n`
* Varianza: `σ^2 = ∑(x_i - x̄)^2 / n`

**Variables y sus Tipos**

* Una variable es una característica o atributo que puede tomar diferentes valores.
* Tipos de variables:
  * Variables Cualitativas (Categóricas): Describen categorías o cualidades y no se expresan mediante números.
  * Variables Cuantitativas (Numéricas): Representan cantidades y se expresan mediante números.

**Ejemplo en Python: Variables Cuantitativas y Temporales**

<pre><div class="relative w-full font-sans codeblock bg-zinc-950"><div class="flex items-center justify-between w-full px-6 py-2 pr-4 bg-zinc-800 text-zinc-100"><span class="text-xs lowercase">python</span><div class="flex items-center space-x-1"><button class="inline-flex items-center justify-center rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none disabled:pointer-events-none disabled:opacity-50 shadow-none hover:text-accent-foreground h-8 w-8 p-0 hover:bg-zinc-800 focus-visible:ring-1 focus-visible:ring-slate-700 focus-visible:ring-offset-0"><svg class="h-4 w-4" width="15" height="15" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M11.8536 1.14645C11.6583 0.951184 11.3417 0.951184 11.1465 1.14645L3.71455 8.57836C3.62459 8.66832 3.55263 8.77461 3.50251 8.89155L2.04044 12.303C1.9599 12.491 2.00189 12.709 2.14646 12.8536C2.29103 12.9981 2.50905 13.0401 2.69697 12.9596L6.10847 11.4975C6.2254 11.4474 6.3317 11.3754 6.42166 11.2855L13.8536 3.85355C14.0488 3.65829 14.0488 3.34171 13.8536 3.14645L11.8536 1.14645ZM4.42166 9.28547L11.5 2.20711L12.7929 3.5L5.71455 10.5784L4.21924 11.2192L3.78081 10.7808L4.42166 9.28547Z" fill="currentColor" fill-rule="evenodd" clip-rule="evenodd"></path></svg><span class="sr-only">Edit</span></button><button class="inline-flex items-center justify-center rounded-md font-medium ring-offset-background transition-colors focus-visible:outline-none disabled:pointer-events-none disabled:opacity-50 shadow-none hover:text-accent-foreground h-8 w-8 p-0 text-xs hover:bg-zinc-800 focus-visible:ring-1 focus-visible:ring-slate-700 focus-visible:ring-offset-0"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" fill="currentColor" class="h-4 w-4"><path d="M216 32H88a8 8 0 0 0-8 8v40H40a8 8 0 0 0-8 8v128a8 8 0 0 0 8 8h128a8 8 0 0 0 8-8v-40h40a8 8 0 0 0 8-8V40a8 8 0 0 0-8-8Zm-56 176H48V96h112Zm48-48h-32V88a8 8 0 0 0-8-8H96V48h112Z"></path></svg><span class="sr-only">Copy code</span></button></div></div><div><code><span class="linenumber react-syntax-highlighter-line-number">1</span><span class="token">import</span><span> pandas </span><span class="token">as</span><span> pd
</span><span class="linenumber react-syntax-highlighter-line-number">2</span><span></span><span class="token">import</span><span> matplotlib</span><span class="token">.</span><span>pyplot </span><span class="token">as</span><span> plt
</span><span class="linenumber react-syntax-highlighter-line-number">3</span>
<span class="linenumber react-syntax-highlighter-line-number">4</span><span></span><span class="token"># Crear un DataFrame con datos ficticios de ventas</span><span>
</span><span class="linenumber react-syntax-highlighter-line-number">5</span><span>data </span><span class="token">=</span><span></span><span class="token">{</span><span class="token">'Mes'</span><span class="token">:</span><span></span><span class="token">[</span><span class="token">'Enero'</span><span class="token">,</span><span></span><span class="token">'Febrero'</span><span class="token">,</span><span></span><span class="token">'Marzo'</span><span class="token">,</span><span></span><span class="token">'Abril'</span><span class="token">,</span><span></span><span class="token">'Mayo'</span><span class="token">]</span><span class="token">,</span><span>
</span><span class="linenumber react-syntax-highlighter-line-number">6</span><span></span><span class="token">'Ventas'</span><span class="token">:</span><span></span><span class="token">[</span><span class="token">200</span><span class="token">,</span><span></span><span class="token">250</span><span class="token">,</span><span></span><span class="token">300</span><span class="token">,</span><span></span><span class="token">280</span><span class="token">,</span><span></span><span class="token">320</span><span class="token">]</span><span class="token">}</span><span>
</span><span class="linenumber react-syntax-highlighter-line-number">7</span>
<span class="linenumber react-syntax-highlighter-line-number">8</span><span>df </span><span class="token">=</span><span> pd</span><span class="token">.</span><span>DataFrame</span><span class="token">(</span><span>data</span><span class="token">)</span><span>
</span><span class="linenumber react-syntax-highlighter-line-number">9</span>
<span class="linenumber react-syntax-highlighter-line-number">10</span><span></span><span class="token"># Graficar las ventas a lo largo del tiempo (meses)</span><span>
</span><span class="linenumber react-syntax-highlighter-line-number">11</span><span>plt</span><span class="token">.</span><span>plot</span><span class="token">(</span><span>df</span><span class="token">[</span><span class="token">'Mes'</span><span class="token">]</span><span class="token">,</span><span> df</span><span class="token">[</span><span class="token">'Ventas'</span><span class="token">]</span><span class="token">,</span><span> marker</span><span class="token">=</span><span class="token">'o'</span><span class="token">)</span><span>
</span><span class="linenumber react-syntax-highlighter-line-number">12</span><span>plt</span><span class="token">.</span><span>title</span><span class="token">(</span><span class="token">'Ventas Mensuales'</span><span class="token">)</span><span>
</span><span class="linenumber react-syntax-highlighter-line-number">13</span><span>plt</span><span class="token">.</span><span>xlabel</span><span class="token">(</span><span class="token">'Mes'</span><span class="token">)</span><span>
</span><span class="linenumber react-syntax-highlighter-line-number">14</span><span>plt</span><span class="token">.</span><span>ylabel</span><span class="token">(</span><span class="token">'Ventas'</span><span class="token">)</span><span>
</span><span class="linenumber react-syntax-highlighter-line-number">15</span><span>plt</span><span class="token">.</span><span>show</span><span class="token">(</span><span class="token">)</span></code></div></div></pre>

**Clase #2**

**Relación entre minutos usados e ingreso de clientes**

* Carga de datos
* Ordenación del DataFrame
* Cruce de información
* Visualización de Datos

**Clase #3**

**Distribuciones de Probabilidad**

* Introducción
* Tipos de distribuciones de probabilidad:
  * Distribuciones Discretas
  * Distribuciones Continuas
* Ejemplos de distribuciones de probabilidad:
  * Distribución Binomial
  * Distribución de Poisson
  * Distribución Normal (Gaussiana)
  * Distribución Exponencial

**Variables Aleatorias**

* Introducción
* Tipos de variables aleatorias:
  * Variables Aleatorias Discretas
  * Variables Aleatorias Continuas
* Ejemplos de variables aleatorias:
  * Lanzamiento de un dado
  * Número de llamadas en una hora
  * Temperatura
  * Tiempo de espera

**Distribuciones de Probabilidad Discreta**

* Introducción
* Fórmulas:
  * Valor Esperado (E[X])
  * Varianza (Var(X))
* Ejemplos de distribuciones de probabilidad discreta:
  * Distribución Uniforme
  * Distribución Binomial
  * Distribución Binomial Negativa
  * Distribución de Poisson

**Distribución Uniforme**

* Definición
* Ejemplos
* Fórmulas
* Ejemplo en Python

**Distribución Binomial**

* Definición
* Ejemplos
* Fórmulas
* Ejemplo en Python

**Distribución Binomial Negativa**

* Definición
* Ejemplos
* Fórmulas
* Ejemplo en Python

**Distribución de Poisson**

* Definición
* Ejemplos
* Fórmulas
* Ejemplo en Python

**Distribución Normal (Gaussiana)**

* Definición
* Ejemplos
* Fórmulas
* Ejemplo en Python

**Distribución Exponencial**

* Definición
* Ejemplos
* Fórmulas
* Ejemplo en Python

**Conclusión**

La estadística es una herramienta fundamental para analizar y tomar decisiones basadas en datos. En este curso, hemos cubierto los conceptos básicos de la estadística, incluyendo la estadística descriptiva y la estadística inferencial. También hemos explorado diferentes tipos de distribuciones de probabilidad y variables aleatorias. Esperamos que este curso haya sido útil para ti y que puedas aplicar estos conceptos en tus futuros proyectos y carreras.
