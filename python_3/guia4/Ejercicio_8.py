'''
    ::::::::::::::::::::::::::::::::::::::::::::::
    ::    @github: adrian273                    ::
    ::    @email: adrianverdugo273@gmail.com    ::
    ::::::::::::::::::::::::::::::::::::::::::::::
    8@  Lea cuatro valores diferentes entre si, determine el valor menor.-­‐

'''
number1 = int(input('Ingrese numero \n'))
number2 = int(input('Ingrese numero \n'))
number3 = int(input('Ingrese numero \n'))
number4 = int(input('Ingrese numero \n'))

if  number1 < number2 and number1 < number3 and number1 < number4:
    print('El numero menor es ' + str(number1))
elif number2 < number1 and number2 < number3 and number2 < number4:
    print('El numero menor es ' + str(number2))
elif number3 < number2 and number3 < number1 and number3 < number4:
    print('El numero menor es ' + str(number3))
elif number4 < number2 and number4 < number3 and number4 < number1:
    print('El numero menor es ' + str(number4))
