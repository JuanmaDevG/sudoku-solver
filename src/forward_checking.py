from Variable import Variable
from copy import deepcopy

def relacionadas(f, c):
    posiciones = set()
    for j in range(9):
        if j != c:
            posiciones.add((f, j))
    for i in range(9):
        if i != f:
            posiciones.add((i, c))
    start_f, start_c = (f // 3) * 3, (c // 3) * 3
    for i in range(start_f, start_f + 3):
        for j in range(start_c, start_c + 3):
            if (i, j) != (f, c):
                posiciones.add((i, j))
    return posiciones


def forward_checking(variables):
    fila, col = None, None
    for i in range(9):
        for j in range(9):
            var = variables[i][j]
            if var.valor == '0':
                fila, col = i, j
                break
        if fila is not None:
            break

    if fila is None:
        return True  # No hay vacías -> completado

    var = variables[fila][col]

    for val in list(var.dominio):
        snapshot = deepcopy(variables)
        var.asignar(val)
        consistente = True
        for (i, j) in relacionadas(fila, col):
            otro = variables[i][j]
            if otro.valor == '0' and val in otro.dominio:
                otro.dominio.remove(val)
                if not otro.dominio:  # dominio vacío -> inconsistente
                    consistente = False
                    break

        if consistente and forward_checking(variables):
            return True

        # Retroceder
        variables = snapshot

    return False


def resolver_sudoku(tablero):
    variables = inicializar_variables(tablero)
    if forward_checking(variables):
        # Extraer solución en formato de tablero
        solucion = [[variables[f][c].valor for c in range(9)] for f in range(9)]
        return solucion
    else:
        return None


# Ejemplo de uso
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
        print("\nSudoku resuelto con Forward Checking:")
        for fila in solucion:
            print(" ".join(fila))
    else:
        print("No tiene solución.")
