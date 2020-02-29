##
##  Programación con Pandas
##  ===========================================================================
##
##  Construya una tabla que contenga _c0 y una lista
##  separada por ',' de los valores de la columna _c4
##  del archivo `tbl1.tsv`.
##
##  Rta/
##      _c0    lista
##  0     0    b,f,g
##  1     1    a,c,f
##  ...
##  38   38      d,e
##  39   39    a,d,f
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
import pandas as pd

data = pd.read_csv('tbl1.tsv', sep = "\t")
data2 = pd.DataFrame({'lista' : data.groupby(['_c0']).apply(lambda x: ','.join(sorted(x['_c4'])))}).reset_index()
data2.columns = ['_c0', 'lista']
print(data2)
