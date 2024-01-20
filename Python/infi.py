# PIRAMIDE DE MARIO
'''for i in range(3):
    for j in range(3):
        print("#", end="")
    print()'''
# FUNC .APPEND() = ADICIONA UM ITEM A LISTA
'''from cs50 import get_int
scores = []
for i in range(3):
    scores.append(get_int("Digite um numero inteiro: "))

media = sum(scores) / len(scores)
print(f"Media dos numeros digitados: {media}")'''
# FUN .UPPER() or .LOWER() transforma a string em letra maiuscula ou minuscula
'''a = input("Frase ou letras: ")
print(a.lower())
for b in a:
    print(b.upper(), end="")
print()'''
#ARGV and ARGC, agrv = voce acessa argumentos na linha de comando importanto a biblioteca /
'''from sys import argv

if len(argv) == 2:
    print(f"Hello, {argv[1]}!") #argv[1] esta executando a primeira palavra da linha de comando depois do "infi.py"
else:
    print("Hello world!")'''
#PESQUISA LINEAR é uma frase preposicional
'''import sys

numeros = [1, 2, 3, 5, 0, 9]

if 0 in numeros:
    print("Tem o numero 0")
else:
    print("Numero 0 não encontrado")'''
# DICIONARIO EM PYTHON
'''pessoas = { # Isso é um dicionario: conjunto de valores-chaves a esquerda e direita
    "Hernando": "(71)9.9741-5316",
    "HernandoAmaral": "(71)9.9754-0987"
}
numero = input("Nome da pessoa: ")
for numero in pessoas: #procurando pelo numero da pessoa no dicionario
    print(f"Numero : {pessoas[numero]}") #busca todas as chaves para os valores que foram pedidos'''

