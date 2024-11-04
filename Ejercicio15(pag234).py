import heapq
from collections import defaultdict

class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def agregar_arista(self, vertice1, vertice2, peso):
        self.vertices[vertice1].append((peso, vertice2))
        self.vertices[vertice2].append((peso, vertice1))

    # Algoritmo de Prim para obtener el árbol de expansión mínima
    def arbol_expansion_minima(self, inicio):
        visitados = set([inicio])
        aristas = [(peso, inicio, adj) for peso, adj in self.vertices[inicio]]
        heapq.heapify(aristas)
        mst = []
        while aristas:
            peso, vertice1, vertice2 = heapq.heappop(aristas)
            if vertice2 not in visitados:
                visitados.add(vertice2)
                mst.append((vertice1, vertice2, peso))
                for arista in self.vertices[vertice2]:
                    if arista[1] not in visitados:
                        heapq.heappush(aristas, (arista[0], vertice2, arista[1]))
        return mst

# Clase para representar las maravillas y sus relaciones en el grafo
class Maravilla:
    def __init__(self, nombre, paises, tipo):
        self.nombre = nombre
        self.paises = paises
        self.tipo = tipo

class MaravillasMundo:
    def __init__(self):
        self.maravillas = []
        self.grafo_arqui = Grafo()
        self.grafo_natural = Grafo()
        self.paises_maravillas = defaultdict(lambda: {'arquitectonica': 0, 'natural': 0})

    def agregar_maravilla(self, nombre, paises, tipo):
        maravilla = Maravilla(nombre, paises, tipo)
        self.maravillas.append(maravilla)
        
        # Actualizar grafo y conteo de maravillas en cada país
        if tipo == "arquitectonica":
            self.grafo_arqui.agregar_vertice(nombre)
            for pais in paises:
                self.paises_maravillas[pais]['arquitectonica'] += 1
        elif tipo == "natural":
            self.grafo_natural.agregar_vertice(nombre)
            for pais in paises:
                self.paises_maravillas[pais]['natural'] += 1

    # b. Agregar distancias entre las maravillas de cada tipo
    def agregar_distancia(self, nombre1, nombre2, tipo, distancia):
        if tipo == "arquitectonica":
            self.grafo_arqui.agregar_arista(nombre1, nombre2, distancia)
        elif tipo == "natural":
            self.grafo_natural.agregar_arista(nombre1, nombre2, distancia)

    # c. Obtener el árbol de expansión mínima para cada tipo
    def obtener_arbol_expansion_minima(self, tipo):
        if tipo == "arquitectonica":
            inicio = next(iter(self.grafo_arqui.vertices))
            return self.grafo_arqui.arbol_expansion_minima(inicio)
        elif tipo == "natural":
            inicio = next(iter(self.grafo_natural.vertices))
            return self.grafo_natural.arbol_expansion_minima(inicio)

    # d. Determinar si existen países con maravillas de ambos tipos
    def paises_con_ambos_tipos(self):
        return [pais for pais, conteo in self.paises_maravillas.items() if conteo['arquitectonica'] > 0 and conteo['natural'] > 0]

    # e. Determinar si algún país tiene más de una maravilla del mismo tipo
    def paises_con_varias_maravillas_mismo_tipo(self):
        return {pais: conteo for pais, conteo in self.paises_maravillas.items() if conteo['arquitectonica'] > 1 or conteo['natural'] > 1}


# Ejemplo de uso
maravillas_mundo = MaravillasMundo()

# Agregar maravillas arquitectónicas
maravillas_mundo.agregar_maravilla("Gran Muralla China", ["China"], "arquitectonica")
maravillas_mundo.agregar_maravilla("Petra", ["Jordania"], "arquitectonica")
maravillas_mundo.agregar_maravilla("Cristo Redentor", ["Brasil"], "arquitectonica")
maravillas_mundo.agregar_maravilla("Machu Picchu", ["Perú"], "arquitectonica")
maravillas_mundo.agregar_maravilla("Chichen Itza", ["México"], "arquitectonica")
maravillas_mundo.agregar_maravilla("Coliseo de Roma", ["Italia"], "arquitectonica")
maravillas_mundo.agregar_maravilla("Taj Mahal", ["India"], "arquitectonica")

# Agregar maravillas naturales
maravillas_mundo.agregar_maravilla("Cataratas del Iguazú", ["Argentina", "Brasil"], "natural")
maravillas_mundo.agregar_maravilla("Amazonas", ["Brasil", "Colombia", "Perú"], "natural")
maravillas_mundo.agregar_maravilla("Bahía de Ha-Long", ["Vietnam"], "natural")
maravillas_mundo.agregar_maravilla("Isla Jeju", ["Corea del Sur"], "natural")
maravillas_mundo.agregar_maravilla("Parque Nacional de Komodo", ["Indonesia"], "natural")
maravillas_mundo.agregar_maravilla("Montaña de la Mesa", ["Sudáfrica"], "natural")
maravillas_mundo.agregar_maravilla("Río Subterráneo de Puerto Princesa", ["Filipinas"], "natural")

# b. Agregar distancias entre maravillas arquitectónicas y naturales
# (Las distancias son ejemplos ficticios)
distancias_arqui = [
    ("Gran Muralla China", "Petra", 5000),
    ("Gran Muralla China", "Cristo Redentor", 17000),
    ("Petra", "Cristo Redentor", 12000),
    ("Petra", "Machu Picchu", 15000),
    ("Cristo Redentor", "Machu Picchu", 3300),
    ("Machu Picchu", "Chichen Itza", 4000),
    ("Chichen Itza", "Coliseo de Roma", 9400),
    ("Coliseo de Roma", "Taj Mahal", 7000)
]

distancias_natural = [
    ("Cataratas del Iguazú", "Amazonas", 2200),
    ("Cataratas del Iguazú", "Bahía de Ha-Long", 17000),
    ("Amazonas", "Isla Jeju", 15000),
    ("Bahía de Ha-Long", "Parque Nacional de Komodo", 3200),
    ("Isla Jeju", "Montaña de la Mesa", 13800),
    ("Parque Nacional de Komodo", "Río Subterráneo de Puerto Princesa", 2300),
    ("Montaña de la Mesa", "Río Subterráneo de Puerto Princesa", 12000)
]

for (a, b, dist) in distancias_arqui:
    maravillas_mundo.agregar_distancia(a, b, "arquitectonica", dist)

for (a, b, dist) in distancias_natural:
    maravillas_mundo.agregar_distancia(a, b, "natural", dist)

# c. Árbol de expansión mínima de cada tipo
arbol_arqui = maravillas_mundo.obtener_arbol_expansion_minima("arquitectonica")
arbol_natural = maravillas_mundo.obtener_arbol_expansion_minima("natural")
print("Árbol de expansión mínima (Arquitectónicas):", arbol_arqui)
print("Árbol de expansión mínima (Naturales):", arbol_natural)

# d. Países con maravillas de ambos tipos
paises_ambos_tipos = maravillas_mundo.paises_con_ambos_tipos()
print("Países con maravillas arquitectónicas y naturales:", paises_ambos_tipos)

# e. Países con más de una maravilla del mismo tipo
paises_varias_mismo_tipo = maravillas_mundo.paises_con_varias_maravillas_mismo_tipo()
print("Países con más de una maravilla del mismo tipo:", paises_varias_mismo_tipo)
