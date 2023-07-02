from data_stark import lista_personajes
import os

def imprimir_superheroes_genero_m():
    for personaje in lista_personajes:
        if personaje["genero"] == "M":
            print(personaje["nombre"])
            
def imprimir_superheroes_genero_f():
    for personaje in lista_personajes:
        if personaje["genero"] == "F":
            print(personaje["nombre"])

def superhero_mas_alto_genero_m():
    lista_mas_altos = []
    bandera_altura_maxima = True
    
    for personaje in lista_personajes:
        if personaje["genero"] == "M" and (bandera_altura_maxima or float(personaje["altura"]) > altura_maxima):
            bandera_altura_maxima = False
            altura_maxima = float(personaje["altura"])
    
    for personaje in lista_personajes:
        if float(personaje["altura"]) == altura_maxima and personaje["genero"] == "M":
            lista_mas_altos.append(personaje["nombre"])
    

    print(f"El superhéroe más alto de género M es: {lista_mas_altos}")


def superhero_mas_alto_genero_f():
    lista_mas_altos = []
    bandera_altura_maxima = True
    
    for personaje in lista_personajes:
        if personaje["genero"] == "F" and (bandera_altura_maxima or float(personaje["altura"]) > altura_maxima):
            bandera_altura_maxima = False
            altura_maxima = float(personaje["altura"])
    
    for personaje in lista_personajes:
        if float(personaje["altura"]) == altura_maxima and personaje["genero"] == "F":
            lista_mas_altos.append(personaje["nombre"])
    

    print(f"El superhéroe más alto de género F es: {lista_mas_altos}")
    

def superhero_mas_bajo_genero_m():
    lista_mas_bajos = []
    bandera_altura_minima = True
    
    for personaje in lista_personajes:
        if personaje["genero"] == "M" and (bandera_altura_minima or float(personaje["altura"]) < altura_minima):
            bandera_altura_minima = False
            altura_minima = float(personaje["altura"])

    
    
    for personaje in lista_personajes:
        if float(personaje["altura"]) == altura_minima and personaje["genero"] == "M":
            lista_mas_bajos.append(personaje["nombre"])
    

    print(f"El superhéroe más bajo de género M es: {lista_mas_bajos}")


def superhero_mas_bajo_genero_f():
    lista_mas_bajos = []
    bandera_altura_minima = True
    
    for personaje in lista_personajes:
        if personaje["genero"] == "F" and (bandera_altura_minima or float(personaje["altura"]) < altura_minima):
            bandera_altura_minima = False
            altura_minima = float(personaje["altura"])
    
    
    for personaje in lista_personajes:
        if float(personaje["altura"]) == altura_minima and personaje["genero"] == "F":
            lista_mas_bajos.append(personaje["nombre"])
    

    print(f"El superhéroe más bajo de género F es: {lista_mas_bajos}")

def altura_promedio_genero_m():
    acumulador_altura_m = 0
    contador_superheroes_m = 0

    for personaje in lista_personajes:
        if personaje["genero"] == "M":
            acumulador_altura_m += float(personaje["altura"])
            contador_superheroes_m += 1

    promedio_m = acumulador_altura_m / contador_superheroes_m
    print(f"La altura promedio de los superhéroes de género M es: {promedio_m}")


def altura_promedio_genero_f():
    acumulador_altura_f = 0
    contador_superheroes_f = 0

    for personaje in lista_personajes:
        if personaje["genero"] == "F":
            acumulador_altura_f += float(personaje["altura"])
            contador_superheroes_f += 1

    promedio_f = acumulador_altura_f / contador_superheroes_f
    print(f"La altura promedio de los superhéroes de género F es: {promedio_f}")

def contar_color_ojos():
    color_ojos_contador = {}

    for personaje in lista_personajes:
        color_ojos = personaje["color_ojos"]

        if color_ojos not in color_ojos_contador:
            color_ojos_contador[color_ojos] = 0


    for personaje in lista_personajes:
        color_ojos2 = personaje["color_ojos"]
        if color_ojos2 in color_ojos_contador.keys():
            color_ojos_contador[color_ojos2] +=1
    
    print(color_ojos_contador)

def contar_color_pelo():
    color_pelo_contador = {}

    for personaje in lista_personajes:
        color_pelo = personaje["color_pelo"]

        if color_pelo not in color_pelo_contador:
            color_pelo_contador[color_pelo] = 0


    for personaje in lista_personajes:
        color_pelo2 = personaje["color_pelo"]
        if color_pelo2 in color_pelo_contador.keys():
            color_pelo_contador[color_pelo2] +=1
    
    print(color_pelo_contador)

def contar_inteligencia():
    inteligencia_contador = {}

    for personaje in lista_personajes:
        inteligencia = personaje["inteligencia"]

        if inteligencia not in inteligencia_contador.keys():
            inteligencia_contador[inteligencia] = 0


    for personaje in lista_personajes:
        inteligencia2 = personaje["inteligencia"]
        if inteligencia2 in inteligencia_contador.keys():
            inteligencia_contador[inteligencia2] +=1
        if inteligencia == "":
            inteligencia_contador[inteligencia2] = "No tiene"
    
    print(inteligencia_contador)

def listar_por_color_ojos():
    superheroes_por_color_ojos = {}

    for personaje in lista_personajes:

        color_ojos = personaje["color_ojos"]
        if color_ojos not in superheroes_por_color_ojos.keys():
           superheroes_por_color_ojos[color_ojos] = [] 

        if color_ojos in superheroes_por_color_ojos:
            superheroes_por_color_ojos[color_ojos].append(personaje["nombre"])

    for color, superheroes in superheroes_por_color_ojos.items():
        print(f"Color de ojos: {color}")
        print(f"Superhéroes: {superheroes}")

def listar_por_color_pelo():
    superheroes_por_color_pelo = {}

    for personaje in lista_personajes:

        color_pelo = personaje["color_pelo"]
        if color_pelo not in superheroes_por_color_pelo.keys():
           superheroes_por_color_pelo[color_pelo] = [] 
        
        if color_pelo in superheroes_por_color_pelo:
            superheroes_por_color_pelo[color_pelo].append(personaje["nombre"])

    for color, superheroes in superheroes_por_color_pelo.items():
        print(f"Color de pelo: {color}")
        print(f"Superhéroes: {superheroes}")


def listar_por_inteligencias():
    superheroes_por_inteligencias = {}

    for personaje in lista_personajes:
        inteligencia = personaje["inteligencia"]
        if inteligencia not in superheroes_por_inteligencias.keys():
           superheroes_por_inteligencias[inteligencia] = [] 

        if inteligencia in superheroes_por_inteligencias:
            superheroes_por_inteligencias[inteligencia].append(personaje["nombre"])

    for inteligencia, superheroes in superheroes_por_inteligencias.items():
        print(f"inteligencias: {inteligencia}")
        print(f"Superhéroes: {superheroes}")

def menu_opciones() -> None:

    while True:
        os.system("cls")
        print("""
        ----------Menú de opciones-----------
        | 1_ Imprimir superheroes genero m  |
        | 2- Imprimir superheroes genero f  |
        | 3-Superhero mas alto genero m     | 
        | 4-Superhero mas alto genero f     |
        | 5-Superhero mas bajo genero m     |
        | 6-Superhero mas bajo genero f     |
        | 7-Altura promedio genero m        |
        | 8-Altura promedio genero f        |
        | 9-Contar color ojos               |
        | 10-Contar color pelo              |    
        | 11-Contar inteligencia            |
        | 12-Listar por color ojos          |
        | 13-Listar por color pelo          |
        | 14-Listar por inteligencias       |
        | 15-Salir                          |
        -------------------------------------    
            """
              )

        opcion = input("Elija opcion(1-14): ")
        os.system("cls")
        if opcion == "1":
            imprimir_superheroes_genero_m()
        elif opcion == "2":
            imprimir_superheroes_genero_f()
        elif opcion == "3":
            superhero_mas_alto_genero_m()
        elif opcion == "4":
            superhero_mas_alto_genero_f()
        elif opcion == "5":
            superhero_mas_bajo_genero_m()
        elif opcion == "6":
            superhero_mas_bajo_genero_f()
        elif opcion == "7":
            altura_promedio_genero_m()
        elif opcion == "8":
            altura_promedio_genero_f()
        elif opcion == "9":
            contar_color_ojos()
        elif opcion == "10":
            contar_color_pelo()
        elif opcion == "11":
            contar_inteligencia()
        elif opcion == "12":
            listar_por_color_ojos ()
        elif opcion == "13":
            listar_por_color_pelo()
        elif opcion == "14":
            listar_por_inteligencias()
        elif opcion == "15":
            break
        else:
            print("opcion invalida")
        input("presione cualquier tecla para continuar...")
        os.system("cls")


menu_opciones()