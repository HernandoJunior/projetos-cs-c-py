texto = input("Digite algum texto:")
for letras in texto:
    a = 0
    b = 0
    c = 0
    if letras.isalpha():
        a += 1
    elif letras.isspace():
        b += 1
    elif letras == '.' or letras == '!' or letras == '?' or letras == ',':
        c += 1
        
qnt_letras = 0
qnt_espaco = 0
if b != 0:
    qnt_letras = (a/b) * 100
if c != 0:
    qnt_espaco = (b/c) * 100

qnt_total = (0.0588 * qnt_letras) - (0.296 * qnt_espaco) - 15.8

if qnt_total >= 16:
    print("Grade: 16+")
elif qnt_total > 1:
    print(f"Grade {qnt_total}")
else:
    print("Antes da grade 1")

