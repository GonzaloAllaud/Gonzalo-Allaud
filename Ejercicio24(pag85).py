#Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de su nombre y la cantidad de películas de la saga en la que participó, implementar las funcionesnecesarias para resolver las siguientes actividades:

#a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;
#b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;
#c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
#d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

    def cima(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            return None

    def tamano(self):
        return len(self.items)

# Función para encontrar la posición de Rocket Raccoon y Groot
def encontrar_posicion_personajes(pila, personajes_buscar):
    posicion = 1
    posiciones = {}
    pila_aux = Pila()
    
    while not pila.esta_vacia():
        personaje = pila.desapilar()
        if personaje['nombre'] in personajes_buscar:
            posiciones[personaje['nombre']] = posicion
        pila_aux.apilar(personaje)
        posicion += 1

    # Volvemos a poner los elementos en la pila original
    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())

    return posiciones

# Función para encontrar personajes con más de 5 películas
def personajes_mas_de_5_peliculas(pila):
    personajes = []
    pila_aux = Pila()
    
    while not pila.esta_vacia():
        personaje = pila.desapilar()
        if personaje['cantidad_peliculas'] > 5:
            personajes.append(personaje)
        pila_aux.apilar(personaje)

    # Volvemos a poner los elementos en la pila original
    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())

    return personajes

# Función para encontrar cuántas películas participó Black Widow
def peliculas_viuda_negra(pila):
    cantidad_peliculas = 0
    pila_aux = Pila()
    
    while not pila.esta_vacia():
        personaje = pila.desapilar()
        if personaje['nombre'] == 'Black Widow':
            cantidad_peliculas = personaje['cantidad_peliculas']
        pila_aux.apilar(personaje)

    # Volvemos a poner los elementos en la pila original
    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())

    return cantidad_peliculas

# Función para mostrar personajes cuyos nombres empiezan con C, D y G
def personajes_letra(pila, letras):
    personajes = []
    pila_aux = Pila()
    
    while not pila.esta_vacia():
        personaje = pila.desapilar()
        if personaje['nombre'][0] in letras:
            personajes.append(personaje)
        pila_aux.apilar(personaje)

    # Volvemos a poner los elementos en la pila original
    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())

    return personajes

# Creación y llenado de la pila de personajes
pila_personajes = Pila()
personajes = [
    {'nombre': 'Iron Man', 'cantidad_peliculas': 10},
    {'nombre': 'Captain America', 'cantidad_peliculas': 9},
    {'nombre': 'Thor', 'cantidad_peliculas': 8},
    {'nombre': 'Black Widow', 'cantidad_peliculas': 7},
    {'nombre': 'Hawkeye', 'cantidad_peliculas': 5},
    {'nombre': 'Hulk', 'cantidad_peliculas': 6},
    {'nombre': 'Rocket Raccoon', 'cantidad_peliculas': 4},
    {'nombre': 'Groot', 'cantidad_peliculas': 4},
    {'nombre': 'Doctor Strange', 'cantidad_peliculas': 3},
    {'nombre': 'Ant-Man', 'cantidad_peliculas': 5}
]

for personaje in personajes:
    pila_personajes.apilar(personaje)

# Resolvemos las actividades
posiciones = encontrar_posicion_personajes(pila_personajes, ['Rocket Raccoon', 'Groot'])
print("Posiciones de Rocket Raccoon y Groot:", posiciones)

personajes_5_peliculas = personajes_mas_de_5_peliculas(pila_personajes)
print("Personajes con más de 5 películas:", personajes_5_peliculas)

peliculas_black_widow = peliculas_viuda_negra(pila_personajes)
print("Películas en las que participó Black Widow:", peliculas_black_widow)

personajes_cdg = personajes_letra(pila_personajes, ['C', 'D', 'G'])
print("Personajes cuyos nombres empiezan con C, D o G:", personajes_cdg)
