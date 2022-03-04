#mientras que 
numero = 0
#pass sirve para indicar dentro de un bloque de codigo 
# que aun no hemos definido la logica
# siempre se quita el pass
#bucle infinito (infinite loop) es un ciclo que se va a ejecutar 
# por siempre y nunca tendra fin
while numero <= 10:
    print(numero)
    numero += 1
#break
else: 
    print('el while termino bien')

numeros =[1,5,16,234,67,29]
#CON WHILE
posicion = 0
par,impar = 0, 0
while posicion < len(numeros):
    if numeros[posicion]% 2 == 0:
        par += 1
    else: 
        impar += 1
        posicion += 1

print('hay {} numeros pares'.format(par))
print('hay {} numeros impares'.format(impar))



#CON FOR
par, impar= 0
for numero in numeros:
    if numero % 2 == 0:
#La division entre dos me da un residuo par
        par +=1
    else: 
        impar += 1
print('hay {} numeros pares'.format(par))
print('hay {} numeros impares'.format(impar))