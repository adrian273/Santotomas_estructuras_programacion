"""ejercicio_6.py
    @description: Definir una función inversa() que calcule la 
        inversión de una cadena. Por ejemplo la cadena 
        "estoy probando" debería devolver la cadena "odnaborp yotse"
"""

def inversa(word):
    return word[::-1]

word = input('Ingresa palabra: ')
print('La palabra invertida es: {}'.format(inversa(word)))