from matplotlib import pyplot as plt
import numpy as np
from collections import Counter
from sklearn import datasets
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

#se especifica google drive como fuente de los archivos
from google.colab import drive
drive.mount('/content/drive')

# Cargar un archivo ef_w_emissions_source_ghg.csv
emissions_data= pd.read_csv("/content/drive/MyDrive/EF_W_EMISSIONS_SOURCE_GHG.csv")


# con este metood se obtiene un resumen de los datos que cargamos
emissions_data.info()


# cambiamos el formato de reporting_year
emissions_data['reporting_year'] = pd.to_datetime(emissions_data['reporting_year'], format='%Y')
emissions_data.dtypes

# identificar cantidad de valores Nan en las columnas.
emissions_data.isnull().sum()

'''Se asume que los valores NaN correspondientes a la columna  total_reported_ch4_emissions 
los cuales corresponden a un 21.21% muy seguramente estan asociados a que no se reportaron emisiones 
de metano entonces se decide reemplazar por 0 (cero) para tener una mejor visualizacion.'''

emissions_data['total_reported_ch4_emissions'].fillna(0, inplace=True)
emissions_data.isnull().sum()


'''**Carga y limpeza de la tabla rlps_ghg_emitter_facilities**'''

# Carga de  los datos de la seguda tabla  y repetimos el procedimeinto .info ()

emitter_facilities= pd.read_csv("/content/drive/MyDrive/rlps_ghg_emitter_facilities.csv")
emitter_facilities.info()


# Chequeo de columna adress2
emitter_facilities['address2'].value_counts()

#Se elimina la columna 'address2' ya que no tiene datos

emitter_facilities.drop('address2', axis=1, inplace=True)
emitter_facilities.info()

# Cambio de formato de la columna 'year'
emitter_facilities['year'] = pd.to_datetime(emitter_facilities['year'], format='%Y')
emitter_facilities.dtypes

'''Ahora prcedemos a unir los dos dataframes a traves de un left join. 
El uso de este Join preserva todas las filas del 'emissions_data' data
frame incluso si no hay filas que hagan match en el 'facilities_data' data frame.'''

# Join 
emisiones = emissions_data.merge(emitter_facilities, on='facility_id', how='left')
emisiones.info()

# Cambio de nombre de la columna 'facility_name_x' a 'facility_name'
emisiones1=emisiones.rename(columns={'facility_name_x': 'facility_name'})
emisiones1.info()

#Se eliminamos la columna facility_name_y ya que es igual a facility name
emisiones1.drop('facility_name_y', axis=1, inplace=True)
emisiones1.head()

'''Se elimina todo lo que esta entre parentesis en la columna parent comany 
con el fin de que no afecte las visualizaciones que  se realizaran posterioermente.'''

emisiones1['parent_company'] = emisiones1['parent_company'].str.split(' \(').str[0]
emisiones1['parent_company']


#Chequeo del tipo de informacion contiene la columna reporting_category
emisiones1['reporting_category'].value_counts()

'Se procede a eliminar la informacion contenida entre corchetes de la columna reporting_category'

# Crear una nueva columna para los valores entre corchetes
emisiones1['reportingcopy'] = emisiones1['reporting_category'].str.extract(r'\[(.*?)\]')

# Eliminar la parte entre corchetes de la columna original
emisiones1['reporting_category'] = emisiones1['reporting_category'].str.replace(r' \[.*?\]', '', regex=True)



# Limpieza de  la columna basin_associated_with_facility Eliminando los numeros de los nombres en las filas 

emisiones1['basin_associated_with_facility'] = emisiones1['basin_associated_with_facility'].str.replace(r'^\d+ - ', '', regex=True)

emisiones1['basin_associated_with_facility'].value_counts()

# Al igual  que en la columna reporting_segment aplicamos en industry_segment el mismo procedimiento
emisiones1['industry_segment'] = emisiones1['industry_segment'].str.replace(r' \[.*?\]', '', regex=True)
emisiones1['industry_segment'].value_counts()

# Se puede notar que hay presentes variso espacios en blanco pertenecientes a la colunma basin_associated_with_facility 
emisiones1[['facility_name','basin_associated_with_facility']]

'''Utilizando el nombre de la fabrica o central tomado como ejemplo burlington generating station 
se realiza una investicagion dand como resultado que dicha planta esta asociada 
#a la cuenca del rio Mississipi. Se realiza la tarea de reemplazar dicha informacion en la columna
# basin_associated_with_facility. '''   


# Convertir a minúsculas para evitar problemas de mayúsculas y minúsculas
emisiones1['facility_name'] = emisiones1['facility_name'].str.lower()
emisiones1['basin_associated_with_facility'] = emisiones1['basin_associated_with_facility'].fillna('')

# Llenar los valores faltantes, considerando posibles variaciones en el nombre
emisiones1.loc[(emisiones1['facility_name'].str.contains('burlington generating station')) &
               (emisiones1['basin_associated_with_facility'] == ''),
               'basin_associated_with_facility'] = 'Mississippi River'

'''En el momento constatar que la anterior operacion fuera satisfactoria se puede todar que los datos
estan presentes en la columna pero no son visibles, Entonces se procede
a verificar si hay valores no vacios en la columna de la siguiente fomra:  '''  

# Verificar si hay valores no vacíos que podrían interpretarse como vacíos
non_empty_values = emisiones1[emisiones1['basin_associated_with_facility'].str.strip() != '']

if not non_empty_values.empty:
    print("There are non-empty values in 'basin_associated_with_facility':")
    print(non_empty_values)

'''Teniendo en cuenta el resultado anteior se pudo verificar que los valores estan presentes 
pero no se pueden ver en la columna. En este punto de la investigacion se decide continuar 
pues luego de varios intentos no es podible lograr una correcta visualizacion de la columna'''   

# se Intenta generar una visualizacion  de las requieridas en el proyecto 
# pero debido a la cantidad de datos Google Colab no pudo generar el grafico requerido.


def create_chart(df, start_year=None, end_year=None, basins=None):
    # Fitro por year range 
    if start_year and end_year:
        df = df[(df['reporting_year'] >= start_year) & (df['reporting_year'] <= end_year)]

    # Filtro por basins
    if basins:
        df = df[df['basin_associated_with_facility'].isin(basins)]

    # Extract the list of industry segments
    industry_segments = df['industry_segment'].tolist()

    # Crear grafico de barras

    legend_name = "Total Methane Emissions by Industry Segment"  


    fig = go.Figure(data=[
    go.Bar(
        x=df['reporting_year'],
        y=df['total_reported_ch4_emissions'],
        name=legend_name, 
        hovertemplate='Year: %{x}<br>Emissions: %{y}<br>Industry: %{customdata[0]}'  
    )
])


    fig.update_layout(
    title='Methane Emissions vs. Year (Stacked by Industry Segment)',
    xaxis_title='Year',
    yaxis_title='Methane Emissions',
    barmode='stack'
    )
    return fig

fig = create_chart(emisiones1)
fig.show()