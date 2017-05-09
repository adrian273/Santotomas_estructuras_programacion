'''
    ::::::::::::::::::::::::::::::::::::::::::::::
    ::    @github: adrian273                    ::
    ::    @email: adrianverdugo273@gmail.com    ::
    ::::::::::::::::::::::::::::::::::::::::::::::
    6@  Lea dos números y determine cuál es el menor.
'''
number1 = int(input('Ingrese numero \n'))
number2 = int(input('Ingrese numero \n'))
if number1 > number2:
    print('El numero ' + str(number2) + ' es menor que ' + str(number1))
else:
    print('El numero ' + str(number1) + ' es menor que ' + str(number2))
