import heapq

class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def agregar_arista(self, vertice1, vertice2, peso):
        self.vertices[vertice1].append((peso, vertice2))
        self.vertices[vertice2].append((peso, vertice1))

    # c. Algoritmo de Prim para encontrar el árbol de expansión mínima
    def arbol_expansion_minima(self):
        inicio = list(self.vertices.keys())[0]
        visitados = set([inicio])
        aristas = [(peso, inicio, adj) for peso, adj in self.vertices[inicio]]
        heapq.heapify(aristas)
        costo_total = 0

        while aristas:
            peso, vertice1, vertice2 = heapq.heappop(aristas)
            if vertice2 not in visitados:
                visitados.add(vertice2)
                costo_total += peso
                for arista in self.vertices[vertice2]:
                    if arista[1] not in visitados:
                        heapq.heappush(aristas, (arista[0], vertice2, arista[1]))

        return costo_total

    # d. Algoritmo de Dijkstra para encontrar el camino más corto
    def camino_mas_corto(self, inicio, fin):
        distancias = {vertice: float('inf') for vertice in self.vertices}
        distancias[inicio] = 0
        cola = [(0, inicio)]
        camino = {}

        while cola:
            distancia_actual, vertice_actual = heapq.heappop(cola)

            if vertice_actual == fin:
                break

            for peso, vecino in self.vertices[vertice_actual]:
                distancia = distancia_actual + peso
                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    camino[vecino] = vertice_actual
                    heapq.heappush(cola, (distancia, vecino))

        # Construir el camino más corto
        ruta = []
        vertice = fin
        while vertice != inicio:
            ruta.append(vertice)
            vertice = camino[vertice]
        ruta.append(inicio)
        ruta.reverse()
        
        return ruta, distancias[fin]


# Crear el grafo y agregar los ambientes (vértices)
grafo = Grafo()
ambientes = [
    "cocina", "comedor", "cochera", "quincho", "baño 1", "baño 2",
    "habitación 1", "habitación 2", "sala de estar", "terraza", "patio"
]

for ambiente in ambientes:
    grafo.agregar_vertice(ambiente)

# b. Agregar las aristas con distancias
grafo.agregar_arista("cocina", "comedor", 3)
grafo.agregar_arista("cocina", "baño 1", 4)
grafo.agregar_arista("cocina", "habitación 1", 7)
grafo.agregar_arista("comedor", "sala de estar", 2)
grafo.agregar_arista("comedor", "terraza", 6)
grafo.agregar_arista("comedor", "quincho", 5)
grafo.agregar_arista("cochera", "quincho", 3)
grafo.agregar_arista("cochera", "patio", 5)
grafo.agregar_arista("cochera", "terraza", 8)
grafo.agregar_arista("quincho", "baño 1", 4)
grafo.agregar_arista("quincho", "patio", 2)
grafo.agregar_arista("quincho", "terraza", 7)
grafo.agregar_arista("baño 1", "baño 2", 3)
grafo.agregar_arista("baño 1", "habitación 1", 4)
grafo.agregar_arista("habitación 1", "habitación 2", 1)
grafo.agregar_arista("habitación 1", "sala de estar", 5)
grafo.agregar_arista("habitación 2", "terraza", 6)
grafo.agregar_arista("sala de estar", "patio", 3)

# c. Obtener el árbol de expansión mínima y calcular la longitud total del cable
costo_total = grafo.arbol_expansion_minima()
print("Metros de cables necesarios para conectar todos los ambientes:", costo_total)

# d. Determinar el camino más corto entre "habitación 1" y "sala de estar"
camino_corto, distancia_corta = grafo.camino_mas_corto("habitación 1", "sala de estar")
print("Camino más corto de habitación 1 a sala de estar:", camino_corto)
print("Metros de cable necesarios para el camino más corto:", distancia_corta)
