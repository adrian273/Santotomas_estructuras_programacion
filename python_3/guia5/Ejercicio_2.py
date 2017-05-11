'''
    ::::::::::::::::::::::::::::::::::::::::::::::
    ::    @github: adrian273                    ::
    ::    @email: adrianverdugo273@gmail.com    ::
    ::::::::::::::::::::::::::::::::::::::::::::::
    2@ Leer notas de un curso y calcular:
        @ a.Porcentaje de notas menores a cuatro
        @ b. Promedio de notas del curso
'''

# @cantidad de estudiantes
quantity_students = int(input('Ingrese numero de estudiantes \n'))
count_notes = 0
count_red = 0

for i in range(quantity_students):
    notes_student = float(input('Ingrese nota \n'))
    if notes_student < 4.0:
        # @contador de notas rojas
        count_red += 1
    #@ contador de notas de los estudiantes
    count_notes += notes_student
porcentaje_notes_red = count_red * 100 / quantity_students
prom_students = count_notes / quantity_students

print('Porcentaje de notas rojas ' + str(porcentaje_notes_red) +"%")
print('El promedio de los estudiantes es ' + str(prom_students))
