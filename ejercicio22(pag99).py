cola_mcu = [
    {'nombre': 'Tony Stark', 'superheroe': 'Iron Man', 'genero': 'M'},
    {'nombre': 'Steve Rogers', 'superheroe': 'Capitán América', 'genero': 'M'},
    {'nombre': 'Natasha Romanoff', 'superheroe': 'Black Widow', 'genero': 'F'},
    {'nombre': 'Carol Danvers', 'superheroe': 'Capitana Marvel', 'genero': 'F'},
    {'nombre': 'Scott Lang', 'superheroe': 'Ant-Man', 'genero': 'M'},
    {'nombre': 'Peter Parker', 'superheroe': 'Spider-Man', 'genero': 'M'}
]

# a. Determinar el nombre del personaje del superhéroe Capitana Marvel
def nombre_personaje_superheroe(cola, superheroe):
    for personaje in cola:
        if personaje['superheroe'] == superheroe:
            print(f"El personaje de {superheroe} es {personaje['nombre']}")
            return personaje['nombre']
    print(f"No se encontró el superhéroe {superheroe}")
    return None

# b. Mostrar los nombres de los superhéroes femeninos
def mostrar_superheroes_femeninos(cola):
    print("Superhéroes femeninos:")
    for personaje in cola:
        if personaje['genero'] == 'F':
            print(f"{personaje['superheroe']}")

# c. Mostrar los nombres de los personajes masculinos
def mostrar_personajes_masculinos(cola):
    print("Personajes masculinos:")
    for personaje in cola:
        if personaje['genero'] == 'M':
            print(f"{personaje['nombre']}")

# d. Determinar el nombre del superhéroe del personaje Scott Lang
def superheroe_personaje(cola, nombre_personaje):
    for personaje in cola:
        if personaje['nombre'] == nombre_personaje:
            print(f"El superhéroe de {nombre_personaje} es {personaje['superheroe']}")
            return personaje['superheroe']
    print(f"No se encontró el personaje {nombre_personaje}")
    return None

# e. Mostrar todos los datos de los personajes o superhéroes cuyos nombres comienzan con la letra S
def mostrar_datos_con_letra(cola, letra):
    print(f"Personajes o superhéroes cuyos nombres empiezan con {letra}:")
    for personaje in cola:
        if personaje['nombre'].startswith(letra) or personaje['superheroe'].startswith(letra):
            print(f"{personaje['nombre']} es {personaje['superheroe']} ({personaje['genero']})")

# f. Determinar si el personaje Carol Danvers está en la cola e indicar su nombre de superhéroe
def buscar_personaje(cola, nombre_personaje):
    for personaje in cola:
        if personaje['nombre'] == nombre_personaje:
            print(f"{nombre_personaje} se encuentra en la cola, y su superhéroe es {personaje['superheroe']}")
            return personaje['superheroe']
    print(f"{nombre_personaje} no se encuentra en la cola")
    return None

# Ejecución
# a
print("a. Nombre del personaje de Capitana Marvel:")
nombre_personaje_superheroe(cola_mcu, 'Capitana Marvel')

# b
print("\nb. Superhéroes femeninos:")
mostrar_superheroes_femeninos(cola_mcu)

# c
print("\nc. Personajes masculinos:")
mostrar_personajes_masculinos(cola_mcu)

# d
print("\nd. Superhéroe del personaje Scott Lang:")
superheroe_personaje(cola_mcu, 'Scott Lang')

# e
print("\ne. Datos de personajes o superhéroes que empiezan con la letra 'S':")
mostrar_datos_con_letra(cola_mcu, 'S')

# f
print("\nf. Buscar si Carol Danvers está en la cola:")
buscar_personaje(cola_mcu, 'Carol Danvers')
