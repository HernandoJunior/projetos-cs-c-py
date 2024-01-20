from cs50 import get_string, get_float, get_int
#ENTRADA DE DADOS EM PYTHON#
answer = get_string("Whats your name? ")
print(f"Hi {answer}, welcome!")

# DECLARAÇÃO DE VARIAVEIS #
x = 0 # (PYTHON IDENTIFICA QUE QUEREMOS UM NUMERO INTEIRO EM X) #
# bool, float, int, str #
# ESTRUTUA CONDICIONAL #
y = 0
if x < y:
    print("X é menor do que Y")
elif x > y:
    print("X é maior do que y")
else:
    ("X e Y são iguais")

# ESTRUTURAS DE REPETIÇÃO - WHILE - #
i = 0
while i < 3:
    print("hello, world")
    i += 1

# ESTRUTURAS DE REPETIÇÃO - FOR - #
for i in range(5):
    print("Hello world!")
