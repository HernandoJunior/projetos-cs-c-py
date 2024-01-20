number = int(input("Numero do cartão: "))
valido = str(number)
primeiro_digito = valido[0]
while True:
    if len(str(number)) != 16:
        print("Numero invalido, digite novamente!")
        number = int(input("Numero do cartão: "))
    if primeiro_digito == '5':
        print("MASTERCARD")
        break
    if primeiro_digito == '3':
        print("AMEX")
        break
    if primeiro_digito == '4':
        print("VISA")
        break
    else:
        print("INVALIDO")
        break
