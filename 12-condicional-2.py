#CONDICIONAL EL IF IFEL ELSE
tipo = 'estudiante'


if tipo=='estudiante':
    print('Tienes un descuento del 50%')
elif tipo=='profesor':
    print('Tienes un descuento del 80%')
elif tipo=='invitado':
    print('Tienes un descuento del 10%')
else:
    print('NO HAY DESCUENTO')


usuario = 'romanlg' 
tipoUsuario = 'admin'
tiposUsuarios = ['admin','superadmin','usuario']

if tipoUsuario in tiposUsuarios and usuario == 'romanlg':
    print(f'puedes entrar {tipoUsuario}')
else:
    print('el usuario no puede entrar al sistema')