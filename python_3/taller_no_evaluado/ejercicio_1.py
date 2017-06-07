'''ejercicio_1.py
    @description: Crear un programa que tenga el siguiente menu:
        Menu
        1. Calcular Multiplicacion de A * B
        2. Calcular el Factorial
        @Utilizar funciones en cada calculo.
        @para el calculo de la multiplicacion de a * b, utilizar solo suma.
'''

def multiplication():
    number_1 = int(input('Ingrese numero: '))
    number_2 = int(input('Ingrese numero: '))
    addition = 0
    for i in range(number_1):
        addition += number_2
    result = '\n El resultado es : {} \n'.format(addition)
    return result


def factorial():
    number = int(input('Ingrese numero: '))
    fact = 1
    while number > 1:
        fact *= number
        number -= 1
    result = '\n El factorial es {} \n'.format(fact)
    return result


def main():
    while True:
        title = '\n | Menu | \n'
        print(title.center(100, '-'))
        print('1.. Calcular Multiplicacion', end='\n')
        print('2.. Calcular el factorial', end='\n')
        print('3.. Salir')
        option = int(input('Ingrese su opcion: '))
        if option == 1:
            print(multiplication().center(120, '-'))
        elif option == 2:
            print(factorial().center(100, '*'))
        elif option == 3:
            exit()
        else:
            MSG_ERROR = '\n ingrese una opcion valida! \n'
            print(MSG_ERROR.center(100, '!'))

if __name__ == '__main__':
    main()