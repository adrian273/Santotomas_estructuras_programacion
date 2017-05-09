'''
    ::::::::::::::::::::::::::::::::::::::::::::::
    ::    @github: adrian273                    ::
    ::    @email: adrianverdugo273@gmail.com    ::
    ::::::::::::::::::::::::::::::::::::::::::::::
    3@  Lea el Promedio de Notas de un  Alumno (70%) y su calificación de examen (30%), determine si el alumno aprobó o reprobó la asignatura.
'''
prom = float(input('Ingrese promedio \n')) #promedio
ex = float(input('Ingrese examen \n')) #examen
result = (prom * 0.7) + (ex * 0.3)
if result >= 4.0:
    print('El alumno aprobo')
else:
    print('El alumno reprobo')
