class NodoCriatura:
    def __init__(self, nombre, derrotado_por=None):
        self.nombre = nombre
        self.derrotado_por = derrotado_por
        self.descripcion = ""
        self.capturada = ""
        self.izquierda = None
        self.derecha = None

class ArbolCriaturas:
    def __init__(self):
        self.raiz = None

    def insertar(self, nombre, derrotado_por=None):
        """Inserta una criatura en el árbol."""
        nuevo_nodo = NodoCriatura(nombre, derrotado_por)
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            self._insertar_recursivo(self.raiz, nuevo_nodo)

    def _insertar_recursivo(self, actual, nuevo_nodo):
        if nuevo_nodo.nombre < actual.nombre:
            if actual.izquierda is None:
                actual.izquierda = nuevo_nodo
            else:
                self._insertar_recursivo(actual.izquierda, nuevo_nodo)
        else:
            if actual.derecha is None:
                actual.derecha = nuevo_nodo
            else:
                self._insertar_recursivo(actual.derecha, nuevo_nodo)

    def recorrido_inorden(self, nodo):
        """Recorrido inorden para listar criaturas y quién las derrotó."""
        if nodo is not None:
            self.recorrido_inorden(nodo.izquierda)
            derrotado = nodo.derrotado_por if nodo.derrotado_por else "No derrotada"
            print(f"{nodo.nombre} - Derrotado por: {derrotado}")
            self.recorrido_inorden(nodo.derecha)

    def agregar_descripcion(self, nombre, descripcion):
        """Agrega una descripción a una criatura."""
        criatura = self.buscar_criatura(nombre)
        if criatura:
            criatura.descripcion = descripcion
            print(f"Descripción añadida a {nombre}: {descripcion}")
        else:
            print("Criatura no encontrada.")

    def buscar_criatura(self, nombre):
        """Busca una criatura por nombre."""
        return self._buscar_recursivo(self.raiz, nombre)

    def _buscar_recursivo(self, nodo, nombre):
        if nodo is None or nodo.nombre == nombre:
            return nodo
        if nombre < nodo.nombre:
            return self._buscar_recursivo(nodo.izquierda, nombre)
        else:
            return self._buscar_recursivo(nodo.derecha, nombre)

    def mostrar_informacion(self, nombre):
        """Muestra toda la información de una criatura."""
        criatura = self.buscar_criatura(nombre)
        if criatura:
            print(f"Nombre: {criatura.nombre}")
            print(f"Derrotado por: {criatura.derrotado_por}")
            print(f"Descripción: {criatura.descripcion}")
            print(f"Capturada por: {criatura.capturada}")
        else:
            print("Criatura no encontrada.")

    def contar_derrotas(self):
        """Cuenta las derrotas por héroe o dios."""
        contador = {}
        self._contar_derrotas_recursivo(self.raiz, contador)
        return sorted(contador.items(), key=lambda x: x[1], reverse=True)[:3]

    def _contar_derrotas_recursivo(self, nodo, contador):
        if nodo:
            if nodo.derrotado_por:
                contador[nodo.derrotado_por] = contador.get(nodo.derrotado_por, 0) + 1
            self._contar_derrotas_recursivo(nodo.izquierda, contador)
            self._contar_derrotas_recursivo(nodo.derecha, contador)

    def listar_derrotadas_por(self, heroe):
        """Lista criaturas derrotadas por un héroe específico."""
        derrotadas = []
        self._listar_derrotadas_por_recursivo(self.raiz, heroe, derrotadas)
        return derrotadas

    def _listar_derrotadas_por_recursivo(self, nodo, heroe, derrotadas):
        if nodo:
            if nodo.derrotado_por == heroe:
                derrotadas.append(nodo.nombre)
            self._listar_derrotadas_por_recursivo(nodo.izquierda, heroe, derrotadas)
            self._listar_derrotadas_por_recursivo(nodo.derecha, heroe, derrotadas)

    def listar_no_derrotadas(self):
        """Lista criaturas que no han sido derrotadas."""
        no_derrotadas = []
        self._listar_no_derrotadas_recursivo(self.raiz, no_derrotadas)
        return no_derrotadas

    def _listar_no_derrotadas_recursivo(self, nodo, no_derrotadas):
        if nodo:
            if not nodo.derrotado_por:
                no_derrotadas.append(nodo.nombre)
            self._listar_no_derrotadas_recursivo(nodo.izquierda, no_derrotadas)
            self._listar_no_derrotadas_recursivo(nodo.derecha, no_derrotadas)

    def actualizar_captura(self, nombre, capturador):
        """Actualiza el campo capturada de una criatura específica."""
        criatura = self.buscar_criatura(nombre)
        if criatura:
            criatura.capturada = capturador
            print(f"{nombre} capturado por {capturador}")
        else:
            print("Criatura no encontrada.")

    def listado_por_nivel(self):
        """Listar criaturas por nivel."""
        if not self.raiz:
            return
        cola = [self.raiz]
        while cola:
            actual = cola.pop(0)
            print(actual.nombre)
            if actual.izquierda:
                cola.append(actual.izquierda)
            if actual.derecha:
                cola.append(actual.derecha)

# Ejemplo de uso
arbol = ArbolCriaturas()

# Insertamos criaturas en el árbol
arbol.insertar("Ceto")
arbol.insertar("Tifón", "Zeus")
arbol.insertar("Equidna", "Argos Panoptes")
arbol.insertar("Medusa", "Perseo")
arbol.insertar("Ladón", "Heracles")

# (a) Recorrido inorden
print("\n(a) Listado inorden de criaturas y quienes la derrotaron:")
arbol.recorrido_inorden(arbol.raiz)

# (b) Cargar descripción
print("\n(b) Agregando descripción a Ceto:")
arbol.agregar_descripcion("Ceto", "Monstruo marino primordial.")

# (c) Mostrar información de Talos (si estuviera en el árbol)
print("\n(c) Mostrar información de Talos:")
arbol.mostrar_informacion("Talos")

# (d) Determinar los 3 héroes que derrotaron más criaturas
print("\n(d) Los 3 héroes que más criaturas derrotaron:")
print(arbol.contar_derrotas())

# (e) Listar criaturas derrotadas por Heracles
print("\n(e) Criaturas derrotadas por Heracles:")
print(arbol.listar_derrotadas_por("Heracles"))

# (f) Listar criaturas que no han sido derrotadas
print("\n(f) Criaturas no derrotadas:")
print(arbol.listar_no_derrotadas())

# (h) Modificar nodos indicando que Heracles las atrapó
print("\n(h) Modificar nodos indicando capturas de Heracles:")
arbol.actualizar_captura("Ceto", "Heracles")
arbol.actualizar_captura("Ladón", "Heracles")

# (m) Listado por nivel del árbol
print("\n(m) Listado por nivel del árbol:")
arbol.listado_por_nivel()
