#Sua tarefa é escrever um programa que pegará uma sequência de DNA e um arquivo
#CSV contendo contagens de STR para uma lista de indivíduos e, em seguida, enviará a quem o DNA (mais provavelmente) pertence.
import sys
import csv

def ler_arquivo_csv(nome_arquivo_csv):
    try:
        with open(nome_arquivo_csv, newline='') as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)
            return list(leitor_csv)
    except FileNotFoundError:
        print(f"Erro: Arquivo CSV '{nome_arquivo_csv}' não encontrado.")
        sys.exit(1)

def ler_sequencia_dna(nome_arquivo_dna):
    try:
        with open(nome_arquivo_dna) as arquivo_dna:
            return arquivo_dna.read()
    except FileNotFoundError:
        print(f"Erro: Arquivo de DNA '{nome_arquivo_dna}' não encontrado.")
        sys.exit(1)

def encontrar_correspondencia(individuos, sequencia_dna):
    for individuo in individuos:
        nome = individuo['name']
        correspondencia = True
        for str_nome, str_contagem in individuo.items():
            if str_nome != 'name':
                repeticoes = contar_repeticoes_consecutivas(sequencia_dna, str_nome)
                if int(str_contagem) != repeticoes:
                    correspondencia = False
                    break
        if correspondencia:
            return nome
    return "No match"

def contar_repeticoes_consecutivas(sequencia, str_nome):
    # Implementação simples para contar repetições consecutivas de uma string em outra
    count = 0
    max_count = 0
    for i in range(len(sequencia)):
        if sequencia[i:i+len(str_nome)] == str_nome:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count

def main():
    if len(sys.argv) != 3:
        print("Erro: Forneça o nome do arquivo CSV e o nome do arquivo de DNA como argumentos.")
        sys.exit(1)

    nome_arquivo_csv = sys.argv[1]
    nome_arquivo_dna = sys.argv[2]

    individuos = ler_arquivo_csv(nome_arquivo_csv)
    sequencia_dna = ler_sequencia_dna(nome_arquivo_dna)

    resultado = encontrar_correspondencia(individuos, sequencia_dna)

    print(resultado)

if __name__ == "__main__":
    main()


