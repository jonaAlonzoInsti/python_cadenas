
def colors(_op_color, _texto):
    opcion_color=_op_color
    texto=_texto
    if opcion_color=='amarillo':
        #amarillo
        print("\033[1;33m"+texto+'\033[0;m') 
    elif opcion_color=='cyan':
        #cyan
        print("\033[;36m"+texto+'\033[0;m')
    elif opcion_color=='morado':
        #morado 
        print("\033[4;35;47m"+texto+'\033[0;m') 
    elif opcion_color=='verde1':
        #verde
        print("\033[4;35m"+texto+'\033[0;m')
    elif opcion_color=='rojo':
        #rojo
        print("\033[1;31m"+texto+'\033[0;m')
    elif opcion_color=='azul':
        #azul
        print("\033[1;34m"+texto+'\033[0;m')
    elif opcion_color=='verde':
        #verde
        print("\033[1;32m"+texto+'\033[0;m')
    elif opcion_color=='preguntas':
        #4=subr 35=morado 47=blanco
        #31=rojo 32=verde 33=amarillo 34=azul 35=morado 36=cyan 37=blanco
        #fondos 40=blanco 41=rojo 42=verde 43=amarillo 44=azul 45=morado 46=cyan 47=gris
        print("\033[4;31;47m"+texto+'\033[0;m')     
    
    return opcion_color