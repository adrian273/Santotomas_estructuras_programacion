'''
        ::::::::::::::::::::::::::::::::::::::::::::::
        ::    @github: adrian273                    ::
        ::    @email: adrianverdugo273@gmail.com    ::
        ::::::::::::::::::::::::::::::::::::::::::::::
    2@ Lea tres números y calcule:
        a. Numero1 + numero2
        b. (numero1 + numero3) / numero2
        c. Numero1 ^ numero2 / numero3
        d. Numero1 MOD numero2
'''
number1 = int(input('Ingrese numero \n'))
number2 = int(input('Ingrese numero \n'))
number3 = int(input('Ingrese numero \n'))

result = number1 + number2
print('El primer resultado es ' + str(result))
result = (number1 + number3) / 2
print('El segundo resultado es ' + str(result))
result = number1 ** number2 / number3
print('El tercer resultado es ' + str(result))
result = number1 % number2
print('El cuarto resultado es ', result)
