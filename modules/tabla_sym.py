from stack import Stack

class Tabla_sym(object):
    """docstring for Tabla_sym"""
    def __init__(self):
        super(Tabla_sym, self).__init__()
        self.table = Stack()

    def insertar_scope(self):
        """ Se copia la nivel actual de la pila y se pega en el tope """
        if self.table.isEmpty():
            self.table.push({})
        else:
            #copiamos la tabla anteriro
            aux = self.table.top().copy()
            self.table.push(aux)

    def eliminar_scope(self):
        if not self.table.isEmpty():
            self.table.pop()
        else:
            raise Exception("Pila vacia: No se ha podido elminar el scope")

    def insertar(self, name, value, type_):
        aux = self.table.top()
        aux[name] = [value, type_]

