import os


DATA_ADMIN = {'admin@nova.cl': 'admin'}
CATEGORY_EMPLOYEE =  ['novato', 'experto', 'supervisor', 'admin']

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
            password = input('Contraseña: ')
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
    """
    data = DataEmployee()
    data.month = input('Mes: ')
    data.year = int(input('Año: '))
    data.rut = input('Rut: ')
    data.name = input('Nombre: ')
    while True:
        category = input('Ingrese categoria [ -h para ayuda ]: ')
        if category in CATEGORY_EMPLOYEE:
            data.category = category
            break
        elif category == '-h':
            help_system('add_data')
        else:
            print('![ERROR] Esta categoria no existe!')
    print(data.category)


def help_system(function):
    if function == 'add_data':
        print(add_data.__doc__)


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