import ply.yacc as yacc
from mooLex import tokens 

# program start
def p_prog_prime(p):
    '''
    prog : prog_prime prog_doubleprime MAIN LBRACKET block RBRACKET 
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
    dec_vars : var dec_vars
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
    arr : VAR smp_type ID LSBRACKET CTE_I RSBRACKET arr_prime SEMICOL
    '''

def p_arr_prime(p):
    '''
    arr_prime : LSBRACKET CTE_I RSBRACKET
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
    function : FUNC ID LPARENTHESES param RPARENTHESES MINUS\
               GTSYM function_prime 
    '''

def p_function_prime(p):
    '''
    function_prime : function_st | function_void
    '''

# simple type functions
def p_function_st(p):
    '''
    function_st : smp_type LBRACKET dec_vars block RETURN exp SEMICOL RBRACKET
    '''

# void functions
def p_function_void(p):
    '''
    function_void : VOID LBRACKET dec_vars block RBRACKET
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
    c_input_prime : comma variable c_input_prime
                  | empty
    '''

# print to console
def p_c_print(p):
    '''
    c_print : PRINT LPARENTHESES c_print_prime RPARENTHESES SEMICOL
    '''

def p_c_print_prime(p):
    '''
    c_print_prime : exp c_print_doubleprime 
                  | CTE_C c_print_doubleprime
    '''

def p_c_print_doubleprime(p):
    '''
    c_print_doubleprime : COMMA c_print_prime
                        | empty
    '''

# conditionals 
def p_condition(p):
    '''
    condition : IF LPARENTHESES exp RPARENTHESES LBRACKET block RBRACKET\
                 condition_prime
    '''

def p_condition_prime(p):
    '''
    condition_prime : ELSE LBRACKET block RBRACKET
                    | empty
    '''

# for loops
def p_for_loop(p):
    '''
    for_loop : FOR id IN RANGE LPARENTHESES exp COMMA exp RPARENTHESES\
          LBRACKET block RBRACKET
    '''

# while loops
def p_while_loop(p):
    '''
    while_loop : WHILE LPARENTHESES exp RPARENTHESES LBRACKET block RBRACKET
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
    std_func : ID RPARENTHESES std_func_prime LPARENTHESES 
    '''

def p_std_func_prime(p):
    '''
    std_func_prime : EXP std_func_doubleprime 
                   | empty
    '''

def p_std_func_prime(p):
    '''
    std_func_doubleprime : comma EXP std_func_doubleprime 
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
    generate_key_func : GENERATE_KEY LPARENTHESES RPARENTHESES 
    '''

# file manipulation
def p_open_file(p):
    '''
    leer_arch : OPEN LPARENTHESES CTE_C RPARENTHESES
    '''

def p_read_file(p):
    '''
    leer_arch : READ LPARENTHESES ID RPARENTHESES 
    '''

def p_write_file(p):
    '''
    write_file : WRITE LPARENTHESES CTE_C ID RPARENTHESES
    '''

def p_close_file(p):
    '''
    close_file : CLOSE LPARENTHESES ID RPARENTHESES
    '''

# cryptography functions
def p_encrypt_func(p):
    '''
    encrypt_func : ENCRYPT LPARENTHESES encrypt_func_prime COMMA ID RPARENTHESES
    '''

def p_encrypt_func_prime(p):
    '''
    encrypt_func_prime : CTE_C
                       | ID
    '''

def p_decrypt_func(p):
    '''
    decrypt_func : DECRYPT LPARENTHESES decrypt_func_prime COMMA ID RPARENTHESES
    '''

def p_decrypt_func_prime(p):
    '''
    decrypt_func_prime : CTE_C
                       | ID
    '''

def p_hash_sha256(p):
    '''
    hash_sha256 : HASH_SHA256 LPARENTHESES hash_sha256_prime RPARENTHESES
    '''

def p_hash_sha256_prime(p):
    '''
    hash_sha256_prime : CTE_C
                      | ID
    '''

def p_hash_md5(p):
    '''
    hash_md5 : HASH_MD5 LPARENTHESES hash_md5_prime RPARENTHESES
    '''

def p_hash_md5_prime(p):
    '''
    hash_md5_prime : CTE_C
                   | ID
    '''

# expressions
def p_exp(p):
    '''
    exp :  t_exp exp_prime
    '''

def p_exp_prime(p):
    '''
    exp_prime : OR t_exp
              | empty
    '''

def p_t_exp(p):
    '''
    t_exp : g_exp t_exp' 
    '''

def p_t_exp_prime(p):
    '''
    t_exp_prime : AND t_exp_prime 
    '''

def p_g_exp(p):
    '''
    g_exp : m_exp g_exp 
    '''

def p_g_exp_prime(p):
    '''
    g_exp_prime : g_exp_doubleprime m_exp 
                | empty
    '''

def p_g_exp_doubleprime(p):
    '''
    g_exp_doubleprime : -GT
                      | -LT
                      | -GE
                      | -LE
                      | -EQ
                      | -NE
                      | empty
    '''

def p_m_exp(p):
    '''
    m_exp : t m_exp_prime 
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
    term_prime : term_doubleprime term
               | empty
    '''

def p_term_doubleprime(p):
    '''
    term_doubleprime : TIMES 
                     | DIVIDE
                     | empty
    '''

def p_f(p):
    '''
    factor : LPARENTHESES exp RPARENTHESES
           | CTE_I 
           | CTE_F
           | CTE_C
           | variable
           | func_call
       
    '''

def p_error(p):
	if p is not None:
		print ("Illegal token %s" % (p.value))
	else:
		print ("Unexpected end of input")
	exit()

with open('Files/example.moo', 'r') as file:
    data = file.read()

parser = yacc.yacc()
result = parser.parse(data)
