#!/usr/bin/env python
# coding=utf-8

"""
    @author: Adrian Verdugo
    @contact: adrianverdugo273@gmail.com
    @github: adrian273
    @info: *Leer un numero y calcular el factorial
"""

number = int(raw_input('Ingrese numero \n'))
fact = 1
while number > 1:
    fact = fact * number
    number = number - 1
print "El factorial es: " + str(fact)
