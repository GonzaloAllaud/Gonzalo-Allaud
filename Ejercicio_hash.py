pokemons = [
    {'numero': 1, 'nombre': 'Bulbasaur', 'tipo': ['Planta', 'Veneno'], 'nivel': 5},
    {'numero': 4, 'nombre': 'Charmander', 'tipo': ['Fuego'], 'nivel': 10},
    {'numero': 7, 'nombre': 'Squirtle', 'tipo': ['Agua'], 'nivel': 15},
    {'numero': 25, 'nombre': 'Pikachu', 'tipo': ['Electrico'], 'nivel': 20},
    {'numero': 37, 'nombre': 'Vulpix', 'tipo': ['Fuego'], 'nivel': 25},
    {'numero': 143, 'nombre': 'Snorlax', 'tipo': ['Normal'], 'nivel': 30},
    {'numero': 199, 'nombre': 'Slowking', 'tipo': ['Agua', 'Psiquico'], 'nivel': 35},
    {'numero': 1009, 'nombre': 'Mew', 'tipo': ['Psiquico'], 'nivel': 100}
]

#Funciones hash

def hash_tipo(pokemon):
    return pokemon['tipo']

def hash_numero(pokemon):
    return str(pokemon['numero'])[-1]

def hash_nivel(pokemon):
    return pokemon['nivel']

#Tablas Hash

tabla_tipo = {}
tabla_numero = {}
tabla_nivel = {}


def agregar_pokemon(pokemon):
    #Tipo
    for tipo in pokemon['tipo']:
        if tipo not in tabla_tipo:
            tabla_tipo[tipo] = []
        tabla_tipo[tipo].append(pokemon)

    #Numero
    clave_numero = hash_numero(pokemon)
    if clave_numero not in tabla_numero:
        tabla_numero[clave_numero] = []
    tabla_numero[clave_numero].append(pokemon)

    #Nivel
    clave_nivel = hash_nivel(pokemon)
    if clave_nivel not in tabla_nivel:
        tabla_nivel[clave_nivel] = []
    tabla_nivel[clave_nivel].append(pokemon)

# e - mostrar todos los Pokémons cuyos numeros terminan en 3, 7 y 9;

def mostrarpokemonesnumero():
    for numero in tabla_numero:
        if numero == '3' or numero == '7' or numero == '9':
            pokemones = tabla_numero[numero]
            print(f"Pokémones que terminan en {numero}:")
            for pokemon in pokemones:
                print(pokemon)
            print()

# f - mostrar todos los Pokémons cuyos niveles son multiplos de 2, 5 y 10;

def mostrarpokemonesnivel():
    print(f"Pokémones con niveles múltiplos de 2, 5 y 10:")
    print("")
    for nivel in tabla_nivel:
        if nivel % 2 == 0 and nivel % 5 == 0 and nivel % 10 == 0:
            pokemones = tabla_nivel[nivel]
            for pokemon in pokemones:
                print(pokemon)
            print()

# g - mostrar todos los Pokémons de los siguientes tipo: Acero, Fuego, Electrifico, Hielo

def mostrarpokemonestipo(tiposinteres):
    for tipo in tiposinteres:
        if tipo in tabla_tipo:
            pokemones = tabla_tipo[tipo]
            if pokemones:
                print(f'Pokémons de tipo: {tipo}:')
                for pokemon in pokemones:
                    print(pokemon)
                print()    
            else:
                print(f"No se encontraron Pokémones del tipo {tipo}")



for pokemon in pokemons:
    agregar_pokemon(pokemon)


print("")
print("---------------------------------------------------")
mostrarpokemonesnumero()
print("")
print("---------------------------------------------------")
mostrarpokemonesnivel()
print("")
print("---------------------------------------------------")
lista = ['Acero', 'Fuego', 'Electrico', 'Hielo']
mostrarpokemonestipo(lista)
