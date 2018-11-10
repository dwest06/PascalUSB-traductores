#! /usr/bin/python

# UNIVERSIDAD SIMON BOLIVAR
# TRADUCTORES E INTERPRETADORES
# Entrega de FASE 2: PARSER del lenguaje BasicTran
# Autores:
#   -Yezabel Rincon 10-11005
#   -Javier Medina 12-10400

import ply.yacc as yacc
from fase1 import tokens  #Se importan los tokens en el lexer
import re
import codecs
import os
import sys

######################################################
#             Definicion  de la Gramatica            #
######################################################

# Precendencia de operadores en el lenguaje BasicTran
precedence = (
  ('left', 'TkConjuncion'),
  ('left', 'TkDisyuncion'),
  ('right', 'TkNegacion'),
  ('nonassoc', 'TkIgual', 'TkDesigual'),
  ('nonassoc', 'TkMayor', 'TkMenor', 'TkMenorIgual', 'TkMayorIgual'),
  ('left', 'TkSuma', 'TkResta'),
  ('left', 'TkMult', 'TkDiv', 'TkMod'),
  ('left', 'TkConcatenacion'),
)

# Regla gramatical para un programa en BasicTran
def p_programa(p):
    '''
    PROGRAMA : DECLARACION_VARIABLES BLOQUE
             | BLOQUE
    '''
    if (len(p) == 3 ):
      p[0] = ("PROGRAMA", p[1],p[2])
    else :
      p[0] = ("PROGRAMA", p[1])
    
# Regla gramatical para bloque de un programa en BasicTran
def p_bloque(p):
    '''
    BLOQUE : TkBegin SECUENCIACION TkEnd
           | TkBegin VACIO TkEnd
           | TkBegin BLOQUE TkEnd
    '''
    p[0] = ("BLOQUE", p[2])
    

# Regla gramatical para declaracion de variables
def p_declaracion_variables(p):
    '''
    DECLARACION_VARIABLES : TkWith LISTA_DECLARACIONES TkDosPuntos TIPO
    '''
    p[0] = ("DECLARACION", p[2],p[4])

# Regla gramatical para lista de declaraciones
def p_lista_declaraciones(p):
    '''
    LISTA_DECLARACIONES : TkVar LISTA_IDENTIFICADORES TkComa LISTA_ASIGNACIONES
                        | TkVar LISTA_ASIGNACIONES TkComa LISTA_IDENTIFICADORES
                        | TkVar LISTA_IDENTIFICADORES
                        | TkVar LISTA_ASIGNACIONES
    '''
    if (len(p) == 5 ):
      p[0] = ("DECLARACION",p[2],p[4])
    else : 
      p[0] =  p[2]

# Regla gramatical para identificador
def p_identificador(p):
    '''
    IDENTIFICADOR : TkId
    '''
    p[0] = p[1]

# Regla gramatical para lista de identificadores
def p_lista_identificadores(p):
    '''
    LISTA_IDENTIFICADORES : IDENTIFICADOR
                          | IDENTIFICADOR TkComa LISTA_IDENTIFICADORES
    '''
    if (len(p) == 2 ):
      p[0] = ("ID", p[1])  
    else :
      p[0] = ("ID", p[1], p[3])



# Regla gramatical para asignacion
def p_asignacion(p):
    '''
    ASIGNACION : EXPRESION TkAsignacion EXPRESION
    '''
    p[0] = ("ASIGNACION\n", p[1], p[3])

# Regla gramatical para listas de asignaciones
def p_lista_asignaciones(p):
    '''
    LISTA_ASIGNACIONES : ASIGNACION
                       | ASIGNACION TkComa  LISTA_ASIGNACIONES
    '''
    if (len(p) == 3 ):
      p[0] = p[1]
    else :
      p[0] = ("ASIGNACION\n",p[1], p[3])


# Regla gramatical para expresiones
def p_expresion(p):
    '''
    EXPRESION : TkParAbre EXP_REL TkParCierra 
              | TkParAbre EXP_ARIT TkParCierra 
              | TkParAbre EXP_BOOL TkParCierra
              | TkParAbre EXP_CAR TkParCierra 
              | TkParAbre EXP_ARR TkParCierra 
              | TkParAbre IDENTIFICADOR TkParCierra
              | TkParAbre LITERAL TkParCierra
              | EXP_ARIT 
              | EXP_REL 
              | EXP_BOOL 
              | EXP_CAR 
              | EXP_ARR 
              | IDENTIFICADOR 
              | LITERAL
    '''
    if len(p) == 4:
      p[0] = ("EXPRESION",p[2])
    else:
      p[0] = ("EXPRESION",p[1])

# Regla gramatical para terminos validos en BasicTran
def p_termino(p):
    '''
    TERMINO : LITERAL
            | IDENTIFICADOR
            | EXP_ARIT
    ''' 
    p[0] = ("TERMINO", p[1])

# Regla gramatical para literales
def p_literal(p):
    '''
    LITERAL : TkNum
            | TkCaracter
            | TkSaltoLinea
            | TkTab
            | TkComillaSimple
            | TkBarraInversa
    '''
    p[0] = ("LITERAL", p[1])

# Regla gramatical para expresiones aritmeticas
def p_exp_arit(p):
    '''
    EXP_ARIT : EXPRESION TkMult EXPRESION
             | EXPRESION TkDiv EXPRESION
             | EXPRESION TkSuma EXPRESION
             | EXPRESION TkResta EXPRESION
             | EXPRESION TkMod EXPRESION
    '''
    #FALTA MENOS UNARIO
    if len(p) == 2:
        p[0] = p[1]
    else:
        if p[2] == '+':
            p[0] = ("SUMA", p[1], p[3])
        elif p[2] == '-':
            p[0] = ("RESTA", p[1], p[3])
        elif p[2] == '*':
            p[0] = ("MULTIPLICACION", p[1], p[3])
        elif p[2] == '/':
            p[0] = ("DIVISION", p[1], p[3])
        elif p[2] == '%':
            p[0] = ("MOD", p[1], p[3])

# Regla gramatical para expresiones booleanas
def p_exp_bool(p):
    '''
    EXP_BOOL : TkTrue
             | TkFalse
             | EXPRESION TkConjuncion EXPRESION
             | EXPRESION TkDisyuncion EXPRESION
             | TkNegacion EXPRESION
             | EXP_REL
    '''
    if len(p) == 2:
        p[0] = ("BOOL",p[1])
    elif len(p) == 4:
        if p[2] == "\/":
            p[0] = ("DISYUNCION" , p[1], p[3])
        else:
            p[0] = ("CONJUNCION" , p[1], p[3])


# Regla gramatical para expresiones con caracteres
def p_exp_car(p):
    '''
    EXP_CAR : TkSiguienteCar
            | TkAnteriorCar
            | TkValorAscci
    '''
    p[0] = ("EXPRESION CARACTER",p[2])

# Regla gramatical para expresiones con arreglos
def p_exp_arr(p):
    '''
    EXP_ARR : TkConcatenacion
            | TkShift
            | INDEXACION
    '''
    p[0] = ("EXPRESION ARREGLO",p[1])

# Regla gramatical para la indexacion
def p_indexacion(p):
    '''
    INDEXACION : TkCorcheteAbre TkInt TkCorcheteCierra
    '''
    p[0] = ("INDEXACION", p[2])

# Regla gramatical para expresiones relacionales
def p_exp_rel(p):
    '''
    EXP_REL : EXPRESION TkMenor EXPRESION
            | EXPRESION TkMayor EXPRESION
            | EXPRESION TkMenorIgual EXPRESION
            | EXPRESION TkMayorIgual EXPRESION
            | EXPRESION TkIgual EXPRESION
            | EXPRESION TkDesigual EXPRESION
    '''
    if p[2] == '<':
        p[0] = ("MENOR", p[1], p[3])
    elif p[2] == '>':
        p[0] = ("MAYOR", p[1], p[3])
    elif p[2] == '<=':
        p[0] = ("MENOR IGUAL", p[1], p[3])
    elif p[2] == '>=':
        p[0] = ("MAYOR IGUAL", p[1], p[3])
    elif p[2] == '=':
        p[0] = ("IGUAL", p[1], p[3])
    elif p[2] == '/=':
        p[0] = ("DIFERENTE", p[1], p[3])
    

# Regla gramatical para los tipos de datos
def p_tipo(p):
    '''
    TIPO : TkInt
         | TkBool
         | TkChar
         | ARREGLO
    '''
    p[0] = ("TIPO", p[1])


# Regla gramatical para los arreglos
def p_arreglo(p):
    '''
    ARREGLO : TkArray TkCorcheteAbre TkInt TkCorcheteCierra TkOf TIPO
    '''
    p[0] = ("ARREGLO",p[3],p[5],p[6])

# Regla gramatical para las diversas instrucciones validas en BasicTran
def p_instruccion(p):
    '''
    INSTRUCCION : ASIGNACION TkPuntoYComa
                | SECUENCIACION TkPuntoYComa
                | CONDICION
                | ITERACION_I
                | ITERACION_D
                | ENTRADA TkPuntoYComa
                | SALIDA TkPuntoYComa
    '''  
    p[0] = ("INSTRUCCION",p[1])

# Regla gramatical para instruccion de condicional
def p_condicion(p):
  '''
  CONDICION : TkIf EXPRESION TkHacer INSTRUCCION TkEnd
            | TkIf EXPRESION TkHacer INSTRUCCION TkOtherwise TkHacer INSTRUCCION TkEnd   
  '''
  if len(p) == 6:
    p[0] = ("IF",p[2],p[4])
  else:
    p[0] = ("IF",p[2],p[4],p[7])

# Regla gramatical para instruccion iteracion indeterminada
def p_iteracion_i(p):
  '''
  ITERACION_I : TkWhile EXP_BOOL TkHacer INSTRUCCION TkEnd
  '''
  p[0] = ("WHILE",p[2],p[4])


# Regla gramatical para instruccion iteracion determinada
def p_iteracion_d(p):
  '''
  ITERACION_D : TkFor IDENTIFICADOR TkFrom TERMINO TkTo TERMINO TkHacer INSTRUCCION TkEnd
              | TkFor IDENTIFICADOR TkFrom TERMINO TkTo TERMINO TkStep TERMINO TkHacer INSTRUCCION TkEnd
  '''
  if len(p) == 10:
    p[0] = ("For",p[2],p[4],p[6],p[8])
  else:
    p[0] = ("For",p[2],p[4],p[6],p[8], p[10])

# Regla gramatical para instruccion de salida (input)
def p_entrada(p):
  '''
  ENTRADA : TkRead IDENTIFICADOR 
  '''
  p[0] = ("Entrada",p[2])

# Regla gramatical para instruccion de salida (output)
def p_salida(p):
  '''
  SALIDA : TkPrint EXPRESION 
  '''
  p[0] = ("Salida",p[2])

# Regla gramatical para instruccion secuenciacion
def p_secuenciacion(p):
    '''
    SECUENCIACION : INSTRUCCION 
                  | INSTRUCCION  SECUENCIACION 
    ''' 
    if (len(p) == 4 ): 
        p[0] = ("SECUENCIACION", p[1],p[3])
    else :
        p[0] = ("SECUENCIACION", p[1])

# Regla para deteccion de errores de sintaxis
def p_error(p):
  print("Se ha encontrado un error")

# Regla para lambda
def p_vacio(p):
    '''
    VACIO : 
    '''
    p[0] = None

#############################################################################
# Metodo auxiliar para la impresion del arbol abstracto en formato solicitado
def listar (result,a):
  for n in result:
    if isinstance(n,tuple):
      listar(n,a)
    else:
      print( "{} {}".format(a ,n) )
      a=a+a
#############################################################################

# Construccion del Parser
parser = yacc.yacc()


############################################################################
#                                 MAIN                                     #
############################################################################
if __name__=="__main__":
  #Lectura del archivo de entrada
  file = open(sys.argv[1] , "r")
  file = file.read() 
  result = parser.parse(file)
  print("Impresion del parser: ")
  print(result)
  print(' \n' +"Impresion en formato solicitado:"+'\n')
  a = ' '
  listar(result,a)
