#ARREGLOS O LIST EN PYTHON
meses= ['octubre','febrero', 'marzo']
print(meses)



#ordenar elementos de la list
meses.sort()
print(meses[0]) #para imrprimir la posicion en especifico
print(meses)









#obtener datos dentro de un arreglos 
aprendiendo =f'estamos en el mes de {meses[0]}'
print(aprendiendo)

#reemplazar el valor de un arreglo
meses[2]= 'noviembre'
print(meses)

#agregar un valor a un arreglos
meses.append('julio')
print(meses)

#eliminar el valor de un arreglo
del meses[2]
print(meses)

#eliminar el valor de un arreglo
meses.pop() #elimina el ultimo elemento de la lista
print(meses)

#liminar un posicion en especifica
meses.pop(1) 
print(meses)

#eliminar por nombre
meses.remove('febrero')
print(meses)