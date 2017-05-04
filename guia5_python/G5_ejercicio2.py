#!/usr/bin/env python
# coding=utf-8
from colored import bg, attr, fg
"""
    @author: Adrian Verdugo
    @contact: adrianverdugo273@gmail.com
    @github: adrian273
"""


print attr('bold'), bg('blue') + fg(15) + "Ejercicio numero 2" + attr('reset')
count = 0
number_students = int(raw_input('Ingrese numero de estudiantes\n'))
matrix = []
for i in range( number_students ):
    print "------------------------------------ \n"
    notes = float(raw_input('Ingrese notas\n'))
    matrix.append(notes)
    prom = sum(matrix) / number_students
    if matrix[i] < 4.0:
        count += 1
count = count * 100 / number_students

print bg('red') + fg(15) + "El porcentaje de promedios reprobados es: %" + str(count) + attr('reset')
print bg('blue') + fg(15) + "El promedio del curso es " + str(prom) + attr('reset')
