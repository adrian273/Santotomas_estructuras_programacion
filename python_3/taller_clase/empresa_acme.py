"""
    @description: La empresa ACME nesecita Registrar las horas 
    de trabajo de un mes X, generar en forma aleatoria valores
    entre 90 y 180.La empresa cuenta con 200 Trabajadores y maneja
    un valor de hora fijo de $1725, el programa debe llenar un 
    arreglo con los valores hora y desplegar el sgte menu:
        @opcion_1 = Renta promedio
        @opcion_2 = Renta mayor
        @opcion_3 = Renta menor
        @opcion_4 = ** tiene que estar vacia
        @opcion_5 = Salir
"""
from random import randint


hour = []
COUNT_PERSON = 200
VALUE_HOUR = 1725

"""" @generar las horas de trabajo aleatoriamente """
def generate_hour():
    for i in range(COUNT_PERSON):
        random_hour = randint(90, 180) 
        hour.append(random_hour)


def prom_renta():
    adittion = 0
    for h in hour:
        renta = h * VALUE_HOUR
        adittion += renta
    return int(adittion / COUNT_PERSON)


def max_renta():
    var_max_renta = 0
    for j in hour:
        renta = j * VALUE_HOUR
        if var_max_renta < renta:
            var_max_renta = renta
    return var_max_renta 


def min_renta():
    var_min_renta = 1000000
    for k in hour:
        renta = k* VALUE_HOUR
        if var_min_renta > renta:
            var_min_renta = renta
    return var_min_renta


def main():
    generate_hour()
    options = ['1.. Renta Promedio', '2.. Renta Mayor', 
                '3.. Renta Menor', '5..Salir']
    while True:
        for o in options:
            print(o)
        op = int(input('Ingresa opcion: '))
        if op == 1:
            print("El promedio de la renta es ${}".format(prom_renta()))
        elif op == 2:
            print('La renta mayor es ${}'.format(max_renta()))
        elif op == 3:
            print('La renta menor es ${}'.format(min_renta()))
        elif op == 5:
            exit()


if __name__  == '__main__':
    main()