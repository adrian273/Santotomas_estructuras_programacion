'''
    ::::::::::::::::::::::::::::::::::::::::::::::
    ::    @github: adrian273                    ::
    ::    @email: adrianverdugo273@gmail.com    ::
    ::::::::::::::::::::::::::::::::::::::::::::::
    14@ Lea un numero y muestre el impar siguiente
'''

number1 = int(input('Ingrese numero \n'))
result_mod = number1 % 2
if result_mod == 0:
    result_mod = number1 + 1
    print('El impar siguiente es: ' + str(result_mod))
else:
    result_mod = number1 + 2
    print('El impar siguiente es: ' + str(result_mod))
