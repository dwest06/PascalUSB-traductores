"""
	Analizador Lexicografico del Lenguaje PascalUSB

	Primera fase del proyecto

	Traductores e Interpretadores (CI-3725)
	David Rodríguez (14-10930)
	Javier Medina ()

	Septiembre - Diciembre 2018


"""


import ply.lex as lex
import sys

reservadas = {
	'program' : 'TkProgram',
	'begin' : 'TkBegin',
	'declare' : 'TkDeclare',
	'as' : 'TkAs',

}



if __name__ == '__main__':
	main()