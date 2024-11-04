cola_personajes = [
    {'nombre': 'Luke Skywalker', 'planeta': 'Tatooine'},
    {'nombre': 'Leia Organa', 'planeta': 'Alderaan'},
    {'nombre': 'Han Solo', 'planeta': 'Corellia'},
    {'nombre': 'Yoda', 'planeta': 'Dagobah'},
    {'nombre': 'Jar Jar Binks', 'planeta': 'Naboo'},
    {'nombre': 'Darth Vader', 'planeta': 'Tatooine'}
]

# Función que muestra personajes de ciertos planetas
def mostrar_personajes_por_planeta(cola, planetas):
    for personaje in cola:
        if personaje['planeta'] in planetas:
            print(f"{personaje['nombre']} es de {personaje['planeta']}")

# Función que encuentra y muestra el planeta natal de un personaje
def indicar_planeta_natal(cola, nombres_personajes):
    for personaje in cola:
        if personaje['nombre'] in nombres_personajes:
            print(f"{personaje['nombre']} es de {personaje['planeta']}")

# Función que inserta un personaje antes de otro
def insertar_antes_de(cola, nombre_referencia, nuevo_personaje):
    for i, personaje in enumerate(cola):
        if personaje['nombre'] == nombre_referencia:
            cola.insert(i, nuevo_personaje)
            break

# Función que elimina el personaje después de otro
def eliminar_despues_de(cola, nombre_referencia):
    for i, personaje in enumerate(cola):
        if personaje['nombre'] == nombre_referencia and i+1 < len(cola):
            eliminado = cola.pop(i+1)
            print(f"Personaje eliminado: {eliminado['nombre']}")
            break

# a. Mostrar personajes de Alderaan, Endor y Tatooine
print("Personajes de Alderaan, Endor y Tatooine:")
mostrar_personajes_por_planeta(cola_personajes, ['Alderaan', 'Endor', 'Tatooine'])

# b. Indicar el planeta natal de Luke Skywalker y Han Solo
print("\nPlaneta natal de Luke Skywalker y Han Solo:")
indicar_planeta_natal(cola_personajes, ['Luke Skywalker', 'Han Solo'])

# c. Insertar un nuevo personaje antes de Yoda
nuevo_personaje = {'nombre': 'Obi-Wan Kenobi', 'planeta': 'Stewjon'}
insertar_antes_de(cola_personajes, 'Yoda', nuevo_personaje)
print("\nPersonajes después de insertar a Obi-Wan Kenobi antes de Yoda:")
for personaje in cola_personajes:
    print(f"{personaje['nombre']} de {personaje['planeta']}")

# d. Eliminar el personaje ubicado después de Jar Jar Binks
eliminar_despues_de(cola_personajes, 'Jar Jar Binks')
print("\nPersonajes después de eliminar el que está después de Jar Jar Binks:")
for personaje in cola_personajes:
    print(f"{personaje['nombre']} de {personaje['planeta']}")
