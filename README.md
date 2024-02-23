# Análisis de Datos sobre Incendios en la República Argentina

### Introducción

Los incendios forestales en Argentina tienen diversos motivos, entre ellos, los tipos de clima extremo en la zona norte del país, en conjunto con climas áridos y secos, la escasez de precipitaciones y la quema ilegal de pastizales para la siembra de diferentes cultivos.

Hacer un análisis para determinar las áreas donde es necesario reforzar la educación y conciencia sobre la realización controlada de fuego, así como las medidas y herramientas esenciales que deben considerarse al llevar a cabo esta actividad en lugares donde podrían provocar incendios forestales. Estos incidentes suelen resultar en la quema de extensas hectáreas de fauna autóctona.

![Imagen_provincias](Imagenes\mapa-incendios-12-provincias.webp)

Fuente: https://www.minutouno.com/sociedad/delta/incendios-forestales-doce-provincias-reportaron-focos-activos-n5537199

En el PDF proporcionado en este [enlace](enero_2024.pdf) se encuentra diversa información que puede ser de gran utilidad para la recomendación y prevención de incendios.

| Provincias            | Total de hectáreas afectadas en 2022 (enero/octubre)  |
|-----------------------|-------------------------------------------------------|
| Corrientes            | 147724                                                |
| San Luis              | 98369                                                 |
| Chubut                | 80226                                                 |
| La Pampa              | 41584                                                 |
| Salta                 | 38871                                                 |
| La Rioja              | 36056                                                 |
| Catamarca             | 22778                                                 |
| Mendoza               | 16081                                                 |
| Río Negro             | 12901                                                 |
| Jujuy                 | 11461                                                 |
| Santiago del Estero   | 9468                                                  |
| Tucumán               | 9133                                                  |
| Formosa               | 8207                                                  |
| Chaco                 | 8189                                                  |
| Córdoba               | 7539                                                  |
| Neuquén               | 4195                                                  |
| Santa Fe              | 3503                                                  |
| Entre Ríos            | 3276                                                  |
| San Juan              | 1403                                                  |
| Buenos Aires          | 142                                                   |
| Misiones              | 49                                                    |
| Santa Cruz            | 10                                                    |
| Total                 | 561164                                                |

Para realizar este proyecto, se utilizó la página del gobierno argentino, la cual tiene este [enlace](https://datos.gob.ar/dataset/ambiente-incendios-forestales). De aquí se obtuvieron los conjuntos de datos necesarios para llevar a cabo el trabajo.

### Objetivo

El objetivo de este proyecto sobre incendios forestales en Argentina, es llevar a cabo un análisis de datos, visualización mediante un dashboard y plantear un KPI:

- Reducir en un 10% los focos de incendios en comparacion con el semestre anterior.

# Proyecto

## Estructura del repositorio

* **Datasets**: Contiene la información con los archivos recaudados para el proyecto en formato CSV. Para visualizarlo, haga clic [aquí](Datasets)

* **Imágenes**: Contiene las imágenes que se utilizarán en el README y en el EDA. Para visualizarlo, haga clic [aquí](Imagenes)

* **ETL**: Incluye las cargas de los datasets y las transformaciones pertinentes de los datos. Para visualizarlo, haga clic [aquí](ETL.ipynb)

* **EDA**: Contiene el Análisis Exploratorio de Datos y las transformaciones necesarias para consumirlas desde el dashboard. Para visualizarlo, haga clic [aquí](EDA.ipynb)

* **Funciones.py**: Es el módulo utilizado para realizar análisis de los datos y reducir tareas repetitivas. Para visualizarlo, haga clic [aquí](Herramientas.py)

* **Py_incendios.pbix**: Contiene el dashboard, el cual puede ser descargado para revisar. Para visualizarlo, haga clic [aquí]()

## ETL

El proceso de Extracción, Transformación y Carga (ETL) fue la primera etapa llevada a cabo en este proyecto. Iniciamos con la carga de un conjunto de datos llamado "incendios_2023", que contenía información sobre los incendios ocurridos por mes y año. Además, se cargaron otros cuatro dataframes con información sobre focos de incendio e incendios por regiones del país.

Proseguimos con la transformación de los datos, realizando tareas como la revisión de todos los tipos de datos de cada columna y la identificación de valores nulos. Los datos eran muy concisos y no presentaban duplicados. Normalizamos valores que, debido a una letra en mayúscula o un espacio, se contabilizaban como diferentes; por ejemplo, 'Sgo. del Estero' y 'Santiago del Estero'. Otra transformación consistió en cambiar valores flotantes por numéricos para contabilizar correctamente los nulos.

Además, agregamos columnas para facilitar el desarrollo del dashboard interactivo en Power BI. Para visualizarlo, haga clic [aquí].

## EDA

El Análisis Exploratorio de Datos fue la segunda etapa llevada a cabo en este proyecto. Consistió en la carga de los DataFrames resultantes del ETL.

Posteriormente, se realizaron visualizaciones específicas para cada DataFrame. El lineplot (gráfico de líneas) fue la elección principal. También se utilizaron otros tipos de gráficos, como un mapa interactivo, que puede no visualizarse directamente en GitHub. Para ello, se proporciona este [enlace](https://nbviewer.org/github/MaximilianoTauil/Incendios/blob/main/EDA.ipynb), que permite ver el notebook completo de EDA, incluyendo el mapa.

Con estos gráficos y una función de nuestro módulo 'Funciones', que nos permitía revisar el conteo de valores y el porcentaje que representaban del total, se extrajeron conclusiones de todo el análisis, tanto de gráficos como de descripciones generales, junto con una justificación de por qué se eligió ese tipo de gráfico. Para visualizarlo, haga clic [aquí](EDA.ipynb).

## KPI

Se dara una breve definicion de kpi para diferenciarlos de las metricas:

 * Un KPI es una métrica específica que evalúa el desempeño de una entidad en relación con sus metas estratégicas. Se utilizan para medir el progreso hacia objetivos, ofreciendo una visión clara del rendimiento en áreas críticas. Los KPIs son seleccionados con cuidado por su conexión directa con los factores clave de éxito, facilitando la toma de decisiones informadas en una organización.

El KPI planteados para este proyecto son : 

* Reducir en un 10% los focos de incendios en comparacion con el semestre anterior.

La fórmula para su cálculo es: 

<br>

![Imagen3]()


# Conclusiones

Los valores generales obtenidos de las conclusiones del EDA son: 

- Se observaron algunos valores que presentaban marcadas diferencias con los demás, lo que indica una gran dispersión de datos en casi todos los dataframes.

- Las épocas de mayor actividad son el invierno y la primavera.

- El año 2022 se destacó como el período con la mayor incidencia de incendios a nivel nacional, alcanzando su punto máximo en septiembre con un total de 496 incendios.

- Las cinco primeras provincias, Santa Fe, Formosa, Corrientes, Chaco y Santiago del Estero, que presentan la mayor cantidad de focos, se encuentran en la región norte del país, donde generalmente se experimentan climas con temperaturas muy altas.

- El máximo de focos se registra en la provincia de Santa Fe, que tuvo un total de 260,116.

- La mayoría de las provincias experimentan un aumento en el número de focos de incendio durante los meses de julio, seguido de un descenso a partir de septiembre.

- Durante el primer semestre del año, se observa la menor cantidad de focos de incendio.

- El NOA, conformado por las provincias de Jujuy, Salta, Tucumán, Catamarca, La Rioja y Santiago del Estero, fue la región con mayor presencia de incendios en el año 2023.

# Contacto

Si tienes preguntas, comentarios o sugerencias, no dudes en ponerte en contacto conmigo a través de las siguientes vías:

Correo Electrónico: maxi.tauil@gmail.com

¡Gracias!