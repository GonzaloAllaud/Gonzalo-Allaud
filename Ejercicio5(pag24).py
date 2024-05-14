#Desarrollar una función que permita convertir un número romano en un número decimal.
def romano(romano):
    valores = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    decimal = 0
    previo = 0
    
    for letra in romano[::-1]:
        valor = valores[letra]
        if valor < previo:
            decimal -= valor
        else:
            decimal += valor
        previo = valor
    
    return decimal

numero_romano = "DXV"
print("El número decimal que pertenece a", numero_romano, "es:", romano(numero_romano))