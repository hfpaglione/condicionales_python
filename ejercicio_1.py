# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Comparadores
# Ingrese dos números cualesquiera y realice las siguientes
# comparaciones entre ellos
numero_1 = int(input('Ingrese el primer número:\n'))

numero_2 = int(input('Ingrese el segundo número:\n'))

# Compare cual de los dos números es mayor
# Imprima en pantalla según corresponda
if numero_1 > numero_2:  
    print('el numero:',numero_1,'es mayor que:',numero_2)
elif numero_1 < numero_2:
    print('el numero:',numero_2,'es mayor que',numero_1)
else:
    print(numero_1,'es igual a',numero_2)

# Verifique si el numero_1 positivo, negativo o cero
# Imprima el resultado en cada caso
if numero_1 > 0:
   print('el mumero:',numero_1,'es positivo')
elif numero_1 <0:
    print('el numero:',numero_1,'es negativo')
else:
    print('el numero es cero')

# Verifique si el numero_1 es mayor a 0 y menor a 100
# Imprima en pantalla si se cumple o no la condición
if (numero_1 > 0 and numero_1 < 100):
    print('el numero:',numero_1,'es mayor a 0 y menor que 100')
else:
    print('el numero:',numero_1,'es menor o igual a 0 o mayor o igual a 100')

# Verifique si el numero_1 es menor a 10 o el numero_2
# es mayor a -2
# Imprima en pantalla si se cumple o no la condición
if (numero_1 < 10 or numero_2 > -2):
    print('el numero:',numero_1,'es menor a 10 o el numero:',numero_2,'es mayor a -2')
else:
    print('el numero:',numero_1,'es mayor a 10 o el numero:',numero_2,'es menor a -2')
