'''
    ::::::::::::::::::::::::::::::::::::::::::::::
    ::    @github: adrian273                    ::
    ::    @email: adrianverdugo273@gmail.com    ::
    ::::::::::::::::::::::::::::::::::::::::::::::
    1@ Leer un numero y generar los impares siguientes hasta el 100
'''

number = int(input('Ingrese numero \n'))
result_mod = number % 2

if result_mod == 0:
    # Si el numero es par se resta en 1
    number -= 1

for i in range(1, 100):
    #Acumulador va ir aumentando en 2
    number += 2
    if number < 100:
        print(number)
