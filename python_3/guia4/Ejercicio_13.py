'''
    ::::::::::::::::::::::::::::::::::::::::::::::
    ::    @github: adrian273                    ::
    ::    @email: adrianverdugo273@gmail.com    ::
    ::::::::::::::::::::::::::::::::::::::::::::::
    13@ Leer el Sueldo y el número de cargas de un trabajador y reajustarlo sí:
        a. Tiene 2 o más cargas, reajuste en un 20%.
        b. Tiene 1 carga, reajuste en un 10%.
        c. No tiene carga, reajuste en 5%.
'''

salary = int(input('Ingrese Sueldo \n'))
number_cargo = int(input('Ingrese Numero de cargas \n'))
if number_cargo >= 2:
    salary = salary * 1.2
    print('El salario es: $' + str(salary))
elif number_cargo == 1:
    salary = salary * 1.1
    print('El salario es: $' + str(salary))
else:
    salary = salary * 1.05
    print('El salario es: $' + str(salary))
