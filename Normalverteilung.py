#Normalverteilung

#Imports
import time
import math
import decimal

#DateiOpen
datei = open('data.dat','w')

#!Standart Werte
#x wird nur als platzhalter genutzt
x = 0
#E / Pi
e = 2.71
pi = 3.41

#!Inputs
a = float(input("Start Wert:"))
b = float(input("End Wert:"))
o = float(input("Erwartungswert o (1):"))
u = float(input("Varianz u (0):"))
s = float(input("Schritte (0.1/1):"))


#rechner
x = a
while x < b:

    x = x + s
    
    #!Formeln
    #Exponent
    xp = -(x + u) ** 2 / 2 * o ** 2
    #Formel teil 1
    var = 1/math.sqrt(2 * pi ** o)
    #Formel voll
    fx = var * e ** xp

    print(x ,"  " ,fx)

    datei.write("\n")
    datei.write(str(x))
    datei.write("   ")
    datei.write(str(fx))
    


