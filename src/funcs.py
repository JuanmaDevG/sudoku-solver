from copy import deepcopy

class Variable:
    def __init__(self, fila, columna, valor):
        self.fila = fila
        self.columna = columna
        self.valor = valor
        if valor == '0':  # celda vacía
            self.dominio = [str(i) for i in range(1, 10)]
            self.fijada = False
        else:  # celda ya fijada
            self.dominio = [valor]
            self.fijada = True

    def __str__(self):
        return f"Var({self.fila},{self.columna}) val={self.valor} dom={self.dominio} fijada={self.fijada}"

    def asignar(self, val):
        self.valor = val
        self.dominio = [val]
        self.fijada = True

    def desasignar(self):
        if not self.fijada:
            self.valor = '0'
            self.dominio = [str(i) for i in range(1, 10)]


def es_valido(tablero, fila, col, val):
    for c in range(9):
        if tablero[fila][c] == val:
            return False
    # Columna
    for f in range(9):
        if tablero[f][col] == val:
            return False
    # Subcuadro 3x3
    inicio_f = (fila // 3) * 3
    inicio_c = (col // 3) * 3
    for f in range(inicio_f, inicio_f + 3):
        for c in range(inicio_c, inicio_c + 3):
            if tablero[f][c] == val:
                return False
    return True


def buscar_vacia(tablero):
    for f in range(9):
        for c in range(9):
            if tablero[f][c] == '0':
                return f, c
    return None


def backtracking(tablero):
    vacia = buscar_vacia(tablero)
    if not vacia:
        return True  # completo
    fila, col = vacia

    for val in map(str, range(1, 10)):
        if es_valido(tablero, fila, col, val):
            tablero[fila][col] = val
            if backtracking(tablero):
                return True
            tablero[fila][col] = '0'  # retroceso
    return False


def resolver_sudoku(tablero):
    copia = deepcopy(tablero)
    if backtracking(copia):
        return copia
    else:
        return None


# Tests unitarios
if __name__ == "__main__":
    sudoku = [
        ['5','3','0','0','7','0','0','0','0'],
        ['6','0','0','1','9','5','0','0','0'],
        ['0','9','8','0','0','0','0','6','0'],
        ['8','0','0','0','6','0','0','0','3'],
        ['4','0','0','8','0','3','0','0','1'],
        ['7','0','0','0','2','0','0','0','6'],
        ['0','6','0','0','0','0','2','8','0'],
        ['0','0','0','4','1','9','0','0','5'],
        ['0','0','0','0','8','0','0','7','9'],
    ]

    print("Sudoku inicial:")
    for fila in sudoku:
        print(" ".join(fila))

    solucion = resolver_sudoku(sudoku)

    if solucion:
        print("\nSudoku resuelto:")
        for fila in solucion:
            print(" ".join(fila))
    else:
        print("No tiene solución.")
