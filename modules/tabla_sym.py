class Stack(object):
    """docstring for Stack"""
    def __init__(self):
        super(Stack, self).__init__()
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def top(self):
        if not self.isEmpty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        lista = ''
        for i in range(len(self.items)):
            lista += '[' + str(self.items[i]) + '],' + '\n'
        return lista


class Tabla_sym:
    """docstring for Tabla_sym"""
    def __init__(self):
        self.table = Stack()

    def insertar_scope(self):
        """ Insertamos en la pila un nuevo hash """
        if self.table.isEmpty():
            self.table.push({})
        else:
            #copiamos la tabla anteriro
            aux = self.table.top().copy()
            self.table.push(aux)

    def eliminar_scope(self):
        """ Eliminamos un hash de la pila si la pila contiene elementos """
        if not self.table.isEmpty():
            self.table.pop()
        else:
            raise Exception("Pila vacia: No se ha podido elminar el scope")

    def insertar(self, name, value, type_):
        """ Insertamos en el hash del nivel actual un nuevo elemento """
        if not self.table.isEmpty():
            aux = self.table.top()
            aux[name] = [value, type_]
            return True
        raise Exception("pila vacia: No se ha podido insertar, por favor inserte un scope")

    def consultar(self, name):
        """ Consultamos en el hash del nivel actual sobre un elemento """
        if not self.table.isEmpty():
            aux = self.table.top()
            return aux[name]

        raise Exception("pila vacia: No se ha podido insertar, por favor inserte un scope")

    def __str__(self):
        """ Metodo para imprimir bonitico el nivel actual de estado de las variables """
        if not self.table.isEmpty():
            aux = self.table.top()
            aux1 = str(aux)
            return aux1
        return {}
