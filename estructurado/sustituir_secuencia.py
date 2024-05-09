from color_consola import colors

def sustituir_secuencia(_registros_array):
        registros_array=_registros_array
        punto_division=19
        cadena_retirar_inicio=19
        cadena_retirar_final=22            
        cadenas_nuevas=[]
        for r in range(len(registros_array)):
            aux_num=str(r+1)
            if(r<10):
                cadena_sustituir="00"+aux_num
            elif(r>10):
                cadena_sustituir="0"+aux_num
            aux_cadena=registros_array[r]
            parte1 = aux_cadena[:punto_division]
            parte_sustituir = aux_cadena[cadena_retirar_inicio:cadena_retirar_final]
            parte3 = aux_cadena[cadena_retirar_final:]
            cadena_nueva = parte1 + cadena_sustituir + parte3
            cadenas_nuevas.append(cadena_nueva)
            print("=====================================")
            colors('verde', 'Cadena original: '+aux_cadena)
            print("parte_1:", parte1)
            print("parte_2:", parte_sustituir)
            print("parte_3:", parte3)
            colors('amarillo', 'Cadena nueva: '+cadena_nueva)
            print("=====================================")
        return cadenas_nuevas


def devolver_prefijo_final(_registros_array):
        registros_array=_registros_array
        punto_division=19
        cadena_retirar_inicio=19
        cadena_retirar_final=22            
        cadenas_prefijo_final=[]
        for r in range(len(registros_array)):
          
            aux_cadena=registros_array[r]
            parte3 = aux_cadena[cadena_retirar_final:]
            cadenas_prefijo_final.append(parte3)

        return cadenas_prefijo_final



def devolver_serie_antigua_num_pregunta(_registros_array):
        registros_array=_registros_array
        punto_division=19
        cadena_retirar_inicio=19
        cadena_retirar_final=22            
        cadena_num_pregunta_antigua=[]
        for r in range(len(registros_array)):
            aux_num=str(r+1)
            
            aux_cadena=registros_array[r]
            parte_sustituir = aux_cadena[cadena_retirar_inicio:cadena_retirar_final]
            
            cadena_num_pregunta_antigua.append(parte_sustituir)

        return cadena_num_pregunta_antigua