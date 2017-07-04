import os
import getpass

DATA_ADMIN = {'a': 'a'}
CATEGORY_EMPLOYEE =  ['novato', 'experto', 'supervisor', 'admin']
HEALTH_EMPLOYEE = ['a', 'b', 'c']
MONTH = ['enero', 'febrero', 'marzo', 'abril',
            'mayo', 'junio', 'julio', 'agosto',
            'septiembre', 'octubre', 'noviembre',
            'diciembre'
        ]
list_employee = []


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
        elif month in MONTH:
            data.month = month
            break
        else:
            print('[ERROR] Mes invalido !')
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
                print('[ERROR] a sobrepaso el limite << min 0 - max 30')
            else:
                data.day_absent = day_absent
            break
        except ValueError:
            print('::. ![ERROR] Solo valores numericos .::')
    while True:
        afp = input('AFP: ')
        if validation_empty(afp):
            print(MSG_EMPTY)
        elif afp == 'si' or afp == 'no':
            data.afp = afp
            break
        else:
            print('[ERROR] Valor ingresado incorrecto')
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
    list_employee.append(data)



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


def calculation_salary():
    bono = 50000
    title = '\n| Calcular Sueldo |\n'
    print(title.center(100, '-'))
    rut = input('Rut: ')
    sub_title = '\n | Resultado | \n'
    print(sub_title.center(100, '-'))
    for l in list_employee:
        if rut == l.rut:
            if l.afp == 'si':
                por_afp = (l.salary/100) * 10
            else:
                por_afp = 0
            """" Resivar este punto """
            if l.sys_health == 'a':
                por = (l.salary/100) * 5.7
            elif l.sys_health == 'b':
                por = (l.salary/100) * 6.1
            elif  l.sys_health == 'c':
                por = (l.salary/100) * 6.5
            # Preguntar sobre duda del sueldo bruto
            if l.day_absent == 0 and l.category == 'experto':
                salary_bono = l.salary + (bono*2)
            elif l.day_absent == 0:
                salary_bono = l.salary + bono
            else:
                salary_bono = l.salary
            salary_total = salary_bono - (por_afp + por)
            print('Nombre: {}'.format(l.name))
            print('Salario en bruto: ${}'
                .format(l.salary))
            print('Descuento de AFP: ${}'
                    .format(por_afp))
            # [IMPORTANT] -> Proximo a cambio!
            print('Descuento de salud [{}]: ${}'
                    .format(l.sys_health, por))
            print('Salario + Bono: {}'.format(salary_bono))
            print('Salario Total: ${}'.format(salary_total))
            return True
    return False


def view_employee():
    title = '\n | Vista de Empleados | \n'
    print(title.center(100, '-'))
    print('Nombre => rut => sueldo bruto => afp => salud')
    print('_____________________________________________\n')
    for e in list_employee:
        print('{0} => {1} => ${2} => {3} => {4}'
            .format(e.name, e.rut, e.salary, e.afp, e.sys_health))


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
            elif select == 2:
                if not calculation_salary():
                    print("![ERROR] trabajador no registrado")
            elif select == 3:
                view_employee()
            elif select == 5:
                break
        except ValueError:
            print('[ERROR] Solo valores numericos: ')
        input('Presione una tecla para continuar []')
        os.system('clear')


if __name__ == '__main__':
    login()
