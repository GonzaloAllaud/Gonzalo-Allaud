class Nodo:
    def __init__(self, nombre, es_heroe):
        self.nombre = nombre
        self.es_heroe = es_heroe
        self.izquierdo = None
        self.derecho = None


class Arbol:
    def __init__(self):
        self.raiz = None

    # Insertar un nodo en el árbol
    def insertar(self, nombre, es_heroe):
        if self.raiz is None:
            self.raiz = Nodo(nombre, es_heroe)
        else:
            self._insertar_recursivo(self.raiz, nombre, es_heroe)

    def _insertar_recursivo(self, nodo, nombre, es_heroe):
        if nombre < nodo.nombre:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(nombre, es_heroe)
            else:
                self._insertar_recursivo(nodo.izquierdo, nombre, es_heroe)
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(nombre, es_heroe)
            else:
                self._insertar_recursivo(nodo.derecho, nombre, es_heroe)

    # b. Listar los villanos ordenados alfabéticamente
    def listar_villanos(self):
        villanos = []
        self._inorden_villanos(self.raiz, villanos)
        return sorted(villanos)

    def _inorden_villanos(self, nodo, villanos):
        if nodo is not None:
            self._inorden_villanos(nodo.izquierdo, villanos)
            if not nodo.es_heroe:
                villanos.append(nodo.nombre)
            self._inorden_villanos(nodo.derecho, villanos)

    # c. Mostrar superhéroes que empiezan con "C"
    def heroes_con_c(self):
        heroes_c = []
        self._buscar_heroes_con_c(self.raiz, heroes_c)
        return heroes_c

    def _buscar_heroes_con_c(self, nodo, heroes_c):
        if nodo is not None:
            self._buscar_heroes_con_c(nodo.izquierdo, heroes_c)
            if nodo.es_heroe and nodo.nombre.startswith("C"):
                heroes_c.append(nodo.nombre)
            self._buscar_heroes_con_c(nodo.derecho, heroes_c)

    # d. Contar la cantidad de superhéroes en el árbol
    def contar_heroes(self):
        return self._contar_heroes(self.raiz)

    def _contar_heroes(self, nodo):
        if nodo is None:
            return 0
        contador = 1 if nodo.es_heroe else 0
        contador += self._contar_heroes(nodo.izquierdo)
        contador += self._contar_heroes(nodo.derecho)
        return contador

    # e. Búsqueda por proximidad para corregir Doctor Strange
    def corregir_doctor_strange(self):
        return self._corregir_nombre(self.raiz, "Doctor Strange", "Dr. Strange")

    def _corregir_nombre(self, nodo, nombre_incorrecto, nombre_correcto):
        if nodo is None:
            return False
        if nodo.nombre.lower() == nombre_incorrecto.lower():
            nodo.nombre = nombre_correcto
            return True
        return self._corregir_nombre(nodo.izquierdo, nombre_incorrecto, nombre_correcto) or \
               self._corregir_nombre(nodo.derecho, nombre_incorrecto, nombre_correcto)

    # f. Listar superhéroes en orden descendente
    def listar_heroes_descendente(self):
        heroes = []
        self._inorden_heroes(self.raiz, heroes)
        return sorted(heroes, reverse=True)

    def _inorden_heroes(self, nodo, heroes):
        if nodo is not None:
            self._inorden_heroes(nodo.izquierdo, heroes)
            if nodo.es_heroe:
                heroes.append(nodo.nombre)
            self._inorden_heroes(nodo.derecho, heroes)

    # g. Generar bosque de héroes y villanos
    def generar_bosque(self):
        arbol_heroes = Arbol()
        arbol_villanos = Arbol()
        self._separar_nodos(self.raiz, arbol_heroes, arbol_villanos)
        return arbol_heroes, arbol_villanos

    def _separar_nodos(self, nodo, arbol_heroes, arbol_villanos):
        if nodo is not None:
            if nodo.es_heroe:
                arbol_heroes.insertar(nodo.nombre, nodo.es_heroe)
            else:
                arbol_villanos.insertar(nodo.nombre, nodo.es_heroe)
            self._separar_nodos(nodo.izquierdo, arbol_heroes, arbol_villanos)
            self._separar_nodos(nodo.derecho, arbol_heroes, arbol_villanos)

    # I. Determinar cantidad de nodos en cada árbol del bosque
    def contar_nodos(self):
        return self._contar_nodos(self.raiz)

    def _contar_nodos(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._contar_nodos(nodo.izquierdo) + self._contar_nodos(nodo.derecho)

    # II. Barrido alfabético de cada árbol
    def listar_alfabeticamente(self):
        nombres = []
        self._inorden(self.raiz, nombres)
        return nombres

    def _inorden(self, nodo, nombres):
        if nodo is not None:
            self._inorden(nodo.izquierdo, nombres)
            nombres.append(nodo.nombre)
            self._inorden(nodo.derecho, nombres)


# Ejemplo de uso
arbol = Arbol()
arbol.insertar("Iron Man", True)
arbol.insertar("Captain America", True)
arbol.insertar("Thanos", False)
arbol.insertar("Doctor Strange", True)
arbol.insertar("Loki", False)
arbol.insertar("Hawkeye", True)
arbol.insertar("Red Skull", False)
arbol.insertar("Black Widow", True)

# Listar villanos alfabéticamente
print("Villanos:", arbol.listar_villanos())

# Superhéroes que empiezan con "C"
print("Superhéroes que empiezan con 'C':", arbol.heroes_con_c())

# Contar la cantidad de superhéroes
print("Cantidad de superhéroes:", arbol.contar_heroes())

# Corregir "Doctor Strange"
arbol.corregir_doctor_strange()
print("Árbol después de corregir Doctor Strange:", arbol.listar_alfabeticamente())

# Listar superhéroes en orden descendente
print("Superhéroes en orden descendente:", arbol.listar_heroes_descendente())

# Generar bosque
arbol_heroes, arbol_villanos = arbol.generar_bosque()
print("Nodos en el árbol de héroes:", arbol_heroes.contar_nodos())
print("Nodos en el árbol de villanos:", arbol_villanos.contar_nodos())
print("Árbol de héroes alfabéticamente:", arbol_heroes.listar_alfabeticamente())
print("Árbol de villanos alfabéticamente:", arbol_villanos.listar_alfabeticamente())
