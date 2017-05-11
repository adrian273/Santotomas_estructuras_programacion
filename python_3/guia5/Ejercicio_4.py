'''
    ::::::::::::::::::::::::::::::::::::::::::::::
    ::    @github: adrian273                    ::
    ::    @email: adrianverdugo273@gmail.com    ::
    ::::::::::::::::::::::::::::::::::::::::::::::
    4@ Leer un numero y calcular el factorial (Usando el ciclo while)
'''

number = int(input('Ingrese numero \n'))
factorial = 1

while number > 1:
    factorial = factorial * number
    number -= 1

print(factorial)
