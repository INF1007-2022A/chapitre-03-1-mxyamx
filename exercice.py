#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
a = 25
liste = [5,5,14]
celsius = 100
farenheit = 451
def square_root(a: float) -> float:
    nombre = math.sqrt(a)
    return (nombre)

def square(a: float) -> float:
    nombre = a**2
    return (nombre)
#
#
def average(a: float, b: float, c: float) -> float:
    moyenne = sum(liste) / len(liste)
    return moyenne


# #Convertir en radians un angle fourni au départ en degrés, minutes, secondes
# def to_degrees(angle_rad):

#Convertir en radians un angle fourni au départ en degré,minutes,secondes
#
def to_celsius(temperature: float) -> float:
    celsius = (farenheit-32)*5/9
    return celsius
#
#
def to_farenheit(temperature: float) -> float:
    farenheit = (celsius * 9/5)+32
    return farenheit
#
#
def main() -> None:
    print(f"La racine carré de {a} est : {square_root(a)}")

    print(f"Le carré de {a} est : {square(a)}")

    print(f"Moyenne des nombres {liste}: {average([0],[1],[2])}")

#     # print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
#  degrees, minutes, seconds = to_degrees(1.0)
#     print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {secondes} secondes")
#
    print(f"Conversion de {celsius} Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de {farenheit} Farenheit en Celsius: {to_celsius(451.0)}")
#
#
if __name__ == '__main__':
    main()
