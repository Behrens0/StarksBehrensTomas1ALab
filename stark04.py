from data_stark import lista_personajes
from stark02 import imprimir_dato
from stark02 import dividir

def imprimir_menu_deafio():
    pass

def leer_archivo(archivo):
    with open(archivo, "r") as file:
        lista = file.read()
        
def guardar_archivo(archivo: str, contenido: str):
    try:
        with open(archivo, "w+") as file:
            file.write(contenido)
        print(f'se creo el archivo{archivo}')    
        return True
    except ValueError:
        print("error al crear archivo")    
        return False

def capitalizar_palabras(cadena: str):
    lista_de_cadena = cadena.split()
    for i in range(len(lista_de_cadena)):
        lista_de_cadena[i] = lista_de_cadena[i].capitalize()
    cadena_capitalizada = " ".join(lista_de_cadena)
    return cadena_capitalizada

def obtener_nombre_capitalizado(heroe: dict):
    cadena = f'''
    nombre: {heroe["nombre"]}
    '''
    return capitalizar_palabras(cadena)

def obtener_nombre_dato(heroe: dict, key: str):
    cadena = f'''
    nombre: {heroe["nombre"]} | {key}: {heroe[key]}
    '''
    return capitalizar_palabras(cadena)

def es_genero(heroe: dict, genero: str):
    if genero == "M" or genero == "F" or genero == "NB":
        if heroe["genero"] == genero:
            return True
    return False

def stark_guardar_heroe_genero(lista_heroes: list, genero: str):
    lista_coincidencias = []
    for i in lista_heroes:
        if es_genero(i, genero):
            imprimir_dato(capitalizar_palabras(i["nombre"]))
            lista_coincidencias.append(i["nombre"])
        else:
            return False
    guardar_archivo(f"heroes_{genero}")
    return True

def calcular_min_genero(lista, key, genero):
    bandera_minimo = True
    for i in lista:
        if (bandera_minimo or i[key] < altura_minima) and (i["genero"] == genero):
            bandera_minimo = False
            altura_minima = i[key]
            heroe_mas_bajo = i
    return heroe_mas_bajo

def calcular_max_genero(lista, key, genero):
    bandera_minimo = True
    for i in lista:
        if (bandera_minimo or i[key] > altura_maxima) and (i["genero"] == genero):
            bandera_minimo = False
            altura_maxima = i[key]
            heroe_mas_alto = i
    return heroe_mas_alto

def calcular_max_min_genero(lista: list, key: str, genero, maximo = True,):
    if maximo:
        return calcular_max_genero(lista, key, genero)
    else:
        return calcular_min_genero(lista, key, genero)

def calcular_imprimir_heroes_genero(lista: list, maximo: bool, key: str, genero: str):
    x = calcular_max_min_genero(lista, key,genero,  maximo)
    imprimir_dato(obtener_nombre_dato(x, key))
    
calcular_imprimir_heroes_genero(lista_personajes, True, "peso", "F")

def sumar_dato_heroe_genero(lista: list, key: str, genero: str):
    acumulador = 0
    for i in lista:
        if (isinstance(i, dict) and len(i) > 0 and i["genero"] == genero):
            acumulador += i[key]
    if acumulador == 0:
        return -1
    return acumulador

def cantidad_heroes_genero(lista_heroes, genero: str):
    contador_heroes_genero = 0    
    for i in lista_heroes:
        if i["genero"] == genero:
            contador_heroes_genero +=1
    
def calcular_promedio_genero(lista: list, key: str, genero: str):
    x = sumar_dato_heroe_genero(lista, key, genero)
    return dividir(x, len(lista))

def stark_calcular_imprimir_promedio_guardar_altura(lista: list, genero: str):
    if len(lista) > 0:
        imprimir_dato(calcular_promedio_genero(lista, "altura", genero))
        guardar_archivo(f'heroes_promedio_altura_{genero}', calcular_promedio_genero(lista, "altura", genero))
        return True
    return False

def calcular_cantidad_tipo(lista_heroes:list, key: str):
    if len(lista_heroes) == 0:
        diccionario_falso = {"Error": "la lista se encuentra vacia"}
        return diccionario_falso
    else:
        diccionario_valores = {}
        for i in lista_heroes:
            if key in i.keys():
                if i[key] not in diccionario_valores.keys():
                    diccionario_valores[i[key]] = 1 
                else:
                    diccionario_valores[i[key]] += 1    
        diccionario_nuevo = {}
        for i in diccionario_valores.keys():
            i_capitalizada =    capitalizar_palabras(i)
            diccionario_nuevo[i_capitalizada] = diccionario_valores[i]
    return diccionario_nuevo

def guardar_cantidad_heroes_tipo(valores: dict, key: str):
    mensaje = ''
    for clave, valor in valores.items():
        mensaje += f"Característica: {key} {clave} - Cantidad de héroes: {valor}\n"

    archivo = f"heroes_cantidad_{key}.csv"
    return guardar_archivo(archivo, mensaje)

def stark_calcular_cantidad_por_tipo(lista_heroes: list, key):
    return guardar_cantidad_heroes_tipo(calcular_cantidad_tipo(lista_heroes, key), key)
   
def obtener_lista_tipos(lista_heroes: list, key: str):
    lista_valores_a_guardar = []
    for i in lista_heroes:
        if key in i.keys():
            nueva_key = capitalizar_palabras(i[key])
            if i[key] == "":
                lista_valores_a_guardar.append("N/A") 
            else:
                lista_valores_a_guardar.append(nueva_key) 
    return set(lista_valores_a_guardar)


def normalizar_dato(valor: str, valor_por_defecto: str):
    if valor == "":
        valor = valor_por_defecto 
        
    return valor

def normalizar_heroe(heroe, key):
    if key in heroe:
        valor = heroe[key]
        valor = capitalizar_palabras(valor)
        valor = normalizar_dato(valor, "N/A")
        heroe[key] = valor

    if "nombre" in heroe:
        heroe["nombre"] = capitalizar_palabras(heroe["nombre"])

    return heroe

def obtener_heroes_por_tipo(lista_heroes: list, variedad: set, tipo_dato: str):
    diccionario_armado = {} 
    for i in variedad:
        diccionario_armado[i] = []
            
    for j in lista_heroes:
        if tipo_dato in j:
            valor = normalizar_dato(j[tipo_dato], "N/A")
            for dato in variedad:
                if valor == dato:
                    diccionario_armado[dato].append(j["nombre"])
    return diccionario_armado
              
def guardar_heroes_por_tipo(dict, key):
    mensaje = ""
    for dato, value in dict.items():
        mensaje += f"{key} {dato}: {' | '.join(value)}\n" 
    archivo = f"heroes_segun_{key}.csv"
    return guardar_archivo(archivo, mensaje)

def stark_listar_heroes_por_dato(lista_heroes: list, key: str):
    return guardar_heroes_por_tipo(obtener_heroes_por_tipo(lista_heroes, obtener_lista_tipos(lista_heroes, key), key), key)

