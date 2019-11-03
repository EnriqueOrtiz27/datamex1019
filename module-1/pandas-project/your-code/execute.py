
import pandas as pd
import re
import clean_columns as cc 


pd.set_option('display.max_columns', 24)
pd.set_option('display.max_rows', 400)
df = pd.read_csv('gsa.csv')


#Renombramos la primer columna,le aplicamos la función para limpiarla y por último la convertimos a formato de tiempo. 
df = df.rename(columns={'Case Number': 'Date of Attack', 'Date': 'Month', 'Area': 'Reference 1', 'Location': 'Reference 2', 'Sex ': 'Sex'})
df['Date of Attack'] = df['Date of Attack'].apply(cc.clean_first_column)
df['Date of Attack'] = pd.to_datetime(df['Date of Attack'], format='%Y%m%d', errors = 'coerce')

#El siguiente paso es la segunda columna, que hay que convertir ahora en el número de mes que nos interesa. 
#La voy a renombrar y le asignaré el mes que corresponde. 
for x in range(5991):
    df['Month'][x] = df['Date of Attack'][x].month

#Con esta función la convierto en string y le quito los empty values.  Lo mismo para la primer columna. 
df['Month'] =  df['Month'].apply(cc.clean_empty_values)
df['Date of Attack'] = df['Date of Attack'].apply(cc.clean_empty_values)

df['Year'] =  df['Year'].astype(int)
df['Year'] =  df['Year'].apply(lambda x: 0 if x < 1700 else x)

#De aquí en adelante básicamente limpio las columnas, les quito los empty values y cambio los nombres de algunas. 
df['Country'] = df['Country'].apply(cc.clean_country)
df['Country'] = df['Country'].fillna("NOT AVAILABLE")
df = df.rename(columns={'Country': 'Country or Island'})

df['Reference 1'] = df['Reference 1'].apply(cc.clean_reference)
df['Reference 2'] = df['Reference 2'].apply(cc.clean_reference)
df['Reference 1'] = df['Reference 1'].str.replace("nan", "Not Available")
df['Reference 2'] = df['Reference 2'].str.replace("nan", "Not Available")
df['Reference 1'] = df['Reference 1'].fillna("None Given")
df['Reference 2'] = df['Reference 2'].fillna("None Given")

df.Sex = df.Sex.apply(cc.clean_sex)
df.Sex = df.Sex.fillna("Unidentified")

df.Activity = df.Activity.apply(cc.clean_activity)

df.Name =  df.Name.str.extract(r'([A-Z][a-z]+ ?[A-Z][a-z]+)')
df.Name = df.Name.str.replace("Coast Guard", "Not Available")
df.Name = df.Name.fillna("Not Available")

df.Injury = df.Injury.apply(cc.clean_injury)
df.Injury = df.Injury.fillna("4")

df.Age = df.Age.apply(cc.clean_age)
df.Age = df.Age.fillna("Unknown")

df.Time = df.Time.apply(cc.clean_time)
df.Time = df.Time.fillna("Not Available")

df['Fatal (Y/N)'] = df['Fatal (Y/N)'].apply(cc.clean_fatal)

df['Investigator or Source'] = df['Investigator or Source'].apply(cc.clean_reference)
df['Investigator or Source'] =  df['Investigator or Source'].str.extract(r'([A-Z][a-z]+ ?[A-Z][a-z]+)|([A-Z][a-z]+ ?[A-Z][a-z]+ ?[A-Z][a-z])')
df['Investigator or Source'] = df['Investigator or Source'].fillna("Not Available")

df = df.rename(columns={'Injury': 'Injury Category', 'pdf': 'PDF', 'href formula': 'Link PDF', 'Case Number.1': 'Case_ID_1','Case Number.2': 'Case_ID_2'})
df = df.rename(columns={'original order': 'Order No.', 'Unnamed: 22': 'Notes 1', 'Unnamed: 23': 'Notes 2', 'href': 'Online PDF'})
df = df.rename(columns={'Species ': 'Species'})
#fill empty blanks 
df['Link PDF'] = df['Link PDF'].fillna("Not Available")
df['Online PDF'] = df['Online PDF'].fillna("Not Available")
df['Notes 1'] = df['Notes 1'].fillna("Pending")
df['Notes 2'] = df['Notes 2'].fillna("Pending")

df['Species']= df['Species'].apply(cc.clean_species)
df.Species.fillna("Unidentified Shark")

export_csv = df.to_csv(r'/Users/enriqueortiz/Desktop/sharks_clean_eoc.csv', index = None, header=True)


