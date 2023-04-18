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
