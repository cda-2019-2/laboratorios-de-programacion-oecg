##
##  Programación en Python
##  ===========================================================================
##
##  La columna 5 del archvio `data.csv` codifica un diccionario donde cada
##  cadena de tres letras corresponde a una clave y el valor despues del
##  caracter `:` corresponde al valor asociado a la clave. Por cada clave,
##  obtenga el valor asociado mas pequeño y el valor asociado mas grande 
##  computados sobre todo el archivo. 
##
##  Rta/
##  aaa,0,6
##  bbb,4,7
##  ccc,0,1
##  ddd,5,5
##  eee,0,0
##  fff,4,9
##  ggg,3,3
##  hhh,6,8
##  iii,2,7
##  jjj,2,5
##
##  >>> Escriba su codigo a partir de este punto <<<
##
from itertools import groupby
from operator import itemgetter


with open('data.csv', 'r') as f:
    file = f.readlines()
    
    file = [line.replace('\n', '') for line in file]
    file = [line.split('\t') for line in file]
    
    data_col5 = [y.split(':') for row in file for y in row[4].split(',')]

    for key, group in groupby(sorted(data_col5, key=itemgetter(0)), itemgetter(0)):
        g = list(group)
        max_g = max(int(x[1]) for x in g)
        min_g = min(int(x[1]) for x in g)
        print(f'{key},{min_g},{max_g}')


