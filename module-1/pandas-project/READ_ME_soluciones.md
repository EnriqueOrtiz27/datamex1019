

Explicación de mi proceso. 

Antes de iniciar, debo decir que aquí pondré un resumen de lo que hice, pero si quieren ver una versión detallada de mi
proceso de limpieza, esto lo pueden encontrar en el archivo "clean_columns.py", en donde escribí todas las funciones que
luego llamé en mi archivo principal. 

Vamos por orden. En las primeras columnas me enfoqué en que tuvieran un formato más limpio de tipo fecha. 
Una está en date time, la otra es el número de mes y por último, year es el año en enteros. No hay mucho problema ahí. 
LLené los empty values con algo tipo "None Available". En Year, los empty values los llené con un cero. Lo óptimo hubiera sido pasarlos a string, llenar eso con un "Not Available", y luego regresarlos a integers cuando fuera posible. 


La cuarta columna ya estaba limpia. La quinta, country, la limpié más o menos caso por caso. 

La quinta y sexta columna están notablemente mezcaldas y sucias, pero decidí solucionar el problema cambiando el nombre 
de la columna. En realidad, lo que nos dan son referencias. Estas van desde coordenadas puntuales hasta frases ambiguas como "cerca de tal cafetería". No vale la pena el esfuerzo por estandarizar algo por naturaleza heterogéneo. Simplemente es más claro notar que son referencias dadas por la gente y que vale la pena tenerlas ahí en caso de visitar el lugar de
ataque. 

La columna de actividad la limpié poniendo todo en unas 15-20 categorías. En nombre seleccioné solo dos palabras que iniciaran con mayúsculas y eso limpió bastante bien la columna. Sexo, Edad, Fatal (Y/N) las limpié de manera sencilla.

Injury decií converirla a "Injury Category", y puse 4 categorías. "0" signfica que no hubo daño. "1" signfica que hubo daño pero que la persona sobrevivió. "2" significa que la persona murió. "Unidentified" significa que no se sabe qué
ocurrió. 


El tiempo lo limpié de manera que quedara solo la hora. En "Species", encontré las 25 categorías más comunes y el resto lo puse en "Unidentified Shark". La columna de "Investigator or Source" la limpié de manera similar al nombre, pero incluí
la opción de que hubiera tres palabras con mayúsculas. 

Las columnas "PDF", "Link to PDF" y "Online PDF" son notoriamente inútiles y no vale la pena hacerles nada. Simplemente son una referencia. ¿Cuál sería el formato ideal? Como están ya tienen toda la información que nos van a dar. 


Las columnas Case_ID_1 y Case_ID_2 también merecen un comentario. Sería fácil dejarse llevar por la tentación de quitarles los caracteres especiales o las letras. Sin embargo, el número de caso es el número de caso. Si en el archivo
un cierto ataque está registrado como "2005.06.23.R", entonces quizá la gente con esa base de datos lo puede accesar así.

Limpiar estas dos columnas sería quedarnos con una columna de fechas, por ejemplo, y esa ya la tenemos. Realmente no nos dan información y no encontré ninguna razón convincente para dedicarles mi tiempo o energía. 

Por último, las dos columnas vacías las decidí renombrar como "Notes 1" y "Notes 2" en caso de que se requieran más notas. 

También se pueden usar para asignarles cierto valores, por ejemplo la versión numérica del mes (recordemos que aunque
en la columna de "Month" hay números, en realidad son strings.) Estas columnas pueden ser usadas de esa manera para hacer más análisis. 


***** Insights *****


El insight que obtuve con el código 'df.loc[df['Fatal (Y/N)']== 'Y'][df.Year > 2008].count()' es que en los 
últimos 10 años solo ha habido 97 muertes registradas por ataques de tiburón. Son menos de 10 muertes por año, 
EN TODO EL MUNDO. 

Creo que eso habla bien de los tiburones. También es importante notar que el 72% de los ataques no fueron fatales. 


***** Insight técnico *****

1- Había una cantidad espeluznante de empty values en varias columnas que necesitaban ser sustituidos. 
2- Enorme desproporción en el género de las víctimas de ataques de tiburón: El 80% de las víctimas fueron
hombres, y del 20% restante, la mitad no tiene registrado el género. 



*** Conclusiones *** 

Al correr el código: null_cols = df.isnull().sum()
null_cols[null_cols>0]

Se puede ver que ya no hay empty values. 

Queda mucho análisis por hacer, y lo que hice no es más que una breve introducción. 









