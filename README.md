# **Repositorio de Estadística de la Probabilidad**

Este repositorio contiene las notas y ejemplos de código en **Python** de la especialización en  **Estadística y Probabilidad** , organizado en clases y cubriendo los temas de inferencia estadística, muestreo, y distribuciones de probabilidad. Cada tema incluye explicaciones detalladas, fórmulas en LaTeX y ejemplos prácticos.

---

## **Tabla de Contenidos**

### **Clase 1: Introducción a las Variables Aleatorias**

1. **Variables Aleatorias** :

* **Discretas vs. Continuas** : Definiciones, diferencias y ejemplos.
* Ejemplo práctico en Python para simular variables aleatorias.

### **Clase 2: Variables Aleatorias Discretas**

1. **Definición** y **propiedades** de las variables discretas.
2. **Ejemplos clásicos** de distribuciones discretas.
3. **Simulaciones en Python** :

* Ejemplo de simulación de lanzamientos de una moneda (Bernoulli).
* Ejemplo de simulación de experimentos binomiales.

### **Clase 3: Variables Aleatorias Continuas**

1. **Definición** y características de las variables continuas.
2. **Ejemplos y gráficos** de distribuciones continuas.
3. **Simulaciones en Python** :

* Generación de números aleatorios para distribuciones continuas (Uniforme, Normal).

### **Clase 4: Distribuciones de Probabilidad**

1. **Distribuciones de Probabilidad** :

* Descripción general para **variables discretas** (Función de Masa de Probabilidad, FMP).
* Descripción para **variables continuas** (Función de Densidad de Probabilidad, FDP).

1. **Distribuciones Discretas:**
   * **Valor esperado** y  **varianza** .
   * Implementación de cálculos en Python.
2. **Distribuciones Continuas:**
   * Distribuciones como la **normal** y  **uniforme** .
   * Uso de Python para la simulación y visualización de estas distribuciones.

### **Muestreo e Inferencia Estadística**

1. **Objetivo de la Inferencia Estadística** : Generalizaciones y predicciones basadas en muestras.
2. **Métodos de Muestreo** :

* **Muestreo Aleatorio Simple** .
* **Muestreo Estratificado** : Definición, ventajas y desventajas.
* **Muestreo Sistemático** : Definición, ventajas, desventajas y pasos.
* **Muestreo por Conglomerados** : Definición y aplicación.

1. **Propiedades de los Estimadores** :

* **Insesgadez** ,  **consistencia** , **eficiencia** y  **suficiencia** .

---

## **Instrucciones para Usar el Repositorio**

Este repositorio está diseñado para funcionar como un material de referencia y estudio práctico. Puedes clonar el repositorio y ejecutar los ejemplos en Python directamente para ver los resultados de las simulaciones.

### **Requisitos**

* Python 3.x
* Librerías necesarias: `numpy`, `matplotlib`, `scipy`, `pandas`

Para instalar las librerías necesarias, puedes ejecutar:

<pre class="!overflow-visible"><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative"><div class="flex items-center text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9">bash</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-main-surface-secondary px-2 font-sans text-xs text-token-text-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor" data-darkreader-inline-fill=""></path></svg>Copy code</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">pip install numpy matplotlib scipy pandas</code></div></div></pre>
