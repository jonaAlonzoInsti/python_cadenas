def generar_serie(inicio, fin):
    array_series=[]
    for i in range(fin):
        aux1=str(i+1)
        if(i<9):
            aux="00"+aux1
        else:
            aux="0"+aux1
        array_series.append(aux)
    return array_series