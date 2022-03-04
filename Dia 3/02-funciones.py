#DFU
#Funciones definidas por el usuario
#almacenara un bloque de codigo con su comportamiento y solamente se ejecutara cuando este sea invocado 
#(llamado)

#al momento de llamar a la funcion tenemos que pasarle el mismo nujmero de parametros que hemos definido
from itertools import product
from ssl import ALERT_DESCRIPTION_UNKNOWN_PSK_IDENTITY
from time import process_time_ns


def sumar(numero1, numero2):
    print('Se realizara la sumatoria . . . ')
    print(numero1+ numero2)

sumar(5,7)

def nombre(x):
    '''Funcion que recibe un string y lo imprime por consola'''
    print(x)

nombre('Nahia')

#mostrara la documentacion de la funcion si es que hay 
print(nombre.__doc__)

#ahora, tambien podriamos definir funciones que ejecuten algo y que nos den una respuesta 
usuario = []
def registrar(nombre, email, telefono):
    '''Funcion que registra un usuario y lo guarda en una lista'''
    #aqui registraremos el usuario
    usuario.append ({
        'nombre': nombre,
        'email': email
        'telefono'= telefono
    })
    
    return {
        'message': 'Usuario registrado exitosamente',
        'usuario': usuario [0]
    },1,True
    #si una funcion retorna mas de un valor (retornara una tupla) entonces podemos hacer dos cosas:1, 
    # si solamente declaramos una variable ahi se almacenara toda la tupla, 2.v si queremos almacenar
    # cada valor de la tupla en una variable podemos hacer una destructuracion de esa tupla declarando el mismo numero de variables que el numero de contenidos de la tupla 
resultado, estado_civil, nacionalidad = registrar('Nahia', 'nahia@gmail.com', '971012900')
rpta= registrar('Nahia', 'nahia@gmail.com','971012900')
    
print(rpta)
print(resultado)
print(estado_civil)
print(nacionalidad)

productos= []
#si nosotros creamos una funcion que opcional reciba ciertos parametros,e stos parametros opcionales siempre deben ir al final, primero los requeridos y luego los opcionales
def registrar_productos(nombre, precio, estado= True, almacen= 'Almacen del cercado'):
    productos.append({
        'nombre': nombre,
        'precio': precio, 
        'estado': estado, 
        'almacen': almacen
    })
    return 'Producto agregado exitosamente'
#siempre tenemos que pasar obligatoriamente los parametros que no tienen valores por defecto
registrar_productos('Tomates', 4.50)
registrar_productos('Apio', 1.40, False)
registrar_productos('Cebolla', 5.30,True, 'Almacen nuevo mercado')
#otra forma de pasar parametros
registrar_productos(almacen='Alamcen de la costa', nombre= 'Pescado tilapia', precio=2.50)

#recibira un numero indeterminado de parametros en los cuales los almacenara en una tupla
#puede recibir un numero indeterminado de parametros y estos pueden ser de diferentes tipos
#se usa el asterisco y solo se recibe uno
def alumnos(*args):
    print(args)

    if(len(args) and args [0] is not None):
        print('si hay el valor del puerto')
    print('la clase es:', clase)

#def alumnos(*args):
#    print(args)

alumnos('nahia', 'eduardo', 'pedro', 'mario', 'jean carlo')

alumnos('roxana', 'luis', 'joshua', 'danny')

alumnos('juanito')

alumnos('martha', 30 , False, 'Juan', 1.5)

#kwargs >keyword argument
#si la funcion queremos recibir un numero ilimitado de argumentos pero estos deben de tener su nombre de parametro con su valor entonces usaremos los kwargs
def ingresarProducto(**kwargs):
    print(kwargs)
    if(kwargs.get('nombre')):
        print('El usuario quiere agregar un producto con el nombre')
    if(kwargs.get('cantidad')):
        print('El usuario quiere ingresar la cantidad del producto')

ingresarProducto(nombre= 'Manzana', precio= 2.40, estado=True, pais_procedencia='Peru')
ingresarProducto(tamanio='Grande', cantidad=100, nombre='Pera de agua')

#recursividad
#es utilizar la funcion dentro de la misma funcion

def saludar_n_veces(limite):
    if(limite == 0):
        return 'Llegue al limite'
    print('saludar')
    return saludar_n_veces(limite-1)

resultado= saludar_n_veces(10)

print(resultado)

def factorial(limite):
    if limite == 0:
        return 1

    return limite * factorial(limite-1)

resultado = factorial(0)
print(resultado)
#ventajas:
#hace el codigo mas limpio y sin mucha duplicidad del mismo
#*una tarea compleja se puede dividir en si misma de una manera mas facil y sencilla
#* la generacion de subsecuencias es mas facil con la recursividad que con alguna iteracion anidad (while)
#
#desventajas:
#* a veces la logica para generar una funcion recursiva es dificil de sguir 
#* las llamas recursivas son mas costosas ya que ocupan mas memoria por el simple hecho de volver a llamar a toda la funcion de nuevo dentro de si misa y obviamente esto generara un mayor tiempo de respuesta
#* las funciones recursivas son dificultades de hacer depuracion (seguimiento al codigo linea x linea)


#Operadores ternarios
#Son condicionales que se pueden realizar en una sola linea de codigo solamente se puede retornar un valor o varios valores pero en una sola linea, no se puede hacer validaciones adicionales a la principal
nombre_persona = 'Maria'
origen_persona = 'arequipa'

def duda(nombre_persona, origen_persona):
    if nombre_persona == 'Maria' and origen_persona == 'arequipa':
        return 'Me caso'
    else: 
        return 'Next'
resultado = 'Me caso' if nombre_persona == 'Maria' and origen_persona == 'arequipa' else 'Next'
resultado2= 'Next'

print(resultado)
print(resultado2)


#lambdafunction
#son funciones que puede tener un numero indeterminado de argumento pero solamente una expresion(una sola linea de ejecucion de codigo) ademas esta sera retornada
cuadrado = lambda numero: numero **2
sacar_igv= lambda precio: precio *0.18

rpta= cuadrado (4)

precio_sin_igv = sacar_igv(100)
print(rpta)
print(precio_sin_igv)

precio_sin_igv = sacar_igv(50)
print(precio_sin_igv)


 print(rpta)


