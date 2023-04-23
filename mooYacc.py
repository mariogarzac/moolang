import ply.yacc as yacc
from mooLex import tokens 

# program start
def p_prog(p):
    '''
    prog : prog1 prog2 MAIN LPAREN RPAREN LCURLY block RCURLY 
    '''

def p_prog1(p):
    '''
    prog1 : dec_vars
          | empty 
    '''

def p_prog2(p):
    '''
    prog2 : function prog2
          | empty 
    '''

def p_dec_vars(p):
    '''
    dec_vars : VAR dec_vars1 
    '''

def p_dec_vars1(p):
    '''
    dec_vars1 : smp_type ID LBRACKET exp RBRACKET dec_vars3 SEMICOL dec_vars4
              | smp_type ID dec_vars2 SEMICOL dec_vars4
              | sp_type ID dec_vars2 SEMICOL dec_vars4
    '''

def p_dec_vars2(p):
    '''
    dec_vars2 : COMMA ID dec_vars2
              | empty
    '''

def p_dec_vars3(p):
    '''
    dec_vars3 : LBRACKET exp RBRACKET
              | empty
    '''

def p_dec_vars4(p):
    '''
    dec_vars4 : dec_vars
              | empty
    '''

# simple type variables
def p_smp_type(p):
    '''
    smp_type : INT
             | FLOAT
             | CHAR
    '''

# special type variable
def p_sp_type(p):
    '''
    sp_type : FILE
    '''

# functions
def p_function(p):
    '''
    function : FUNC ID LPAREN param RPAREN ARROW function2 LCURLY function1 block RCURLY
    '''

def p_function1(p):
    '''
    function1 : dec_vars
              | empty
    '''

def p_function2(p):
    '''
    function2 : smp_type
              | VOID
    '''

# parameters
def p_param(p):
    '''
    param : smp_type ID param1
          | empty
    '''

def p_param1(p):
    '''
    param1 : COMMA smp_type ID param1 
           | empty
    '''

# code blocks
def p_block(p):
    '''
    block : statement block 
          | empty
    '''

# statements
def p_statement(p):
    '''
    statement : assignment
              | c_input
              | c_print
              | condition
              | for_loop
              | while_loop
              | std_func
              | sp_func
              | return_func
    '''

# variable assignment 
def p_assignment(p):
    '''
    assignment : variable EQUAL assignment1 
    '''

def p_assignment1(p):
    '''
    assignment1 : exp SEMICOL
                | sp_func
    '''

def p_variable(p):
    '''
    variable : ID variable1 
    '''

def p_variable1(p):
    '''
    variable1 : LBRACKET exp RBRACKET variable2
              | empty
    '''

def p_variable2(p):
    '''
    variable2 : LBRACKET exp RBRACKET 
              | empty
    '''

# read user input
def p_c_input(p):
    '''
    c_input : INPUT variable c_input1 
    '''

def p_c_input1(p):
    '''
    c_input1 : COMMA variable c_input1
             | empty
    '''

# print to console
def p_c_print(p):
    '''
    c_print : PRINT LPAREN c_print1 RPAREN
    '''

def p_c_print1(p):
    '''
    c_print1 : exp c_print2 
             | CTE_CHAR c_print2
    '''

def p_c_print2(p):
    '''
    c_print2 : COMMA c_print1
             | empty
    '''

# conditionals 
def p_condition(p):
    '''
    condition : IF LPAREN exp RPAREN LCURLY block RCURLY condition1
    '''

def p_condition1(p):
    '''
    condition1 : ELSE LCURLY block RCURLY
               | empty
    '''

# for loops
def p_for_loop(p):
    '''
    for_loop : FOR ID EQUAL exp IN RANGE LPAREN exp COMMA exp for_loop1 RPAREN LCURLY block RCURLY
    '''

def p_for_loop1(p):
    '''
    for_loop1 : COMMA ID EQUAL exp
              | empty
    '''
    

# while loops
def p_while_loop(p):
    '''
    while_loop : WHILE LPAREN exp RPAREN LCURLY block RCURLY
    '''

# standard functions
def p_std_func(p):
    '''
    std_func : ID LPAREN std_func1 RPAREN 
    '''

def p_std_func1(p):
    '''
    std_func1 : exp std_func2
              | empty
    '''

def p_std_func2(p):
    '''
    std_func2 : COMMA exp std_func2
              | empty
    '''

# special functions
def p_sp_func(p):
    '''
    sp_func : generate_key_func
            | file_func
            | crypto_func
    '''

def p_return_func(p):
    '''
    return_func : RETURN exp SEMICOL
    '''

# file functions
def p_file_func(p):
    '''
    file_func : open_file
              | read_file
              | write_file
              | close_file
    '''

# cryptography functions
def p_crypto_func(p):
    '''
    crypto_func : encrypt_func 
                | decrypt_func
                | hash_sha256 
                | hash_md5 
    '''

def p_generate_key_func(p):
    '''
    generate_key_func : GENERATE_KEY LPAREN RPAREN 
    '''

# file manipulation
def p_open_file(p):
    '''
    open_file : OPEN LPAREN CTE_CHAR RPAREN
    '''

def p_read_file(p):
    '''
    read_file : READ LPAREN ID RPAREN 
    '''

def p_write_file(p):
    '''
    write_file : WRITE LPAREN CTE_CHAR ID RPAREN
    '''

def p_close_file(p):
    '''
    close_file : CLOSE LPAREN ID RPAREN
    '''

# cryptography functions
def p_encrypt_func(p):
    '''
    encrypt_func : ENCRYPT LPAREN encrypt_func1 COMMA ID RPAREN
    '''

def p_encrypt_func1(p):
    '''
    encrypt_func1 : CTE_CHAR
                  | ID
    '''

def p_decrypt_func(p):
    '''
    decrypt_func : DECRYPT LPAREN decrypt_func1 COMMA ID RPAREN
    '''

def p_decrypt_func1(p):
    '''
    decrypt_func1 : CTE_CHAR
                  | ID
    '''

def p_hash_sha256(p):
    '''
    hash_sha256 : HASH_SHA256 LPAREN hash_sha2561 RPAREN
    '''

def p_hash_sha2561(p):
    '''
    hash_sha2561 : CTE_CHAR
                 | ID
    '''

def p_hash_md5(p):
    '''
    hash_md5 : HASH_MD5 LPAREN hash_md51 RPAREN
    '''

def p_hash_md51(p):
    '''
    hash_md51 : CTE_CHAR
              | ID
    '''

# expressions
def p_exp(p):
    '''
    exp : t_exp exp1
    '''

def p_exp1(p):
    '''
    exp1 : OR exp
         | empty
    '''

def p_t_exp(p):
    '''
    t_exp : g_exp t_exp1
    '''

def p_t_exp1(p):
    '''
    t_exp1 : AND t_exp
           | empty
    '''

def p_g_exp(p):
    '''
    g_exp : m_exp g_exp1
    '''

def p_g_exp1(p):
    '''
    g_exp1 : GT m_exp 
           | LT m_exp 
           | GE m_exp 
           | LE m_exp 
           | EQ m_exp 
           | NE m_exp 
           | empty
    '''

def p_m_exp(p):
    '''
    m_exp : term m_exp1 
    '''

def p_m_exp1(p):
    '''
    m_exp1 : PLUS m_exp
           | MINUS m_exp
           | empty
    '''


def p_term(p):
    '''
    term : factor term1
    '''

def p_term1(p):
    '''
    term1 : TIMES term
          | DIVIDE term
          | empty
    '''

def p_factor(p):
    '''
    factor : LPAREN exp RPAREN
           | variable
           | std_func
           | CTE_INT
           | CTE_FLOAT
       
    '''

def p_empty(p):
	'''
	empty : 
	'''
	pass

def p_error(p):
    if p:
        # Print the line number and character position where the error occurred
        print(f"Syntax error at line {p.lineno}, position {p.lexpos}: unexpected {p.value}")
    else:
        print("Syntax error: unexpected end of input")

with open('Tests/example.moo', 'r') as file:
    data = file.read()

parser = yacc.yacc()
result = parser.parse(data)


