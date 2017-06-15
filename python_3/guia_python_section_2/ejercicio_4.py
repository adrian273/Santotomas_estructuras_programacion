"""ejercicio_4.py
    @description: Escribir una funcion que tome un caracter
    y devuelva True si es una vocal, de lo contrario devuelve False.
"""


def vocal(leter):
    vocals = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(vocals)):
        """
            @upper = Revisa las letras mayusculas
        """
        if vocals[i].upper() == leter or vocals[i] == leter:
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