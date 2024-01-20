# DECLARANDO UMA VARIAVEL "WORD" DO TIPO "SET"(Conjunto de coleção de valores)
word = set()

#FUNÇÃO QUE CHECA
def check(words)
    if words.lower() in word:
        return True
    else:
        return False

# DEFININDO UMA FUNÇÃO "LOAD" COM DICIONARIO COMO PARAMETRO DAS VARIAVEIS #
def load(dicionario):
    file = open(dicionario, "r")
    for line in file:
        word.add(line.rstrip()) #adicionando as linhas do dicionario na variavel "WORD" // rstrip = RETIRE AS LINHAS EM BRANCO DO DICIONARIO
    close(file)
    return True
