
#Práctica del curso "Using Python to Access Web Data" de la Universidad de Michigan-Coursera.

#Programa que realiza una búsqueda de direcciones de correo en un archivo de texto,
#que examina las líneas usando expresiones regulares para detectar aquellas 
#que tengan una arroba entre caracteres y las imprime



import re
fname = ('mbox_short.txt')
fh = open (fname)


for linea in fh:
    linea = linea.rstrip()
    x = re.findall(r'[a-zA-Z0-9]\S+@\S+[a-zA-Z]', linea)
    if len(x) > 0:
        print (x)

