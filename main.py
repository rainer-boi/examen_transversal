juegos={
    'G001': ["Eclipse Runner", "PC", "accion", "T", True, "NovaStudio"],
    'G002': ["Puzzle Atlas", "Switch", "puzzle", "E", False, "BrightWorks"],
    'G003': ["Sky Legends", "PS5", "aventura", "T", True, "OrionGames"],
    'G004': ["Racing Pulse", "PC", "carreras", "E", True, "VelocityLab"],
    'G005': ["Mystic Farm", "Switch", "simulacion", "E", False, "GreenSeed"],
    'G006': ["Shadow Tactics", "Xbox", "estrategia", "M", False, "IronGate"],
}
inventario={
    'G001': [9990, 7],
    'G002': [19990, 0],
    'G003': [42990, 3],
    'G004': [14990, 5],
    'G005': [17990, 9],
    'G006': [39990, 2],
}
######################################################
#1
def stock_plataforma(plataforma):
    total=0
    for clave,valor in juegos.items():
        if valor[1].lower()==plataforma.lower():
            total+=inventario[clave][1]
    if total==0:
        print("No existen juegos con esa caregoría")
    else:
        print(f"El total de stock disponibles es: {total}")
#2
def busqueda_precio(p_min, p_max):
    lista=[]
    for clave,valor in juegos.items():
        if valor[0]>=p_min and valor[0]<=p_max:
            print("INCOMPLETO (pipipi)")
#3
def actualizar_precio(codigo, nuevo_precio):
    if codigo in inventario:
        inventario[codigo][0]=nuevo_precio
        return True
    return False
######################################################
def ValCod(cod):
    if len(cod.strip())>0:
        return True
    return False

def ValTitu(titu):
    if len(titu.strip())>0:
        return True
    return False

def ValPlat(pla):
    if len(pla.strip())>0:
        return True
    return False

def ValGen(gen):
    if len(gen.strip())>0:
        return True
    return False

def ValCla(cla):
    if cla in ["E","T","M"]:
        return True
    return False

def ValEd(ed):
    if len(ed.strip())>0:
        return True
    return False

def ValPre(pre):
    if pre>0:
        return True
    return False

def ValSt(st):
    if st>=0:
        return True
    return False
######################################################
#4
def agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock):
    if codigo.upper() in juegos:
        print("INCOMPLETO (pipipi)")
#5
def eliminar_juego(codigo):
    if codigo in juegos:
        del inventario[codigo]
        del juegos[codigo]
        return True
    return False
######################################################
def menu():
    print('''
        ========== MENÚ PRINCIPAL ==========
        1. Stock por plataforma
        2. Búsqueda de juegos por rango de precio
        3. Actualizar precio de juego
        4. Agregar juego
        5. Eliminar juego
        6. Salir
        =====================================
        ''')

def seleccione():
    try:
        opcion=int(input("Seleccione: "))
        return opcion
    except:
        return 0
######################################################
while True:
    menu()
    op=seleccione()
    match op:
        case 1:
            plataforma=input("Ingrese plataforma a consultar: ")
            stock_plataforma(plataforma)
        case 2:
            minimo=int(input("Ingrese precio mínimo: "))
            maximo=int(input("Ingrese precio máximo: "))
            if minimo<=maximo and minimo>=0:
                print("INCOMPLETO (pipipi)")
        case 3:
            while True:
                codigo=input("Ingrese código del juego: ")
                n_precio=int(input("Ingrese nuevo precio: "))
                resp=actualizar_precio(codigo)
                if resp==False:
                    print("El código no existe")
                else:
                    print("Precio actualizado")
        case 4:
            cod=input("Ingrese código del juego: ")
            print("INCOMPLETO (pipipi)")
        case 5:
            eliminar=input("Ingrese código del juego: ")
            resp=eliminar_juego(eliminar)
            if resp==False:
                print("Juego no eliminado")
            else:
                print("Juego eliminado")
        case 6:
            print("Programa finalizado")
            break
        case _:
            print("Debe seleccionar una opción válida")