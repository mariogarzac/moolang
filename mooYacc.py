import ply.yacc as yacc
from mooLex import tokens 

# program start
def p_prog(p):
    '''
    prog : prog_prime prog_doubleprime MAIN LCURLY block RCURLY 
    '''

def p_prog_prime(p):
    '''
    prog_prime : dec_vars prog_prime
               | empty 
    '''

def p_prog_doubleprime(p):
    '''
    prog_doubleprime : function prog_doubleprime
                     | empty 
    '''

# variable declaration
def p_dec_vars(p):
    '''
    dec_vars : vars dec_vars
             | arr dec_vars
             | empty
    '''

# simple type variables
def p_vars(p):
    '''
    vars : VAR vars_prime ID vars_doubleprime SEMICOL
    '''

def p_vars_prime(p):
    '''
    vars_prime : sp_type 
               | smp_type
    '''

def p_vars_doubleprime(p):
    '''
    vars_doubleprime : COMMA ID vars_doubleprime 
                     | empty
    '''

# array declaration
def p_arr(p):
    '''
    arr : VAR smp_type ID LBRACKET CTE_INT RBRACKET arr_prime SEMICOL
    '''

def p_arr_prime(p):
    '''
    arr_prime : LBRACKET CTE_INT RBRACKET
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
    function : FUNC ID LPAREN param RPAREN MINUS GTSYM function_prime 
    '''

def p_function_prime(p):
    '''
    function_prime : function_st 
                   | function_void
    '''

# simple type functions
def p_function_st(p):
    '''
    function_st : smp_type LCURLY dec_vars block RETURN exp SEMICOL RCURLY
    '''

# void functions
def p_function_void(p):
    '''
    function_void : VOID LCURLY dec_vars block RCURLY
    '''

# parameters
def p_param(p):
    '''
    param : smp_type ID param_prime
          | empty
    '''

def p_param_prime(p):
    '''
    param_prime : COMMA ID param_prime 
                | empty
    '''

# code blocks
def p_block(p):
    '''
    block : statement block 
          | empty
    '''

def p_variable(p):
    '''
    variable : ID variable_prime 
             | empty
    '''

def p_variable_prime(p):
    '''
    variable_prime : LBRACKET exp RBRACKET variable_doubleprime
                   | empty
    '''

def p_variable_doubleprime(p):
    '''
    variable_doubleprime : LBRACKET exp RBRACKET 
                         | empty
    '''

# statements
def p_statement(p):
    '''
    statement : assignment
             |  c_input
             |  c_print
             |  condition
             |  for_loop
             |  while_loop
             |  func_call
    '''

# variable assignment 
def p_assignment(p):
    '''
    assignment : variable EQUAL assignment_prime SEMICOL 
    '''

def p_assignment_prime(p):
    '''
    assignment_prime : exp
                     | func_call
    '''

# read user input
def p_c_input(p):
    '''
    c_input : INPUT variable c_input_prime SEMICOL
    '''

def p_c_input_prime(p):
    '''
    c_input_prime : COMMA variable c_input_prime
                  | empty
    '''

# print to console
def p_c_print(p):
    '''
    c_print : PRINT LPAREN c_print_prime RPAREN SEMICOL
    '''

def p_c_print_prime(p):
    '''
    c_print_prime : exp c_print_doubleprime 
                  | CTE_CHAR c_print_doubleprime
    '''

def p_c_print_doubleprime(p):
    '''
    c_print_doubleprime : COMMA c_print_prime
                        | empty
    '''

# conditionals 
def p_condition(p):
    '''
    condition : IF LPAREN exp RPAREN LCURLY block RCURLY condition_prime
    '''

def p_condition_prime(p):
    '''
    condition_prime : ELSE LCURLY block RCURLY
                    | empty
    '''

# for loops
def p_for_loop(p):
    '''
    for_loop : FOR ID IN RANGE LPAREN exp COMMA exp RPAREN LCURLY block RCURLY
    '''

# while loops
def p_while_loop(p):
    '''
    while_loop : WHILE LPAREN exp RPAREN LCURLY block RCURLY
    '''

# function calls 
def p_func_call(p):
    '''
    func_call : std_func
              | sp_func
    '''

# standard functions
def p_std_func(p):
    '''
    std_func : ID RPAREN std_func_prime LPAREN 
    '''

def p_std_func_prime(p):
    '''
    std_func_prime : exp std_func_doubleprime
                   | empty
    '''

def p_std_func_doubleprime(p):
    '''
    std_func_doubleprime : COMMA exp std_func_doubleprime
                         | empty
    '''

# special functions
def p_sp_func(p):
    '''
    sp_func : generate_key_func
            | file_func
            | crypto_func
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
    encrypt_func : ENCRYPT LPAREN encrypt_func_prime COMMA ID RPAREN
    '''

def p_encrypt_func_prime(p):
    '''
    encrypt_func_prime : CTE_CHAR
                       | ID
    '''

def p_decrypt_func(p):
    '''
    decrypt_func : DECRYPT LPAREN decrypt_func_prime COMMA ID RPAREN
    '''

def p_decrypt_func_prime(p):
    '''
    decrypt_func_prime : CTE_CHAR
                       | ID
    '''

def p_hash_sha256(p):
    '''
    hash_sha256 : HASH_SHA256 LPAREN hash_sha256_prime RPAREN
    '''

def p_hash_sha256_prime(p):
    '''
    hash_sha256_prime : CTE_CHAR
                      | ID
    '''

def p_hash_md5(p):
    '''
    hash_md5 : HASH_MD5 LPAREN hash_md5_prime RPAREN
    '''

def p_hash_md5_prime(p):
    '''
    hash_md5_prime : CTE_CHAR
                   | ID
    '''

# expressions
def p_exp(p):
    '''
    exp : t_exp exp_prime
    '''

def p_exp_prime(p):
    '''
    exp_prime : OR t_exp
              | empty
    '''

def p_t_exp(p):
    '''
    t_exp : g_exp t_exp_prime
    '''

def p_t_exp_prime(p):
    '''
    t_exp_prime : AND t_exp
                | empty
    '''

def p_g_exp(p):
    '''
    g_exp : m_exp g_exp_prime
    '''

def p_g_exp_prime(p):
    '''
    g_exp_prime : g_exp_doubleprime m_exp 
                | empty
    '''

def p_g_exp_doubleprime(p):
    '''
    g_exp_doubleprime : GT
                      | LT
                      | GE
                      | LE
                      | EQ
                      | NE
                      | empty
    '''

def p_m_exp(p):
    '''
    m_exp : term m_exp_prime 
    '''

def p_m_exp_prime(p):
    '''
    m_exp_prime : m_exp_doubleprime m_exp
                | empty
    '''

def p_m_exp_doubleprime(p):
    '''
    m_exp_doubleprime : PLUS 
                      | MINUS
    '''

def p_term(p):
    '''
    term :  factor term_prime
    '''

def p_term_prime(p):
    '''
    term_prime : TIMES term
               | DIVIDE term
               | empty
    '''

# def p_term_prime(p):
#     '''
#     term_prime : term_doubleprime term
#                | empty
#     '''
#
# def p_term_doubleprime(p):
#     '''
#     term_doubleprime : TIMES 
#                      | DIVIDE
#                      | empty
#     '''

def p_factor(p):
    '''
    factor : LPAREN exp RPAREN
           | CTE_INT
           | CTE_FLOAT
           | CTE_CHAR
           | variable
           | func_call
       
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

with open('Files/example.moo', 'r') as file:
    data = file.read()

parser = yacc.yacc(debug = True)
result = parser.parse(data)


