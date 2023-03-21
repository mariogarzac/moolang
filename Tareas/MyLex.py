# ----------------------------------
#
#           Mario Garza Chapa
#               A01720245
#
# ----------------------------------

import ply.lex as lex

tokens = (
   'PROGRAMA',
   'ID',
   'COLON',
   'SEMICOL',
   'COMMA',
   'LPAREN',
   'RPAREN',
   'LBRACKET',
   'RBRACKET',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'EQUAL',
   'GT',
   'LT',
   'NOT',
   'CTE_INT',
   'CTE_FLOAT',
   'CTE_STRING',
   'VAR',
   'PRINT',
   'IF',
   'ELSE',
   'FLOAT',
   'INT',
)

reserved = {
   'programa' : 'PROGRAMA',
   'var' : 'VAR',
   'print' : 'PRINT',
   'if' : 'IF',
   'else' : 'ELSE',
   'float' : 'FLOAT',
   'int' : 'INT',
        }

t_LPAREN =  r'\('
t_RPAREN =  r'\)'
t_LBRACKET=  r'\{'
t_RBRACKET =  r'\}'
t_EQUAL =  r'='
t_PLUS =  r'\+'
t_MINUS =  r'-'
t_TIMES =  r'\*'
t_DIVIDE =  r'/'
t_GT = r'<'
t_LT = r'>'
t_NOT = r'<>'
t_COMMA =  r','
t_COLON =  r':'
t_SEMICOL =  r';'
t_CTE_STRING = r'"[\w\d\s!?_\.]*"'
t_ignore  = ' \t'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_CTE_FLOAT(t):
    r'[0-9]+\.[0-9]+'
    t.value = float(t.value)
    return t

def t_CTE_INT(t):
    r'\d+'
    t.value = int(t.value)    
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

with open('programa.txt', 'r') as file:
    data = file.read()

lexer = lex.lex()

lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)

