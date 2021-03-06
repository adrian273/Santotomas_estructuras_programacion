import os

CATEGORY_EMPLOYEE = ['novato', 'experto', 'supervisor', 'administrativo']
HEALTH_EMPLOYEE = ['a', 'b', 'c']
MONTH = ['enero', 'febrero', 'marzo',
         'abril', 'mayo', 'junio', 'julio',
         'agosto', 'septiembre', 'octubre',
         'noviembre', 'diciembre'
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
    salary = 0  # monto en sueldo bruto


def login(DATA_ADMIN={None: None}):
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
                clear()
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
    title = '\n | Agregar Datos | \n'
    print(title.center(100, '-'))
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
    """ Para ayudar a ingresar datos, entre otros  (Ayudas)"""
    if function == 'add_data':
        print(add_data.__doc__)


def validation_empty(var):
    """ Validacion si esta vacio """
    if var and var.strip():
        return False
    return True


def calculation_salary(rut=None, month=None, year=None):
    """ Calcular Salario del trabajador ingresando su mes"""
    bono = 50000
    title = '\n| Calcular Sueldo |\n'
    print(title.center(100, '-'))
    if rut is None and month is None:
        rut = input('Rut: ')
        month = input('Mes: ')
        if validation_empty(rut) or validation_empty(month):
            print('![ERROR] campos vacios!')
        else:
            sub_title = '\n | Resultado | \n'
            print(sub_title.center(100, '-'))
            for l in list_employee:
                if month not in MONTH:
                    print('![ERROR] * Ingreso de mes incorrecto ')
                    return False
                elif rut == l.rut and month in MONTH and month == l.month:
                    if l.afp == 'si':
                        por_afp = (l.salary / 100) * 10
                    else:
                        por_afp = 0
                    if l.sys_health == 'a':
                        por = (l.salary / 100) * 5.7
                    elif l.sys_health == 'b':
                        por = (l.salary / 100) * 6.1
                    elif l.sys_health == 'c':
                        por = (l.salary / 100) * 6.5
                    if l.day_absent == 0 and l.category == 'experto':
                        salary_bono = l.salary + (bono * 2)
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
                    print('Descuento de salud [{}]: ${}'
                        .format(l.sys_health, por))
                    print('Salario + Bono: {}'.format(salary_bono))
                    print('Salario Total: ${}'.format(salary_total))
            return True
    elif rut and month is None and year is None:
        for s_rut in list_employee:
            if rut == s_rut.rut:
                if s_rut.afp == 'si':
                    por_afp = (s_rut.salary / 100) * 10        
                else:
                    por_afp = 0    
                if s_rut.sys_health == 'a':
                    por = (s_rut.salary / 100) * 5.7
                elif s_rut.sys_health == 'b':
                    por = (s_rut.salary / 100) * 6.1
                elif s_rut.sys_health == 'c':
                    por = (s_rut.salary / 100) * 6.5
                if s_rut.day_absent == 0 and s_rut.category == 'experto':
                    salary_bono = s_rut.salary + (bono * 2)
                elif s_rut.day_absent == 0:
                    salary_bono = s_rut.salary + bono
                else:
                    salary_bono = s_rut.salary
                salary_total = salary_bono - (por_afp + por)
                print('Nombre: {}'.format(s_rut.name))
                print('Salario en bruto: ${}'
                    .format(s_rut.salary))
                print('Descuento de AFP: ${}'
                    .format(por_afp))
                print('Descuento de salud [{}]: ${}'
                    .format(s_rut.sys_health, por))
                print('Salario + Bono: {}'.format(salary_bono))
                print('Salario Total: ${}'.format(salary_total))
                print('Mes: {}'.format(s_rut.month))
                print('---------------------------------------')
        return True
    elif rut is None and month and year:
        for s_my in list_employee:
            if month not in MONTH:
                print('![ERROR] * Ingreso de mes incorrecto ')
                return False
            elif month == s_my.month and year == s_my.year:
                if s_my.afp == 'si':
                    por_afp = (s_my.salary / 100) * 10        
                else:
                    por_afp = 0    
                if s_my.sys_health == 'a':
                    por = (s_my.salary / 100) * 5.7
                elif s_my.sys_health == 'b':
                    por = (s_my.salary / 100) * 6.1
                elif s_my.sys_health == 'c':
                    por = (s_my.salary / 100) * 6.5
                if s_my.day_absent == 0 and s_my.category == 'experto':
                    salary_bono = s_my.salary + (bono * 2)
                elif s_my.day_absent == 0:
                    salary_bono = s_my.salary + bono
                else:
                    salary_bono = s_my.salary
                salary_total = salary_bono - (por_afp + por)
                print('Nombre: {}'.format(s_my.name))
                print('Salario en bruto: ${}'
                    .format(s_my.salary))
                print('Descuento de AFP: ${}'
                    .format(por_afp))
                print('Descuento de salud [{}]: ${}'
                    .format(s_my.sys_health, por))
                print('Salario + Bono: {}'.format(salary_bono))
                print('Salario Total: ${}'.format(salary_total))
                print('Mes: {}'.format(s_my.month))
                print('año: {}'.format(s_my.year))
                print('---------------------------------------')
        return True
    return False


def view_employee():
    """ Listar Empleados """
    title = '\n | Vista de Empleados | \n'
    print(title.center(100, '-'))
    print('Nombre => rut => sueldo bruto => afp => salud')
    print('_____________________________________________\n')
    for e in list_employee:
        print('{0} => {1} => ${2} => {3} => {4}'
              .format(e.name, e.rut, e.salary, e.afp, e.sys_health))


def data_employee_main():
    """ Menu de listar liquidaciones """
    options = ['1.. Por mes - año', '2.. Por Rut', '3.. Salir']
    while True:
        title = '\n | Menu de liquidaciones | \n'
        print(title.center(100, '-'))
        for o in options:
            print(o)
        try:
            select = int(input('Opcion: '))
            if select == 1:
                month = input('Mes: ')
                year = int(input('Año: '))
                if validation_empty(month):
                    print('![ERROR] Campo vacio!')
                elif not calculation_salary(None, month, year):
                    print('![ERROR] no se encuentra el registro')
            elif select == 2:
                rut = input('Rut: ')
                if validation_empty(rut):
                    print('![ERROR] Campo vacio!')
                if not calculation_salary(rut): print('![ERROR] no se encuentra el registro')
            elif select == 3:
                break
            else:
                print('![ERROR] Opcion no disponible')
        except ValueError:
            print('[ERROR] Tipo de dato incorrecto!')
        input('[]Presiona')
        clear()


def clear():
    if os.name == 'posix':
        os.system('clear')
    elif os.name in ('nt', 'dos', 'ce'):
        os.system('cls')


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
                    print("![ERROR] No se encuentra en el registro")
            elif select == 3:
                view_employee()
            elif select == 4:
                data_employee_main()
            elif select == 5:
                break
        except ValueError:
            print('[ERROR] Solo valores numericos: ')
        input('Presione una tecla para continuar []')
        clear()


if __name__ == '__main__':
    login({'admin@nova.cl': 'admin'})
