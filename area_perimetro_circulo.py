# programa para calcular el area y el perimetro de un circulo 

# Libreria
import math
#---------
# input
#---------

print ("                            ")
print ("area y perimetro del circulo")
print ("                            ")

# input
r = input ("Ingrese el valor del radio del circulo: ")
r = int(r)

# processing
a = math.pi*r**2
p = 2*math.pi*r

# output
print("                                      ")
print("              Resultados              ")
print("                                      ")
print("El area del circulo es : " + str(a))
print("El perimetro del circulo es: " + str(p))
print("                                      ")