'''
    @description:
        La escuela informatica desea tabular la siguiente
        informacion de cada alumno, con un total de 223:
            * Nombre, Edad, Peso, Estatura, Genero
        Con ella realizar los siguientes procesos:
            * Determinar La Alumna mas joven de la escuela {ok}
            * Determinar cuantos Alumnos tienen entre 19 y 22 años {ok}
            * Determinar cuantas Alumnas pesan entre 45 y 55 Kilos {ok}
            * Quien es el alumno mas alto de la escuela {ok}
            * porcentaje de mujeres de la escuela
            * promedio de estatura de la escuela
    @author: Adrian Verdugo
'''


title = " Escuela Informatica "
print(title.center(50, '*'))
line = "Ingreso de datos"

#  Variables
COUNT_STUDENTS = 3  # cantidad de estudiantes
MIN = 9999
MAX = 0
count_students_m = 0
count_weight_f = 0
count_f = 0

for i in range(COUNT_STUDENTS):
    print(line.center(50, '_'))
    name = input('Ingresar nombre \n')
    age = int(input('Ingresar edad \n'))
    weight = float(input('Ingresar peso \n'))
    height = float(input('Ingresar altura \n'))
    gender = input('Ingresar genero \n')
    if gender == 'f':
        if MIN > age:
            # @alumna mas joven de la escuela
            MIN = age
            name_min = name
        if weight > 45 and weight < 55:
            # @contador de alumnas que pesan entre 45 y 55 kg
            count_weight_f += 1
        # @alumnas totales
        count_f += 1
    elif gender == 'm':
        if MAX < height:
            MAX = height
            # @alumno mas alto
            name_max_height = name
        if age > 19 and age < 22:
            # @contador de alumnos que tienen entre 19 y 22 años
            count_students_m += 1

por_women = count_f * 100 / 3
print('La edad menor es '+ str(MIN) + ' años de la alumna ' + name_min)
print('La cantidad de alumnos que tienen entre 19 y 22 años son ' + str(count_students_m))
print('La cantidad de alumnas que pesan entre 45 y 55 kg son ' + str(count_weight_f))
print('El alumno mas alto de la escuela es ' + name_max_height + ' con ' + str(MAX) + 'cm')
print('El porcentaje de mujeres es ' + str(por_women) + '%')