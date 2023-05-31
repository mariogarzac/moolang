import ply.lex as lex

tokens = (
    'MAIN',
    'ID',
    'VAR',
    'FUNC',
    'RETURN',
    'WHILE',
    'FOR',
    # 'IN',
    # 'RANGE',
    'IF',
    'ELSE',
    'PRINT',
    'AND',
    'OR',
    'INT',
    'FLOAT',
    'VOID',
    'FILE',
    'INPUT',
    'GENERATE_KEY',
    'HASH_SHA256',
    'HASH_MD5',
    'OPEN',
    'WRITE',
    'CLOSE',
    'ENCRYPT',
    'DECRYPT',
    'EQUAL',
    'CTE_INT',
    'CTE_FLOAT',
    'CTE_CHAR',
    'SEMICOL',
    'LPAREN',
    'RPAREN',
    'COMMA',
    'CHAR',
    'LCURLY',
    'RCURLY',
    'LBRACKET',
    'RBRACKET',
    'ARROW',
    'GT',
    'LT',
    'GE',
    'LE',
    'EQ',
    'NE',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
)

reserved = {
    'main' : 'MAIN',
    'var' : 'VAR',
    'func' : 'FUNC',
    'return' : 'RETURN',
    'while' : 'WHILE',
    'for' : 'FOR',
    # 'in' : 'IN',
    # 'range' : 'RANGE',
    'if' : 'IF',
    'else' : 'ELSE',
    'print' : 'PRINT',
    'input' : 'INPUT',
    'and' : 'AND',
    'or' : 'OR',
    'int' : 'INT',
    'float' : 'FLOAT',
    'char' : 'CHAR',
    'void' : 'VOID',
    'file' : 'FILE',
    'open' : 'OPEN',
    'write' : 'WRITE',
    'close' : 'CLOSE',
    'hash_sha256' : 'HASH_SHA256',
    'hash_md5' : 'HASH_MD5',
    'generate_key' : 'GENERATE_KEY',
    'encrypt' : 'ENCRYPT',
    'decrypt' : 'DECRYPT',
    '-gt' : 'GT',
    '-ge' : 'GE',
    '-lt' : 'LT',
    '-le' : 'LE',
    '-eq' : 'EQ',
    '-ne' : 'NE',
        }


t_LPAREN =  r'\('
t_RPAREN =  r'\)'
t_LBRACKET=  r'\['
t_RBRACKET =  r'\]'
t_LCURLY=  r'\{'
t_RCURLY =  r'\}'
t_ARROW = r'->'
t_COMMA =  r','
t_SEMICOL =  r';'
t_CTE_CHAR = r'"[\w\d\s!?_\.:-]*"'
t_GT = r'-gt'
t_GE = r'-ge'
t_LT = r'-lt'
t_LE = r'-le'
t_EQ = r'-eq'
t_NE = r'-ne'
t_EQUAL =  r'='
t_PLUS =  r'\+'
t_MINUS =  r'-'
t_TIMES =  r'\*'
t_DIVIDE =  r'/'
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

def t_COMMENT(t):
    r'\#.*'
    pass
    # No return value. Token discarded

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

# with open('Tests/simple.moo', 'r') as file:
#     data = file.read()
#
# lexer.input(data)
# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print(tok)
#
