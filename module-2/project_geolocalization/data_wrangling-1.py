#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import folium
from folium import plugins
import pymongo
from pandas.io.json import json_normalize


# In[2]:


"""
Mi plan es algo así:
1. Describir a mi cliente imaginario
2. Inspeccionar la base de datos de Mongo
3. Filtrar la base y crear una nueva base de datos con base en mis requerimientos
4. Pasar esta nueva base a un data frame y ordenar mejor lo de las coordenadas y todo para tenerlo como
   puntos de geolocalización y después hacer searches de eso. 
5. Llegar a las conclusiones con un mapa complementado con cierta investigación de Google. 

"""


# # Paso 1 : Describir a mi cliente imaginario. 

# Mi cliente imaginario es una startup de consultoría con Big Data que quiere estar en un lugar donde haya muchas corporaciones grandes. La propuesta de mi cliente es venderle a grandes compañías (compañías con más de 5,000 empleados) su servicio de análisis de datos patentado por Kike. A mi cliente le gustaría estar cerca de muchas empresas grandes porque ese es su principal cliente y ha encontrado que las reuniones presenciales siempre son más potentes que las videollamadas. Además, es cierto que si estás cerca de muchas empresas grandes, se puede correr la voz de que eres bueno y así tendrás más oportunidades. 

# In[3]:


#Me conecto a la base de datos. 


# In[4]:


client = pymongo.MongoClient()


# In[5]:


db = client.companies_db


# In[6]:


data = db.data


# Vamos a filtrar la base de datos según lo que yo requiero y después la inspeccionaré.
# Los requerimientos de mi cliente son los siguientes:
#     
# 1. Estar con una empresa con más de 5,000 empleados.
# 2. La empresa debe tener mínimo 10 años de haberse fundado. Dado que la propuesta de valor de mi cliente
# depende de que haya una gran base de datos que analizar, se ha descubierto que conviene trabajar con empresas
# que tienen mucho tiempo en la industria. 
# 3. La empresa debe tener al menos una oficina. 

# # Paso 2: Filtrar e inspeccionar la base de datos. Crear una nueva base de datos.

# In[7]:


#Filtramos la base de datos. 

q1 = db.data.find()


# In[8]:


df = pd.DataFrame(q1)
print(set(df.category_code.unique()))


# In[9]:


big_companies = db.data.find({'$and': [{'number_of_employees': {'$gte': 5000}},                                       {'offices':{'$not':{'$size':0}}},                                      {'founded_year': {'$lte': 2010}}]},
                            {'name':1,'category_code':1,'offices':1, 'ipo.valuation_amount':1, '_id':0, 'deadpooled_year':1})


# In[10]:


df = pd.DataFrame(big_companies)
df.head(4)


# In[43]:


df.shape #interesante, tenemos 103 empresas que cumplen con estos requisitos. ¿Dónde estarán?


# In[44]:


df.dtypes #puros objetos, un par de columnas son diccionarios. 


# In[45]:


df.isnull().sum() #esto nos deja ver que ninguna ha quebrado, por lo que podemos ignorar esa columna. 


# In[14]:


df = df.drop(columns=['deadpooled_year', 'ipo']) #la de IPO tampoco nos sirve tanto. 


# In[15]:


#es útil la función de Yona que nos ayuda a encontrar las direcciones de las empresas. 


# In[16]:


def get_first(data):
    res=[]
    ofi=[]
    
    data=data['offices']
    for e in data:
        principal=None   # solo las tienen geodata
        if e[0]['latitude'] and e[0]['longitude']:
            principal={'type':'Point',
                       'coordinates':[
                           e[0]['longitude'],
                           e[0]['latitude']
                       ]}
            
        ofi.append(principal)
        
        res.append({
            'total_offices':len(e),
            'lat':e[0]['latitude'],
            'lng':e[0]['longitude'],
            'oficina_principal':principal
        })
    
    return res, ofi


# In[ ]:


#Aplico la función creando un nuevo data frame. 


# In[18]:


first_office=json_normalize(get_first(df)[0])
first_office['oficina_principal']=get_first(df)[1]
first_office.head()


# In[ ]:


#Pongo esta información limpia junto con la original en un nuevo dataframe. 
#En realidad para mí es un poco indiferente el número de oficinas, por lo que ignoro eso. 
#A pesar de que a mi cliente le importa que sí tengan al menos una, da igual cuántas tengan porque su servicio
#es en la nube. 


# In[19]:


df_clean=pd.concat([df, first_office], axis=1)[['name', 'category_code', 'lat', 'lng', 'oficina_principal']]


# In[20]:


df_clean.head()


# # Paso 3. Preparar la geolocalización. Esto incluye:
#     -Crear un nuevo collection en mi Compass con base en los requerimientos seleccionados.
#     -Crear un índice en donde añada los valores de 'oficina_principal' como geopuntos.
#     

# In[21]:


df_clean.category_code.value_counts() #me dio curiosidad qué tipo de empresas son 


# In[22]:


#db.collection_friday.insert_many(df_clean.to_dict('records'))
#corrí este código una sola vez y luego lo comenté: en mi CompassDB ya está la nueva colección.


# In[23]:


#ahora hacemos las coordenadas como geopoint. Esto se puede hacer desde CompassDB, pero este es el código.


# In[24]:


#db.collection_friday.create_index([('oficina_principal', '2dsphere')])
#también corrí ese código una sola vez.


# # Paso 4. Graficar como Markers las 103 empresas seleccionadas. 
# 
#     -Preparar un mapa con Folium
# 
#     -Crear una lista con las latitudes
# 
#     -Crear una lista con las longitudes
# 
#     -Hacer un bucle en donde las vaya añadiendo
# 
#     -Checar que todo vaya bien.

# In[25]:


m = folium.Map(location=[39.8282,-98.5795], tiles='stamentoner', zoom_start=4)


# In[35]:


list_lat = df_clean.lat.values
list_long = df_clean.lng.values


# In[33]:


df_clean = df_clean.dropna(axis=0)


# In[38]:


df_clean.reset_index(inplace=True)


# In[39]:


names = df_clean.name.astype(str)


# In[40]:


for i in range(len(list_lat)):
    folium.CircleMarker(
        location=[float(list_lat[i]), float(list_long[i])],
        radius = 12,
        popup = names[i],
        color = '#3186cc',
        fill=True,
        fill_color= '#3186cc'
    ).add_to(m)


# In[46]:


#display(m) <<<--- correr este código! yo lo comenté porque se traba un poco mi pantalla con el mapa. 
#le pueden picar a cada uno de los circulitos y les dice el nombre de la empresa :) 


# In[47]:


#m.save("potential_clients.html")


# # Conclusiones Preliminares:
# 
# Las empresas que mi cliente busca se encuentran repartidas a lo largo de todo el país, 
# con una fuerte concentración en California y cerca de Nueva York. 
# 
# El siguiente paso es el siguiente:
# 
#     -Vamos a buscar a startups que sean más o menos parecidas a mi cliente
#     (vamos a imaginar que eso significa: category_code=='consulting' y fundada después del 2010)
#     
#     -Vamos a buscar en dónde están localizadas estas startups
#     
#     -Veremos si eso nos da insight respecto a dónde le conviene estar a mi cliente. (por ejemplo,
#     si una gran cantidad de empresas grandes no tiene startups de consultoría cerca, a mi cliente
#     le conviene estar ahí.)
#     
#     

# # Paso 5: Búsqueda de posibles competidores. 
# 
#     -Más o menos repetir los mismos pasos, pero ahora para crear una base de datos con posibles 
#     competidores. Esto lo hice en otro jupyter notebook llamado "competitors". Al final guardé el mapa 
#     como html, lo mismo hice con el de aquí, y a partir de la comparación de ambos mapas es posible descubrir cosas interesantes. 

# In[48]:


#ya encontré los valores que me interesan de los competidores: los añadiré en el mismo mapa pero con otro color


# In[49]:


list_lat2=[ 37.7983181,  42.281569 , -37.9924155,  40.3113504,  28.490886 ,
        39.394564 ,  37.7896292,  38.989124 ,  37.78424  ,  41.857204 ,
        52.126616 ,  40.7645772,  26.2480738,  27.4081935,  37.4513629,
        42.6751888,   9.9396253,  28.1524632,  34.0909811,  40.7078343,
        32.920073 ,  55.7794043,  48.8524775,  55.6770321,  27.3858   ,
        38.9569894,  48.3400291, -23.5815208,  54.520135 ,  40.438423 ,
        12.9164537,  45.5058782,  41.9174637,  33.5341548,  40.4244585,
        52.3655578,  30.305809 ,  53.3328144,  42.3672873]


# In[51]:


#list_lat2


# In[52]:


list_long2 = [-122.4000032,  -83.813914 ,  -57.5538238,  -75.1135236,
        -82.540512 , -119.8120795, -122.3998782,  -77.026676 ,
       -122.274771 ,  -87.623923 ,    5.038078 ,  -73.9799007,
        -80.135487 ,  -82.5294065, -122.1842112,  -71.1469003,
         76.2594981,  -80.5883964, -118.325739 ,  -74.0136605,
        -96.740444 ,   37.6899674,    2.3660117,   12.5751278,
        -82.423    ,  -92.3227556,   10.9059804,  -46.6773686,
         18.5416342,  -80.001933 ,   77.6101165,  -73.5673333,
        -87.6664837, -117.7769669,   -3.6990948,    4.9345824,
        -97.8177601,   -6.2493777,  -71.0814466]


# In[53]:


names2 = ['The Vertical Action Group', 'Compel Interaction', 'Fan',
       'Nalts Consulting', 'Outspoken Media', 'MyChances', 'Macroaxis',
       'Carfeine', 'BitRock', 'JumpForward', 'Navara',
       'Unison Technologies', 'Reachoo', 'kinDragon', 'Transifex',
       'AppZero', 'PebbleForge', 'OBE Pro', 'Setster',
       'GameChanger Media', 'crush tweet', 'CineSoft', 'Antelink',
       '1calendar', 'AlphaPoint Technology', "Book'd", 'makandra',
       'DP7 Digital', 'JustProto', 'The Resumator', 'IndiaOnAPage',
       'Nirvana', 'Eventric', 'ResuWe', 'Taxi Fares app', 'Lipperhey',
       'LugIron Software', 'ftopia', 'Tiverias Apps']


# In[54]:


for i in range(len(list_lat2)):
    folium.CircleMarker(
        location=[float(list_lat2[i]), float(list_long2[i])],
        radius = 12,
        popup = names2[i],
        color = '#cc1144',
        fill=True,
        fill_color= '#cc1144'
    ).add_to(m)


# In[56]:


#display(m)


# In[57]:


#m.save("final_map.html")
#recordar que en el mapa le pueden picar a cada bolita y ver el nombre de todas. 


# # CONCLUSIONES
# 
# -Dado que mi cliente quiere estar en una zona más accesible que Sillicon Valley, yo le recomiendo dirigirse 
# a la zona este del país.
# 
# -A pesar de que hay muchos puntos rojos de ese lado, si inspeccionamos cada una de las empresas, vemos que realmente solo ninguna es competencia directa. 
# 
# -El resto de empresas entran en la categoría de Software y se dedican a cosas muy distintas: por ejemplo, está 
# App Zero que es para medir tu ritmo cardiaco, Tiverias Apps que es para conectar aplicaciones móviles en la nube,
# Resumator que es para contratar gente, etc. En realidad no hacen consultoría con Big Data. Nalts Consulting, una empresa en esa área, parecería que es competencia por el nombre, pero una vez que investigamos un poco vemos que no lo es. En realidad es una empresa que hace consultoría de REDES SOCIALES y ayuda a crear más engagement a través de videos en línea. 
# 
# -Por lo tanto, es posible concluir que hay una gran oportunidad de poner una startup de consultoría en Ciencia de Datos en la zona Este del país. La ciudad queda a discreción de mi cliente.

# In[ ]:




