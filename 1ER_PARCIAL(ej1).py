def invertir_lista(lista):
    if not lista:
        return []
    else:
        return invertir_lista(lista[1:]) + [lista[0]]

# EJEMPLO
mi_lista = [1, 2, 3, 4, 5]
lista_invertida = invertir_lista(mi_lista)
print(lista_invertida)
