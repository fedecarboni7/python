resultado = 1
base = int(input("Ingrese la base: "))
potencia = int(input("Ingrese la potencia: "))
for i in range(potencia):
    resultado *= base
print(resultado)