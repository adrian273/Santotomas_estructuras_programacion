'''
    ::::::::::::::::::::::::::::::::::::::::::::::
    ::    @github: adrian273                    ::
    ::    @email: adrianverdugo273@gmail.com    ::
    ::::::::::::::::::::::::::::::::::::::::::::::
    7@ Lea las horas trabajadas de un trabajador, valor hora, número de cargas y determine,Si el número de cargas es mayor o igual a 3 asigne un bono de un 10% sobre el salario, Si el
    número de cargas es 2, asigne un bono del 5% y si tiene una carga entonces asigne un 3%
    de bono. Muestre el salario del trabajador.
'''
time_work = int(input('Ingrese horas de trabajo \n'))
value_time = int(input('Ingrese valor de hora \n'))
number_cargo = int(input('Ingrese numero de carga \n'))
salary = time_work * value_time
if number_cargo >= 3:
    salary_bono = salary * 1.1
    print('El salario final es $' + str(int(salary_bono)))
elif number_cargo == 2:
    salary_bono = salary * 1.05
    print('El salario final es $' + str(int(salary_bono)))
else:
    salary_bono = salary * 1.03
    print('El salario final es $' + str(int(salary_bono)))
