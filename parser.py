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
import ply.yacc as yacc
#precedencia

precedence = (
  ('right','TkItoi'),
  ('right','TkPrintln','TkPrint'),
  ('right', 'TkRead' ),
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

def p_programa(p):
    """
    PROGRAMA : TkProgram SECUENCIACION
    """
    # p[0] = programa(p[1])
    print ("programa")

def p_bloque(p):
    """
    BLOQUE : TkBegin SECUENCIACION TkEnd TkSemicolon
           | TkBegin VACIO TkEnd TkSemicolon
           | TkBegin SECUENCIACION TkEnd VACIO
           | TkBegin TkDeclare DECL_VAR SECUENCIACION TkEnd TkSemicolon
           | TkBegin TkDeclare DECL_VAR SECUENCIACION TkEnd VACIO 
    """
    #if len(p) >= 4:
        #p[0] = bloque([p[3],p[4]])
    #else:
        #p[0] = bloque([p[]])
    print ("bloque")

def p_instruccion(p):
    """
    INSTRUCCION : BLOQUE
                | ASIGNACION TkSemicolon
                | ASIGNACION VACIO
                | ENTRADA TkSemicolon
                | ENTRADA VACIO
                | SALIDA TkSemicolon
                | SALIDA VACIO
                | CONVERTIR
                | CONDICIONAL_IF
                | CONDICIONAL_CASE
                | ITERACION_FOR
                | ITERACION_WHILE
                | POST
                | VACIO
    """
    #if  len(p) == 2:
        #p[0] = instruccion([p[1]])
    #else
        #p[0] = instruccion([p[1],p[2]])
    print ("instruccion")

def p_secuenciacion(p):
    '''
    SECUENCIACION : INSTRUCCION 
                  | INSTRUCCION  SECUENCIACION 
    ''' 
    #if (len(p) == 3 ): 
    #    p[0] = secuenciacion([p[1],p[3]])
    #else :
    #    p[0] = secuenciacion([p[1]])
    print ("secuencia")

def p_identificador(p):
    '''
    IDENTIFICADOR : TkId
    '''
    #p[0] = p[1]
    print ("identificador")
    print (p[1])

def p_asignacion(p):
    """
    ASIGNACION : EXPRESION TkAsig EXPRESION
    """
    #p[0] = asignacion([p[1],p[3]])
    print ("Asignacion")


def p_entrada(p):
    """
    ENTRADA : TkRead IDENTIFICADOR
    """
    #p[0] = entrada([p[2]])

    print ("entrada")

def p_salida(p):
    """
    SALIDA : TkPrint LISTA_VAR
           | TkPrintln LISTA_VAR
           | TkPrint CADENA
           | TkPrintln CADENA
    """
    #p[0] = salida([p[2]])
    print ("salida")

def p_cadena(p):
    """
    CADENA : TkString
    """
    #p[0] = cadena([p[1]])
    print ("string")

def p_condicional_if(p):
    """
    CONDICIONAL_IF : TkIf EXP_BOOL TkThen SECUENCIACION TkElse SECUENCIACION
              | TkIf EXP_BOOL TkThen SECUENCIACION
    """
    #if len (p) == 7:
        #p[0] = condicional_if([p[2],p[4],p[6]])
    #else:
        #p[0] = condicional_if([p[2],p[4]])
    print ("if")

def p_condicional_case(p):
    """
    CONDICIONAL_CASE : TkCase EXPRESION TkOf LISTA_CASE TkEnd
                     | TkCase EXPRESION TkOf LISTA_CASE TkEnd TkSemicolon                    
    """

    #p[0] = condicional_case([p[2],p[4]])
    print ("case")

def p_lista_case(p):
    """
    LISTA_CASE : EXPRESION TkArrow SECUENCIACION
               | EXPRESION TkArrow SECUENCIACION LISTA_CASE
    """
    #if len(p) == 4:
        #p[0] = lista_case([p[1],p[3]])
    #else
        #p[0] = lista_case([p[1],p[3],p[4]])
    print ("lista case")

def p_iteracion_for(p):
    """
    ITERACION_FOR : TkFor IDENTIFICADOR TkIn EXPRESION TkDo SECUENCIACION
    """
    #p[0] = iteracion_for([p[2],p[4],p[6]])
    print ("for")

def p_iteracion_while(p):
    """
    ITERACION_WHILE : TkWhile EXP_BOOL TkDo SECUENCIACION
    """
    #p[0] = iteracion_while([p[2],p[4]])
    print ("while")

def p_declaracion_var(p):
    """
    DECL_VAR : LISTA_VAR TkAs LISTA_TIPO TkSemicolon DECL_VAR
             | LISTA_VAR TkAs LISTA_TIPO
    """
    #p[0] = lista_var([p[1],p[3]])
    print ("declaracion")

def p_lista_var(p):
    """
    LISTA_VAR : IDENTIFICADOR
              | IDENTIFICADOR TkComma LISTA_VAR
    """
    #if len(p) == 2:
        #p[0] = lista_var([p[1]])
    #else
        #p[0] = lista_var([p[1],p[3]])

    print ("lista var")

def p_lista_tipo(p):
    """
    LISTA_TIPO : DATO
              | DATO TkComma LISTA_TIPO
    """
    #if len(p) == 2:
        #p[0] = lista_dato([p[1]])
    #else
        #p[0] = lista_dato([p[1],p[3]])
    print ("lista dato")

def p_dato(p):
    """
    DATO : TkInt
         | TkBool
         | TkInter
    """
    #p[0] = dato([p[1]])
    print ("dato")

def p_expresion(p):
    """
    EXPRESION : TkNum
              | IDENTIFICADOR
              | EXP_ENTEROS
              | EXP_INTERVALOS
              | EXP_BOOL
              | TkOpenPar EXPRESION TkClosePar
    """
    #if len(p) == 4:
        #p[0] = expresion([p[2]])
    #else
        #p[0] = expresion([p[1]])
    print ("expresion")

def p_exp_enteros(p):
    """
    EXP_ENTEROS : EXPRESION TkMod EXPRESION
                | EXPRESION TkMult EXPRESION
                | EXPRESION TkDiv EXPRESION
                | EXPRESION TkPlus EXPRESION
                | EXPRESION TkMinus EXPRESION %prec UMINUS
    """

    #if len(p) == 6:
    #    p[0] = exp_entero([-p[1]])
    #else:
        #if p[2] == '+':
        #    p[0] = exp_entero([p[1], p[3]])
        #elif p[2] == '-':
        #    p[0] = exp_entero([p[1], p[3]])
        #elif p[2] == '*':
        #    p[0] = exp_entero([p[1], p[3]])
        #elif p[2] == '/':
        #    p[0] = exp_entero([p[1], p[3]])
        #elif p[2] == '%':
        #    p[0] = exp_entero([p[1], p[3]]) 
    print ("exp_entero")

def p_exp_intervalo(p):
    """
    EXP_INTERVALOS : EXPRESION TkSoForth EXPRESION
                  | EXPRESION TkCap EXPRESION
    """
    #p[0] = exp_intervalo([p[1],p[3]])
    print ("exp_intervalo")

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

#   if len(p) == 2:
#       p[0] = exp_bool([p[1]])
#   elif len(p) == 3:
#       p[0] = exp_bool([p[2]]) revisar#
#   else:
#       if p[2] == '<':
 #          p[0] = exp_bool([p[1], p[3]])
 #      elif p[2] == '>':
 #          p[0] = exp_bool([p[1], p[3]])
 #      elif p[2] == '<=':
 #          p[0] = exp_bool([p[1], p[3]])
 #      elif p[2] == '>=':
 #          p[0] = exp_bool([p[1], p[3]])
 #      elif p[2] == '=':
 #          p[0] = exp_bool([p[1], p[3]])
 #      elif p[2] == '/=':
 #          p[0] = exp_bool([p[1], p[3]])
    print ("exp bool")

def p_convertir(p):
    """
    CONVERTIR : TkItoi TkOpenPar IDENTIFICADOR TkClosePar
              | TkLen TkOpenPar IDENTIFICADOR TkClosePar
              | TkMax TkOpenPar IDENTIFICADOR TkClosePar
              | TkMin TkOpenPar IDENTIFICADOR TkClosePar
    """
    #p[0] = convertir([p[3]])
    print ("convertir")

def p_postcondicion(p):
    """
    POST : TkOpenBra TkPost TkTwoPoints EXP_CUANTIFICADOR TkCloseBra
    """ 
    #p[0] = post([p[4]])

    print ("post")

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
    #p[0] = None
    print ("Vacio")

def p_error(p):
    print("Se ha encontrado un error",p)
    print("Error en la linea " + str(p.lineno))



parser = yacc.yacc('SLR')
#abrimos la ruta pasada por argumento
filepath = argv[1]
#Abrimos el contenido del la ruta
file = open(filepath, 'r')
#Guardamos las lineas de cada
data = file.read()
print (data)
parser.parse(data)