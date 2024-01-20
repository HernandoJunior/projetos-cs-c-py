
altura = int(input("Qual sera a altura da piramide? "))

while altura > 8:
    print("Digite a altura entre 1 e 8")
    altura = int(input("Qual sera a altura da piramide? "))

for i in range(1, altura+1):
    hashes = '#' * i
    print(hashes.rjust(altura, ' '))

