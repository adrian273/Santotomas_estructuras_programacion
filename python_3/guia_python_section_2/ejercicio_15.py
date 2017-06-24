"""ejercicio_15.py
    @description: Que gestiona las notas de una clase de 20 alumnos de los cuales 
    sabemos el nombre y la nota. El programa debe ser capaz de:
            @Buscar un alumno. {ok}
            @Modificar su nota. {ok}
            @Realizar la media de todas las notas. {ok}
            @Realizar la media de las notas menores de 5. {sin terminar}
            @Mostrar el alumno que mejores notas ha sacado. {sin terminar}
            @Mostrar el alumno que peores notas ha sacado. {sin terminar}
"""
import os


COUNT_STUDENT = 20
data_students = {
                'adrian': 6.5, 'gonzalo': 4.2, 'andres': 5.6,
                'juan': 1.3, 'karen': 1.2, 'alice': 7.0, 
                'maria': 5.5, 'juana': 5.3,
                'jose': 4.3, 'perez': 2.3, 'gonzales': 5.3, 
                'peña': 4.3, 'verdugo': 5.3,
                'escalona': 4.2, 'navarrete': 4.2, 
                'adasme': 1.3, 'villegas': '4.3', 
                'elliot': 1.3, 'jovina': 7.0, 'rosa': 6.9
                }

print(data_students)
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
    return  count / COUNT_STUDENT


def main():
    options = ['1.. Buscar alumno', '2.. Editar nota',
                '3.. Media de las notas', '5.. Salir',]
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
            elif select == 2:
                title_1 = '\n | Actualizar Nota | \n'
                print(title_1.center(80, '-'))
                update_note()
            elif select == 3:
                title_1 = '\n | Media de las notas | \n'
                print(title_1.center(80, '-'))
                print('La media de las notas es {:.1F}'.format(prom_note()))
            elif select == 5:
                title_1 = '\n | Adios... | \n'
                print(title_1.center(80, '-'))
                break
        except ValueError:
            print('![ERROR] Opcion no valida <<')
        input('::. Pesione una tecla para continuar .::')
        os.system('clear')

if __name__ == '__main__':
    main()