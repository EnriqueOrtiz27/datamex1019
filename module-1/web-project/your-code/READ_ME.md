Proyecto API and Web Scraping. 

Un breve resumen de mi proyecto.

1. Como ninguna base de datos me convenció, decidí improvisar la mía. Me metí a 'https://www.rollingstone.com/culture/culture-lists/50-best-stand-up-comics-of-all-time-126359/elayne-boosler-126829/'. Esa página es un artículo de la revista Rolling Stone intitulado: "50 Best Stand-up Comics of All Time". Mi base de datos "original" consistió en crear un data frame con los nombres y las descripciones de los 50 comediantes. 

2. Para añadirle el factor "API", lo que hice fue usar la API de youtube. Utilicé esta API para encontrar el video más visto que está disponible cuando buscas el nombre del comediante en youtube. Por ejemplo, tomemos al comediante número uno, Richard Pryor. Si buscas en youtube "Richard Pryor" y ordenas los resultados por vistas, el que tiene más vistas es una entrevista con George Carlin, justo el resultado que me da la API. Yo añadí una columna en donde puse el título del video más visto y luego otra columna en donde puse el link a ese video. Por alguna razón, en el comediante 10, Mort Sahl, la API estaba teniendo problemas para encontrar el link, por lo que tuve que programar un pequeño bloque de "try—except"

3. El resto de mis funciones son para limpiar toda la basura HTML o para darle el formato que yo quería a los nombres y demás. 

4. Como estaba corriendo el código muchas veces, el primer día tuve problemas con mi número de requests en la API de youtube. Para evitar tener este problema, limité mi base de datos a los primeros 10 comediantes. Solo tendría que cambiar un par de parámetros en algunas funciones para que este programa abarque la lista entera de 50 comediantes. Otra razón por la que elegí 10 comediantes es porque en un par de funciones hay un "time.sleep(10)" que escribí para no tener problemas con la API de youtube. Dado que esto corre dos veces, necesito esperar al menos 10 segundos por 10 comediantes por 2 funciones en que necesito la API = (10*10*2)= 200 segundos=3minutos con 20 segundos para que corra el programa. Si lo hiciera con los 50 comediantes, me tomaría más de 15 minutos correr el programa. Se puede hacer más eficiente combinando ambas funciones en una sola y reduciendo el time.sleep, probablemente haga pruebas de eso al rato a ver si puedo incluir a los 50 comediantes. Por lo pronto solo quería un código que sirviera. 

5. Por último, exporté el Data Frame como un csv para que se pueda ver más claramente la tabla y no tener que esperar ese tiempo cada que corriera el código. 


