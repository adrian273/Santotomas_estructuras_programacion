"""ejercicio_15.py
    @description: Que gestiona las notas de una clase de 20 alumnos de los cuales 
    sabemos el nombre y la nota. El programa debe ser capaz de:
            @Buscar un alumno. {ok}
            @Modificar su nota. {ok}
            @Realizar la media de todas las notas. {ok}
            @Realizar la media de las notas menores de 5. {sin terminar}
            @Mostrar el alumno que mejores notas ha sacado. {ok}
            @Mostrar el alumno que peores notas ha sacado. {ok}
"""
import os


COUNT_STUDENT = 20
data_students = {
                'adrian': 6.5, 'gonzalo': 4.2, 'andres': 5.6,
                'juan': 2.3, 'karen': 3.2, 'alice': 7.0, 
                'maria': 5.5, 'juana': 5.3,
                'jose': 4.3, 'perez': 2.3, 'gonzales': 5.3, 
                'peña': 4.3, 'verdugo': 5.3, 'catalina': 6.0,
                'escalona': 4.2, 'navarrete': 4.2, 'villegas': 4.3, 
                'elliot': 1.3, 'jovina': 6.9, 'rosa': 6.7
                }

def search_students():
    name = input('Ingrese nombre a buscar [ingresa -A para mostrar todos]: ')
    if name == '-A':
        for name, note in data_students.items():
            print("{} #=> {}".format(name, note))
    elif name in data_students:
        print("Nombre {}, nota {} ".format(name, data_students[name]))
    else:
        print("![ERROR]Este alumno no existe")


def update_note():
    update_note = input('Ingre alumno a editar [nota]: ')
    if update_note in data_students:
        print("Nota actual {} del alumno {}".format(data_students[update_note],update_note))
        new_note = float(input('Ingrese nueva nota: '))
        data_students[update_note] = new_note
        print("La nueva nota es {}".format(data_students[update_note]))
    else:
        print("![ERROR] Alumno no encontrado...")


def prom_note():
    count = 0
    for i in data_students:
        count += float(data_students[i])
    return  count / len(data_students)


def ranking_student(state=True):
    """ @Para saber cual es el alumno que tiene mejores y peores notas """
    best_note_student =  0.0
    bad_note_student = 8.0
    if state is not False:
        for best in data_students:
            if best_note_student < data_students[best]:
                best_note_student = data_students[best]
                name_alumn = best
        return 'La mejor nota es {} del alumn@ {}'.format(best_note_student, name_alumn)
    else:
        for bad in data_students:
            if bad_note_student > data_students[bad]:
                bad_note_student = data_students[bad]
                name_alumn = bad
        return 'La peor nota es {} del alumn@ {}'.format(bad_note_student, name_alumn)


def main():
    options = ['1.. Buscar alumno', '2.. Editar nota','3.. Media de las notas', 
                '5.. Mejor nota', '6.. Peor nota', '7.. Salir',]
    while True:
        print(" _____            _   _                   _        _   _       _            ")
        print("/ ____|          | | (_)                 | |      | \ | |     | |           ")
        print("| |  __  ___  ___| |_ _  ___  _ __     __| | ___  |  \| | ___ | |_ __ _ ___ ")
        print("| | |_ |/ _ \/ __| __| |/ _ \| '_ \   / _` |/ _ \ | . ` |/ _ \| __/ _` / __|")
        print("| |__| |  __/\__ \ |_| | (_) | | | | | (_| |  __/ | |\  | (_) | || (_| \__ \ ")
        print(" \_____|\___||___/\__|_|\___/|_| |_|  \__,_|\___| |_| \_|\___/ \__\__,_|___/")
        for op in options:
            print(op)
        try:
            select = int(input('Ingrese Opcion: '))
            if select == 1:
                title_1 = '\n | Buscador de Alumnos | \n'
                print(title_1.center(80, '-'))
                search_students()
            elif select == 2:
                title_1 = '\n | Actualizar Nota | \n'
                print(title_1.center(80, '-'))
                update_note()
            elif select == 3:
                title_1 = '\n | Media de las notas | \n'
                print(title_1.center(80, '-'))
                print('La media de las notas es {:.1F}'.format(prom_note()))
            elif select == 5:
                title_1 = '\n | Mejor nota | \n'
                print(title_1.center(80, '-'))
                print(ranking_student())
            elif select == 6:
                title_1 = '\n | Peor nota | \n'
                print(title_1.center(80, '-'))
                print(ranking_student(False))
            elif select == 7:
                title_1 = '\n | Adios... | <adrianverdugo273@gmail.com> \n'
                print(title_1.center(80, '-'))
                break
        except ValueError:
            print('![ERROR] Opcion no valida <<')
        input('::. Pesione una tecla para continuar .::')
        os.system('clear')

if __name__ == '__main__':
    main()