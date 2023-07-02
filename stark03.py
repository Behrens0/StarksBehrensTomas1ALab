import re
from data_stark import lista_personajes
import os
def extraer_iniciales(nombre_heroe):
    nombre_heroe = re.sub(r'\bthe\b', '', nombre_heroe, flags=re.IGNORECASE)
    nombre_heroe = re.sub(r'-', ' ', nombre_heroe)
    iniciales = re.findall(r'\b\w', nombre_heroe)
    iniciales = ".".join(iniciales) + "."   
    return iniciales


def definir_iniciales_nombre(heroe:dict):
    if isinstance(heroe, dict) and "nombre" in heroe.keys():
        heroe["iniciales"] = extraer_iniciales(heroe["nombre"])
        return True
    else:
        return False
def agregar_iniciales_nombre(lista: list):
    if isinstance(lista, list) and len(lista) > 0:
       for i in lista:
                definir_iniciales_nombre(i)
    return lista

def stark_imprimir_nombres_con_iniciales(lista: list):
    agregar_iniciales_nombre(lista)
    for i in lista:
        print(f"* {i['nombre']}({i['iniciales']})")

def generar_codigo_heroe(id_heroe: int, genero_heroe: str):
    if not isinstance(id_heroe, int) or id_heroe <= 0:
        return 'N/A'
    id_str = str(id_heroe)
    if genero_heroe not in ['M', 'F', 'NB']:
        return 'N/A'
    
    elif genero_heroe == "NB":
        id_str = id_str.zfill(7)
    else:
        id_str = id_str.zfill(8)
    codigo = f"{genero_heroe}-{id_str}"
    if len(codigo) > 10:
        return 'N/A'
    
    return codigo

def agregar_codigo_heroe(heroe:dict, id_heroe:int):
    if isinstance(heroe, dict) and len(generar_codigo_heroe(id_heroe, heroe["genero"])) == 10:
            heroe["codigo_heroe"] = generar_codigo_heroe(id_heroe, heroe["genero"])
            return heroe["codigo_heroe"]
    return False

def stark_generar_codigos_heroes(lista: list):
    id = 1
    for i in lista:
        id_heroe = agregar_codigo_heroe(i, id)
        print(f"* El codigo del {id:02d} es:  {id_heroe}")
        id += 1
    return
def sanitizar_entero(numero_str: str):
    numero_str = numero_str.strip()
    if not numero_str.isdigit():
        return -1
    elif int(numero_str) < 0:
        return -2
    elif numero_str.isdigit() and int(numero_str) >= 0:
        return int(numero_str)
    return -3
        
def sanitizar_flotante(numero_str: str):
    numero_str = numero_str.strip()
    if not numero_str.isdigit():
        return -1
    elif float(numero_str) < 0:
        return -2
    elif numero_str.isdigit() and float(numero_str) >= 0:
        return float(numero_str)
    return -3

def sanitizar_string(valor_str, valor_por_defecto = "-"):
    
    if valor_str.isalnum():
        return "N/A"
    valor_str = valor_str.replace("/", " ")
    
    if valor_str.strip().isalpha():
        return valor_str.lower()
    if len(valor_str) == 0:
        return valor_por_defecto.lower()

def sanitizar_dato(heroe: dict, key: str, tipo_dato: str):
    if key not in heroe.keys():
        print("La clave especificada no existe en el héroe.")
        return False
    if tipo_dato.lower() == "flotante":
        sanitizar_flotante(heroe[key]) 
        return True
    elif tipo_dato.lower() == "entero":
         sanitizar_entero(heroe[key])
         return True
    elif tipo_dato.lower() == "string":
        sanitizar_string(heroe[key])
        return True
    else: 
        print("tipo de dato no reconocido")
        return False
    
def stark_normalizar_datos(lista: list):
    if len(lista) > 0:
        for i in lista:
            sanitizar_dato(i, "altura", "flotante")
            sanitizar_dato(i, "peso", "flotante")
            sanitizar_dato(i, "color_ojos", "string")
            sanitizar_dato(i, "color_pelo", "string")
            sanitizar_dato(i, "fuerza", "entero")
            sanitizar_dato(i, "inteligencia", "string")
        print("datos sanitizados")
    else:
        print("error sin datos")

def generar_indice_nombres(lista: list):
    if len(lista ) == 0:
        print("error")
    lista_nueva = []
    for i in lista:
        if not isinstance(i, dict) or "nombre" not in i.keys():
            print("error")
        else:
            lista_nueva.extend(i["nombre"].split())
    return lista_nueva

# a = generar_indice_nombres(lista_personajes)
# print(a)
def stark_imprimir_indice_nombre(lista: list):
    x = generar_indice_nombres(lista)
    print(f"{'-'.join(x)}")
    
def convertir_cm_mtrs(valor_cm: float):
    if isinstance(valor_cm, float) and valor_cm > 0:
        return valor_cm / 100
    return -1

def generar_separador(patron: str, largo: int, imprimir = True):
    if not (1 <= largo <= 235) or not (1 <= len(patron) <= 2):
        return 'N/A'

    separador = re.sub(f".{{1,{len(patron)}}}", patron, patron * largo)

    if imprimir:
        print(separador)

    return separador
generar_separador("aaa", 5, True)

def generar_encabezado(titulo: str):
    encabezado = f"""
    *********************************************************************************************
    {titulo.upper()}
    *********************************************************************************************
    """
    return encabezado

def imprimir_ficha_heroe(heroe:dict):
    ficha_heroe = f'''
    {generar_encabezado("principal")}
    
        NOMBRE DEL HEROE:               {heroe["nombre"]}  
        IDENTIDAD SECRETA:              {heroe["identidad"]}
        CONSULTORA:                     {heroe["empresa"]}
        CÓDIGO DE HÉROE:                {agregar_codigo_heroe(heroe, lista_personajes.index(heroe) + 1)}
   {generar_encabezado("fisico")}
      
        ALTURA:                         {heroe["altura"]}
        PESO:                           {heroe["peso"]}
        FUERZA:                         {heroe["fuerza"]}
    {generar_encabezado("señas particulares")}
        COLOR DE OJOS:                  {heroe["color_ojos"]}
        COLOR DE PELO:                  {heroe["color_pelo"]}
    '''
    print(ficha_heroe)
    

def stark_navegar_fichas(lista_heroes):
    indice_actual = 0
    largo_lista = len(lista_heroes)

    while True:
        imprimir_ficha_heroe(lista_heroes[indice_actual])

        accion_a_realizar = input("Ingrese una opción: [1] Ir a la izquierda, [2] Ir a la derecha, [S] Salir: ").lower()
        while accion_a_realizar != "1" and accion_a_realizar != "2" and accion_a_realizar != "s":
            accion_a_realizar = input("Ingrese una opción: [1] Ir a la izquierda, [2] Ir a la derecha, [S] Salir: ").lower()
        if accion_a_realizar == "1":
            indice_actual -= 1
            if indice_actual < 0:
                indice_actual = largo_lista - 1

        elif accion_a_realizar == "2":
            indice_actual += 1
            if indice_actual >= largo_lista:
                indice_actual = 0

        elif accion_a_realizar == "s":
            break

        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

            
def imprimir_menu():
    menu = """

        1 - Imprimir la lista de nombres junto con sus iniciales
        2 - Generar códigos de héroes   
        3 - Normalizar datos
        4 - Imprimir índice de nombres
        5 - Navegar fichas
        S - Salir

        ____________________________________________________________
            """
    print(menu)

def stark_menu_principal():
    imprimir_menu()
    opcion = input("ingrese opcion(1-5) o (s)").lower()
    while opcion not in ["1", "2", "3", "4", "5", "s"]:
        opcion = input("error.ingrese opcion(1-5) o (s)").lower()
    return opcion

def stark_marvel_app(lista_heroes):
    while True:
        os.system("cls")
        opcion = stark_menu_principal()
        if opcion == "1":
            stark_imprimir_nombres_con_iniciales(lista_heroes)
        elif opcion == "2":
            stark_generar_codigos_heroes(lista_heroes)
        elif opcion == "3":
            stark_normalizar_datos(lista_heroes)
        elif opcion == "4":
            stark_imprimir_indice_nombre(lista_heroes)
        elif opcion == "5":
            stark_navegar_fichas(lista_heroes)
        elif opcion == "s":
            break        
        os.system("pause")
        os.system("cls")
