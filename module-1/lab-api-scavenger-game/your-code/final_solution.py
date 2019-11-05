with open('token2.txt', 'r') as f:
    acceso=f.readlines()[0].split('=')

user=acceso[0]
key=acceso[1].rstrip('\n')

import json
import requests
import pandas as pd
import time


repo='ironhack-datalabs/madrid-oct-2018'

get_forks='http://api.github.com/repos/'+ repo +'/forks'

res_fork=requests.get(get_forks, auth=(user, key))

res=res_fork.json()

#Primero: ver los idiomas 
languages=set()

for i in range(len(res)):
    languages.add(res[i]['language'])

print(languages)

lan=[]

for i in range(len(res)):
    lan.append(res[i]['language'])
    
print(set(lan))

#Challenge2

repo='ironhack-datalabs/datamad0819'

desde='2017-10-01T00:00:00Z'
hasta='2019-11-04T23:59:59Z'

get_commits='http://api.github.com/repos/{}/commits?since={}&until={}'.format(repo, desde, hasta)

res_commit=requests.get(get_commits, auth=(user, key))
results_commit=res_commit.json()


commits=[]
for i in range(len(results_commit)):
    commits.append(results_commit[i]['committer'])

print(len(commits))


#Challenge3

repo='ironhack-datalabs/scavenger'
get_repo='http://api.github.com/repos/{}/git/trees/master?recursive=1'.format(repo)

get_repo=requests.get(get_repo, auth=(user, key))
res=get_repo.json()
res['tree']

url='https://api.github.com/repos/ironhack-datalabs/scavenger/contents/'

tree=res['tree']

archivos=[]
for i in range(len(tree)):
    if tree[i]['type']=='blob' and 'scavengerhunt' in tree[i]['path']:
        #obtengo el path y el contenido del archivo
        get_contenido=requests.get(url + tree[i]['path'])
        contenido=get_contenido.json()
        archivos.append((contenido['name'], contenido['content']))
        time.sleep(1)
print(archivos)

archivos.sort()

import base64
frase=''
for texto in archivos:
    frase+=str(base64.b64decode(texto[1]))

#La frase buscada es:
frase=frase.replace('b\'', '').replace('\\n\'', ' ')
print(frase)







