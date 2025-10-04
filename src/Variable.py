
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
