# 15. Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: 
# nombre, cantidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. 
# Y además la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver
#las siguientes actividades utilizando lista de lista implementando las funciones necesarias:

entrenadores = [
    {
        "nombre": "Ash Ketchum",
        "torneos_ganados": 7,
        "batallas_perdidas": 50,
        "batallas_ganadas": 120,
        "pokemones": [
            {"nombre": "Pikachu", "nivel": 80, "tipo": "Eléctrico", "subtipo": None},
            {"nombre": "Charizard", "nivel": 32, "tipo": "Fuego", "subtipo": "Volador"},
            {"nombre": "Bulbasaur", "nivel": 65, "tipo": "Planta", "subtipo": "Veneno"},
            {"nombre": "Squirtle", "nivel": 60, "tipo": "Agua", "subtipo": None},
            {"nombre": "Greninja", "nivel": 90, "tipo": "Agua", "subtipo": "Siniestro"}
        ]
    },
    {
        "nombre": "Goh",
        "torneos_ganados": 2,
        "batallas_perdidas": 10,
        "batallas_ganadas": 40,
        "pokemones": [
            {"nombre": "Cinderace", "nivel": 75, "tipo": "Fuego", "subtipo": None},
            {"nombre": "Flygon", "nivel": 70, "tipo": "Tierra", "subtipo": "Dragón"},
            {"nombre": "Golurk", "nivel": 65, "tipo": "Tierra", "subtipo": "Fantasma"},
            {"nombre": "Sobble", "nivel": 50, "tipo": "Agua", "subtipo": 'Volador'},
            {"nombre": "Scyther", "nivel": 60, "tipo": "Bicho", "subtipo": "Volador"}
        ]
    },
    {
        "nombre": "Leon",
        "torneos_ganados": 10,
        "batallas_perdidas": 5,
        "batallas_ganadas": 100,
        "pokemones": [
            {"nombre": "Charizard", "nivel": 100, "tipo": "Fuego", "subtipo": "Volador"},
            {"nombre": "Rillaboom", "nivel": 85, "tipo": "Planta", "subtipo": None},
            {"nombre": "Haxorus", "nivel": 88, "tipo": "Dragón", "subtipo": None},
            
        ]
    },
    {
        "nombre": "Chloe",
        "torneos_ganados": 1,
        "batallas_perdidas": 8,
        "batallas_ganadas": 30,
        "pokemones": [
            {"nombre": "Eevee", "nivel": 45, "tipo": "Normal", "subtipo": None},
            {"nombre": "Espeon", "nivel": 55, "tipo": "Psíquico", "subtipo": None},
            {"nombre": "Terrakion", "nivel": 80, "tipo": "Eléctrico", "subtipo": None}
        ]
    },
    {
        "nombre": "Raihan",
        "torneos_ganados": 4,
        "batallas_perdidas": 15,
        "batallas_ganadas": 60,
        "pokemones": [
            {"nombre": "Duraludon", "nivel": 85, "tipo": "Acero", "subtipo": "Dragón"},
            {"nombre": "Flygon", "nivel": 80, "tipo": "Tierra", "subtipo": "Dragón"},
            {"nombre": "Garchomp", "nivel": 85, "tipo": "Dragón", "subtipo": "Tierra"},
            {"nombre": "Togekiss", "nivel": 75, "tipo": "Hada", "subtipo": "Volador"},
            {"nombre": "Tyranitar", "nivel": 82, "tipo": "Roca", "subtipo": "Siniestro"}
        ]
    }
]

print("")
print("------------------------------------------------------")
print("")
print("EJERCICIO 15")
print("")
print("------------------------------------------------------")
print("")


# a. obtener la cantidad de Pokémons de un determinado entrenador;
print("")
print("EJERCICIO A")
print("")

def contadorpok(list_values):
    numpokemon = 0
    for entrenador in list_values:
        if 'pokemones' in entrenador:
            for pokemon in entrenador['pokemones']:
                numpokemon += 1
            print("El entrenador" ,entrenador['nombre'], "tiene" ,numpokemon, "pokemones.")
            numpokemon = 0

contadorpok(entrenadores)
         
# b. listar los entrenadores que hayan ganado más de tres torneos;
print("")
print("------------------------------------------------------")
print("")
print("")
print("EJERCICIO B")
print("")
def contadortorneo(list_values):
    lista3 = []
    for entrenador in list_values:
        if 'torneos_ganados' in entrenador:
            if entrenador['torneos_ganados'] > 3:
                lista3.append(entrenador['nombre'])
    return lista3

resultadob = contadortorneo(entrenadores)

print("Los entrenadores con mas de 3 torneos ganados son: ",resultadob)

# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
print("")
print("------------------------------------------------------")
print("")
print("")
print("EJERCICIO C")
print("")

def entrenadorgan(list_values):
    mayorentrenador = 0
    nombremayor = None
    nombrepokemon = None
    pokemonmayor = 0
    
    for entrenador in list_values:
        if 'torneos_ganados' in entrenador:
            if entrenador['torneos_ganados'] > mayorentrenador:
                nombremayor = entrenador['nombre'] 
                mayorentrenador = entrenador['torneos_ganados']
                for pokemon in entrenador['pokemones']:
                    if pokemon['nivel'] > pokemonmayor:
                        nombrepokemon = pokemon['nombre']
                        pokemonmayor = pokemon['nivel']
    print("Pokemon: " ,nombrepokemon, "- Nivel: " ,pokemonmayor,  "- Entrenador: " ,nombremayor, "- Torneos ganados: " ,mayorentrenador )

entrenadorgan(entrenadores)           
            
# d. mostrar todos los datos de un entrenador y sus Pokemones;
print("")
print("------------------------------------------------------")
print("")
print("")
print("EJERCICIO D")
print("")

def mostrarpj(list_values, nombre):
    for entrenador in list_values:
        if 'nombre' in entrenador:
            if entrenador['nombre'] == nombre:
                print("Entrenador:", entrenador['nombre'])
                print("Torneos ganados:", entrenador['torneos_ganados'])
                print("Batallas perdidas:", entrenador['batallas_perdidas'])
                print("Batallas ganadas:", entrenador['batallas_ganadas'])
                print("Pokémones:")
                for pokemon in entrenador['pokemones']:
                 print(f"  - Nombre: {pokemon['nombre']}, Nivel: {pokemon['nivel']}, Tipo: {pokemon['tipo']}, Subtipo: {pokemon['subtipo']}")
                return
    print(f"No se encontró al entrenador {nombre}.")


nombre = "Ash Ketchum"
mostrarpj(entrenadores, nombre)

# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
print("")
print("------------------------------------------------------")
print("")
print("")
print("EJERCICIO E")
print("")

def porbat(list_values):
    totalbatallas = 0

    for entrenador in list_values:
        if 'batallas_ganadas' in entrenador:
            if entrenador['batallas_ganadas']:

                totalbatallas = totalbatallas + entrenador ["batallas_ganadas"] + entrenador['batallas_perdidas']

                promedio = (entrenador["batallas_ganadas"]*100) / totalbatallas
                
                if promedio > 79:
                    print("El entrenador " ,entrenador['nombre'], " tiene mas del 79 porciento de batallas ganadas.")
                else:
                    print("El entrenador " ,entrenador['nombre'], " tiene igual o menos a 79 porciento de batallas ganadas. :(")

                totalbatallas = 0


porbat(entrenadores)

# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo);
print("")
print("------------------------------------------------------")
print("")
print("")
print("EJERCICIO F")
print("")

def pok(list_values):

    for entrenador in list_values:
        if 'pokemones' in entrenador:
            for pokemon in entrenador['pokemones']:
                if (pokemon['tipo'] == 'Fuego') or (pokemon['tipo'] == 'Planta') or (pokemon['tipo'] == 'Agua' and pokemon['subtipo'] == 'Volador'):
                    print(entrenador['nombre'])
                    print("Pokemon:" ,pokemon['nombre'], 
                          "/Tipo:" ,pokemon['tipo'], 
                          " /Subtipo:" ,pokemon['subtipo'])
                    print("")

pok(entrenadores)


# g. el promedio de nivel de los Pokémons de un determinado entrenador;
print("")
print("------------------------------------------------------")
print("")
print("")
print("EJERCICIO G")
print("")

def prom(list_values,nombre):

    promedio = 0
    numpok = 0
    for entrenador in list_values:
        if nombre == entrenador['nombre']:
            if 'pokemones' in entrenador:
                for pokemon in entrenador['pokemones']:
                    promedio = promedio + pokemon['nivel']
                    numpok += 1
                
                promediofinal = promedio/numpok
                print("Entrenador " ,entrenador['nombre'], 
                      "Promedio Nivel Pokemon: " ,promediofinal)
                
prom(entrenadores,'Leon')


# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
print("")
print("------------------------------------------------------")
print("")
print("")
print("EJERCICIO H")
print("")

def detpok(list_values,nombre):
    listaentre = []
    for entrenador in list_values:
        if 'pokemones' in entrenador:
            for pokemon in entrenador['pokemones']:
                if pokemon['nombre'] == nombre:
                    listaentre.append(entrenador['nombre'])
    print("Los entrenadores con el pokemon" ,nombre,)
    return listaentre
    

resultadoh = detpok(entrenadores,'Charizard')

print( "son: " ,resultadoh)



# i. mostrar los entrenadores que tienen Pokémons repetidos;
print("")
print("------------------------------------------------------")
print("")
print("")
print("EJERCICIO I")
print("")

def pokemonesrepetidos(list_values):
    pokemones = []
    for entrenador in list_values:
        pokemones_vistos = []
        tiene_repetidos = False
        if 'pokemones' in entrenador:
            for pokemon in entrenador['pokemones']:
                if pokemon['nombre'] in pokemones_vistos:
                    tiene_repetidos = True
                    break
                else:
                    pokemones_vistos.append(pokemon['nombre'])
        if tiene_repetidos:
            pokemones.append(entrenador['nombre'])
    return pokemones


entrenadorespokemonrepetido = pokemonesrepetidos(entrenadores)
if len(entrenadorespokemonrepetido) > 0:
    print("Los siguientes entrenadores tienen Pokémon repetidos:")
    for nombre_entrenador in entrenadorespokemonrepetido:
        print(nombre_entrenador)
else:
    print("Ningún entrenador tiene Pokémon repetidos.")


# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
print("")
print("------------------------------------------------------")
print("")
print("")
print("EJERCICIO J")
print("")

def busquedaj(list_values):
    entrenadorfalso = True
    entrenadov = False
    for entrenador in list_values:
        if 'pokemones' in entrenador:
            for pokemon in entrenador['pokemones']:
                if pokemon['nombre'] == "Tyrantrum" or pokemon['nombre'] == 'Terrakion' or pokemon['nombre'] == 'Wingull':
                    print("El entrenador" ,entrenador['nombre'], "posee uno de los pokemones requeridos: " ,pokemon['nombre'])
                    entrenadov = True
                    entrenadorfalso = False
                

    if entrenadov:
        entrenadorfalso == False
    if entrenadorfalso:
        print("Ningunos de los entrenadores tienen algunos de los pokemones requeridos.")

busquedaj(entrenadores)


# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se deberán mostrar los datos de ambos;
print("")
print("------------------------------------------------------")
print("")
print("")
print("EJERCICIO K")
print("")

nombre_entrenador = input("Ingresa el nombre del entrenador: ")
nombre_pokemon = input("Ingresa el nombre del Pokémon: ")

def ingresar(list_values, nombre_entrenador, nombre_pokemon):
    for entrenador in list_values:
        if entrenador['nombre'] == nombre_entrenador:
            for pokemon in entrenador['pokemones']:
                if pokemon['nombre'] == nombre_pokemon:
                    inf_entrenador = {
                        "nombre": entrenador['nombre'],
                        "torneos_ganados": entrenador['torneos_ganados'],
                        "batallas_ganadas": entrenador['batallas_ganadas'],
                        "batallas_perdidas": entrenador['batallas_perdidas']
                    }
                    return inf_entrenador, pokemon
    return None, None


entrenadorencontrado, pokemonencontrado = ingresar(entrenadores,nombre_entrenador, nombre_pokemon)

if entrenadorencontrado and pokemonencontrado:
    print("Entrenador encontrado:", entrenadorencontrado)
    print("Pokemon encontrado:", pokemonencontrado)
else:
    print("El entrenador no tiene ese Pokémon.")

                
