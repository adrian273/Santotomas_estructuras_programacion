'''
    @description:  Leer dos números y calcular (A+B)**2 utilizando solo la suma.
    @author: Adrian Verdugo
'''

number_1 = int(input('Ingrese numero: '))
number_2 = int(input('Ingrese numero: '))

result = (number_1 + number_2)
for i in range(1):
    result += result
print('El resultado es: ' + str(result))
