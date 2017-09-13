# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 14:54:22 2017

@author: fani2
"""

"1).Inicio."
"2).Pedir las coordenadas"
"3).Recibir las coordenadas"
"4).hallar los lados"
"5).hallar los angulos"
"6).imprimir el resultado"



print"Ingresar las coordenadas de los vertices"

x1= float(input ("x1= ")) 
y1= float(input ("y1= ")) 
x2= float(input ("x2= ")) 
y2= float(input ("y2= ")) 
x3= float(input ("x3= ")) 
y3= float(input ("y3= ")) 

import math

l1 = abs(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))

print"lado 1: coordenadas de (x1,y1) a (x2,y2)= ",l1,"\n"

l2 = abs(math.sqrt((x3 - x2)**2 + (y3 - y2)**2))

print"lado 2: coordenadas de (x2,y2) a (x3,y3)= ",l2,"\n"

l3 = abs(math.sqrt((x1 - x3)**2 + (y1 - y3)**2))

print"lado 3: coordenadas de (x3,y3) a (x1,y1)= ",l3,"\n"

print"__________________________________________________________"

q = math.acos(((l3**2)+(l1**2)-(l2**2))/(2*l1*l3))
w = math.acos(((l2**2)+(l1**2)-(l3**2))/(2*l2*l1))
e = math.acos(((l3**2)+(l2**2)-(l1**2))/(2*l3*l2))

a = (q*180)/math.pi
b = (w*180)/math.pi
c = (e*180)/math.pi

print"ángulo a = ", a
print"ángulo b = ", b
print"ángulo c = ", c
            
