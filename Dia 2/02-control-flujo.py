#IF -ELSE
#Python al no tilizar las llaves para definir bloque de un comportamiento diferente tenemos que utilizar tabulaciones (TAB)
edad =int(input('Ingresa tu edad'))

if(edad > 18): 
    #todo lo que escriba dentro
    print('La persona es mayor de edad')
    #La alineacion nunca debe de variar si estamos en el mismo bloque de codigo
    print('otra impresion')
    #se utiliza si la primera condicion fallo pero queremos hacer una segunda condicion 
elif edad>15:
    print('Puedes ingresar a la preparatoria')
    #el else es completamente opcional y no siempre se debe utilizar un if
elif edad> 10: 
    print('Puedes vacunarte con la Pfizer') 
else: 
    #todo lo demas
    print('Eres muy niño')
print('finalizo el programa')

#Validar si un numero (ingresos de una persona) ingresado por teclado es:
#* mayo a 50: indicar que no recibe el bono yanapay
#* entre 500 y 250: indicar que si recibe el bono
#* es menor que 250: indicar que recibe el bono y un balon de gas
# REsolucion

if ingreso >500:
    print ('No recibe el bono yanapay')
elif ingreso >= 250 and ingreso <= 500:
     print('Recibes el bono yanapay')
else:
    print('Recibe el bono y ademas su balon de gas')