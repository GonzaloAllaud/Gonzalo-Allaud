class Grafo:
    def __init__(self):
        self.adyacencia = {}

    def agregar_vertice(self, personaje):
        if personaje not in self.adyacencia:
            self.adyacencia[personaje] = []

    def agregar_arista(self, personaje1, personaje2, episodios_compartidos):
        self.agregar_vertice(personaje1)
        self.agregar_vertice(personaje2)
        self.adyacencia[personaje1].append((personaje2, episodios_compartidos))
        self.adyacencia[personaje2].append((personaje1, episodios_compartidos))

    def hallar_arbol_expansion_minimo(self):
        import heapq
        
        if not self.adyacencia:
            return None, False
        
        nodo_inicial = next(iter(self.adyacencia))
        visitados = set([nodo_inicial])
        aristas = [(peso, nodo_inicial, vecino) for vecino, peso in self.adyacencia[nodo_inicial]]
        heapq.heapify(aristas)

        arbol_expancion_minimo = []
        contiene_yoda = False

        while aristas and len(visitados) < len(self.adyacencia):
            peso, nodo1, nodo2 = heapq.heappop(aristas)
            if nodo2 not in visitados:
                visitados.add(nodo2)
                arbol_expancion_minimo.append((nodo1, nodo2, peso))
                if nodo2 == "Yoda":
                    contiene_yoda = True
                for vecino, peso_arista in self.adyacencia[nodo2]:
                    if vecino not in visitados:
                        heapq.heappush(aristas, (peso_arista, nodo2, vecino))
        
        return arbol_expancion_minimo, contiene_yoda

    def maximo_episodios_compartidos(self):
        max_episodios = 0
        personajes = (None, None)

        for personaje, vecinos in self.adyacencia.items():
            for vecino, episodios in vecinos:
                if episodios > max_episodios:
                    max_episodios = episodios
                    personajes = (personaje, vecino)

        return personajes, max_episodios




grafo = Grafo()
grafo.agregar_arista("Yoda", "Luke", 5)
grafo.agregar_arista("Yoda", "Obi-Wan", 3)
grafo.agregar_arista("Luke", "Han", 4)
grafo.agregar_arista("Han", "Leia", 6)
grafo.agregar_arista("Leia", "Obi-Wan", 2)

# b
arbol_expancion_minimo, contiene_yoda = grafo.hallar_arbol_expansion_minimo()
print("Árbol de expansión mínimo:", arbol_expancion_minimo)
print("¿El Arbol de expansion minimo contiene a Yoda?", contiene_yoda)

# c
personajes, max_episodios = grafo.maximo_episodios_compartidos()
print(f"Personajes que más episodios comparten: {personajes}, con {max_episodios} episodios.")
