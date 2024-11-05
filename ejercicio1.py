pokemon_list = [
    {"nombre": "Jolteon", "numero": 135, "tipos": ["Eléctrico"]},
    {"nombre": "Typhlosion", "numero": 157, "tipos": ["Fuego"]},
    {"nombre": "Swampert", "numero": 260, "tipos": ["Agua", "Tierra"]},
    {"nombre": "Luxray", "numero": 405, "tipos": ["Eléctrico"]},
    {"nombre": "Haxorus", "numero": 612, "tipos": ["Dragón"]},
    {"nombre": "Talonflame", "numero": 663, "tipos": ["Fuego", "Volador"]},
    {"nombre": "Lycanroc", "numero": 745, "tipos": ["Roca"]},
    {"nombre": "Tyrantrum", "numero": 697, "tipos": ["Roca", "Dragón"]},
    {"nombre": "Inteleon", "numero": 818, "tipos": ["Agua"]},
    {"nombre": "Dragapult", "numero": 887, "tipos": ["Dragón", "Fantasma"]}
]

pokemon_por_nombre = {}
pokemon_por_numero = {}
pokemon_por_tipo = {}

for pokemon in pokemon_list:
    # Árbol por nombre
    nombre = pokemon["nombre"].lower()
    pokemon_por_nombre[nombre] = pokemon
    
    # Árbol por número
    numero = pokemon["numero"]
    pokemon_por_numero[numero] = pokemon
    
    # Árbol por tipo
    for tipo in pokemon["tipos"]:
        if tipo not in pokemon_por_tipo:
            pokemon_por_tipo[tipo] = []
        pokemon_por_tipo[tipo].append(pokemon)

# b)
def buscar_pokemon_proximidad(nombre_substring, numero=None):
    nombre_substring = nombre_substring.lower()
    resultados = []
    if numero:
        if numero in pokemon_por_numero:
            pokemon = pokemon_por_numero[numero]
            if nombre_substring in pokemon["nombre"].lower():
                resultados.append(pokemon)
    else:
        for nombre, pokemon in pokemon_por_nombre.items():
            if nombre_substring in nombre:
                resultados.append(pokemon)
    return resultados

# c)
def mostrar_pokemons_por_tipo(tipo):
    tipo = tipo.capitalize()  #El capitalize sirve para que la palabra arranque con mayuscula
    return [pokemon["nombre"] for pokemon in pokemon_por_tipo.get(tipo, [])]

# d)
def listar_pokemons_por_numero():
    return sorted(pokemon_list, key=lambda p: (p["numero"], p["nombre"]))

def listar_pokemons_por_nombre():
    return sorted(pokemon_list, key=lambda p: p["nombre"])

# e)
def mostrar_datos_pokemons_especificos(*nombres):
    return [pokemon_por_nombre.get(nombre.lower()) for nombre in nombres if nombre.lower() in pokemon_por_nombre]

# f)
def contar_pokemons_por_tipos(*tipos):
    conteo = {}
    for tipo in tipos:
        conteo[tipo] = len(pokemon_por_tipo.get(tipo.capitalize(), []))
    return conteo




# b
print("Búsqueda de Pokémon por proximidad de nombre 'ly' y número 745:")
print(buscar_pokemon_proximidad("ly", 745))

# c
print("Nombres de todos los Pokémon de tipo Agua:")
print(mostrar_pokemons_por_tipo("Agua"))

# b
# Listado ordenado por número
print("Listado ordenado por número:")
print(listar_pokemons_por_numero())

# Listado ordenado por nombre
print("Listado ordenado por nombre:")
print(listar_pokemons_por_nombre())

# e
print("Datos de los Pokémon Jolteon, Lycanroc y Tyrantrum:")
print(mostrar_datos_pokemons_especificos("Jolteon", "Lycanroc", "Tyrantrum"))

# f
print("Conteo de Pokémon de tipo Eléctrico y Acero:")
print(contar_pokemons_por_tipos("Eléctrico", "Acero"))
