notas= [10, 20, 16, 8, 6,1]

#for(let i=0; i<10; i++) {...}
#En cada iteracion de la lista notas tendremos su valor y lo almacnaremos en una variable llamada nota
for nota in notas:
    print(nota)

for numero in range(5,10):
    print(numero)












aprobados = ['Nahia', 'Eduardo', 'Fatima','Pedro']
for aprobado in aprobados:
    if(aprobado == 'PJhon'):
     print('Pedro esta aprobado')
#break quiebre se hace que la iteracion se detenga de manera abrupta
#  y no espere a que continue y en ese caso no se ejecutara el else
     break
#El else en el caso de los for se ejecutara despues de haber hecho la iteracion del bucle FOR 
#Se ejecutara aun asi hubo iteraciones o si no las hubo y si no hubo algun break
#El else se ejecutara si el for termino sin problemas
else: 
    print ('No se encontro el alumno a buscar')

print('Termino de ejecutarse el for')

productos = ['Manzana', 'Peras', 'Tallarines', 'Tazas']
busqueda = input('Ingrese el producto a buscar:')

for producto in productos:
    if producto == busqueda:
        print('El producto si esta en la tienda')
        break
#El else se colocara si al finalizar la iteracion no hubo un break o sea todo finalizo sin una busqueda esperada
else:
    print('No se encontro el producto')
    
print('Igual yo me ejecuto')


