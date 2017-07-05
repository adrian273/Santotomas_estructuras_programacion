"""recuperativa.py
    @description: Almacenar ->
                            @ nombre
                            @ edad
                            @ estatura
                implementar usando funciones
                - Agregar una persona
                - Listar personas
                - Nombre persona mayor
                - Promedio edad persona
                - Nombre persona mas baja
                - Salir
    @author: Adrian Verdugo
"""

data = []

class Person:

    name = ''
    age = ''
    height = ''


def add_person():
    title = '\n | Agregar Personas | \n'
    print(title.center(100, '-'))
    p = Person()
    p.name = input('Nombre: ')
    p.age = int(input('Edad: '))
    p.height = float(input('Altura: '))
    data.append(p)


def view_person():
    title = '\n | Lista de Personas | \n'
    print(title.center(100, '-'))
    for i in data:
        print('{} -> {} años -> {}cm'.format(i.name, i.age, i.height))


def max_age_person():
    title = '\n | Edad Mayor | \n'
    print(title.center(100, '-'))
    max_age = 0
    for d in data:
        if max_age < d.age:
            max_age = d.age
            name_age = d.name
    print('La persona mayor es {} con {} años'.format(name_age, max_age))


def prom_age_person():
    title = '\n | Promedio Edad | \n'
    print(title.center(100, '-'))
    prom = 0
    for i in range(len(data)):
        prom += data[i].age
    prom = prom / len(data)
    print('El promedio es {} años'.format(prom))


def min_height_person():
    title = '\n | Altura mas baja | \n'
    print(title.center(100, '-'))
    min_height = 99999999
    for d in data:
        if min_height > d.height:
            min_height = d.height
            name_ = d.name
    print('La persona mas baja es {} con {}cm'.format(name_, min_height))


def main():
    options = ['1.. Agregar', '2.. Listar', 
                '3.. Nombre persona mayor', '4.. Promedio Edad', 
                '5.. Persona mas baja', '6.. Salir']
    while True:
        for o in options:
            print(o)
        try:
            select = int(input('Ingrese su opcion: '))
            if select == 1:
                add_person()
            elif select == 2:
                view_person()
            elif select == 3:
                max_age_person()
            elif select == 4:
                prom_age_person()
            elif select == 5:
                min_height_person()
            elif select == 6:
                break
        except ValueError:
            print('[ERROR] Solo valores numericos')


if __name__ == '__main__':
    main()