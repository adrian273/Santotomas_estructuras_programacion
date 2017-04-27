#!/usr/bin/env python
# coding=utf-8
from colored import bg, fg, attr
"""
    @author: Adrian Verdugo
    @contact: adrianverdugo273@gmail.com
    @github: adrian273
"""

# array para los datos de los trabajadores
data_workers = []
total = 0

"""
    @type = variables para dar estilos
"""
colors = [bg('blue') + fg(15), bg('red') + fg(15), bg('purple_3') + fg(15)]
reset = attr('reset')
bold = attr('bold')

print bold + colors[0] + "Ejercicio numero 3" + reset
for i in range(1):
    #_____________ datos de trabajadores _______________________
    print "¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨"
    name =  str(raw_input('>> ingresa nombre \n'))
    hours_work = int(raw_input('>> ingresa horas de trabajo \n'))
    value_hours = int(raw_input('>> ingresa valor hora \n'))
    number_cargo = int(raw_input('>> Ingrese numero carga \n'))
    #_____________ salario normal del trabajador _______________
    salary = hours_work  * value_hours
    if number_cargo >= 3:
        salary = salary * 1.1
    elif number_cargo == 1 or number_cargo == 2:
        salary = salary * 1.05
    """
        * agregando los valores al
        * @diccionario de datos
    """
    data_workers.append(
        {
            'name': name,
            'hours_work': hours_work,
            'value_hours': value_hours,
            'number_cargo': number_cargo,
            'salary': salary
        }
    )

print colors[2] + bold + "Datos a pagar al trabajador \n" +reset

"""
    @data_workers = [{}]

"""
for data in data_workers:
    print colors[0] + "* Nombre "+ data['name'].title() + ", sueldo a pagar $" + str(int(data['salary'])) + reset
    total = int(data['salary']) + total
print "--------------------------------------------------------------\n"
print colors[1] + "Total a pagar: $" + str(total) + reset
