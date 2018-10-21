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

#Palabras reservadas del lenguaje

reserved = {
    #Generales del lenguaje
    'program' : 'TkProgram',
    'begin' : 'TkBegin',
    'end' : 'TkEnd',
    'declare' : 'TkDeclare',
    'as' : 'TkAs',

    #Tipos de datos
    'int' : 'TkInt',
    'bool' : 'TkBool',
    'inter' : 'TkInter',

    #Condicionales
    'if' : 'TkIf',
    'else' : 'TkElse',
    'then' : 'TkThen',
    'case' : 'TkCase',

    #Iteraciones
    'for' : 'TkFor',
    'while' : 'TkWhile',

    #Auxiliares de Codicionales e iteraciones
    'do' : 'TkDo',
    'of' : 'TkOf',

    #Entrada y salida
    'read' : 'TkRead',
    'print' : 'TkPrint',
    'println' : 'TkPrintln',

    #funciones de conversión de tipos y embebidas
    'itoi' : 'TkItoi',
    'len' : 'TkLen',
    'max' : 'TkMax',
    'min' : 'TkMin',

    #Postcondicion
    'Post' : 'TkPost',
    'forall' : 'TkForall',
    'exists' : 'TkExists',

    #Operadores
    'or' : 'TkOr',
    'and' : 'TkAnd',
    'not' : 'TkNot',
    'in' : 'TkIn',
}

#Lista de tokens del lenguaje
tokens = [
    #Para las variables
    'TkId',

    #Para los numero enteros
    'TkNum',

    #Para los valores Booleanos
    'TkTrue',
    'TkFalse',

    #Para las cadenas de caracteres encerradas entre comillas
    'TkString',


    #Separadores
    'TkComma',      # ','
    'TkPoint',      # '.'
    'TkOpenPar',    # '('
    'TkClosePar',   # ')'
    'TkOpenBra',    # '{'
    'TkCloseBra',   # '}'
    'TkTwoPoints',  # ':'
    'TkPipe',       # '|'
    'TkAsig',       # ':='
    'TkSemicolon',  # ';'
    'TkArrow',      # '==>'


    #Operadores Aritmeticos, booleanos, relacionales o de intervalos
    'TkPlus',       # '+'
    'TkMinus',      # '-'
    'TkMult',       # '*'
    'TkDiv',        # '/'
    'TkMod',        # '%'
    'TkSoForth',    # '..'
    'TkCap',        # '<>'
    'TkLess',       # '<'
    'TkLeq',        # '<='
    'TkGeq',        # '>='
    'TkGreater',    # '>'
    'TkEqual',      # '=='
    'TkNEqual',     # '/='

    #Comentarios
    'TkComment',    # '//'

] + list(reserved.values())

#Reglas de expresiones regulares de cada token. Especificaciones de cada token
t_TkComma = r'\,'
t_TkPoint = r'\.'
t_TkOpenPar = r'\('
t_TkClosePar = r'\)'
t_TkOpenBra = r'{'
t_TkCloseBra = r'}'
t_TkTwoPoints = r':'
t_TkPipe = r'\|'
t_TkAsig = r':='
t_TkSemicolon = r';'
t_TkArrow = r'==>'

t_TkPlus = r'\+'
t_TkMinus = r'\-'
t_TkMult = r'\*'
t_TkDiv = r'\/'
t_TkMod = r'\%'
t_TkSoForth = r'\..'
t_TkCap = r'<>'
t_TkLess = r'<'
t_TkLeq = r'<='
t_TkGeq = r'>='
t_TkGreater = r'>'
t_TkEqual = r'=='
t_TkNEqual = r'/='

#Ignoramos cuando se encuentre un comentario
t_ignore_TkComment = r'//(.)*'

#Reglas ignoradas
t_ignore = r' \t'


#Funciones para las variables, numeros, string, etc

# Regla de expresion regular para los numeros
def t_TkNum(number):
    r'\d+'
    number.value = int(number.value)
    return number


#Regla de expresion regular para las variables
def t_TkId(identificador):
    r'[a-zA-Z]+[a-zA-Z0-9_]+'
    print("El identificador es", identificador)
    identificador.type = reserved.get(identificador.value, 'TkId')
    return identificador


#Funcion para saber la linea del token
def t_newline(line):
    r'\n+'
    line.lexer.lineno += len(line.value)


#Funcion por "default" cuando encuentra un token que no pertenece a la lista de tokens
def t_error(invalido):
    print("Caracter" + str(invalido.value) + "invalido. Linea " + 
        str(invalido.lineno) + " y columna " + str(invalido.lexpos))
    invalido.lexer.skip(1)


#Inicializamos el lexer
lexer = lex.lex()



def main():
    """Main"""

    #Verificamos si se paso el argumento correctamente
    if len(sys.argv) < 2 :
        print("Uso del programa: python3 lexer.py <Nombre del archivo>.")
        return 0

    #abrimos la ruta pasada por argumento
    filepath = sys.argv[1]

    #Guardamos la extension del archivo
    ext = filepath.split('.')

    #Verificamos si la extension es la correcta
    if ext[1] != 'pusb':
        print("Error al leer el archivo: Extension incorrecta.")
        return 0

    #Abrimos el contenido del la ruta 
    file = open(filepath, 'r')
    data = file.read()

    lexer.input(data)

    #Iteramos sobre el la entrada para extraer los tokens
    for tok in lexer:
        print(tok.type, tok.value, tok.lineno, tok.lexpos)


if __name__ == '__main__':
    main()
    