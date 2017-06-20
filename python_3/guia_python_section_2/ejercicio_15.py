"""ejercicio_15.py
    @description: Que gestiona las notas de una clase de 20 alumnos de los cuales 
    sabemos el nombre y la nota. El programa debe ser capaz de:
            @Buscar un alumno. {ok}
            @Modificar su nota. {sin terminar}
            @Realizar la media de todas las notas. {sin terminar}
            @Realizar la media de las notas menores de 5. {sin terminar}
            @Mostrar el alumno que mejores notas ha sacado. {sin terminar}
            @Mostrar el alumno que peores notas ha sacado. {sin terminar}
"""


# uniform -> devuelve un numero float incluido los valores indicados.
# choise -> develve una lista al azar string
from random import uniform, choice
import os


COUNT_STUDENT = 20
NAME_STUDENTS = [
                'adrian', 'gonzalo', 'andres',
                'juan', 'karen', 'alice', 'maria', 'juana'
                ]

SURNAME_STUDENTS = [
                    'perez', 'gonzales', 'peña', 'verdugo',
                    'escalona', 'navarrete', 'adasme'
                    ]

data_students = []


def generate_data_students():
    for i in range(COUNT_STUDENT):
        note = uniform(1, 7)
        name = choice(NAME_STUDENTS)
        surname = choice(SURNAME_STUDENTS)
        data_students.append(
                                {
                                    'name': '{} {}'.format(name, surname), 
                                    'note': '{:.1F}.'.format(note)
                                }
                            )


def search_students():
    name = input('Ingrese nombre a buscar: ')
    sub_title_1 = '\n [resultados] \n'
    print(sub_title_1.center(80, '~'))
    for i in data_students:
        if name in i['name']:
            print('{} => {} '.format(i['name'], i['note']))


def main():
    generate_data_students()
    options = ['1.. Buscar alumno', '5.. Salir']
    while True:
        title = '\n | Gestion de Notas | \n'
        print(title.center(80, '-'))
        for op in options:
            print(op)
        try:
            select = int(input('Ingrese Opcion: '))
            if select == 1:
                title_1 = '\n | Buscador de Alumnos | \n'
                print(title_1.center(80, '-'))
                search_students()
            elif select == 5:
                break
        except ValueError:
            print('![ERROR] Opcion no valida <<')
        input('::. Pesione una tecla para continuar .::')
        os.system('clear')


if __name__ == '__main__':
    main()
