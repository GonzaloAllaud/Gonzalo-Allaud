def buscar(list_values, criterio, value):
    for index, personaje in enumerate(list_values):
        if personaje[criterio] == value:
            return index
    return None

def mostrarlista(title, list_values):
    print()
    print(f"{title}")
    for index, elemento in enumerate(list_values):
        print(index, elemento)
    print()

def eliminar(list_values, criterio, value):
    index = buscar(list_values, criterio, value)
    if index is not None:
        return list_values.pop(index)

# 6. Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
# casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesa-
# rias para poder realizar las siguientes actividades:

superheroes = [
    {
        "nombre": "Spider-Man",
        "año_aparicion": 1962,
        "casa_comic": "Marvel",
        "biografia": "Peter Parker, un joven que obtiene habilidades arácnidas después de ser mordido por una araña radiactiva."
    },
    {
        "nombre": "Batman",
        "año_aparicion": 1939,
        "casa_comic": "DC",
        "biografia": "Bruce Wayne, un millonario que combate el crimen en Gotham City usando su intelecto y habilidades físicas, con su caracteristico traje."
    },
    {
        "nombre": "Mujer Maravilla",
        "año_aparicion": 1941,
        "casa_comic": "DC",
        "biografia": "Diana, princesa de las Amazonas, que lucha por la justicia, el amor y la igualdad en el mundo."
    },
    {
        "nombre": "Iron Man",
        "año_aparicion": 1963,
        "casa_comic": "Marvel",
        "biografia": "Tony Stark, un genio inventor y empresario que crea una armadura avanzada para convertirse en el superhéroe Iron Man."
    },
    {
        "nombre": "Linterna Verde",
        "año_aparicion": 1940,
        "casa_comic": "DC",
        "biografia": "Hal Jordan, un piloto que se convierte en miembro de la Green Lantern Corps, una fuerza policial intergaláctica."
    },
    {
        "nombre": "Wolverine",
        "año_aparicion": 1974,
        "casa_comic": "Marvel",
        "biografia": "Logan, un mutante con habilidades regenerativas y garras de adamantium."
    },
    {
        "nombre": "Doctor Strange",
        "año_aparicion": 1963,
        "casa_comic": "Marvel",
        "biografia": "Stephen Strange, un neurocirujano que se convierte en el Hechicero Supremo para proteger la Tierra contra amenazas místicas."
    },
    {
        "nombre": "Capitana Marvel",
        "año_aparicion": 1968,
        "casa_comic": "Marvel",
        "biografia": "Carol Danvers, una ex-piloto de la Fuerza Aérea que obtiene superpoderes y se convierte en una de las heroínas más poderosas del universo."
    },
    {
        "nombre": "Flash",
        "año_aparicion": 1940,
        "casa_comic": "DC",
        "biografia": "Barry Allen, un científico forense que obtiene la capacidad de moverse a supervelocidad después de un accidente en su laboratorio."
    },
    {
        "nombre": "Star-Lord",
        "año_aparicion": 1976,
        "casa_comic": "Marvel",
        "biografia": "Peter Quill, un aventurero intergaláctico y líder de los Guardianes de la Galaxia."
    },
    {
        "nombre": "Superman",
        "año_aparicion": 1938,
        "casa_comic": "DC",
        "biografia": "Clark Kent, un extraterrestre del planeta Krypton que posee poderes sobrehumanos en la Tierra."
    },
    {
        "nombre": "Aquaman",
        "año_aparicion": 1941,
        "casa_comic": "DC",
        "biografia": "Arthur Curry, el rey de la Atlántida que tiene la capacidad de comunicarse con la vida marina y posee una fuerza sobrehumana."
    },
    {
        "nombre": "Thor",
        "año_aparicion": 1962,
        "casa_comic": "Marvel",
        "biografia": "El dios del trueno, originario de Asgard, que protege tanto su hogar como la Tierra con su poderoso martillo Mjolnir."
    },
    {
        "nombre": "Viuda Negra",
        "año_aparicion": 1964,
        "casa_comic": "Marvel",
        "biografia": "Natasha Romanoff, una espía y asesina altamente entrenada que se convierte en una agente de S.H.I.E.L.D. y miembro de los Vengadores."
    },
    {
        "nombre": "Flecha Verde",
        "año_aparicion": 1941,
        "casa_comic": "DC",
        "biografia": "Oliver Queen, un millonario que combate el crimen como un arquero experto con un arco y una variedad de flechas especiales."
    }
]


# a. eliminar el nodo que contiene la información de Linterna Verde

# b. mostrar el año de aparición de Wolverine

# c. cambiar la casa de Dr. Strange a Marvel

# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
# “traje” o “armadura”

# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
# sea anterior a 1963

# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla

# g. mostrar toda la información de Flash y Star-Lord

# h. listar los superhéroes que comienzan con la letra B, M y S

# i. determinar cuántos superhéroes hay de cada casa de comic.


print("")
print("------------------------------------------------------")
print("")
print("EJERCICIO 5")
print("")
print("------------------------------------------------------")
print("")
#a

print("")
print("------------------------------------------------------")
print("")
print("")
print("EJERCICIO A")
print("")

aeliminar = "Linterna Verde"
criterio = "nombre"
resultado = eliminar(superheroes, criterio, aeliminar)

print("Resultado eliminacion: " ,resultado)

mostrarlista("Lista final: ", superheroes)

#b
print("")
print("------------------------------------------------------")
print("")
print("")
print("EJERCICIO B")
print("")

pj = "Wolverine"


def buscar_año(list_values, criterio):
    for personaje in list_values:
        if 'nombre' in personaje and personaje['nombre'] == criterio:
            if 'año_aparicion' in personaje:
                return personaje['año_aparicion']
            else:
                return None
    return None



busqueda = buscar_año(superheroes, pj)
print("El año de aparicion de Wolverine es: ",busqueda)

#c
print("")
print("------------------------------------------------------")
print("")
print("")
print("EJERCICIO C")
print("")

pj = "Doctor Strange"
casanueva = "DC"

def cambiocasa(list_values, pj, casanueva):
    for personaje in list_values:
        if 'nombre' in personaje and personaje['nombre'] == pj:
            personaje['casa_comic'] = casanueva
            return personaje
    return False


resultado = cambiocasa(superheroes,pj,casanueva)

print("Cambio de casa de Doctor Strange: " ,resultado)

#d
print("")
print("------------------------------------------------------")
print("")
print("")
print("EJERCICIO D")
print("")

def buscar_palabra(list_values):
    resultados = []
    for personaje in list_values:
        if 'biografia' in personaje and ('armadura' in personaje['biografia'] or 'traje' in personaje['biografia']):
            resultados.append(personaje['nombre'])
    return resultados if resultados else None

resultado = buscar_palabra(superheroes)

print("Los superheroes con 'traje/armadura' son: " ,resultado)

#e
print("")
print("------------------------------------------------------")
print("")
print("")
print("EJERCICIO E")
print("")

año = 1963

def busquedaaño(list_values,criterio):
    listaaños = []
    for personaje in list_values:
        if 'año_aparicion' in personaje and personaje['año_aparicion'] < criterio:
            if 'nombre' in personaje and 'año_aparicion' in personaje:
                listaaños.append("(")
                listaaños.append(personaje['nombre'] )
                listaaños.append(personaje['casa_comic'])
                listaaños.append(")")
    return listaaños if listaaños else None

resultadoaños = busquedaaño(superheroes,año)

print("Los superheroes anteriores al año 1963 son: " ,resultadoaños)

#f
print("")
print("------------------------------------------------------")
print("")
print("")
print("EJERCICIO F")
print("")

def busquedawmcp(list_values):
    listanueva= []
    for personaje in list_values:
        if 'nombre' in personaje:
            if personaje['nombre'] == 'Capitana Marvel':
                listanueva.append(personaje['nombre'])
                listanueva.append(personaje['casa_comic'])
            elif personaje['nombre'] == 'Mujer Maravilla':
                listanueva.append(personaje['nombre'])
                listanueva.append(personaje['casa_comic'])
    return listanueva if listanueva else None

resultadowmcp = busquedawmcp(superheroes)

print("A continuacion estan los siguientes superheroes con sus casas: " ,resultadowmcp)

#g
print("")
print("------------------------------------------------------")
print("")
print("")
print("EJERCICIO G")
print("")

def impresion(list_values, criterio):
    for personaje in list_values:
        if 'nombre' in personaje:
            if personaje['nombre'] == criterio:
                return personaje
            

print("1) Informacion de: " ,impresion(superheroes, 'Flash'))
print("2) Informacion de: " ,impresion(superheroes, 'Star-Lord'))

#h
print("")
print("------------------------------------------------------")
print("")
print("")
print("EJERCICIO H")
print("")

def busquedaletra(list_values):
    listaletras = []
    for personaje in list_values:
        if 'nombre' in personaje:
            if personaje['nombre'][0] == 'B' or personaje['nombre'][0] == 'M' or personaje['nombre'][0] == 'S':
                listaletras.append(personaje['nombre'])
    return listaletras if listaletras else None

resultadoletras = busquedaletra(superheroes)
print("Los superheroes con B,M o S son: " ,resultadoletras)
            
#i
print("")
print("------------------------------------------------------")
print("")
print("")
print("EJERCICIO I")
print("")


def casas(list_values):
    DC = 0
    MA = 0
    for personaje in superheroes:
            if 'casa_comic' in personaje:
                if personaje['casa_comic'] == 'DC':
                    DC += 1
                else:
                    MA += 1  

            
    print("Personajes de Marvel: " ,MA)
    print("Personajes de DC: " ,DC)

casas(superheroes)

print("")
print("------------------------------------------------------")
print("")
