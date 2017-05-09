'''
    ::::::::::::::::::::::::::::::::::::::::::::::
    ::    @github: adrian273                    ::
    ::    @email: adrianverdugo273@gmail.com    ::
    ::::::::::::::::::::::::::::::::::::::::::::::
    5@ Lea un	número, si	el	número	es	par muestre el	antecesor	del número	y si es	impar que muestre el	sucesor	del	número.
'''
number = int(input('Ingrese un numero \n'))
result = number % 2
if result == 0:
    mod_result = number - 1
    print('El antecesor de ' + str(number) + ' es ' + str(mod_result))
else:
    mod_result = number + 1
    print('El sucesor de ' + str(number) + ' es ' + str(mod_result))
