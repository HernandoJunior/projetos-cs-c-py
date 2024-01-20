import csv

with open("telefone.csv", "a") as arquivo: #abrindo um arquivo
    nome = input("Nome: ")
    numero = input("Numero: ")
    escrever = csv.writer(arquivo) #csv.writer espera como entrada o arquivo que voce abriu
    escrever.writerow([nome, numero])
arquivo.close()
