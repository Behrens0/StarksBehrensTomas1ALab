from data_stark import lista_personajes
import os

def mostrar_nombres():
    for i in lista_personajes:
        print(i["nombre"])

def mostrar_nombres_altura():
    for i in lista_personajes:
        print(f'{i["nombre"]}, {i["altura"]}')

def maximo_altura(): 
    lista_mas_altos = []
    bandera_altura_maxima = True
    for i in lista_personajes:
        if ((i["genero"] == "M") and bandera_altura_maxima or float(i["altura"]) > altura_maxima):
            bandera_altura_maxima = False
            altura_maxima = float(i["altura"])
    for i in lista_personajes:
        if(float(i["altura"]) == altura_maxima and i["genero"] == "M"):
            lista_mas_altos.append(i["nombre"])
    print(lista_mas_altos)

def minimo_altura():
    min_personaje = min(float(p['altura']) for p in lista_personajes)
    print(min_personaje)

    for i in lista_personajes:
        if(float(i["altura"]) == min_personaje):
            print(i["nombre"])

def maximo_peso(): 
    lista_mas_altos = []
    bandera_peso_maxima = True
    for i in lista_personajes:
        if ((i["genero"] == "M") and bandera_peso_maxima or float(i["peso"]) > peso_maxima):
            bandera_peso_maxima = False
            peso_maxima = float(i["peso"])
    for i in lista_personajes:
        if(float(i["peso"]) == peso_maxima and i["genero"] == "M"):
            lista_mas_altos.append(i["nombre"])
    print(lista_mas_altos)

def minimo_peso():
    min_personaje = min(float(p['peso']) for p in lista_personajes)
    print(min_personaje)

    for i in lista_personajes:
        if(float(i["peso"]) == min_personaje):
            print(i["nombre"])

def promedio():
    acumulador = 0
    for i in lista_personajes:
        acumulador += float(i["altura"])
    print(acumulador/len(lista_personajes))


            
def menu_opciones():

    while True:
        os.system("cls")
        print("""
        ----------Menú de opciones-----------
        | 1_Mostrar_nombres                 |
        | 2-Mostrar_nombres_altura          |
        | 3-Maximo_altura                   | 
        | 4-Minimo_altura                   |
        | 5-Maximo_peso                     |
        | 6-Promedio                        |
        | 7-Salir                           |
        -------------------------------------
            """
              )

        opcion = input("Elija opcion(1-14): ")
        os.system("cls")
        if opcion == "1":
            mostrar_nombres()
        elif opcion == "2":
            mostrar_nombres_altura()
        elif opcion == "3":
            maximo_altura()
        elif opcion == "4":
            minimo_altura()
        elif opcion == "5":
            maximo_peso()
        elif opcion == "6":
            promedio()
        elif opcion == "7":
            break
        else:
            print("opcion invalida")
        input("presione cualquier tecla para continuar...")
        os.system("cls")


menu_opciones()
    







