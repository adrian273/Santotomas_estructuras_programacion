'''ejercicio_6.py
    @Description:   Hacer el codigo que Lea tres números y calcular (Número Uno POR
                    Número Uno POR Número Tres POR Número Dos) utilizando solo la suma
                    como operación.
'''
title = '\n | Calcular utilizando solamente la suma | \n'
print(title.center(100, '-'))

number_1 = int(input('Ingrese numero: '))
number_2 = int(input('Ingrese numero: '))
number_3 = int(input('Ingrese numero: '))

addition = 0
addition_1 = 0
addition_2 = 0

for i in range(number_1):
    addition += number_1

for j in range(addition):
    addition_1 += number_3

for k in range(addition_1):
    addition_2 += number_2

print('El resultado es {}'.format(addition_2))