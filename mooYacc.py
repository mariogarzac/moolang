import ply.yacc as yacc
from mooLex import tokens 
from quadruples import QuadrupleTable 
from FunctionDirectory import FunctionDirectory as FD
from FunctionDirectory import Variable as V


################################
######## Global Variables ######
################################
currId = ""
currType = 1
currScope = 21
currXDims = 0
currYDims = 0
tmpDims = 0
counter = 0
solve = True

quads = QuadrupleTable()
V = V()
FD = FD()

################################
######## Convert Strings #######
################################

CONV = {
    'void':          0,
    'int':           1,
    'float':         2,
    'char':          3,
    'file':          4,
    'bool':          5,
    '+':             6,
    '-':             7,
    '*':             8,
    '/':             9,
    '(':             10,
    ')':             11,
    '=':             12,
    '-gt':           13,
    '-ge':           14,
    '-lt':           15,
    '-le':           16,
    '-eq':           17,
    '-ne':           18,
    'and':           19,
    'or':            20,
    'GOTO':          21,
    'GOTOF':         22,
    'GOTOV':         23,
    'local':         24,
    'global':        25,
    'open' :         26, 
    'read' :         27, 
    'write'  :       28, 
    'close' :        29,
    'encrypt' :      30,
    'decrypt' :      31,
    'hash_md5' :     32,
    'hash_sha256' :  33, 
    'generate_key':  34
    }



################################
######### Syntax Rules ######### 
################################

# program start
def p_prog(p):
    '''
    prog : prog_1 prog_2 MAIN LPAREN RPAREN LCURLY block RCURLY 
    '''

def p_prog_1(p):
    '''
    prog_1 : dec_vars 
           | empty 
    '''

def p_prog_2(p):
    '''
    prog_2 : function prog_2
           | empty 
    '''

# variable declaration
def p_dec_vars(p):
    '''
    dec_vars : VAR dec_vars_1 
    '''

def p_dec_vars_1(p):
    '''
    dec_vars_1 : smp_type ID get_id LBRACKET CTE_INT get_xdims RBRACKET dec_vars_3 add_variable reset_dims  SEMICOL dec_vars_4
               | smp_type ID get_id add_variable dec_vars_2 SEMICOL add_variable dec_vars_4
               | sp_type ID get_id dec_vars_2 SEMICOL add_variable dec_vars_4
    '''

def p_dec_vars_2(p):
    '''
    dec_vars_2 : COMMA ID get_id add_variable dec_vars_2 
               | empty
    '''

def p_dec_vars_3(p):
    '''
    dec_vars_3 : LBRACKET CTE_INT get_ydims RBRACKET
               | empty
    '''

def p_dec_vars_4(p):
    '''
    dec_vars_4 : dec_vars
               | empty
    '''

# simple type variables
def p_smp_type(p):
    '''
    smp_type : INT
             | FLOAT
             | CHAR
    '''
    global currType
    currType = CONV[p[1]]

# special type variable
def p_sp_type(p):
    '''
    sp_type : FILE
    '''
    global currType
    currType = CONV[p[1]]

# functions
def p_function(p):
    '''
    function : FUNC ID get_id LPAREN param RPAREN ARROW function_2 create_func LCURLY function_1 block RCURLY
    '''

def p_function_1(p):
    '''
    function_1 : set_scope dec_vars 
               | empty
    '''

def p_function_2(p):
    '''
    function_2 : smp_type
               | VOID
    '''
    global currType
    if (currType == 'void'):
        currType = CONV[p[1]]
    else:
        pass

# parameters
def p_param(p):
    '''
    param : smp_type ID get_id add_param param_1
          | empty
    '''

def p_param_1(p):
    '''
    param_1 : COMMA smp_type ID get_id add_param param_1 
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
    assignment : variable EQUAL push_to_operator_stack assignment_1 
    '''

def p_assignment_1(p):
    '''
    assignment_1 : exp assign_var SEMICOL
                 | sp_func
    '''

# accesing variables
def p_variable(p):
    '''
    variable : ID variable_1 
    '''
    quads.insertOpAndType(p[1],FD.getVarType(p[1]))

def p_variable_1(p):
    '''
    variable_1 : LBRACKET exp RBRACKET variable_2
               | empty
    '''

def p_variable_2(p):
    '''
    variable_2 : LBRACKET exp RBRACKET 
               | empty
    '''

# read user input
def p_c_input(p):
    '''
    c_input : INPUT variable c_input_1 
    '''

def p_c_input_1(p):
    '''
    c_input_1 : COMMA variable c_input_1
              | empty
    '''

# print to console
def p_c_print(p):
    '''
    c_print : PRINT LPAREN c_print_1 RPAREN
    '''

def p_c_print_1(p):
    '''
    c_print_1 : exp c_print_2 
              | CTE_CHAR c_print_2
    '''

def p_c_print_2(p):
    '''
    c_print_2 : COMMA c_print_1
              | empty
    '''

# conditionals 
def p_condition(p):
    '''
    condition : IF LPAREN exp RPAREN LCURLY block RCURLY condition_1
    '''

def p_condition_1(p):
    '''
    condition_1 : ELSE LCURLY block RCURLY
                | empty
    '''

# for loops
def p_for_loop(p):
    '''
    for_loop : FOR ID EQUAL exp IN RANGE LPAREN exp COMMA exp for_loop_1 RPAREN LCURLY block RCURLY
    '''

def p_for_loop_1(p):
    '''
    for_loop_1 : COMMA ID EQUAL exp
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
    std_func : ID LPAREN std_func_1 RPAREN 
    '''

def p_std_func_1(p):
    '''
    std_func_1 : exp std_func_2
               | empty
    '''

def p_std_func_2(p):
    '''
    std_func_2 : COMMA exp std_func_2
               | empty
    '''

# special functions
def p_sp_func(p):
    '''
    sp_func : generate_key_func
            | file_func
            | crypto_func
    '''

# return for functions
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
                | hash_sha_256 
                | hash_md5 
    '''

def p_generate_key_func(p):
    '''
    generate_key_func : GENERATE_KEY insert_sp_func LPAREN RPAREN 
    '''

# file manipulation
def p_open_file(p):
    '''
    open_file : OPEN insert_sp_func LPAREN CTE_CHAR RPAREN
    '''

def p_read_file(p):
    '''
    read_file : READ insert_sp_func LPAREN ID RPAREN 
    '''

def p_write_file(p):
    '''
    write_file : WRITE insert_sp_func LPAREN CTE_CHAR ID RPAREN
    '''

def p_close_file(p):
    '''
    close_file : CLOSE insert_sp_func LPAREN ID RPAREN
    '''

# cryptography functions
def p_encrypt_func(p):
    '''
    encrypt_func : ENCRYPT insert_sp_func LPAREN encrypt_func_1 COMMA ID RPAREN
    '''

def p_encrypt_func_1(p):
    '''
    encrypt_func_1 : CTE_CHAR
                   | ID
    '''

def p_decrypt_func(p):
    '''
    decrypt_func : DECRYPT LPAREN decrypt_func_1 COMMA ID RPAREN
    '''

def p_decrypt_func_1(p):
    '''
    decrypt_func_1 : CTE_CHAR
                   | ID
    '''

def p_hash_sha_256(p):
    '''
    hash_sha_256 : HASH_SHA256 LPAREN hash_sha_256_1 RPAREN
    '''

def p_hash_sha_256_1(p):
    '''
    hash_sha_256_1 : CTE_CHAR
                   | ID
    '''

def p_hash_md5(p):
    '''
    hash_md5 : HASH_MD5 LPAREN hash_md5_1 RPAREN
    '''

def p_hash_md5_1(p):
    '''
    hash_md5_1 : CTE_CHAR
               | ID
    '''

# expressions
def p_exp(p):
    '''
    exp : t_exp exp_1  solve_exp 
    '''

def p_exp_1(p):
    '''
    exp_1 : OR push_to_operator_stack exp
          | empty
    '''

def p_t_exp(p):
    '''
    t_exp : g_exp t_exp_1 solve_t_exp 
    '''

def p_t_exp_1(p):
    '''
    t_exp_1 : AND push_to_operator_stack t_exp
            | empty
    '''

# TODO THIS G_EXP
def p_g_exp(p):
    '''
    g_exp : m_exp solve_g_exp g_exp_1 
    '''

def p_g_exp_1(p):
    '''
    g_exp_1 : GT push_to_operator_stack m_exp 
            | LT push_to_operator_stack m_exp 
            | GE push_to_operator_stack m_exp 
            | LE push_to_operator_stack m_exp 
            | EQ push_to_operator_stack m_exp 
            | NE push_to_operator_stack m_exp 
            | empty
    '''

def p_m_exp(p):
    '''
    m_exp : term solve_m_exp  m_exp_1 
    '''

def p_m_exp_1(p):
    '''
    m_exp_1 : PLUS push_to_operator_stack m_exp
            | MINUS push_to_operator_stack m_exp
            | empty
    '''

def p_term(p):
    '''
    term : factor solve_term term_1
    '''

def p_term_1(p):
    '''
    term_1 : TIMES push_to_operator_stack term
           | DIVIDE push_to_operator_stack term
           | empty
    '''

def p_factor(p):
    '''
    factor : LPAREN insert_lparen exp solve_paren RPAREN 
           | CTE_INT push_to_operand_stack
           | CTE_FLOAT push_to_operand_stack
           | variable
           | std_func
    '''

################################
####### Neuralgic Points ####### 
################################

# <VARS>
def p_set_scope(p):
    '''
    set_scope : empty
    '''
    global currScope
    currScope = 20

def p_get_id(p):
    '''
    get_id : empty
    '''
    global currId, currScope, currType
    currId = p[-1]

def p_get_xdims(p):
    '''
    get_xdims : empty
    '''
    global currXDims
    currXDims = p[-1]

def p_get_ydims(p):
    '''
    get_ydims : empty
    '''
    global currYDims
    currYDims = p[-1]

def p_reset_dims(p):
    '''
    reset_dims : empty
    '''
    global currXDims, currYDims
    currXDims = 0
    currYDims = 0


# <FUNCS>
def p_insert_sp_func(p):
    '''
    insert_sp_func : empty
    '''
    global currId
    currId = p[-1]
    quads.insertOpAndType(currId, 0)

def p_create_func(p):
    '''
    create_func : empty
    '''
    global currId, currType
    FD.addFunc(currId, currType)

def p_add_param(p):
    '''
    add_param : empty
    '''
    global  currId, currType
    FD.addParam(currId,currType)

def p_add_variable(p):
    '''
    add_variable : empty
    '''
    global currType, currId, currScope, currXDims, currYDims
    tmpVar = V.addVar(currId, currType, currScope, 0, currXDims, currYDims)
    FD.addVariable(tmpVar)

# <EXPRESSIONS>
def p_push_to_operator_stack(p):
    '''
    push_to_operator_stack : empty
    '''
    quads.insertOperator(CONV[p[-1]])

def p_push_to_operand_stack(p):
    '''
    push_to_operand_stack : empty
    '''
    if (type(p[-1]) is float):
        quads.insertOpAndType(p[-1], CONV['float'])
    elif(type(p[-1]) is int):
        quads.insertOpAndType(p[-1], CONV['int'])
 
def p_solve_m_exp(p):
    '''
    solve_m_exp : empty
    '''
    # + or -
    if (quads.getOperator() == CONV['+'] or quads.getOperator() == CONV['-']):
        # quads.checkPending(CONV['+'], CONV['-'])
        quads.generateQuad()

def p_solve_term(p):
    '''
    solve_term : empty
    '''
    # * or /
    if (quads.getOperator() == CONV['*'] or quads.getOperator() == CONV['/']):
        # quads.checkPending(CONV['*'], CONV['/'])
        quads.generateQuad()

def p_solve_t_exp(p):
    '''
    solve_t_exp : empty
    '''
    if (quads.getOperator() == CONV['and']):
        quads.generateQuad()

def p_solve_g_exp(p):
    '''
    solve_g_exp : empty
    '''
    if (quads.getOperator() == CONV['or']):
        quads.generateQuad()

def p_solve_exp(p):
    '''
    solve_exp : empty
    '''
    if (quads.getOperator() == CONV['or']):
        quads.generateQuad()

def p_insert_lparen(p):
    '''
    insert_lparen : empty
    '''
    quads.insertOperator(CONV['('])

def p_solve_paren(p):
    '''
    solve_paren : empty
    '''
    while (quads.getOperator() != CONV['(']):
        quads.generateQuad()
    quads.popParen()

def p_assign_var(p):
    '''
    assign_var : empty
    '''
    quads.generateQuad()
    value = quads.popOperand()
    id = quads.popOperand()
    FD.assignValue(id, value)

################################
######## Empty && Error ######## 
################################
def p_empty(p):
	'''
	empty : 
	'''
	pass

def p_error(p):
    if p:
        # Print the line number and character position where the error occurred
        print(f"Syntax error at line {p.lineno}: unexpected {p.value}")
    else:
        print("Syntax error: unexpected end of input")


################################
######## Testing && Run ######## 
################################
with open('Tests/simple.moo', 'r') as file:
    data = file.read()

    parser = yacc.yacc()
    result = parser.parse(data)
# try:
# except IndexError:
#     print("AN ERROR OCCURRED")
FD.printFuncDir()

