##### LOS BALDES #####
# Esta función permite saber cuántas veces aparece un número aleatorio de una lista en un intervalo

import random

#lista de n valores aleatorios
def lista_aleatorios(n):
    return [round(random.random(),2) for i in range(0,n)]

#valores en intervalo: determina para cada elemento e de la lista dada, si este está en un intervalo dado
def valor_en_intervalo (equis,min,max):
    cuenta=[True if min<=e and e<max else False for e in equis].count(True)
    print("Hay " + str(cuenta) + " elementos de la lista en el intervalo (" + str(min) + "," + str(max) + ")")

#generar intervalos y decir cuántos números de la lista están en cada intervalo
def final_intervalo(cantaleat,cantbald):
    [valor_en_intervalo(lista_aleatorios(cantaleat),j/cantbald,j/cantbald+1/cantbald) for j in range(cantbald)]

final_intervalo(1000,8)