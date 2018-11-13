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
#precedencia

class Node():
    """docstring for Node"""
    def __init__(self, tipo, hijos=None, hoja=None, tabs=0):
        self.type = tipo
        if hijos:
            self.hijos = hijos
        else:
            self.hijos = []
        self.hoja = hoja
        self.tabs = tabs

    def imprimir(self):
        for i in range(self.tabs):
            print("\t", end='')


precedence = (
    ('right', 'TkItoi'),
    ('right', 'TkPrintln', 'TkPrint'),
    ('right', 'TkRead'),
    ('right', 'TkBegin'),
    ('left', 'TkAnd'),
    ('left', 'TkOr'),
    ('right', 'TkNot'),
    ('nonassoc', 'TkEqual'),
    ('nonassoc', 'TkGreater', 'TkLess', 'TkGeq', 'TkLeq'),
    ('left', 'TkPlus', 'TkMinus'),
    ('left', 'TkMult', 'TkDiv', 'TkMod'),
    ('right', 'UMINUS'),
    ('right', 'TkProgram'),
    ('right', 'TkSemicolon')
)

#La gramatica empieza por p_qc

def p_qc(p):
    """
    INICIO : PROGRAMA
    """
    #p[0] = ("INICIO", p[1])

def p_programa(p):
    """
    PROGRAMA : TkProgram 
             | TkProgram INSTRUCCION
             | TkProgram INSTRUCCION POSTCOND
    """
    #p[0] = ("PROGRAM", p[2])
    print ("program")
    
def p_bloque(p):
    """
    BLOQUE : TkBegin TkEnd
           | TkBegin INSTRUCCION TkEnd
           | TkBegin TkDeclare DECL_VAR INSTRUCCION TkEnd
    """
    #if len(p) == 4:
    #    p[0] = ("BLOQUE", p[2], p[3])
    #elif len(p) == 3:
    #    p[0] = ("BLOQUE", p[2])
    #else: 
    #    p[0] = ("BLOQUE")
    print("bloque")

#def p_secuenciacion(p):
    '''
    SECUENCIACION : INSTRUCCION
                  | INSTRUCCION TkSemicolon SECUENCIACION
    '''

#    if len(p) == 4:
#        p[0] = ("SECUENCIACION", p[1], p[3])
#        print("secuenciacion")
#    else:
#        p[0] = ("INSTRUCCION", [p[1]])
#        print ("instruccion")

def p_declaracion_var(p):
    """
    DECL_VAR : VARIABLES TkAs TIPOS TkSemicolon DECL_VAR
             | VARIABLES TkAs TIPOS
    """
    #p[0] = lista_var([p[1],p[3]])
    #if len(p) == 6:
    #    p[0] = ("DECLARACION", p[1], p[3], p[5])
    #else:
    #    p[0] = ("DECLARACION", p[1], p[3])

    print("declaracion")

def p_tipos(p):
    """
    TIPOS : TIPO TkComma TIPOS
          | TIPO
    """
    #if len(p) == 4:
    #    p[0] = ("TIPOS", p[1], p[3])
    #else:
    #    p[0] = ("TIPOS", p[1])

    print("tipos")

def p_tipo(p):
    """
    TIPO : TkInt
         | TkBool
         | TkInter
    """
    #p[0] = ("TIPO", p[1])
    print("tipo")

def p_variables(p):
    """
    VARIABLES : TkId TkComma VARIABLES
              | TkId
              | LITERAL
    """
    #if len(p) == 4:
    #    p[0] = ("VARIABLES", p[3])
    #else:
    #    p[0] = ("VARIABLES", p[1])

    print("variables") #+ str(p[0]))


def p_instruccion(p):
    """
    INSTRUCCION : IO
                | VARIABLES TkAsig EXPRESION
                | CONDICIONAL
                | ITERACION
                | BLOQUE
                | CONVERTIR
                | INSTRUCCION TkSemicolon INSTRUCCION
    """
    #if len(p) == 4:
    #    if  p[2] == ";":
    #        p[0] = ("SECUENCIACION", p[1], p[3])
    #        print ("SECUENCIACION " + str(p[0]) )
    #    elif p[2] == ":=":
    #        p[0] = ("INSTRUCCION", p[1], p[3])
    #        print("instruccion " + str(p[0]))
    #else:
    #    p[0] = ("INSTRUCCION", p[1])
    #    print ("instruccion " + str(p[0]))
    if len(p) == 4:
        if p[2] == ";":
            print("secuenciacion")
    else:
        print ("Instruccion")

def p_io(p):
    """
    IO : TkRead TkId
       | TkRead EXPRESION TkSoForth EXPRESION
       | TkPrint VARIABLES
       | TkPrintln VARIABLES
    """
    #if len(p) == 5:
    #    p[0] = ("IO", p[2], p[4])
    #else:
    #    p[0] = ("IO", p[2])

    print("IO ")# + str(p[0]))

def p_condicional(p):
    """
    CONDICIONAL : TkIf EXPRESION TkThen INSTRUCCION TkElse INSTRUCCION
                | TkIf EXPRESION TkThen INSTRUCCION
                | TkCase EXPRESION TkOf LISTA_CASE TkEnd
    """
    #if len(p) == 7:
    #    p[0] = ("CONDICIONAL", p[2], p[4], p[6])
    #else:
    #    p[0] = ("CONDICIONAL", p[2], p[4])

    print("codicional")


def p_lista_case(p):
    """
    LISTA_CASE : EXPRESION TkArrow INSTRUCCION
               | EXPRESION TkArrow INSTRUCCION LISTA_CASE
    """
    #if len(p) == 4:
    #    p[0] = ("LISTA_CASE", p[1], p[3])
    #else:
    #    p[0] = ("LISTA_CASE", p[1], p[3], p[4])
    print("lista case")

def p_iteracion(p):
    """
    ITERACION : TkFor TkId TkIn EXPRESION TkDo INSTRUCCION
              | TkWhile EXPRESION TkDo INSTRUCCION
    """
    #if len(p) == 7:
    #    p[0] = ("ITERACION", p[2], p[4], p[6])
    #else:
    #    p[0] = ("ITERACION", p[2], p[4])

    print("iteracion")

def p_expresion(p):
    """
    EXPRESION : TkId
              | LITERAL
              | TkNot EXPRESION
              | TkOpenPar EXPRESION TkClosePar
              | EXPRESION TkMod EXPRESION
              | EXPRESION TkMult EXPRESION
              | EXPRESION TkDiv EXPRESION
              | EXPRESION TkPlus EXPRESION
              | EXPRESION TkMinus EXPRESION %prec UMINUS
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
    """

    """
    if len(p) == 4:
        if p[1] == '(':
            p[0] = ("EXPRESION", p[2])
        elif p[2] == '+':
            p[0] = ("EXPRESION", p[1], p[3])
        elif p[2] == '-':
            p[0] = ("EXPRESION", p[1], p[3])
        elif p[2] == '*':
            p[0] = ("EXPRESION", p[1], p[3])
        elif p[2] == '/':
            p[0] = ("EXPRESION", p[1], p[3])
        elif p[2] == '%':
            p[0] = ("EXPRESION", p[1], p[3])
        if p[2] == '<':
            p[0] = ("EXPRESION", p[1], p[3])
        elif p[2] == '>':
            p[0] = ("EXPRESION", p[1], p[3])
        elif p[2] == '<=':
            p[0] = ("EXPRESION", p[1], p[3])
        elif p[2] == '>=':
            p[0] = ("EXPRESION", p[1], p[3])
        elif p[2] == '=':
            p[0] = ("EXPRESION", p[1], p[3])
        elif p[2] == '/=':
            p[0] = ("EXPRESION", p[1], p[3])

    elif len(p) == 3:
        p[0] = ("EXPRESION", p[2])
    elif len(p) == 6:
        p[0] = ("EXPRESION", -p[1])
    else:
        p[0] =("EXPRESION", p[1])
    """
    print("expresion")# + str(p[0]))

def p_literal(p):
    """
    LITERAL : TkNum
            | TkTrue
            | TkFalse
            | TkString
    """
    #p[0] = ("literal",p[1])
    print("literal")# + str(p[0]))

################################################

def p_convertir(p):
    """
    CONVERTIR : TkItoi TkOpenPar TkId TkClosePar
              | TkLen TkOpenPar TkId TkClosePar
              | TkMax TkOpenPar TkId TkClosePar
              | TkMin TkOpenPar TkId TkClosePar
    """
    #p[0] = ([p[3]])
    print("convertir")

def p_postcondicion(p):
    """
    POSTCOND : TkOpenBra TkPost TkTwoPoints EXP_CUANTIFICADOR TkCloseBra
    """
    #p[0] = p[4]

    print("post")

def p_exp_cuantificador_forall(p):
    """
    EXP_CUANTIFICADOR : TkOpenPar TkForall TkId TkPipe TkId TkIn TkId TkTwoPoints EXP_CUANTIFICADOR TkClosePar
                      | TkOpenPar TkForall TkId TkPipe TkId TkIn TkId TkTwoPoints EXPRESION TkClosePar
    """ 
    #p[0] = p[3], p[5], p[7], p[9]

    print("forall")

def p_exp_cuantificador_exist(p):
    """
    EXP_CUANTIFICADOR : TkOpenPar TkExists TkId TkPipe TkId TkIn TkId TkTwoPoints EXP_CUANTIFICADOR TkClosePar
                      | TkOpenPar TkExists TkId TkPipe TkId TkIn TkId TkTwoPoints EXPRESION TkClosePar
    """
    #p[0] = p[3], p[5], p[7], p[9]

    print ("exists")
"""
def p_vacio(p):
    '''
    VACIO :
    '''
    pass
"""

def p_error(p):
    print("Se ha encontrado un error", p)
    print("Error en la linea " + str(p.lineno))



parser = yacc.yacc()
#abrimos la ruta pasada por argumento
filepath = argv[1]
#Abrimos el contenido del la ruta
file = open(filepath, 'r')
#Guardamos las lineas de cada
data = file.read()
#print (data)
result = parser.parse(data)
#print ("RESULT: ")
#print (result) 