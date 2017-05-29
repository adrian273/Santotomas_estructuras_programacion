#!/usr/bin/env python
# coding=utf-8

'''
    1. Hacer el codigo que Lea, para los participantes de una maratón, el
        tiempo que se demoraron en llegar a la meta, el género, la estatura y la
        edad(Los tiempos son ingresados sin orden), dejara de leer cuando la
        estatura sea igual a cero. Calcular:
            a. Número de personas que llegaron a la meta. {ok}
            b. Tiempo promedio de la maratón. {ok}
            c. Estatura promedio de los atletas. {ok}
            d. Edad promedio de los atletas. {ok}
            e. El tiempo Mayor. {ok}
            f. La edad Menor. {ok}
            g. Porcentaje de Mujeres que participaron en la maratón. {ok}
    @author: Adrian Verdugo
'''

# title
title = '\n | Participantes de la maraton |\n'
print(title.center(120, '-'))
# end title

height = float(input('Ingrese altura: '))
number_person = 0
female = 0
prom_time = 0
prom_height = 0
prom_age = 0
max_time = 0
min_age = 99999

while height > 0:
    time = float(input('Ingrese tiempo: '))
    gender = input('Ingrese genero: ')
    age = int(input('Ingrese edad: '))
    if gender == 'femenino':
        female += 1
    if max_time < time:
        max_time = time
    if min_age > time:
        min_age = age
    number_person += 1  # Numero de personas que llegaron a la meta
    prom_time += time  # Para calcular el tiempo promedio de la maraton
    prom_height += height  # Para calcular estatura promedio de los participantes
    prom_age += age
    print('-------------------------------')
    height = float(input('Ingrese altura: '))

title_result = '\n  Resultados  \n'
print(title_result.center(100, '_'))

prom_time = prom_time/number_person
prom_height = prom_height/number_person
prom_age = prom_age/number_person
por_female = female*100 / number_person

print('--> El numero de personas que llegaron a la meta son: ' + str(number_person))
print('--> El tiempo promedio de la maraton es: {:.1f}'.format(prom_time))
print('--> El promedio de la altura es: {:.1f}'.format(prom_height))
print('--> El promedio de la edad de los atletas es {:.1f}'.format(prom_age))
print('--> El tiempo mayor en llegar a la meta es {}'.format(max_time))
print('--> La edad menor es {} '.format(min_age))
print('--> El porcentaje de mujeres que participaron en la maraton es {}%'.format(por_female))
