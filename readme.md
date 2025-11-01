🎵 **Música en la Gran Ciudad.**

📊 **Proyecto de Analítica de Datos.**

**Autor:** Edwin Herrera
**Lenguaje:** Python
**Librerías utilizadas:** pandas, numpy, os
**Tipo de proyecto:** Exploración y análisis de datos (EDA)
**Nivel:** Analista de Datos Jr. — Intermedio

⚙️**Configuración del entorno:**

Para garantizar la correcta ejecución del proyecto, se recomienda crear un entorno virtual y usar las dependencias listadas en requirements.txt.

``` sh
1️⃣ Crear el entorno virtual
python -m venv venv

2️⃣ Activarlo (Windows)
. ./.venv/Scripts/activate

 3️⃣ Activarlo (Mac / Linux)
source venv/bin/activate

4️⃣ Instalar las dependencias
pip install -r requirements.txt

```


🧩 **Descripción general**

Este proyecto analiza los *hábitos musicales en dos ciudades ficticias: Springfield y Shelbyville*, con el objetivo *de comparar la actividad de los usuarios, sus preferencias de género y los momentos del día en que más escuchan música.*

El propósito principal es *practicar y demostrar dominio en la limpieza, exploración y análisis de datos reales usando Python*, empleando buenas prácticas de estilo y lógica de programación.

Como parte complementaria, se incluye un *archivo adicional de verificación de núcleos del CPU*, que evalúa los recursos del equipo desde el cual se ejecuta el notebook, como una curiosidad técnica relacionada con la *optimización y desempeño computacional durante la ejecución del análisis.*

🧠 **Objetivos**

-1. *Analizar patrones de comportamiento musical* según ciudad y día de la semana.

-2. *Identificar géneros más escuchados* en diferentes horarios y ciudades.

-3. *Comprobar hipótesis* sobre diferencias en gustos musicales entre Springfield y Shelbyville.

-4. *Aplicar técnicas de limpieza de datos profesionales* (detección y corrección de duplicados, valores nulos, normalización de texto).

-5. *Monitorear el entorno de ejecución*, verificando el rendimiento de CPU mediante el archivo complementario.

⚙️ **Estructura del proyecto:**

``` sh 
    Musica-en-la-Gran-Ciudad/
│
├── data/
│   └── music_project_en.csv
│
├── scripts/
│   ├── musica_en_la_gran_ciudad.py
│   └── nucleos_del_CPU.py
│
└── README.md


```
🧹 **Etapas del análisis:**

1️⃣  Carga y exploración inicial

*1-Lectura del dataset con* ``` pandas.read_csv() ``` 

*2-Inspección general* ``` (.info(), .describe(), .head())```


2️⃣ **Limpieza y preparación:**

*1-Estandarización de nombres de columnas.* ``` (snake_case) ``` 

*2-Reemplazo de valores nulos con.* ``` 'unknown' ``` 

*3-Eliminación de duplicados.*

*4-Corrección de duplicados implícitos.* ``` ('hip-hop', 'hip', 'hop' → 'hiphop') ``` 

3️⃣ **Análisis comparativo:**

*1-Conteo de reproducciones por ciudad y día.*

*2-Análisis de los géneros más escuchados por hora y día*

*3-Validación de hipótesis sobre patrones de comportamiento.*

4️⃣ **Resultados y conclusiones:**

*1-Springfield presenta mayor actividad musical los lunes y viernes.*

*2-Shelbyville muestra mayor actividad los miércoles.*

*3-En ambas ciudades predomina el género Pop.*

*4-Las diferencias musicales entre ciudades son mínimas.**

🧪 **Cómo ejecutar el proyecto**

📘 **Opción 1: Desde el Notebook:**

*1. Abre el archivo musica_en_la_gran_ciudad.ipynb en Jupyter Notebook, Colab o VSCode.*

*2. Ejecuta las celdas en orden.*

*3. Visualiza las conclusiones directamente en el notebook.*

🐍 **Opción 2: Desde consola (versión .py)**

``` sh
 python musica_en_la_gran_ciudad.py
 
 ``` 
⚙️ **Opción 3: Verificar los recursos del sistema**

**Para ejecutar el script de núcleos del CPU:**

``` sh 
python nucleos_del_CPU.py

```
Este archivo imprime información sobre los núcleos disponibles, útil para comprender la capacidad del sistema al procesar datasets más grandes.

📈 **Habilidades demostradas:**

*1. -Limpieza y normalización de datos con pandas.*

*2. -Agrupaciones y filtrado condicional.*

*3. -Creación de funciones analíticas personalizadas.*

*4. -Manejo de valores nulos y duplicados.*

*5. -Validación de hipótesis mediante análisis exploratorio.*

*6. -Comprensión del entorno técnico (CPU, optimización básica).*

💬 **Conclusión general:**

Este proyecto combina el análisis exploratorio con la práctica del pensamiento crítico.
A través de un dataset musical, se demostraron técnicas sólidas de preprocesamiento y análisis, generando conclusiones interpretables y reproducibles.

Además, el análisis del CPU introduce un enfoque curioso y profesional sobre cómo el entorno de ejecución puede influir en la eficiencia de un proyecto de datos.
