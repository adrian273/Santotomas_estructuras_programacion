"""trabajador.py
    @description: Almacrnr los siguientes datos:
        @rut
        @nombre
        @valor hora
        @horas trabajadas
    Hacer un menu con las siguientes operaciones
        @agregar un trabajador
        @buscar un trabajador por rut
        @buscar un trabajador por nombre
        @Calcular sueldo de un trabajador
        @ver lista trabajadores
        @salir
"""
import os

data_employee = []

class Employee:
    rut = ''
    name = ''
    value_hour = 0
    worked_time = 0


def add_employee():
    e = Employee()
    e.name = input('Ingrese nombre: ')
    e.rut = input('Ingrese rut: ')
    e.value_hour = int(input('Ingrese valor hora: '))
    e.worked_time = int(input('Ingrese horas trabajadas: '))
    data_employee.append(e)
    print('[ Agregado con exito ]')


def search_rut():
    rut = input('Ingrese rut: ')
    for e in data_employee:
        if rut in e.rut and rut == e.rut:
            print('Nombre {}, valor hora ${}, horas trabajadas {}'.format(e.name,e.value_hour, 
                                                                            e.worked_time))

def search_name():
    name = input('Ingrese nombre: ')
    for e in data_employee:
        if name in e.name and name == e.name:
            print('Nombre {}, valor hora ${}, horas trabajadas {} '.format(e.name, e.value_hour, 
                                                                            e.worked_time))

def salary():
    rut = input('Ingrese rut: ')
    for e in data_employee:
        if rut in e.rut and e.rut == rut:
            salary = e.value_hour * e.worked_time
            print('Nombre {}, sueldo total ${}'.format(e.name, salary))


def view_data_employee():
    for data in data_employee:
        print('-> {} [{}]'.format(data.name, data.rut))


def main():
    while True:
        print(" _______         _            _          _                     ")
        print("|__   __|       | |          (_)        | |                    ")
        print("    | |_ __ __ _| |__   __ _ _  __ _  __| | ___  _ __ ___  ___   ")
        print("    | | '__/ _` | '_ \ / _` | |/ _` |/ _` |/ _ \| '__/ _ \/ __|  ")
        print("    | | | | (_| | |_) | (_| | | (_| | (_| | (_) | | |  __/\__ \  ")
        print("    |_|_|  \__,_|_.__/ \__,_| |\__,_|\__,_|\___/|_|  \___||___/  ")
        print("                           _/ |                                  ")
        print("                          |__/                                   ")
        options = ['1.. Agregar Trbajadores','2.. Buscar por rut',
                    '3.. Buscar por nombre', '4.. Salario Total', 
                    '5.. Ver lista','6.. Salir']
        for o in options:
            print(o)
        try:
            select = int(input('Ingrese opcion: '))
            if select == 1:
                title = '\n | Agregar Trabajadores | \n'
                print(title.center(100, '-'))
                add_employee()
            elif select == 2:
                if not data_employee:
                    print('![ERROR]::. No hay datos ingresados.::')
                else:
                    title = '\n | Buscar por rut | \n'
                    print(title.center(100, '-'))
                    search_rut()
            elif select == 3:
                if not data_employee:
                    print('![ERROR]::. No hay datos ingresados.::')
                else:
                    title = '\n | Buscar por nombre | \n'
                    print(title.center(100, '-'))
                    search_name()
            elif select == 4:
                if not data_employee:
                    print('![ERROR]::. No hay datos ingresados.::')
                else:
                    title = '\n | Ver salario total | \n'
                    print(title.center(100, '-'))
                    salary()
            elif select == 5:
                if not data_employee:
                    print('![ERROR]::. No hay datos ingresados.::')
                else:
                    title = '\n | Ver trabajadores| \n'
                    print(title.center(100, '-'))
                    view_data_employee()
            elif select == 6:
                msg = '\n | Adios ... | \n'
                print(msg.center(100, '-'))
                break
        except ValueError:
            print ('![ERROR]:: Solo valores numericos ::.')
        input('::.Presione una tecla para continuar ::.')
        if os.name == 'nt':
            os.system('cls')
        elif os.name == 'posix':
            os.system('clear')

if __name__ == '__main__':
    main()
