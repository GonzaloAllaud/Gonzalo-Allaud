
#! El general Hux es la persona encargada de administrar todas las operaciones de la base Starkiller, 
#! para lo cual nos solicita desarrollar un algoritmo que permita controlar las actividades
#! que se realizan, contemplando lo siguiente:

#! a. debe contemplar distintas prioridades para el control de operaciones de acuerdo al siguiente criterio:
#! pedidos de líder supremo Snoke y de Kylo Ren nivel tres, de capitán Phasma nivel dos y el
#! resto de las operaciones nivel a cargo de los generales de la base de nivel uno;

#! b. de cada actividad se conoce quien es el encargado, una descripción, la hora y
#! opcionalmente la cantidad de Stormtroopers requeridos;

#! c. utilizar una cola de prioridad para administrar las distintas operaciones, debe cargar al
#! menos ocho: dos de nivel tres, cuatro de nivel dos y cuatro de nivel uno;

#! d. opcionalmente se podrán agregar operaciones luego de atender una;

#! e. realizar la atención de las operaciones de la cola;

#! f. luego de atender la quinta operación, agregar una operación solicitada por capitán Phasma
#! para revisión de intrusos en el hangar B7 que requiere 25 Stormstroopers;

#! g. luego de atender la sexta operación, agregar una operación solicitada por el líder supremo
#! Snoke para destruir el planeta Takodana.

from heap import HeapMax

# Usamos el HeapMax para la cola de prioridad
heap = HeapMax()

# Cargamos las operaciones iniciales (2 de nivel 3, 4 de nivel 2, 4 de nivel 1)
operaciones_iniciales = [
    (3, "Líder Supremo Snoke", "Destruir base rebelde", "10:00", None),   # Prioridad 3
    (3, "Kylo Ren", "Capturar espía rebelde", "11:00", None),             # Prioridad 3
    (2, "Capitán Phasma", "Inspeccionar sector B", "12:00", None),        # Prioridad 2
    (2, "Capitán Phasma", "Revisar inventario", "13:00", None),           # Prioridad 2
    (2, "Capitán Phasma", "Entrenamiento de Stormtroopers", "14:00", None),# Prioridad 2
    (2, "Capitán Phasma", "Revisar sistema de comunicaciones", "15:00", None), # Prioridad 2
    (1, "General Hux", "Patrullaje sector A", "16:00", None),             # Prioridad 1
    (1, "General Hux", "Supervisar construcción", "17:00", None),         # Prioridad 1
    (1, "General Hux", "Revisar informes", "18:00", None),                # Prioridad 1
    (1, "General Hux", "Reunión con oficiales", "19:00", None)            # Prioridad 1
]

# Agregamos las operaciones a la cola de prioridad usando el método arrive del heap
for operacion in operaciones_iniciales:
    heap.arrive(operacion, operacion[0])  # La prioridad es el primer elemento de la tupla

# Función para procesar las operaciones
def atender_operaciones():
    contador = 0
    while True:
        if contador == 5:
            # Después de la quinta operación, agregamos la solicitud de Capitán Phasma
            nueva_operacion = (2, "Capitán Phasma", "Revisión de intrusos en el hangar B7", "20:00", 25)
            heap.arrive(nueva_operacion, nueva_operacion[0])
            print("\nSe agregó una nueva operación de Capitán Phasma: Revisión de intrusos en el hangar B7 con 25 Stormtroopers.")
        
        if contador == 6:
            # Después de la sexta operación, agregamos la solicitud de Snoke
            nueva_operacion = (3, "Líder Supremo Snoke", "Destruir el planeta Takodana", "21:00", None)
            heap.arrive(nueva_operacion, nueva_operacion[0])
            print("\nSe agregó una nueva operación del Líder Supremo Snoke: Destruir el planeta Takodana.")

        # Atendemos la siguiente operación en la cola de prioridad usando el método atention
        siguiente_operacion = heap.atention()
        if siguiente_operacion is None:
            print("\nNo hay más operaciones para atender.")
            break

        # Verifica el contenido de la operación antes de desempaquetar
        print(f"\nSiguiente operación recibida: {siguiente_operacion}")
        print(f"Longitud de la operación: {len(siguiente_operacion)}")

        # Desempaquetamos la operación si tiene la longitud correcta
        if len(siguiente_operacion) == 2:  # La operación contiene la prioridad y detalles
            prioridad, detalles = siguiente_operacion
            if len(detalles) == 4:  # Verifica si los detalles tienen los 4 valores esperados
                encargado, descripcion, hora, stormtroopers = detalles
                print(f"Atendiendo operación:\n - Encargado: {encargado}\n - Descripción: {descripcion}\n - Hora: {hora}\n - Stormtroopers: {stormtroopers if stormtroopers else 'No requeridos'}")
            else:
                print("Error: Los detalles de la operación no tienen el formato esperado.")
        else:
            print("Error: La operación no tiene la estructura esperada.")

        contador += 1

# Ejecutamos el proceso
atender_operaciones()
