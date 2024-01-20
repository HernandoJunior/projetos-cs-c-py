import csv

newfile = set()
with open("CS50 2019 - Lecture 7 - Favorite TV Shows (Responses) - Form Responses 1.csv", "r") as arquivo:
    read = csv.DictReader(arquivo) #LENDO O ARQUIVO CSV = PEGANDO OS TITULOS E SEUS VALORES COM O DICTREADER
    for linhas in read: #PERCORRENDO AS LINHAS DOS ARQUIVOS, ADICIONANDO AO SET, ELIMINANDO OS ESPAÇOS COM .strip, e aumentando as letras .upper
        newfile.add(linhas["title"].strip().upper())

for titulos in sorted(newfile):#Colocando em ordem alfabetica com sorted
    print(titulos)

