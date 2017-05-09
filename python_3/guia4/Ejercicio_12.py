'''
    ::::::::::::::::::::::::::::::::::::::::::::::
    ::    @github: adrian273                    ::
    ::    @email: adrianverdugo273@gmail.com    ::
    ::::::::::::::::::::::::::::::::::::::::::::::
    12@ Leer dos números, si el número uno es mayor que el número dos calcule
    Número1*Número2, si el número dos es mayor y además es distinto d cero calcule Número1/Número2, si el número dos es cero muestre “no se puede calcular”.
'''

number1 = int(input('Ingrese un numero \n'))
number2 = int(input('Ingrese un numero \n'))
if number1 > number2:
    result = number1 * number2
    print('El resultado es ' + str(result))
if number2 > number1 and number2 != 0:
    result = number1 / number2
    print('El resultado es ' + str(result))
if number2 == 0:
    print('No se puede calcular')
