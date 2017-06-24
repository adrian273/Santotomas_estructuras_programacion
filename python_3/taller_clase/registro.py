COUNT_PERSON = 1

class Person:
    name = ''
    dni = ''
    age = 0


def add_data_person():
    for i in range(COUNT_PERSON):
        p = Person()
        p.name = input('Ingrese Nombre: ')
        p.dni = input('Ingrese Rut: ')
        p.age = int(input('Ingrese numero: '))
        print(p.name)


add_data_person()
