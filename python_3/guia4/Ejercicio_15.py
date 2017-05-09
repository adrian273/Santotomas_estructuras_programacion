'''
    ::::::::::::::::::::::::::::::::::::::::::::::
    ::    @github: adrian273                    ::
    ::    @email: adrianverdugo273@gmail.com    ::
    ::::::::::::::::::::::::::::::::::::::::::::::
    15@ Lea tres números y determine el valor intermedio.
'''
number1 = int(input('Ingrese numero \n'))
number2 = int(input('Ingrese numero \n'))
number3 = int(input('Ingrese numero \n'))
if number1 > number2 and number1 < number3 or number1 > number3 and number1 < number2:
    print('El valor intermedio es ' + str(number1))
elif number2 > number3 and number2 < number1 or number2 > number1 and number2 < number3:
    print('El valor intermedio es ' + str(number2))
elif number3 > number2 and number3 < number1 or number3 < number2 and number3 > number1:
    print('El valor intermedio es ' + str(number3))
