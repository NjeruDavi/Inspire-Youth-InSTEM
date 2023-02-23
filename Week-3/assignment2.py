#program to solve quadratic equation
import math

a =int( input("Enter the value of (a)the firt coefficient :"))
b =int(input("Enter the value of (b)the second coefficient :"))
c =int (input("Enter the constant (c) :"))
d = (d**2) - (4*a*c)
sol1 = (-b + math.sqrt(d)) / (2*a)
sol2 = (-b - math.sqrt(d)) / (2*a)
