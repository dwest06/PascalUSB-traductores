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
    ('right', 'TkProgram')
)

#La gramatica empieza por p_qc
start = 'qc'


def p_qc(p):
    """
    INICIO : PROGRAMA
    """
    p[0] = ("INICIO", p[1])

def p_programa(p):
    """
    PROGRAMA : TkProgram BLOQUE
    """
    p[0] = ("PROGRAM", p[2])
    print ("program")
    
def p_bloque(p):
    """
    BLOQUE : TkBegin TkEnd
           | TkBegin SECUENCIACION TkEnd
           | TkBegin TkDeclare DECL_VAR SECUENCIACION TkEnd
    """
    if len(p) == 4:
        p[0] = ("BLOQUE", p[2], p[3])
    elif len(p) == 3:
        p[0] = ("BLOQUE", p[2])
    else: 
        p[0] = ("BLOQUE")
    print("bloque")

def p_secuenciacion(p):
    '''
    SECUENCIACION : INSTRUCCION 
                  | INSTRUCCION TkSemicolon SECUENCIACION 
    ''' 
    
    if len(p) == 3: 
       p[0] = ("SECUENCIACION", [p[1],p[3]])
    else:
       p[0] = ("SECUENCIACION", [p[1]])
    
    print("secuenciacion")
    

def p_declaracion_var(p):
    """
    DECL_VAR : VARIABLES TkAs TIPOS TkSemiColon DECL_VAR
             | VARIABLES TkAs TIPOS
    """
    #p[0] = lista_var([p[1],p[3]])
    if len(p) == 6:
        p[0] = ("DECLARACION", p[1], p[3], p[5])
    else:
        p[0] = ("DECLARACION", p[1], p[3])

    print("declaracion")

def p_tipos(p):
    """
    TIPOS : TIPO TkComma TIPOS
          | TIPO
    """
    if len(p) == 4:
        p[0] = ("TIPOS", p[1], p[3])
    else:
        p[0] = ("TIPOS", p[1])

    print("tipos")

def p_tipo(p):
    """
    TIPO : TkInt
         | TkBool
         | TkInter
    """
    p[0] = ("TIPO", p[1])
    print("tipo", p[1])

def p_variables(p):
    """
    VARIABLES : ID TkComma VARIABLES
              | ID
    """
    if len(p) == 4:
        p[0] = ("VARIABLES", p[1], p[3])
    else:
        p[0] = ("VARIABLES", p[1])
    print("variables")


def p_instruccion(p):
    """
    INSTRUCCION : IO
                | VARIABLES TkAsig EXPRESION 
                | CONDICIONAL
                | ITERACION
                | BLOQUE
                | POSTCOND
    """
    if  len(p) == 2:
        p[0] = ("INSTRUCCION", p[1])
    else:
        p[0] = ("INSTRUCCION", p[1], p[3])

    print("instruccion ")

def p_identificador(p):
    '''
    ID : TkId
    '''
    p[0] = ("ID", p[1])
    print("identificador")
    print(p[1])


def p_io(p):
    """
    IO : read ID
       | read EXPRESION soFarth EXPRESION
       | print VARIABLES
       | println VARIABLES
    """
    if len(p) == 5:
        p[0] = ("IO", p[2], p[4])
    else:
        p[0] = ("IO", p[2])

    print("IO")

def p_cadena(p):
    """
    CADENA : TkString
    """

    p[0] = ("STRING", p[1])

    print ("string", p[1])

def p_condicional(p):
    """
    CONDICIONAL : TkIf EXP_BOOL TkThen SECUENCIACION TkElse SECUENCIACION
                | TkIf EXP_BOOL TkThen SECUENCIACION
                | TkCase EXPRESION TkOf LISTA_CASE TkEnd
    """
    if len(p) == 7:
        p[0] = ("CONDICIONAL", p[2], p[4], p[6])
    else:
        p[0] = ("CONDICIONAL", p[2], p[4])

    print("codicional")


def p_lista_case(p):
    """
    LISTA_CASE : EXPRESION TkArrow SECUENCIACION
               | EXPRESION TkArrow SECUENCIACION LISTA_CASE
    """
    if len(p) == 4:
        p[0] = ("LISTA_CASE", p[1], p[3])
    else:
        p[0] = ("LISTA_CASE", p[1], p[3], p[4])
    print ("lista case")

def p_iteracion_for(p):
    """
    ITERACION_FOR : TkFor IDENTIFICADOR TkIn EXPRESION TkDo SECUENCIACION
                  | TkWhile EXPRESION TkDo SECUENCIACION 
                  | 
    """
    p[0] = ("ITERACION", p[2], p[4], p[6])

def p_expresion(p):
    """
    EXPRESION : ID
              | EXP_ENTEROS
              | EXP_INTERVALOS
              | EXP_BOOL
              | TkOpenPar EXPRESION TkClosePar
    """
    if len(p) == 4:
        p[0] = ("EXPRESION", p[2])
    else:
        p[0] = ("EXPRESION", p[1])
    print ("expresion")

def p_exp_enteros(p):
    """
    EXP_ENTEROS : EXPRESION TkMod EXPRESION
                | EXPRESION TkMult EXPRESION
                | EXPRESION TkDiv EXPRESION
                | EXPRESION TkPlus EXPRESION
                | EXPRESION TkMinus EXPRESION %prec UMINUS
                | TkNum
    """

    if len(p) == 6:
        p[0] = ("EXP_ENTERO", -p[1])
    else:
        if p[2] == '+':
            p[0] = ("EXP_ENTERO", p[1], p[3])
        elif p[2] == '-':
            p[0] = ("EXP_ENTERO", p[1], p[3])
        elif p[2] == '*':
            p[0] = ("EXP_ENTERO", p[1], p[3])
        elif p[2] == '/':
            p[0] = ("EXP_ENTERO", p[1], p[3])
        elif p[2] == '%':
            p[0] = ("EXP_ENTERO", p[1], p[3])

    print("exp_entero")

def p_exp_intervalo(p):
    """
    EXP_INTERVALO : EXPRESION soFarth EXPRESION
                  | EXPRESION suma EXPRESION
                  | EXPRESION inter EXPRESION
                  | EXPRESION escala EXPRESION
    """

    #########################
    #
    # AQUI NO SE QUE HACER SEGUN LOS OPERADORES
    #
    #########################
    p[0] = ("EXP_INTERVALO", p[1], p[3])
    print("exp_intervalo")

def p_exp_bool(p):
    """
    EXP_BOOL : TkTrue
             | TkFalse
             | TkNot EXP_BOOL
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

    if len(p) == 2:
        p[0] = ("EXP_BOOL", p[1])
    elif len(p) == 3:
        p[0] = ("EXP_BOOL", p[2])
    else:
        if p[2] == '<':
            p[0] = ("EXP_BOOL", p[1], p[3])
        elif p[2] == '>':
            p[0] = ("EXP_BOOL", p[1], p[3])
        elif p[2] == '<=':
            p[0] = ("EXP_BOOL", p[1], p[3])
        elif p[2] == '>=':
            p[0] = ("EXP_BOOL", p[1], p[3])
        elif p[2] == '=':
            p[0] = ("EXP_BOOL", p[1], p[3])
        elif p[2] == '/=':
            p[0] = ("EXP_BOOL", p[1], p[3])

    print("exp bool")


################################################

def p_convertir(p):
    """
    CONVERTIR : TkItoi TkOpenPar IDENTIFICADOR TkClosePar
              | TkLen TkOpenPar IDENTIFICADOR TkClosePar
              | TkMax TkOpenPar IDENTIFICADOR TkClosePar
              | TkMin TkOpenPar IDENTIFICADOR TkClosePar
    """
    #p[0] = convertir([p[3]])
    print("convertir")

def p_postcondicion(p):
    """
    POST : TkOpenBra TkPost TkTwoPoints EXP_CUANTIFICADOR TkCloseBra
    """
    #p[0] = post([p[4]])

    print("post")

def p_exp_cuantificador_forall(p):
    """
    EXP_CUANTIFICADOR : TkOpenPar TkForall IDENTIFICADOR TkPipe IDENTIFICADOR TkIn IDENTIFICADOR TkTwoPoints EXP_CUANTIFICADOR TkClosePar
                      | TkOpenPar TkForall IDENTIFICADOR TkPipe IDENTIFICADOR TkIn IDENTIFICADOR TkTwoPoints EXP_BOOL TkClosePar
    """ 
    #p[0] = exp_cuantificador([p[3],p[5],p[7],p[9]])

    print ("forall")

def p_exp_cuantificador_exist(p):
    """
    EXP_CUANTIFICADOR : TkOpenPar TkExists IDENTIFICADOR TkPipe IDENTIFICADOR TkIn IDENTIFICADOR TkTwoPoints EXP_CUANTIFICADOR TkClosePar
                      | TkOpenPar TkExists IDENTIFICADOR TkPipe IDENTIFICADOR TkIn IDENTIFICADOR TkTwoPoints EXP_BOOL TkClosePar
    """ 
    #p[0] = exp_cuantificador([p[3],p[5],p[7],p[9]])

    print ("exists")

def p_vacio(p):
    '''
    VACIO : 
    '''
    pass

def p_error(p):
    print("Se ha encontrado un error",p)
    print("Error en la linea " + str(p.lineno))



parser = yacc.yacc()
#abrimos la ruta pasada por argumento
#filepath = argv[1]
#Abrimos el contenido del la ruta
#file = open(filepath, 'r')
#Guardamos las lineas de cada
#data = file.read()
#print (data)
result = parser.parse(tokens)
#print ("RESULT: ")
#print (result)