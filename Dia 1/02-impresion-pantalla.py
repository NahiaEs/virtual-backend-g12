nombre = 'nahia'

print(nombre)
#concatenar (juntar) varios valores
print('El nombre es:', nombre,'del usuario') 

estado_civil = 'soltera'

#si queremos usar el metodo format tenemos que coincidir el mismo numero de veces que colocamos {} con la cantidad de variables
print('La persona {} es {}'.format(nombre, estado_civil))

#podemos agregar la posición de la variable que queremos imprimir dentro de las llaves
print('{1} es una persona {0}'.format (estado_civil, nombre))
