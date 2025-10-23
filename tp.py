class Celda:
    def __init__(self, fila: int, columna: int, valor: int):
        self.fila = fila
        self.columna = columna
        self.valor = valor


matrizCeldas = []

while True:
    valor = input("Ingrese el valor para la celda o 'fin' para terminar: ").lower().strip()
    if valor == "fin":
        break

    fila = int(input("Ingrese la posición de la fila: "))
    columna = int(input("Ingrese la posición de la columna: "))

  
    existe = False
    for celda in matrizCeldas:
        if celda.fila == fila and celda.columna == columna:
            existe = True
            break

    if existe:
        print(" Ya existe una celda en esa posición.\n")
    else:
        nueva_celda = Celda(fila, columna, valor)
        matrizCeldas.append(nueva_celda)
        print(" Celda agregada correctamente.\n")


print("\n Celdas cargadas:")
for celd in matrizCeldas:
    print(f"Fila: {celd.fila}, Columna: {celd.columna}, Valor: {celd.valor}")


def buscar_valor(fila, columna):
    for celda in matrizCeldas:
        if celda.fila == fila and celda.columna == columna:
            return celda.valor
    return "La fila y columna indicada no ha sido asignada en ninguna celda"


print("\n Búsqueda de valor en la matriz")
fila_buscar = int(input("Ingrese la fila a buscar: "))
columna_buscar = int(input("Ingrese la columna a buscar: "))

resultado = buscar_valor(fila_buscar, columna_buscar)
print("Resultado:", resultado)
