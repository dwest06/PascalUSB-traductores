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

    def get_level(self, level):
        if not self.isEmpty() and level < self.size() and level >= 0:
            return self.items[level]

    def __str__(self):
        lista = ''
        for i in range(len(self.items)-1, -1, -1):
            lista += '[' + str(self.items[i]) + '],' + '\n'
        return lista


class Tabla_sym:
    """docstring for Tabla_sym"""
    def __init__(self):
        self.table = Stack()

    def insertar_scope(self):
        """ Insertamos en la pila un nuevo hash """
        self.table.push({})

    def eliminar_scope(self):
        """ Eliminamos un hash de la pila si la pila contiene elementos """
        if not self.table.isEmpty():
            self.table.pop()
        else:
            raise Exception("Pila vacia: No se ha podido elminar el scope")

    def insertar(self, name, value):
        """ Insertamos en el hash del nivel actual un nuevo elemento """
        if not self.table.isEmpty():
            aux = self.table.top()
            if not name in aux:
                aux[name] = value
            else:
                print("variable ya declarada")
            return True
        raise Exception("pila vacia: No se ha podido insertar, por favor inserte un scope")

    def consultar(self, name):
        """ Consultamos en el hash del nivel actual sobre un elemento """
        if not self.table.isEmpty():
            for i in range(self.table.size() + 1, -1, -1):
                aux = self.table.get_level(i)
                result = self.esta(aux, name)
                if  result is not None:
                    return result

        raise Exception("pila vacia: No se ha podido insertar, por favor inserte un scope")

    def esta(self, hash_, key):
        """ Metodo 'Privado' para uso de otro metodo """
        try:
            return hash_[key]
        except:
            return None

    def modificar(self, name, valor):
        """ Metodo para asignacion de un nuevo valor a una variable """
        if not self.table.isEmpty():
            for i in range(self.table.size() - 1, -1, -1):
                aux = self.table.get_level(i)
                result = self.esta(aux, name)
                if result is not None:
                    aux[name] = valor

    def __str__(self):
        """ Metodo para imprimir bonitico el nivel actual de estado de las variables """
        if not self.table.isEmpty():
            aux1 = ''
            for i in range(self.table.size() - 1, -1, -1):
                aux = self.table.get_level(i)
                aux1 += str(i) + ') ' + str(aux) + '\n'
            return aux1
        return ''
