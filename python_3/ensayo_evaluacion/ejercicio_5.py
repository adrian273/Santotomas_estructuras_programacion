'''ejercicio_5.py
    @description: Convertir el diagramna de flujo a codigo [python]
    @author: Adrian Verdugo
'''

number = int(input('Ingrese numero: '))
resto = number % 2

if resto == 1:
    number -= 1

while number <= 100:
    print(number)
    number += 2