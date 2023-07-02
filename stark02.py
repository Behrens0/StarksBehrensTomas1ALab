from data_stark import *
import os

def stark_normalizar_datos(lista: list)->None:
    if len(lista) > 0:
        for i in lista:
            for key, value in i.items():
                if value.isnumeric() and not isinstance(value, int) :
                    i[key] = int(value)
                    # print("datos normalizados")
                elif value.replace(".", "").isnumeric() and not isinstance(value, float):
                    i[key] = float(value)
                    # print("dato float normalizado")
    else:
        print("error, lista vacia")
stark_normalizar_datos(lista_personajes)

def obtener_nombre(heroe: dict)->str:
    return f"Nombre: {heroe['nombre']}"


def imprimir_dato(mensaje: str)->None:
    print(mensaje)

def stark_imprimir_nombres_heroes(lista: list):
    if len(lista) > 0:
        for i in lista:
            imprimir_dato((obtener_nombre(i)))
    else:
        return -1


def obtener_nombre_y_dato(heroe: dict, key: str):
    return f'Nombre: {heroe["nombre"]}| {key}: {heroe[key]}'

def stark_imprimir_nombres_alturas(lista: list):
    if len(lista) > 0:
        for i in lista:
            print(obtener_nombre_y_dato(i, "altura"))
    else:
        return -1
    
def calcular_max(lista: list, key: str):
    bandera_maximo = True
    for i in lista:
        if bandera_maximo or i[key] > altura_maxima:
            bandera_maximo = False
            altura_maxima = i[key]
            heroe_mas_alto = i
    return heroe_mas_alto

def calcular_min(lista: list, key: str):
    bandera_minimo = True
    for i in lista:
        if bandera_minimo or i[key] < altura_minima:
            bandera_minimo = False
            altura_minima = i[key]
            heroe_mas_bajo = i
    return heroe_mas_bajo

def calcular_max_min(lista: list, key: str, maximo: bool):
    if maximo:
        return calcular_max(lista, key)
    else:
        return calcular_min(lista, key)


def calcular_imprimir_heroes(lista: list, maximo: bool, key: str):
    x = calcular_max_min(lista, key, maximo)
    imprimir_dato(obtener_nombre_y_dato(x, key))

def sumar_dato_heroes(lista: list, key: str):
    acumulador = 0
    for i in lista:
        if isinstance(i, dict) and len(i) > 0:
            acumulador += i[key]
    return acumulador

def dividir(dividendo: int, divisor: int):
    if divisor == 0:
        return 0
    else:
        return dividendo/divisor
    
def calcular_promedio(lista: list, key: str):
    x = sumar_dato_heroes(lista, key)
    return dividir(x, len(lista))

def stark_calcular_imprimir_promedio_altura(lista: list):
    imprimir_dato(calcular_promedio(lista, "altura"))

def imprimir_menu():
        imprimir_dato(
            """
            *** Menu de opciones ***
            ------------------------
            1-Imprimir los nombres de los heroes
            2-imprimir los nombres con las alturas
            3-Elegir buscar un maximo o un minimo y un atributo y ver el resultado
            4-calcular el promedio de las alturas
            5-Salir del programa
            """
            
        )
     
def validar_entero(check_value: str):
    return check_value.isdigit()

def stark_menu_principal():
    imprimir_menu()
    opcion = input("Ingrese opcion: ")
    if opcion.isdigit() and (int(opcion) > 0 and int(opcion) < 6):
        return int(opcion)
    else:
        return -1
def stark_marvel_app(lista: list):
   
   
    while True:
        os.system("cls") 
        opcion = stark_menu_principal()
       
         
        if opcion == 1:
            stark_imprimir_nombres_heroes(lista_personajes)
        elif opcion == 2:
            stark_imprimir_nombres_alturas(lista_personajes)
        elif opcion == 3:
            maximo = input("Elegir calculo: (maximo o minimo)") == "maximo"
            key = input("elegir key")
            calcular_imprimir_heroes(lista_personajes, maximo, key)
        elif opcion ==  4:
            stark_calcular_imprimir_promedio_altura(lista_personajes)
        elif opcion == 5:
            break
        input("Presione Enter para continuar...")
         
