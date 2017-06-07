'''ejercicio_2.py
    @descrition: Crear un programa que permita registrar en un arreglo el tiempo de llegada a la meta de un maraton, el programa debe contar con el sgte menu:
            -> tiempo Promedio de la maraton.
            -> Tiempo Mayor de la maraton.
            -> Tiempo menor de la maraton.
            -> Cuantos Competidores llegaron sobre el tiempo promedio (Despues de).
            ** la competencia conto con 25 participantes.
            {'author' : 'Adrian Verdugo' }
'''
import os

person = []
COUNT_PERSON = 5

def add_person():
    for i in range(COUNT_PERSON):
        time = float(input('Ingrese tiempo: '))
        person.append(time)

def time_prom():
    """ Tiempo promedio de la maraton """
    prom = sum(person) / COUNT_PERSON
    return prom

def time_max():
    return max(person)

def time_min():
    return min(person)

def count_person_prom():
    count = 0
    for i in range(len(person)):
        if person[i] > time_prom():
            count += 1
    return count

def main():
    add_person()
    option = (
        ['\n | Menu de opciones | \n', None],
        ['1.. Tiempo promedio ', time_prom],
        ['2.. Tiempo Mayor ', time_max],
        ['3.. Tiempo Menor ', time_min],
        ['4.. Cantidad de personas que llegaron sobre el promedio', count_person_prom],
        ['5.. Salir', exit]
    )
    while True:
        for element in range(len(option)):
            print(option[element][0])
        try:
            select = int(input('> '))
            if select == 1:
                 print('El tiempo promedio es {}'.format(option[1][1]()))
            elif select == 2:
                print('Tiempo mayor: {}'.format(option[2][1]()))
            elif select == 3:
                print('Tiempo menor {}'.format(option[3][1]()))
            elif select == 4:
                print('Cantidad de personas que llegaron sobre el promedio: {}'.format(option[4][1]()))
            elif select == 5:
                option[5][1]()
        except ValueError:
            print('[Error] Ingresa un numero !')
        input('.:Pesiona una Tecla para continuar:.')
        os.system('clear')

if __name__ == '__main__':
    main()

