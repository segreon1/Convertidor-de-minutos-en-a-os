# -*- coding: utf-8 -*-

print "Ingrese un número en minutos: "
minh = 60
hdia = 24
diaa = 365.25
dias = 0
horas = 0
minutos = 0 
minu = 0

y = minh*hdia*diaa

minutos = input()

res = minutos/y

dias = ( res - int(res) ) * diaa

res = int(res)

horas = ( dias - int(dias)) * hdia

dias = int(dias)

minu = ( horas - int(horas)) * minh

horas = int(horas)

minu = int(minu)
 
    
print "Numero de años = ",res
print "Numero de dias = ",dias
print "Numero de horas = ",horas
print "Numero de minutos = ",minu




