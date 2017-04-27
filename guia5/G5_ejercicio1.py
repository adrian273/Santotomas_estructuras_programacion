#!/usr/bin/env python
# coding=utf-8
from colored import bg
"""
    @author: Adrian Verdugo
    @contact: adrianverdugo273@gmail.com
    @github: adrian273
"""

def _loops(number, length):
    print  bg('blue'), "Los impares siguientes son: "
    while True:
        number = number + length
        if number < 100:
            print bg('red'),number
        else:
            break

number = int(raw_input("Ingrese un numero \n"))
result = number % 2
if result == 0:
    _loops(number, 1)
else:
    _loops(number, 2)
