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
from tabla_sym import Tabla_sym

# Clase nodo que permite la creacion del AST
class Node:
    """ Clase Nodo: Para crear un Arbol el cual facilita la impresion del AST"""
    def __init__(self, nombre=None, hijos=None):
        self.nombre = nombre
        self.espacios = 0
        self.tipo = None

        if hijos:
            self.hijos = hijos
        else:
            self.hijos = []

    def imprimir(self, espacios, end=False):
        if self.nombre is not None:
            if not end:
                print(" "*espacios +self.nombre)
            else:
                print(" "*espacios +self.nombre, end='')
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
    elif len(p) == 3:
        p[0] = Node("Sequencing", [p[1], p[2]])
        #print("aja instruccion sin seq y suq " + str(p[2].nombre))
    else:
        p[0] = Node("Sequencing", [p[1]])
    #print("SEQ")

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
    #print("asignacion")

def p_identficador(p):
    """
    IDENTIFICADOR : TkId
    """
    p[0] = Node("Ident: " + str(p[1]), None)

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
    #print("bloque")

def p_declaracion_var(p):
    """
    DECL_VAR : LISTA_VAR TkAs TIPOS TkSemicolon DECL_VAR
             | LISTA_VAR TkAs TIPOS
    """
    if len(p) == 6:
        p[0] = Node("Declare", [p[1], p[3], p[5]])
    else:
        p[0] = Node("Declare", [p[1], p[3]])

def p_lista_var(p):
    """
    LISTA_VAR : TkId TkComma LISTA_VAR
              | TkId
    """
    if len(p) == 4:
        p[0] = Node(str(p[1]) + ', ' + str(p[3].nombre), None)
    else:
        p[0] = Node(str(p[1]), None)

def p_tipos(p):
    """
    TIPOS : TIPO TkComma TIPOS
          | TIPO
    """
    if len(p) == 4:
        p[0] = Node(str(p[1].nombre) + ', ' + str(p[3].nombre), None)
    else:
        p[0] = Node(str(p[1].nombre), None)

    #print("tipos")

def p_tipo(p):
    """
    TIPO : TkInt
         | TkBool
         | TkInter
    """
    p[0] = Node(str(p[1]), None)
    #print("tipo")

def p_variables(p):
    """
    VARIABLES : LITERAL
              | IDENTIFICADOR
              | LITERAL TkComma VARIABLES
              | IDENTIFICADOR TkComma VARIABLES
    """
    if len(p) == 2:
        p[0] = Node(None, [p[1]])
    else:
        p[0] = Node(None, [p[1], p[3]])

    #print("variables")

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
        elif p[2] == '+':
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
        elif p[2] == ',':
            p[0] = Node(None, [p[1], p[3]])
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
        if ((p[1].nombre == "itoi") or (p[1].nombre == "len") or (p[1].nombre == "max") or (p[1].nombre == "min")):
            p[0] = Node("Exp", [Node(None, [p[1]])])
        else:
            p[0] = Node(None, [Node(None, [p[1]])])

    #print("expresion " + str(p[1].nombre))

def p_lista_exp(p):
    """
    LISTA_EXP : EXPRESION
              | EXPRESION TkComma LISTA_EXP
    """
    if len(p) == 2:
        p[0] = Node("Lista_exp", [p[1]])
    else:
        p[0] = Node("Lista_exp", [p[1], p[3]])

def p_literal(p):
    """
    LITERAL : TkNum
            | TkTrue
            | TkFalse
            | TkString
    """
    if type(p[1]) == str:
        p[0] = Node(str(p[1]), None)
    else:
        p[0] = Node('Literal: '+ str(p[1]), None)
    #print("literal ")


def p_convertir(p):
    """
    CONVERTIR : TkItoi TkOpenPar EXPRESION TkClosePar
              | TkLen TkOpenPar EXPRESION TkClosePar
              | TkMax TkOpenPar EXPRESION TkClosePar
              | TkMin TkOpenPar EXPRESION TkClosePar
    """
    p[0] = Node(str(p[1]), [p[3]])
    #print("convertir " + str(p[1]))

def p_postcondicion(p):
    """
    POSTCOND : TkOpenBra TkPost TkTwoPoints EXP_CUANTIFICADOR TkCloseBra
    """
    p[0] = Node("POST", [p[4]])

    #print("post")

def p_exp_cuantificador_forall(p):
    """
    EXP_CUANTIFICADOR : TkOpenPar TkForall IDENTIFICADOR TkPipe IDENTIFICADOR TkIn IDENTIFICADOR TkTwoPoints EXP_CUANTIFICADOR TkClosePar
                      | TkOpenPar TkForall IDENTIFICADOR TkPipe IDENTIFICADOR TkIn IDENTIFICADOR TkTwoPoints EXPRESION TkClosePar
    """
    p[0] = Node("Forall", [p[3], p[5], p[7], p[9]])

    #print("forall")

def p_exp_cuantificador_exist(p):
    """
    EXP_CUANTIFICADOR : TkOpenPar TkExists IDENTIFICADOR TkPipe IDENTIFICADOR TkIn IDENTIFICADOR TkTwoPoints EXP_CUANTIFICADOR TkClosePar
                      | TkOpenPar TkExists IDENTIFICADOR TkPipe IDENTIFICADOR TkIn IDENTIFICADOR TkTwoPoints EXPRESION TkClosePar
    """
    p[0] = Node("Exist", [p[3], p[5], p[7], p[9]])

    #print("exists")
"""
def p_vacio(p):
    '''
    VACIO :
    '''
    pass
"""

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
    result = parser.parse(data, tracking=True)
    result.imprimir(0)


if __name__ == '__main__':
    main()
