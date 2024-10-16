# Methane-Emissions

Preparación y Limpieza de Datos

En esta sección del proyecto, nos enfocamos en transformar los datos crudos sobre emisiones de metano en un formato adecuado para su visualización en Power BI. A continuación, se detallan los pasos clave y las decisiones tomadas:

1. Carga y Exploración Inicial:

Fuente de datos: Los datos se obtuvieron de la EPA (Agencia de Protección Ambiental de Estados Unidos) y se almacenaron en Google Drive.
Lectura de datos: Se utilizaron las bibliotecas de Python Pandas para cargar los datos en DataFrames, que son estructuras de datos tabulares similares a hojas de cálculo.
Análisis exploratorio: Se aplicaron funciones como info() para obtener un resumen de las columnas, tipos de datos y dimensiones de los DataFrames. Esto permitió comprender la estructura general de los datos y identificar posibles problemas.

2. Limpieza de Datos:

-Manejo de valores faltantes: Se identificaron los valores faltantes (NaN) en las columnas, especialmente en la columna de emisiones de metano. Se decidió reemplazar estos valores por ceros, asumiendo que indican la ausencia de datos.
-Conversión de tipos de datos: La columna de año se convirtió a un formato de fecha para facilitar el análisis temporal.
-Eliminación de columnas innecesarias: Se eliminaron columnas que no aportaban información relevante para el análisis, como direcciones secundarias.
-Unificación de datos: Se combinaron los dos conjuntos de datos iniciales (emisiones y facilidades emisoras) utilizando un left join basado en el identificador de la instalación. Esto permitió relacionar las emisiones con información adicional sobre las instalaciones.
-Limpieza de texto: Se eliminaron caracteres especiales y se normalizaron los nombres de las columnas para facilitar el análisis y la visualización.

3. Tratamiento de valores atípicos:

-Valores extremos: Se analizaron los valores extremos en las columnas numéricas para identificar posibles errores o outliers. Sin embargo, no se realizaron ajustes en este caso, ya que no se detectaron valores claramente anómalos.
-Inconsistencias: Se verificaron las consistencias entre las diferentes columnas para asegurar la integridad de los datos.

Justificación de las decisiones:

-Reemplazar valores faltantes por ceros: Se asumió que la ausencia de datos de emisiones indicaba que no se registraron emisiones en ese período. Sin embargo, esta decisión podría revisarse en futuros análisis si se dispone de más información.
-Eliminar columnas innecesarias: Se eliminaron columnas que no eran relevantes para el objetivo del análisis, con el fin de simplificar el modelo de datos y mejorar el rendimiento.
-Unificar datos: La unión de los dos conjuntos de datos permitió obtener una visión más completa de las emisiones, relacionando las emisiones con las características de las instalaciones.

Herramientas y bibliotecas utilizadas:

Pandas: Biblioteca fundamental para la manipulación y análisis de datos en Python.
NumPy: Biblioteca para realizar operaciones numéricas y trabajar con arrays.
Matplotlib: Biblioteca para crear visualizaciones estáticas.
Plotly: Biblioteca para crear visualizaciones interactivas.

Conclusión:

La preparación y limpieza de datos es una etapa crucial en cualquier proyecto de análisis de datos. Al seguir estos pasos, se garantiza que los datos sean precisos, consistentes y adecuados para su visualización en Power BI.

Creación del Dashboard en Power BI

Una vez que los datos han sido limpiados y preparados en Python, el siguiente paso es crear un dashboard interactivo en Power BI para visualizar los resultados. A continuación, se detalla el proceso:

Importar los datos:

-Conectar a la fuente de datos: Importa el archivo CSV  generado por Python a Power BI.
-Crear una nueva tabla: Define una nueva tabla en Power BI basada en los datos importados.

Crear relaciones:

-Identificar las claves: Identifica las columnas que relacionan las diferentes tablas (por ejemplo, facility_id).
-Establecer relaciones: Crea relaciones entre las tablas en el modelo de datos de Power BI.


Visualizaciones clave:

-Emisiones de metano por año y sector: Un gráfico de barras apiladas que muestra la evolución de las emisiones a lo largo del tiempo, desglosadas por sector industrial.
-Emisiones de metano por empresa y fuente: Se decide utilizar una tabla resaltando las columnas con colores para mostrar los datos de una manera mas adecuada ya que al haber tantos nombres presentes en una grafica no se verian muy bien los resultados  de las emisiones de diferentes empresas, clasificadas por tipo de emisión.
-Mapa de calor de emisiones por estado: Un mapa que muestra geográficamente las emisiones de metano en cada estado.

Beneficios adicionales de Power BI:

Interactividad: Permite a los usuarios explorar los datos de forma dinámica mediante filtros y slicers.
Colaboración: Facilita la colaboración en equipos, permitiendo compartir y actualizar el dashboard.
Integración: Se puede integrar con otras herramientas de Microsoft y de terceros.

 
