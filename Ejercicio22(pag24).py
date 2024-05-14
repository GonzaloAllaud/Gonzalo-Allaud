# El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con ayuda de la fuerza” realizar las siguientes actividades:

# a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no queden más objetos en la mochila;

# b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sa- car para encontrarlo;

# c. Utilizar un vector para representar la mochila.

mochila = ["llaves", "cartuchera", "pala", "caramelos", "sable de luz"]
#Desarrollo
def fuerza (mochila, posicion=0,  objetos=0):
    if posicion >= len(mochila):
        return False, posicion   
    
    objetos += 1
    if mochila[posicion] == "sable de luz":
        return True, posicion

    return fuerza(mochila, posicion + 1, objetos)

encontrado, objetos = fuerza(mochila)

if encontrado:
    print("¡Luke encontró el sable de luz!")
    print(f"Número de objetos sacados: {objetos}")
else:
    print("No se encontró un sable de luz en la mochila.")
    print(f"Se sacaron {objetos} objetos de la mochila.")