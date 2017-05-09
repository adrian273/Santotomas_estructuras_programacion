'''
    ::::::::::::::::::::::::::::::::::::::::::::::
    ::    @github: adrian273                    ::
    ::    @email: adrianverdugo273@gmail.com    ::
    ::::::::::::::::::::::::::::::::::::::::::::::
    4@  Lea	un	número	y determine	si	un	número	es	par o impar.Considere que un número par, al ser dividido por dos devuelve resto cero Utilice la operación MOD para calcular el resto, como se muestra a continuación:
                << resto = numero % 2
'''
number = int(input('Ingrese un numero \n'))
result = number % 2
if result == 0:
    print('El numero ' + str(number) + ' es par')
else:
    print('El numero ' + str(number) + ' es impar')
