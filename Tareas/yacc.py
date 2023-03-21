# ----------------------------------
#
#           Mario Garza Chapa
#               A01720245
#
# ----------------------------------

import ply.yacc as yacc
from MyLex import tokens 

# program start
def p_prog(p):
   '''
    prog :  PROGRAM ID SEMICOL prog_prime bloque
   '''

def p_prog_prime(p):
    '''
    prog_prime  : vars
                | empty
    '''

# define variables
def p_vars(p):
    '''
    vars : VAR ID vars_prime COLON tipo SEMICOL vars_doubleprime 
    '''

def p_vars_prime(p):
    '''
    vars_prime  : COMMA ID vars_prime
                | empty
    '''

def p_vars_doubleprime(p):
    '''
    vars_doubleprime  : ID vars_prime COLON tipo SEMICOL vars_doubleprime
                      | empty
    '''

# define type
def p_tipo(p):
    '''
    tipo : INT
         | FLOAT
    '''

# assign a value
def p_asignacion(p):
    '''
    asignacion : ID EQUAL expresion SEMICOL
    '''

# output
def p_escritura(p):
    '''
    escritura : PRINT LPAREN escritura_prime RPAREN SEMICOL
    '''
    
def p_escritura_prime(p):
    '''
    escritura_prime : escritura_doubleprime escritura_tripleprime
    '''

def p_escritura_doubleprime(p):
    '''
    escritura_doubleprime : CTE_STRING  
                          | expresion
    '''

def p_escritura_tripleprime(p):
    '''
    escritura_tripleprime : COMMA escritura_prime
                          | empty
    '''

# conditionals
def p_condicion(p):
    '''
    condicion : IF LPAREN expresion RPAREN condicion_prime
    '''

def p_condicion_prime(p):
    '''
    condicion_prime : bloque condicion_doubleprime SEMICOL
    '''

def p_condicion_doubleprime(p):
    '''
    condicion_doubleprime : ELSE bloque 
                          | empty
    '''

    # type 
def p_estatuto(p):
    '''
    estatuto : asignacion
             | condicion
             | escritura
    '''

# block of code
def p_bloque(p):
    '''
    bloque : LBRACKET bloque_prime RBRACKET 
    '''

def p_bloque_prim(p):
    '''
    bloque_prime : estatuto bloque_prime 
                 | empty
    '''

# expression
def p_expresion(p):
    '''
    expresion : exp expresion_prime
    '''

def p_expresion_prime(p):
    '''
    expresion_prime : expresion_doubleprime exp
                    | empty
    '''

def p_expresion_doubleprime(p):
    '''
    expresion_doubleprime : GT 
                          | LT
                          | NOT
    '''

# plus and minus 
def p_exp(p):
    '''
    exp : termino exp_prime 
    '''

def p_exp_prime(p):
    '''
    exp_prime : PLUS exp 
              | MINUS exp
              | empty
    '''

# mutliplication or division
def p_termino(p):
    '''
    termino : factor termino_prime 
    '''

def p_termino_prime(p):
    '''
    termino_prime : TIMES termino
                  | DIVIDE termino
                  | empty
    '''

# factor 
def p_factor(p):
    '''
    factor : LPAREN expresion RPAREN
           | factor_prime
    '''

def p_factor_prime(p):
    '''
    factor_prime : factor_doubleprime var_cte 
    '''

def p_factor_doubleprime(p):
    '''
    factor_doubleprime : PLUS
                       | MINUS
                       | empty
    '''

# var_cte
def p_var_cte(p):
    '''
    var_cte : ID 
            | CTE_FLOAT
            | CTE_INT
    '''

def p_empty(p):
	'''
	empty : 
	'''
	pass

def p_error(p):
	if p is not None:
		print ("Illegal token %s" % (p.value))
	else:
		print ("Unexpected end of input")
	exit()

with open('programa.txt', 'r') as file:
    data = file.read()

parser = yacc.yacc()
result = parser.parse(data)
