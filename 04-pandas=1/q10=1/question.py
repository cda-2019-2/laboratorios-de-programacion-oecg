##
##  Programación con Pandas
##  ===========================================================================
##
##  Construya una tabla que contenga _c0 y una lista
##  separada por ',' de los valores de la columna _c5a
##  y _c5b (unidos por ':') de la tabla tbl2.tsv
## 
##  Rta/
##      _c0                                lista
##  0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
##  1     1              aaa:3,ccc:2,ddd:0,hhh:9
##  ...
##  38   38                    eee:0,fff:9,iii:2
##  39   39                    ggg:3,hhh:8,jjj:5
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import pandas as pd

data = pd.read_csv('tbl2.tsv', sep = "\t")
data['_c5b'] = data['_c5b'].astype(str)
data2 = pd.DataFrame({'lista' : data.groupby(['_c0']).apply(lambda x: ','.join(sorted(x['_c5a'] + ':' + x['_c5b'])))}).reset_index()
data2.columns = ['_c0', 'lista']
print(data2)
