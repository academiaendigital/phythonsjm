#COMO SABER SI UN NUMERO ES PAR
numero = input('agrega un número y te dire si es impar\r\n')
numero = int(numero)

if numero %2 == 0:
    print(f'tu numero {numero} es par')
else:
    print(f'tu numero {numero} es impar')


