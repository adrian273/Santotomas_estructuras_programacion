#!/usr/bin/env python
# coding=utf-8
from colored import bg
"""
    @author: Adrian Verdugo
    @contact: adrianverdugo273@gmail.com
    @github: adrian273
"""

number = int(raw_input("Ingrese un numero \n"))
result = number % 2
if result == 0:
    number = number - 1

while True:
    number = number + 2
    if number < 100:
        print "Los numeros impares son ", number
    else:
        break
