# OPERADORES DE COMPARACION 
# == Igual a
#!= Diferente de
# <  Menor que
# >  Mayor que
# <= Menor o igual que
# >= Mayor o igual que

a = 5
b = 3
igual = a == b  # igual es False
diferente = a !=  b  # diferente es True
mayor = a >= b  # mayor es True





#CONDICIONAL 
ahorro = 0
if ahorro >=0:
    print("Nos vamos de viaje")
else:
    print("no tenemos ahorros")







#REVISAMOS SI UN VALOR ES DIFERENTE EN PYTHON STRING
lenguaje = 'python'
if not lenguaje == 'python':
    print(f'super eres un crack de {lenguaje}')
else:
    print(f"no eres un crack de {lenguaje}")





#EVALUACION BOOLEAN
usuario_autenticado = False
if usuario_autenticado:
    print('el usuario se autentico con exito')
else:
    print('el usuario no se autentico vuelva a intentarlo')


#CONDICONALES CON LIST 
superherores = ['superman','spiderman','mujer maravilla','hercules']
if  'superman' in superherores:
    print('amas a batman')
else:
    print('tu superheroe no es batman')









#condicionales anidados
acceso_usuario = True
acceso_admin = False

if acceso_usuario:
    if acceso_admin:
        print('ACCESO TOTAL')
    else:
        print('El usuaro no es admin')
else:
    print('El usuario no esta autenciado')


