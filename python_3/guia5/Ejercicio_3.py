'''
    ::::::::::::::::::::::::::::::::::::::::::::::
    ::    @github: adrian273                    ::
    ::    @email: adrianverdugo273@gmail.com    ::
    ::::::::::::::::::::::::::::::::::::::::::::::
    3@ Leer para un empresa de 50 trabajadores, horas de trabajo, valor hora, numero de cargas. Si el numero de cargas es 3 o mas, aumentar el sueldo en 10%. Si tiene 1 o 2 cargas, aumentar en 5% el sueldo calcular:
        a. sueldo de cada trabajador
        b. sueldo que se debe pagar la empresa
'''

salary_count = 0

for i in range(3):
    time_work = int(input('Ingrese horas de trabajo \n'))
    value_time = int(input('Ingrese valor hora \n'))
    number_cargo = int(input('Ingrese numero de cargas \n'))
    salary = time_work * value_time
    if number_cargo >= 3:
        salary = salary * 1.1
    elif number_cargo == 1 or number_cargo == 2:
        salary = salary * 1.05
    salary_count += salary
    print('El sueldo del trabajador es $' + str(int(salary)))
print('El sueldo total a pagar de la empresa es $' + str(int(salary_count)))
