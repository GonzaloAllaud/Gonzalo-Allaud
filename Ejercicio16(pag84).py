# Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire strikes back” y la otra los del episodio VII “The force awakens”. 
# Desarrollar un algoritmo que permita obtener la intersección de ambas pilas, es decir los personajes que aparecen en ambos episodios.

class Pila:
    def __init__(self):
        self.items = []
    def esta_vacia(self):
        return self.items == []
    def apilar(self, item):
        self.items.append(item)
    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None
    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            return None
    def tamaño(self):
        return len(self.items)
def interseccion_pilas(pila1, pila2):
    # Desapilo todos los elementos de pila1 y los agrego a un conjunto
    conjunto1 = set()
    while not pila1.esta_vacia():
        conjunto1.add(pila1.desapilar())
    # Desapilo todos los elementos de pila2 y los agrego a un conjunto
    conjunto2 = set()
    while not pila2.esta_vacia():
        conjunto2.add(pila2.desapilar())
        
    interseccion = conjunto1.intersection(conjunto2)
    # Apilo los elementos de la intersección en una nueva pila
    pila_interseccion = Pila()
    for elemento in interseccion:
        pila_interseccion.apilar(elemento)
    return pila_interseccion


pila_5 = Pila()
pila_5.apilar("Luke Skywalker")
pila_5.apilar("Darth Vader")
pila_5.apilar("Han Solo")

pila_6 = Pila()
pila_6.apilar("Han Solo")
pila_6.apilar("Leia Organa")
pila_6.apilar("Luke Skywalker")

pila_resultado = interseccion_pilas(pila_5, pila_6)

# Elementos de la pila de intersección
while not pila_resultado.esta_vacia():
    print(pila_resultado.desapilar())