from pandas import ExcelWriter
import pandas as pd
from color_consola import colors
from openpyxl import Workbook
from cadenas_finales import *

def guardado(_array_datos_nuevos):
    cadenas_nuevas=_array_datos_nuevos

    texto_guardado=colors('preguntas','Quiere guardar los datos en un archivo Excel? (S/N):')
    guardar=(input(texto_guardado))

    if(guardar=="S" or guardar=="s"):
        df_datos_array_ok=pd.DataFrame(cadenas_nuevas,columns=['Cadena'])
        writer = ExcelWriter('prueba1.xlsx')
        df_datos_array_ok.to_excel(writer,'Hoja1')
        writer._save()
    elif(guardar=="N" or guardar=="n"):
        colors('rojo', 'No se guardaron los datos')

def guardado_all():
    cadenas_nuevas=for_to=devolver_datos_antiguos()
    cadenas_antiguas=for_to=devolver_datos_finales()
    cadenas_query=for_to=devolver_cadenas_query() 
    # Crear un nuevo libro de Excel
    libro_excel = Workbook()
    # Seleccionar la hoja activa (por defecto es la primera hoja)
    hoja = libro_excel.active
    # Combinar los datos de los arrays usando zip y agregarlos a la hoja
    for nueva, antiguas, query in zip(cadenas_nuevas, cadenas_antiguas, cadenas_query):
        hoja.append([nueva, antiguas, query])
    # Guardar el libro de Excel
    libro_excel.save("final.xlsx")

def guardado_txt_tres_array():
    cadenas_nuevas=for_to=devolver_datos_antiguos()
    cadenas_antiguas=for_to=devolver_datos_finales()
    cadenas_query=for_to=devolver_cadenas_query() 
    # Crear un nuevo archivo de texto
    archivo_txt = open("total_datos.txt", "w")
    # Combinar los datos de los arrays usando zip y agregarlos al archivo de texto
    for nueva, antiguas, query in zip(cadenas_nuevas, cadenas_antiguas, cadenas_query):
        archivo_txt.write(f"{nueva}\t{antiguas}\t{query}\n")
    # Cerrar el archivo de texto
    archivo_txt.close()

def guardado_txt_query():
    cadenas_query=for_to=devolver_cadenas_query() 
    # Crear un nuevo archivo de texto
    archivo_txt = open("total_datos.sql", "w")
    # Combinar los datos de los arrays usando zip y agregarlos al archivo de texto
    for query in cadenas_query:
        archivo_txt.write(query+"\n")
    # Cerrar el archivo de texto
    archivo_txt.close()