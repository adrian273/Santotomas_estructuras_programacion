'''
    ::::::::::::::::::::::::::::::::::::::::::::::
    ::    @github: adrian273                    ::
    ::    @email: adrianverdugo273@gmail.com    ::
    ::::::::::::::::::::::::::::::::::::::::::::::
    10@ Para el ejercicio número ocho considere el genero del trabajador, Si el trabajador e Femenino, aplique un reajuste del 5%, sino lo es aplique un reajuste del 3% al salario.-
'''
time_work = int(input('Ingrese horas de trabajo \n'))
value_time = int(input('Ingrese valor de hora \n'))
number_cargo = int(input('Ingrese numero de carga \n'))
gender = input('Ingrese su genero \n')
salary = time_work * value_time

if gender == 'femenino':
    salary = salary * 1.05
    print('Salario con reajuste de genero $' + str(salary))
else:
    salary = salary * 1.03
    print('Salario con reajuste de genero $' + str(salary))

if number_cargo >= 3:
    salary_bono = salary * 1.1
    print('El salario final es $' + str(int(salary_bono)))
elif number_cargo == 2:
    salary_bono = salary * 1.05
    print('El salario final es $' + str(int(salary_bono)))
else:
    salary_bono = salary * 1.03
    print('El salario final es $' + str(int(salary_bono)))
