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
        if self.table.isEmpty():
            self.table.push({'a': [4,'int']})
            print("push dic vacio")
        else:
            #copiamos la tabla anteriro
            aux = self.table.top().copy()
            self.table.push(aux)
            print("push dic")

    def eliminar_scope(self):
        if not self.table.isEmpty():
            self.table.pop()
        else:
            raise Exception("Pila vacia: No se ha podido elminar el scope")

    def insertar(self, name, value, type_):
        if not self.table.isEmpty():
            aux = self.table.top()
            print("aux: ", aux)
            aux[name] = [value, type_]
            print("jejej")
            return True
        else:
            raise Exception("pila vacia: No se ha podido insertar, por favor inserte un scope")

    def consultar(self, name):
        if not self.table.isEmpty():
            aux = self.table.top()
            return aux[name]
        else:
            raise Exception("pila vacia: No se ha podido insertar, por favor inserte un scope")

    def __str__(self):
        if not self.table.isEmpty():
            aux = self.table.top()
            aux1 = str(aux)
            return aux1
        else:
            return {}
