from sustituir_secuencia import devolver_serie_antigua_num_pregunta,devolver_prefijo_final
from leer_archivo import leer_fichero
from genrar_serie import generar_serie
from color_consola import colors

#cargar datos antiguos
_array_registros=leer_fichero()
   #Cadena original: DIGGINGQ-06-001-el-130+6SC-5PS-B2
cadena_prefijo="DIGGINGQ-06-"
    #001-014
cadena_cuestionario=generar_serie(1,14)
    #el,en,es,hu,lv,nl
cadena_idioma=["-el-","-en-","-es-","-hu-","-lv-","-nl-"]
    #001-088
cadena_prengunta=generar_serie(1,88)
#serie antigua
registro=devolver_serie_antigua_num_pregunta(_array_registros)
#cadenas completas antiguas
cadenas_antiguas_array=[]
#prefijo final
cadenas_prefijo_final=devolver_prefijo_final(_array_registros)
#cadenas completas finales
cadenas_finales=[]
#rangos para los bucles
rango_preguntas=len(cadenas_prefijo_final)
rango_cuestionarios=len(cadena_cuestionario)
rango_idiomas=len(cadena_idioma)
#cadena query final
cadenas_query_array=[]

def cadenas():
    for c in range(rango_cuestionarios):
        for i in range(rango_idiomas):
            for p in range(rango_preguntas):
                cadena_final=cadena_prefijo+cadena_cuestionario[c]+cadena_idioma[i]+cadena_prengunta[p]+cadenas_prefijo_final[p]
                cadenas_finales.append(cadena_final)
                cadenas_antiguas=cadena_prefijo+cadena_cuestionario[c]+cadena_idioma[i]+registro[p]+cadenas_prefijo_final[p]
                cadenas_antiguas_array.append(cadenas_antiguas)
                cadenas_query="update mdl_question set name='"+cadena_final+"' where name='"+cadenas_antiguas+"' and category in(select id from mdl_question_categories where contextid=42 and name like 'DIGGINGQ%');"
                cadenas_query_array.append(cadenas_query)
    # print("update mdl_question set name='"+cadenas_finales[66]+"' where name='"+cadenas_antiguas_array[66]+"' and category in(select id from mdl_question_categories where contextid=42 and name like 'DIGGINGQ%');")
# print(len(cadenas_finales))


def mostrar_datos():
    rango=len(cadenas_finales)
    aux2=0
    aux=len(cadena_prengunta)    
    cuestionario=616
    for k in range(rango):
        if(k==aux):
            colors('verde', '_____________________________________________________________________________'+str(aux2))
            colors('rojo', "FINAL")
            colors('verde', '_____________________________________________________________________________'+str(aux2))
            aux=aux+len(cadena_prengunta)
        if(k==cuestionario-1):
            colors('rojo', '_____________________________________________________________________________')
            colors('rojo', '_____________________________________________________________________________')
            cuestionario=cuestionario+616
        aux2=aux2+1
        print("=====================================")
        colors('verde', 'Cadena original: '+cadenas_antiguas_array[k])
        colors('amarillo', 'Cadena nueva:    '+cadenas_finales[k])
        colors('azul', 'Cadena query:    '+cadenas_query_array[k])
        print(k)
        print("=====================================")

def devolver_datos_antiguos():
    return cadenas_antiguas_array

def devolver_datos_finales():
    return cadenas_finales

def devolver_cadenas_query():
    return cadenas_query_array



        