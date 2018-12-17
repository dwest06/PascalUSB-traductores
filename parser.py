"""
    Analizador Sintactico del Lenguaje PascalUSB

    Segunda fase del proyecto

    Traductores e Interpretadores (CI-3725)
    David Rodríguez (14-10930)
    Javier Medina (12-10400)

    Septiembre - Diciembre 2018
"""

from sys import argv
from lexer import tokens
from ply import yacc as yacc
from modules.tabla_sym import Tabla_sym
from modules.stack import Stack

#Tabla de symbolos
TABLA = Tabla_sym()

# Clase nodo que permite la creacion del AST
class Node:
    """ Clase Nodo: Para crear un Arbol el cual facilita la impresion del AST"""
    def __init__(self, nombre=None, hijos=None, tipo=None):
        self.nombre = nombre
        self.espacios = 0
        self.tipo = tipo

        if hijos:
            self.hijos = hijos
        else:
            self.hijos = []

    def imprimir(self, espacios, end=False):
        """ Este metodo es para imprimir el AST """
        if self.nombre is not None:
            if not end:
                print(" "*espacios + self.nombre)
            else:
                print(" "*espacios + self.nombre, end='')
            self.espacios = espacios + 1
        else:
            self.espacios = espacios

        for index, hijo in enumerate(self.hijos):
            if self.nombre == 'Declare':
                if index == 0:
                    if hijo is not None:
                        hijo.imprimir(self.espacios, True)
                elif index == 1:
                    print(' as', end='')
                    if hijo is not None:
                        hijo.imprimir(1)
                else:
                    if hijo is not None:
                        hijo.imprimir(self.espacios)
            else:
                if hijo is not None:
                    hijo.imprimir(self.espacios)

    def set_tipo(self, tipo):
        """ Metodo para guardar el tipo de dato de un nodo """
        self.tipo = tipo

    def head(self):
        """ Metodo para regresar el primer hijo de un nodo """
        if self.hijos == []:
            return None
        return self.hijos[0]

    def set_simbolos(self):
        """
            Metodo para guardar en la tabla de symbolos las variables
            en su recpectivo scope
        """
        # Por comodidad, guardamos el apuntador de cada hijo (Nombre de las variables y los tipos)
        variables = self.hijos[0]
        tipos = self.hijos[1]
        # Verificamos la cantidad de tipos, si es 1, entonces todas las variables seran de ese tipo
        # de lo contrario, deben tener la misma cantidad los tipos que las variables.
        if tipos.head() is None:
            tipo = tipos.nombre
            while variables is not None:
                # Guardamos en el nodo el tipo de dato
                variables.set_tipo(tipo)
                nombre = variables.nombre
                # Insertamos en la tabla la variable junto a su tipo
                # Verificamos si la tabla devuelve true si se inserto correctamente
                # O false si ya la variable ha sido declarada
                if not TABLA.insertar(nombre, tipo):
                    print("Error Semantico: Variable '" + nombre + "' ya esta declarada con tipo '" +
                          tipo + "'.")
                    exit(1)
                variables = variables.head()
        else:
            while variables is not None:
                nombre = variables.nombre
                tipo = tipos.nombre
                # Guardamos en el nodo el tipo de dato
                variables.set_tipo(tipo)
                # Insertamos en la tabla la variable junto a su tipo
                # Verificamos si la tabla devuelve true si se inserto correctamente
                # O false si ya la variable ha sido declarada
                if not TABLA.insertar(nombre, tipo):
                    print("Error Semantico: Variable '" + nombre + "' ya esta declarada con tipo '" +
                          tipo + "'.")
                    exit(1)
                # Buscamos los siguientes
                tipos = tipos.head()
                variables = variables.head()

                # Verificamos si hay la misma cantidad de variables que tipos
                if tipos is None and not variables is None:
                    #raise Exception("Error semantico: cantidad de tipos de datos insuficientes.")
                    print("Error semantico: cantidad de tipos de datos insuficientes.")
                    exit(1)
        try:
            if self.hijos[2] is not None:
                self.hijos[2].set_simbolos()
        except Exception:
            pass

    def validar_exp(self):
        """ Metodo para validar la expresion"""
        # Revisamos si el tipo no es nulo entonces es un atomo
        # Devolvemos de una el tipo de atomo
        if self.tipo is not None:
            #print(self.nombre)
            if self.tipo == 'var':
                tipo = TABLA.consultar(self.nombre)
                #Verificamos que se haya declarado anteriormente la variable
                if tipo is None:
                    print("Error Semantico: Variable '" + self.nombre + "' no declarada.")
                    exit(1)
                return tipo
            return self.tipo

        # Si no, definimos 2 variables auxiliares, una donde se
        # guarda el tipo de los hijos y otra que verifica si son igules
        primer_tipo, final_tipo = '', ''
        for i in self.hijos:
            primer_tipo = i.validar_exp()
            if final_tipo != '':
                if final_tipo != primer_tipo:
                    print("Error Semantico: bad expression. '" + final_tipo + "' incompatible con '"
                          + primer_tipo + "'")
                    exit(1)
            else:
                final_tipo = primer_tipo
        self.set_tipo(final_tipo)
        return final_tipo


    def validar_semantica(self):
        """ Metodo para validar la semantica del lenguaje """

        # Verificamos si entra en un nuevo scope, en ese caso se llena la tabla de
        # simbolos junto con el tipo de Sla variable
        if self.nombre == 'Block' and self.head():
            # Insertamos nuevo scope
            TABLA.insertar_scope()
            # Llenamos la tabla
            self.hijos[0].set_simbolos()
            #Continuar con el DFS
            try:
                self.hijos[1].validar_semantica()
            except Exception:
                pass

            TABLA.eliminar_scope()
        # Si el es una Asignacion, entonces se verifica el tipo de la variable y expresion
        elif self.nombre == 'Asig':
            # Verificamos si el tipo de la variable es igual al tipo que devuelve la expresion
            tipo_var = TABLA.consultar(self.hijos[0].nombre)
            #Verificamos que se haya declarado anteriormente la variable
            if tipo_var is None:
                print("Error Semantico: Variable '" + self.hijos[0].nombre + "' no declarada.")
                exit(1)
            tipo_exp = self.hijos[1].validar_exp()
            #Guardamos en el nodo el tipo de la variable
            self.hijos[0].set_tipo(tipo_var)

            if tipo_var != tipo_exp:
                print("Error semantico: linea " + " Columna " +
                      "\nError al asignar expresion de tipo " +
                      tipo_exp + " a variable de tipo " + tipo_var)
                exit(1)
        elif self.nombre == 'Exp':
            #Validar una expresion
            self.validar_exp()
            
        else:
            for i in self.hijos:
                i.validar_semantica()

    def imp(self, espacios):
        """ Otro metodo util para imprimir el arbol con mas informacion"""
        if self.nombre == 'Declare':
            print('  '*espacios + self.nombre)
            self.hijos[0].imp_aux(espacios + 1)
        else:
            if self.nombre is not None and self.tipo != 'tipo':

                if self.tipo is not None:
                    print('  '*espacios + self.nombre + ' ' + self.tipo)
                else:
                    print('  '*espacios + self.nombre)

            for i in self.hijos:
                if i is not None:
                    i.imp(espacios + 1)

    def imp_aux(self, espacios):
        """ Metodo auxiliar para imprimir las declaraciones de variables """
        print('  '*espacios + self.nombre + ' ' + self.tipo)
        #Si hay mas de una declaracion se imprime
        for i in self.hijos:
            if i is not None:
                i.imp_aux(espacios)




#precedencia

precedence = (
    ('right', 'TkSemicolon'),
    ('right', 'TkItoi', 'TkMax', 'TkMin', 'TkLen'),
    ('right', 'TkPrintln', 'TkPrint'),
    ('right', 'TkRead'),
    ('right', 'TkBegin'),
    ('left', 'TkMod'),
    ('left', 'TkAnd'),
    ('left', 'TkOr'),
    ('nonassoc', 'TkEqual', 'TkNEqual'),
    ('nonassoc', 'TkGreater', 'TkLess', 'TkGeq', 'TkLeq'),
    ('nonassoc', 'TkElse'),
    ('left', 'TkIn'),
    ('right', 'TkNot'),
    ('left', 'TkPlus', 'TkMinus'),
    ('left', 'TkMult', 'TkDiv'),
    ('left', 'TkCap'),
    ('right', 'TkComma'),
    ('left', 'TkSoForth'),
    ('right', 'UMINUS')
)

#La gramatica empieza por p_qc

def p_qc(p):
    """
    INICIO : PROGRAMA
    """
    p[0] = Node(None, [p[1]])

def p_programa(p):
    """
    PROGRAMA : TkProgram
             | TkProgram INSTRUCCION
             | TkProgram INSTRUCCION POSTCOND
    """
    if len(p) == 2:
        p[0] = Node("Program")
    elif len(p) == 3:
        p[0] = Node("Program", [p[2]])
    else:
        p[0] = Node("Program", [p[2], p[3]])
    #print ("program")

def p_seq(p):
    """
    SEQ : INSTRUCCION
        | INSTRUCCION TkSemicolon SEQ
    """
    if len(p) == 4:
        p[0] = Node("Sequencing", [p[1], p[3]])
    else:

        p[0] = Node("Sequencing", [p[1]])

def p_instruccion(p):
    """
    INSTRUCCION : IO
                | ASIGNACION
                | BLOQUE
                | ITERACION
                | CONDICIONAL
    """
    #print("aqui " + str(p[1].nombre))
    p[0] = Node(None, [p[1]])

def p_io(p):
    """
    IO : TkRead EXPRESION
       | TkPrint LISTA_EXP
       | TkPrintln LISTA_EXP
    """
    if p[1] == "println":
        p[0] = Node("Printl", [p[2]])
    elif p[1] == "print":
        p[0] = Node("Print", [p[2]])
        #print("print " + str(p[2].nombre))
    else:
        p[0] = Node("Read", [p[2]])

    #print("IO ")# + str(p[0]))

def p_asignacion(p):
    """
    ASIGNACION : IDENTIFICADOR TkAsig EXPRESION
    """
    p[0] = Node("Asig", [p[1], p[3]])

def p_identficador(p):
    """
    IDENTIFICADOR : TkId
    """
    p[0] = Node(str(p[1]), None, tipo="var")

def p_bloque(p):
    """
    BLOQUE : TkBegin TkEnd
           | TkBegin SEQ TkEnd
           | TkBegin TkDeclare DECL_VAR TkEnd
           | TkBegin TkDeclare DECL_VAR SEQ TkEnd
    """
    if len(p) == 6:
        p[0] = Node("Block", [p[3], p[4]])
    elif len(p) == 5:
        p[0] = Node("Block", [p[3]])
    elif len(p) == 4:
        p[0] = Node("Block", [p[2]])
    else:
        p[0] = Node("Block")

def p_declaracion_var(p):
    """
    DECL_VAR : LISTA_VAR TkAs TIPOS TkSemicolon DECL_VAR
             | LISTA_VAR TkAs TIPOS
    """
    if len(p) == 6:
        p[0] = Node("Declare", [p[1], p[3], p[5]])
    else:
        p[0] = Node("Declare", [p[1], p[3]])

    #Hacer dfs para asignarle a la tabla de simbolos las variables con su tipo

def p_lista_var(p):
    """
    LISTA_VAR : TkId TkComma LISTA_VAR
              | TkId
    """
    if len(p) == 4:
        p[0] = Node(str(p[1]), [p[3]], tipo='var')
    else:
        p[0] = Node(str(p[1]), None, tipo='var')

def p_tipos(p):
    """
    TIPOS : TIPO TkComma TIPOS
          | TIPO
    """
    if len(p) == 4:
        p[0] = Node(str(p[1].nombre), [p[3]], tipo='tipo')
    else:
        p[0] = Node(str(p[1].nombre), None, tipo='tipo')

def p_tipo(p):
    """
    TIPO : TkInt
         | TkBool
         | TkInter
    """
    p[0] = Node(str(p[1]), None)
    #print("tipo")

def p_condicional(p):
    """
    CONDICIONAL : TkIf EXPRESION TkThen INSTRUCCION TkElse INSTRUCCION
                | TkIf EXPRESION TkThen INSTRUCCION
                | TkCase EXPRESION TkOf LISTA_CASE TkEnd
    """
    #Cuando es if then else
    if len(p) == 7:
        p[0] = Node("If", [p[2], Node("Then", [p[4]]), p[6]])
    #Cuando es if then
    elif len(p) == 5:
        p[0] = Node("If", [p[2], Node("Then", [p[4]])])
    #Cuando es Case
    else:
        p[0] = Node("Case", [p[2], p[4]])

    #print("codicional")

def p_lista_case(p):
    """
    LISTA_CASE : EXPRESION TkArrow INSTRUCCION
               | EXPRESION TkArrow INSTRUCCION LISTA_CASE
    """
    if len(p) == 4:
        p[0] = Node("Guard", [p[1], p[3]])
    else:
        p[0] = Node("Guard", [p[1], p[3], p[4]])

    #print("lista case")

def p_iteracion(p):
    """
    ITERACION : TkFor IDENTIFICADOR TkIn EXPRESION TkDo INSTRUCCION
              | TkWhile EXPRESION TkDo INSTRUCCION
    """
    if len(p) == 7:
        p[0] = Node("For", [p[2], p[4], p[6]])
    else:
        p[0] = Node("While", [p[2], p[4]])

    #print("iteracion")

def p_expresion(p):
    """
    EXPRESION : VARIABLES
              | CONVERTIR
              | EXPRESION TkPlus EXPRESION
              | EXPRESION TkMinus EXPRESION
              | EXPRESION TkMod EXPRESION
              | EXPRESION TkMult EXPRESION
              | EXPRESION TkDiv EXPRESION
              | EXPRESION TkCap EXPRESION
              | EXPRESION TkSoForth EXPRESION
              | EXPRESION TkAnd EXPRESION
              | EXPRESION TkOr EXPRESION
              | EXPRESION TkIn EXPRESION
              | EXPRESION TkEqual EXPRESION
              | EXPRESION TkNEqual EXPRESION
              | EXPRESION TkGreater EXPRESION
              | EXPRESION TkGeq EXPRESION
              | EXPRESION TkLess EXPRESION
              | EXPRESION TkLeq EXPRESION
              | TkOpenPar EXPRESION TkClosePar
              | TkNot EXPRESION
              | TkMinus VARIABLES %prec UMINUS
    """

    if len(p) == 4:
        if p[1] == '(':
            p[0] = Node("Exp", [p[2]])
            #especial por que cambia la posicion de la exp
        else:
            if p[2] == '+':
                p[0] = Node("Exp", [Node("Plus", [p[1], p[3]])])
            elif p[2] == '-':
                p[0] = Node("Exp", [Node("Minus", [p[1], p[3]])])
            elif p[2] == '*':
                p[0] = Node("Exp", [Node("Mult", [p[1], p[3]])])
            elif p[2] == '/':
                p[0] = Node("Exp", [Node("Div", [p[1], p[3]])])
            elif p[2] == '%':
                p[0] = Node("Exp", [Node("Mod", [p[1], p[3]])])
            if p[2] == '<':
                p[0] = Node("Exp", [Node("Less", [p[1], p[3]])])
            elif p[2] == '>':
                p[0] = Node("Exp", [Node("Greater", [p[1], p[3]])])
            elif p[2] == '<=':
                p[0] = Node("Exp", [Node("LessEq", [p[1], p[3]])])
            elif p[2] == '>=':
                p[0] = Node("Exp", [Node("GreaterEq", [p[1], p[3]])])
            elif p[2] == '==':
                p[0] = Node("Exp", [Node("Equal", [p[1], p[3]])])
            elif p[2] == '/=':
                p[0] = Node("Exp", [Node("Not Equal", [p[1], p[3]])])
            elif p[2] == '..':
                p[0] = Node("Exp", [Node("So Forth", [p[1], p[3]])])
            elif p[2] == '<>':
                p[0] = Node("Exp", [Node("Cap", [p[1], p[3]])])
            elif p[2] == 'or':
                p[0] = Node("Exp", [Node("Or", [p[1], p[3]])])
            elif p[2] == 'and':
                p[0] = Node("Exp", [Node("And", [p[1], p[3]])])
            elif p[2] == 'in':
                p[0] = Node("Exp", [Node("In", [p[1], p[3]])])

    elif len(p) == 3:
        if p[1] != "-":
            p[0] = Node("Exp", [Node("Not", [p[2]])])
        elif p[1] == "-":
            p[0] = Node("Exp", [Node("Minus", [p[2]])])
    elif len(p) == 2:
        #CONVERTIR
        if ((p[1].nombre == "itoi") or (p[1].nombre == "len") or
                (p[1].nombre == "max") or (p[1].nombre == "min")):
            p[0] = Node("Exp", [Node(None, [p[1]])])
        #VARIABLES
        else:
            p[0] = Node("Exp", [Node(None, [p[1]])])

def p_lista_exp(p):
    """
    LISTA_EXP : EXPRESION
              | EXPRESION TkComma LISTA_EXP
    """
    if len(p) == 2:
        p[0] = Node("Lista_exp", [p[1]])
    else:
        p[0] = Node("Lista_exp", [p[1], p[3]])

def p_variables(p):
    """
    VARIABLES : LITERAL
              | IDENTIFICADOR
    """
    if p[1].tipo == 'bool' or p[1].tipo == 'int' or p[1].tipo == 'string':
        p[0] = Node("Variable", [p[1]])
    else:
        p[0] = Node("Variable", [p[1]])

def p_literal(p):
    """
    LITERAL : TkNum
            | TkTrue
            | TkFalse
            | TkString
    """
    if (p[1] == 'true' or p[1] == 'false'):
        p[0] = Node(str(p[1]), None, tipo='bool')
    elif isinstance(p[1], int):
        p[0] = Node(str(p[1]), None, tipo='int')
    else:
        p[0] = Node(str(p[1]), None, tipo='string')

def p_convertir(p):
    """
    CONVERTIR : TkItoi TkOpenPar EXPRESION TkClosePar
              | TkLen TkOpenPar EXPRESION TkClosePar
              | TkMax TkOpenPar EXPRESION TkClosePar
              | TkMin TkOpenPar EXPRESION TkClosePar
    """
    p[0] = Node(str(p[1]), [p[3]])

def p_postcondicion(p):
    """
    POSTCOND : TkOpenBra TkPost TkTwoPoints EXP_CUANTIFICADOR TkCloseBra
    """
    p[0] = Node("POST", [p[4]])

def p_exp_cuantificador_forall(p):
    """
    EXP_CUANTIFICADOR : TkOpenPar TkForall IDENTIFICADOR TkPipe IDENTIFICADOR TkIn IDENTIFICADOR TkTwoPoints EXP_CUANTIFICADOR TkClosePar
                      | TkOpenPar TkForall IDENTIFICADOR TkPipe IDENTIFICADOR TkIn IDENTIFICADOR TkTwoPoints EXPRESION TkClosePar
    """
    p[0] = Node("Forall", [p[3], p[5], p[7], p[9]])

def p_exp_cuantificador_exist(p):
    """
    EXP_CUANTIFICADOR : TkOpenPar TkExists IDENTIFICADOR TkPipe IDENTIFICADOR TkIn IDENTIFICADOR TkTwoPoints EXP_CUANTIFICADOR TkClosePar
                      | TkOpenPar TkExists IDENTIFICADOR TkPipe IDENTIFICADOR TkIn IDENTIFICADOR TkTwoPoints EXPRESION TkClosePar
    """
    p[0] = Node("Exist", [p[3], p[5], p[7], p[9]])

def p_error(p):
    print("Syntax error in line " + str(p.lineno) + ", column " + \
        str(p.lexpos) + ": unexpected token '" + str(p.value) + "'")
    exit(1)

def main():    
    parser = yacc.yacc()
    #abrimos la ruta pasada por argumento
    filepath = argv[1]
    #Abrimos el contenido del la ruta
    file = open(filepath, 'r')
    #Guardamos las lineas de cada
    data = file.read()
    result = parser.parse(data)
    result.validar_semantica()
    result.imp(0)
    #result.imprimir(0)
    print(TABLA)

if __name__ == '__main__':
    main()
