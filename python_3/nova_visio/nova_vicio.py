
DATA_ADMIN = {'admin@nova.cl': 'admin'}


class DataEmployee:

    month = ''
    year = 0
    rut = ''
    name = ''
    category = ''
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


def main():
    while True:
        try:
            select = int(input('add new'))
            if select == 2:
                break
        except ValueError:
            print('[ERROR] Solo valores numericos: ')


if __name__ == '__main__':
    login()