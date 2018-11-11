"""
    Analizador Sintactico del Lenguaje PascalUSB

    Segunda fase del proyecto

    Traductores e Interpretadores (CI-3725)
    David Rodríguez (14-10930)
    Javier Medina (12-10400)

    Septiembre - Diciembre 2018
"""

from sys import argv
from lexer import TOKENS_VALIDOS

#precedencia


def p_programa(p):
	"""
	PROGRAMA : INSTRUCCION
	"""
	# p[0] = programa(p[1])
	print "programa"

def p_instruccion(p):
	"""
	INSTRUCCION : BLOQUE
				| ASIGNACION TkSemicolon
				| ASIGNACION
				| ENTRADA TkSemicolon
				| ENTRADA
				| SALIDA TkSemicolon
				| SALIDA
				| CONDICIONAL_IF
				| CONDICIONAL_CASE
				| ITERACION
				| INSTRUCCION INSTRUCCION
	"""
	#if  len(p) == 2:
		#p[0] = instruccion([p[1]])
	#else
		#p[0] = instruccion([p[1],p[2]])
	print "instruccion"

def p_bloque(p):
	"""
	BLOQUE : TkBegin INSTRUCCION TkEnd TkSemicolon
		   | TkBegin DECL_VAR INSTRUCCION TkEnd TkSemicolon
		   | TkBegin empty TkEnd TkSemicolon
		   | TkBegin INSTRUCCION TkEnd 
		   | TkBegin DECL_VAR INSTRUCCION TkEnd 
		   | TkBegin empty TkEnd 
	"""
	#if len(p) >= 4:
		#p[0] = bloque([p[2],p[3]])
	#else:
		#p[0] = bloque([p[12]])
	print "bloque"	

def p_identificador(p):
    '''
    IDENTIFICADOR : TkId
    '''
    #p[0] = p[1]
    print "identificador"

def p_asignacion(p):
	"""
	ASIGNACION : EXPRESION TkAsig EXPRESION
	"""
	#p[0] = asignacion([p[1],p[3]])
	print "Asignacion"

def p_entrada(p):
	"""
	ENTRADA : TkRead IDENTIFICADOR
	"""
	#p[0] = entrada([p[2]])

	print "entrada"

def p_salida(p):
	"""
	salida : TkPrint LISTA_VAR
		   | TkPrintln LISTA_VAR
	"""
	#p[0] = salida([p[2]])
	print "salida"

def p_condicional_if(p):
	"""
	CONDICIONAL_IF : TkIf EXPBOOL TkThen INSTRUCCION TkElse INSTRUCCION
			  | TkIf EXPBOOL TkThen INSTRUCCION
	"""
	#if len (p) == 7:
		#p[0] = condicional_if([p[2],p[4],p[6]])
	#else:
		#p[0] = condicional_if([p[2],p[4]])
	print "if"

def p_condicional_case(p):
	"""
	CONDICIONAL_CASE : TkCase EXPRESION TkOf LISTA_CASE TkEnd
					 | TkCase EXPRESION TkOf LISTA_CASE TkEnd TkSemicolon					 
	"""

	#p[0] = condicional_case([p[2],p[4]])
	print "case"

def p_lista_case(p):
	"""
	LISTA_CASE : EXPRESION TkArrow INSTRUCCION
			   | EXPRESION TkArrow INSTRUCCION LISTA_CASE
	"""
	