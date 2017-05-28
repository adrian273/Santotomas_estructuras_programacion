'''
    @ Leer el tiempo que se demoraron las personas en correr una maratón (Los
    tiempos son ingresados sin orden), dejara de leer cuando se ingrese cero.
    Calcular:
        a. Número de personas que llegaron a la meta.
        b. Tiempo promedio de la maratón.
        c. El tiempo menor.
        d. El tiempo mayor.
'''
time = float(input('Ingrese tiempo: '))
numer_person = 0
prom_time = 0
time_min = 100000
time_max = 0

while time > 0:
    numer_person += 1
    prom_time += time
    if time_min > time:
        time_min = time
    if time_max < time:
        time_max = time
    time = float(input('Ingrese tiempo: '))

prom_time = prom_time / numer_person
print('El numero de personas que llegaron fueron: ' + str(numer_person))
print('El tiempo promedio de la maraton es: ' + str(prom_time))
print('El tiempo menor es: ' + str(time_min))
print('El tiempo mayor de la maraton es: ' + str(time_max))
