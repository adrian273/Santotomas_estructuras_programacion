
'''ejercicio_2.py
    @description: Hacer el Pseudocódigo que Lea las notas de un curso de 40 alumnos y calcule:
        a. Porcentaje de notas Rojas.
        b. Porcentaje de notas Azules.
        c. Número de Notas entre 3,5 y 4,0.
    @author: Adrian Verdugo
'''
title = '\n | Notas de los estudiantes | \n'
print(title.center(100, '-'))

count_student = 40
red_note = 0
blue_note = 0
count_note = 0

for i in range(count_student):
    note_student = float(input('Ingrese nota: '))
    if note_student < 4.0:
        red_note += 1
    else:
        blue_note += 1
    if note_student > 3.5 and note_student < 4.0:
        count_note += 1

por_red_note = red_note*100 / count_student
por_blue_note = blue_note*100 / count_student

end_title = '\n | Resultados | \n'
print(end_title.center(100, '-'))

print(':: El porcentaje de notas rojas es {}%'.format(por_red_note))
print(':: El porcentaje de notas azules es {}%'.format(por_blue_note))
print(':: El numero de notas entre 3.5 & 4.0 son {}'.format(count_note))