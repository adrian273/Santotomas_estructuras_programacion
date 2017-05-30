'''ejercicio_3.py
    description:Lea las Horas trabajadas, valor hora para los trabajadores de una empresa. 
                Si el número de cargas es 3 o más, aumentar el sueldo en 12%, 
                si tiene 1 ó 2 cargas, aumentar en 7% el sueldo. Dejará de
                leer cuando las Horas Trabajadas sea igual a cero. Calcular:
                    a. Sueldo de cada trabajador.
                    b. Sueldo promedio.
                    c. Promedio de Horas trabajadas
                    @author: Adria Verdugo
 
'''
title = '\n | Horas Trabajadas | \n'
print(title.center(100, '-'))

salary_count = 0
working_count = 0
time_count = 0
time_work = int(input('Ingrese horas de trabajo: '))
while time_work != 0:
    time_value = int(input('Ingrese valor hora: '))
    number_cargo = int(input('Ingrese numero de cargas: '))
    salary = time_work*time_value
    if number_cargo >= 3:
        salary *= 1.12
    elif number_cargo == 1 or number_cargo == 2:
        salary *= 1.07
    salary_count += salary
    working_count += 1
    time_count += time_work
    salary_title = ' Salario del trabajador '
    print(salary_title.center(50, '*'))
    print(':: El salario del trabajador es: ${:.0f}'.format(salary))
    print('------------------------------------------')
    time_work = int(input('Ingrese horas de trabajo: '))

end_title = '\n | Resultados | \n'
print(end_title.center(100, '-'))

prom_value = salary_count/working_count
prom_time = time_count/working_count
print(':: El sueldo promedio es : ${:.2f}'.format(prom_value))
print(':: El promedio de las horas trabajadas es: {}'.format(prom_time))