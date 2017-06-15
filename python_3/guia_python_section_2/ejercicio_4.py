"""ejercicio_4.py
    @description: Escribir una funcion que tome un caracter
    y devuelva True si es una vocal, de lo contrario devuelve False.
"""


def vocal(leter):
    vocals = ['a', 'e', 'i', 'o', 'u']
    vocals_upper = ['A', 'E', 'I', 'O', 'U']
    if leter in vocals or leter in vocals_upper:
        return True
    else:
        return False

while True:
    leter = input('Ingrese un caracter: ')
    if len(leter) > 1:
        print('![ERROR]Ingrese solamente un caracter >>')
    else:
        print(vocal(leter))
        break