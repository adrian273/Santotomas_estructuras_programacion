"""ejercicio_11.py
    @description: Que lea 5 números por teclado, los copie a otro 
    array multiplicados por 2 y los muestre todos
    ordenados usando un tercer array.
"""

number = []
number_copy = []
number_order = []


def generate_array():
    for i in range(5):
        n = int(input('Ingrese numero: '))
        number.append(n)
    return number

def generate_array_copy():
    for j in number:
        multiplication = j * 2
        number_copy.append(multiplication)
    return number_copy


def order_number():
    for k in number_copy:
        number_order.append(k)
    """ soted se utiliza para ordenar de menor a mayor """
    return sorted(number_order)


print('Numeros ingresados: {}'.format(generate_array()))
print('Numeros multiplicados: {}'.format(generate_array_copy()))
print('Numeros ordenados: {}'.format(order_number()))