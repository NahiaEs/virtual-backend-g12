#coleccion de datos es una variable que puede almacenar varios valores

#Listas (List)
#ordenadas y que puede ser modificadas

nombre= ['Pedro', 'Luis', 'Danny', 'Cesar', 'Magaly', 'Anahi']
combinada = ['Eduardo', 80,False, 15.8, [1,2,3]]

#Las listas siempre empiezan en la posicion cero 0
print(nombre[0])

#cuando hacemos el uso de valores negativos en una lista internamente python le dara vuelta
print(nombre[-1])

print(nombre)
#Si queremos ingerasr a una posicion inexistente nos lanzara un error de 'indice fuera de rango'
#print(nombre[10])

#Elimina remueve el último elemento de la lista y se puede almacenar en otra varible
nombre.pop()
resultado = nombre.pop()
print (resultado)
print(nombre)

#append agrega una nueva posicion, append()> ingresa un nuevo elemento a la ultima posicion de la lista
nombre.append('Juana')

#elimina el contenido de una posicion de una lista pero no lo podemos almacenar en otra variable
del nombre[0]

print(nombre)
#clear() > Limpia toda la lista y la deja como nueva
nombre.clear()
print(nombre)

x = combinada[:] # .copy()
y = combinada
#Indicar subseleccion de la lista
print(combinada[1:4])


#indicando el contenido de la lista y esto es muy util para hacer una copia de la lista sin usar su misma posicion de memoria
print(combinada[:])
print(id(x))
print(id(combinada))
print(id(y))

#desde el inicio hasta <2
print(combinada[:2])
#desde la posicion 2 hasta el final
print(combinada[2:])

meses_dscto= ['Enero', 'Marzo', 'Julio']
mes= 'Septiembre'
mes2= 'Enero'

#indicara si el valor no se encuentra dentro de la lista
print(mes not in meses_dscto)
#indicar si el valor se encuentra en la lista
print(mes2 in meses_dscto)

seccion_a= ['Roxana', 'Juan']
seccion_b=['Julieta', 'Martin']
#si hacemos una sumatoria en las listas estas se combinaran en la cual la segunda lista ira despues de la primera
print(seccion_a + seccion_b)

#sirve para esperar un dato ingresado por el usuario
#dato= input('Ingresa tu nombre:')
#print(dato)

#tuplas
#muy similar a la lista a excepcion que no se puede modificar
cursos = ('backend', 'frontend')
print(cursos)
print(cursos[0:1])

#cursos[0] = 'mobile design' no se puede modificarrrr, tampoco se puede agregar (append)
#En la tupla solamente no podremos alterar los valores pertenecientes a ella pero si dentro
#  de esta hay una lista u otra coleccion de datos que si se puede modificar entonces si 
# podremos alterar esta sub coleccion sin problemas
variada = (1,2,3, [4,5,6])

variada[3][0]='Hola'
print(variada)

print(2 in variada)
#creamos una nueva lista a raiz de una tupla llamando a la clase list en la cual en el construstor 
# de esa clase le pasos los valores que contendra la nueva lista

variada_lista = list(variada)
#no se puede crear una lista a raiz  de otra lista eso lanzara un error,
#  solo se puede crear una lista mediante su constructor mediante una tupla

list((1,2,3)) #[1,2,3]

print(variada_lista)
#para ver la cantidad de elementos que conforman una tupla o una lista
#NOTA: la longitud siempre sera la cantidad de elementos y esta siempre empezara en 1 mientras
#  que la posicion siempre empezara en 0, es por eso que siempre la longitud = posicion - 1
print(len(variada))

#Conjuntos (Set)
#coleccion de datos desordenada, una vez que se crea ya no se puede acceder a sus posiciones de sus elementos
estaciones= {'Verano','Otonio','Primavera', 'Invierno'}
#una vez que se crea se asigna una posicion aleatoria pero no cambia cada vezs que se manda a llamar a este conjunto
print('Invierno' in estaciones)
estaciones.add('Otro')
#al ser desordenada al momento de retirar el ultimo elemento este sera completamente aleatorio y retirara el
#  ultimo elemento agregado de forma aleatoria
#pop()> quita el ultimo elemento de la coleccion de datos (list, tuples, set)
estacion = estaciones.pop()
print(estacion)

#Diccionarios
#una coleccion de datos DESORDENADA pero cada elemento obedece a una llave definida
persona= {
    'nombre': 'Nahia',
    'apellido': 'Escalante',
    'correo': 'nahiaescalanteccoyllo@gmail.com'

}
#hacemos la busqeuda de una determinada llave y si no la encuentra nos retornara opcionalmnete None
print(persona.get('apellido', 'No hay no existe'))
#print(persona['apellidos'])

#devuelve todas las llaves de mi diccionario
print(persona.keys())

#devuelve todos los contenidos de mi diccionario
pront(persona.values())

#devuelve todas las llaves y su contenido en forma de tuplas dentro de una lista
print(persona.items())

#si definimos una llave que no existe, la creara, caso contrario modificara su valor
persona['edad'] = 28
#NOTA: Si la llave no es exactamente igual creara una nueva(tiene que coincidir minus y mayus)
persona ['Nombre'] = 'Ximena'
print(persona)

#eliminar una llave de un diccionario
persona.pop('apellido')







