import os
import getpass

DATA_ADMIN = {'admin@nova.cl': 'admin'}
CATEGORY_EMPLOYEE =  ['novato', 'experto', 'supervisor', 'admin']
HEALTH_EMPLOYEE = ['a', 'b', 'c']
DATA = []


class DataEmployee:

    month = ''
    year = 0
    rut = ''
    name = ''
    category = ''  # => [novato, experto, supervisor, admin]
    day_absent = 0
    afp = ''
    sys_health = ''  # sistema de salud => [a, b, c]
    salary = 0  #  monto en sueldo bruto
    

def login():
    print(" _                 _       ")
    print("| |               (_)      ")
    print("| |     ___   __ _ _ _ __  ")
    print("| |    / _ \ / _` | | '_ \ ")
    print("| |___| (_) | (_| | | | | |")
    print("|______\___/ \__, |_|_| |_|")
    print("              __/ |        ")
    print("             |___/         ")
    blocking = 0
    count = 3
    msg_error = '\n | ![ERROR] ACCESO DENEGADO ! | \n'
    attempts = 'Numeros de intentos disponibles: {}'
    while True:
        email = input('Email: ')
        if email in DATA_ADMIN:
            password = getpass.getpass('Contraseña: ')
            if DATA_ADMIN[email] == password:
                os.system('clear')
                main()
                break
            else:
                blocking += 1
                count -= 1
                print(msg_error.center(100, '*'))
                print(attempts.format(count))
        else:
            blocking += 1
            count -= 1
            print(msg_error.center(100, '*'))
            print(attempts.format(count))
        if blocking == 3:
            print('No quedan mas intentos disponibles ...')
            break


def add_data():
    """ 
    Agregar datos de los trabajadores:
    @ Categorias Disponibles:
        -> novato
        -> experto
        -> supervisor
        -> administrativo
    @ sistemas de salud disponibles:
        -> a
        -> b
        -> c
    """
    MSG_EMPTY = '[ERROR] no hay datos que ingresar'
    data = DataEmployee()
    while True:
        month = input('Mes: ')
        if validation_empty(month):
            print(MSG_EMPTY)
        else:
            data.month = month
            break
    while True:
        year = input('Año: ')
        if validation_empty(year):
            print(MSG_EMPTY)
        else:
            data.year = int(year)
            break
    while True:
        rut = input('Rut: ')
        if validation_empty(rut):
            print(MSG_EMPTY)
        else:
            data.rut = rut
            break
    while True:
        name = input('Nombre: ')
        if validation_empty(name):
            print(MSG_EMPTY)
        else:
            data.name = name
            break
    while True:
        category = input('Ingrese categoria [ h para ayuda ]: ')
        if validation_empty(category):
            print(MSG_EMPTY)
        elif category in CATEGORY_EMPLOYEE:
            data.category = category
            break
        elif category == 'h':
            help_system('add_data')
        else:
            print('![ERROR] Esta categoria no existe!')
    while True:
        try:
            day_absent = int(input('Dias ausentes: '))
            if day_absent > 30 or day_absent < 0:
                print('[ERROR] a sobrepaso el limite << max 30')
            else:
                data.day_absent = day_absent
                break
        except ValueError:
            print('::. ![ERROR] Solo valores numericos .::')
    while True:
        afp = input('AFP: ')
        if validation_empty(afp):
            print(MSG_EMPTY)
        else:
            data.afp = afp
            break
    while True:
        sys_health = input('Sistema de salud: [ h para ayuda]: ')
        if validation_empty(sys_health):
            print(MSG_EMPTY)
        elif sys_health in HEALTH_EMPLOYEE:
            data.sys_health = sys_health
            break
        elif sys_health == 'h':
            help_system('add_data')
        else:
            print('![ERROR] Este sistema no existe!')
    while True:
        try:
            salary = int(input('Salario: '))
            if salary < 0:
                print('[ERROR] Numero negativo')
            else:
                data.salary = salary
                break
        except ValueError:
            print('::. ![ERROR] Solo valores numericos .::')



def help_system(function):
    if function == 'add_data':
        print(add_data.__doc__)


def validation_empty(var):
    """ 
        Validacion si esta vacio 
        -> strip() elimina caracteres
    """
    if var and var.strip():
        return False
    return True



def main():
    OPTIONS = ['1.. Ingresar datos', '2.. Calcular sueldo', 
                '3.. Mostrar Empleados ', '4.. Mostrar liquidaciones', 
                '5.. Salir']
    while True:
        print("                -> Bienvenido <-                ")
        print("  _   _              __      ___  _____ _       ")
        print(" | \ | |             \ \    / (_)/ ____(_)      ")
        print(" |  \| | _____   ____ \ \  / / _| (___  _  ___  ")
        print(" | . ` |/ _ \ \ / / _` \ \/ / | |\___ \| |/ _ \ ")
        print(" | |\  | (_) \ V / (_| |\  /  | |____) | | (_) |")
        print(" |_| \_|\___/ \_/ \__,_| \/   |_|_____/|_|\___/ ")
        print("                                                ")
        for o in OPTIONS:
            print(o)
        try:
            select = int(input('Ingresa tu opcion: '))
            if select == 1:
                add_data()
            elif select == 5:
                break
        except ValueError:
            print('[ERROR] Solo valores numericos: ')
        input('Presione una tecla para continuar []')
        os.system('clear')


if __name__ == '__main__':
    login()