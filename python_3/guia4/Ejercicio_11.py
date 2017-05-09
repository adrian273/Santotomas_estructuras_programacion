'''
    ::::::::::::::::::::::::::::::::::::::::::::::
    ::    @github: adrian273                    ::
    ::    @email: adrianverdugo273@gmail.com    ::
    ::::::::::::::::::::::::::::::::::::::::::::::
    11@ Dado dos valores y una operación (“Suma”, “Resta”, “División”, “Multiplicación”), realice el cálculo de la operación indicada.
'''
number1 = int(input('Ingrese numero \n'))
number2 = int(input('Ingrese numero \n'))
print('Ingrese operacion a realizar \n 1: suma \n 2: resta \n 3: multiplicacion \n 4: division')
option = int(input('Ingresar opcion : '))
if option == 1:
    result = number1 + number2
    print(' * El resultado es ' + str(result))
elif option == 2:
    result = number1 - number2
    print(' * El resultado es ' + str(result))
elif option == 3:
    result = number1 * number2
    print(' * El resultado es ' + str(result))
elif option == 4:
    result = number1 / number2
    print(' * El resultado es ' + str(result))
else:
    print('ninguna opcion elegida')
