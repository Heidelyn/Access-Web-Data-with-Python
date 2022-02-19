
#Programa que calcula la cantidad de números en un archivo, su sumatoria y el promedio
#Usando expresiones regulares para extraerlos

import re

fname= ('regex_sum_1286704.txt')

try:
    handle = open (fname)
except:
    print ('El archivo es inválido')
    exit()

sumalst= list()

for linea in handle:
    linea = linea.rstrip()
    x = re.findall(('[0-9]+'),linea)
    if len(x) > 0:
        for num in x:
            inum = int(num)
            sumalst.append(inum)

print ("La cantidad de números en el archivo es:", len(sumalst))
print ("La sumatoria es:" , sum(sumalst))
print ("El promedio es:" , (sum(sumalst)/len(sumalst)))