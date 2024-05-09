import pandas as pd
from color_consola import colors

def leer_fichero():
    archivo_xlsx = "./q2.xlsx"
    registros_archivo=pd.ExcelFile(archivo_xlsx)
    registros_hoja1=registros_archivo.parse("Hoja1")
    registros_array=[]
    recorrido=len(registros_hoja1)
    for i in range(recorrido):
        registros_array.append(registros_hoja1.iloc[i, 0])
    colors('verde', 'Datos leídos correctamente')
    return registros_array
