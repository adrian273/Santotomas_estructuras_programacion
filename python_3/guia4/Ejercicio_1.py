'''
    ::::::::::::::::::::::::::::::::::::::::::::::
    ::    @github: adrian273                    ::
    ::    @email: adrianverdugo273@gmail.com    ::
    ::::::::::::::::::::::::::::::::::::::::::::::
    1@ Lea el Radio de una circunferencia y calcule:
    a. Diámetro = 2 * Radio.
    b. Perímetro = 2 * Radio * Pi
    c. Área = Pi * Radio ^ 2
'''
# desde el modulo {math} se import {pi} para sacar el resultado exacto
from math import pi

radio = int(input('Ingrese radio \n'))
diametro = 2 * radio
perimetro = 2 * radio + pi
area = pi * radio **2

print("El diametro es " + str(diametro))
print('El perimetro es ' + str(perimetro))
print('El area es ' + str(area))
