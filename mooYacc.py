import os
import pickle

'''
TODO:
    - func calls with two params
    - funcs
'''
import ply.yacc as yacc
from mooLex import tokens 
from quadruples import QuadrupleTable 
from FunctionDirectory import FunctionDirectory as FD
from FunctionDirectory import Variable as V
from cube import CONV

file = input('filename: ')
directory = 'Tests/'
filename = directory + file + '.moo'
 
# arch = input('filename: ')
# directory = 'Tests/'
# file = directory + arch + '.moo'
# ------------------------------------------------------------------------------
## Global Variables-------------------------------------------------------------

currId = ""
currStmntId = ""
currFuncId = ""
currModuleId = ""
currType = 1
currScope = CONV['global']
currXDims = 1
currYDims = 1
tmpDims = 0
counter = 0
input = ""
hasReturn = False
seenFor = 0

quads = QuadrupleTable()
V = V()
FD = FD()

# ------------------------------------------------------------------------------
## Syntax Rules-----------------------------------------------------------------

# program start
def p_prog(p):
    '''
    prog : insert_goto_main prog_1 set_scope prog_2 fill_goto_main MAIN get_func_id\
           create_main update_func_dir LPAREN RPAREN LCURLY prog_1 block generate_endfunc RCURLY 
    '''

def p_insert_goto_main(p):
    '''
    insert_goto_main : empty
    '''
    quads.generateGotoMain()

def p_fill_goto_main(p):
    '''
    fill_goto_main : empty
    '''
    quads.fillGotoMain()

def p_generate_endfunc(p):
    '''
    generate_endfunc : empty
    '''
    quads.generateEndfunc()

def p_generate_func_endfunc(p):
    '''
    generate_func_endfunc : empty
    '''
    FD.clearVarTable()
    quads.generateEndfunc()

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

# vars declaration
def p_dec_vars(p):
    '''
    dec_vars : VAR dec_vars_1 
    '''

def p_dec_vars_1(p):
    '''
    dec_vars_1 : smp_type ID get_id LBRACKET CTE_INT get_xdims RBRACKET dec_vars_3 add_variable reset_dims SEMICOL dec_vars_4
               | smp_type ID get_id add_variable dec_vars_2 SEMICOL dec_vars_4
               | sp_type ID get_id add_variable  dec_vars_2 SEMICOL dec_vars_4
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

# simple type vars
def p_smp_type(p):
    '''
    smp_type : INT
             | FLOAT
             | CHAR
    '''
    global currType
    currType = CONV[p[1]]

# special type vars
def p_sp_type(p):
    '''
    sp_type : FILE
    '''
    global currType
    currType = CONV[p[1]]

# functions
def p_function(p):
    '''
    function : FUNC ID get_func_id create_func LPAREN param RPAREN ARROW function_2 update_func_type update_func_dir\
               LCURLY function_1 block RCURLY check_return generate_func_endfunc reset_return update_era
    '''

def p_update_era(p):
    '''
    update_era : empty
    '''
    era = quads.getEraTable()
    FD.updateEra(currFuncId, era)
    quads.resetEra()

def p_check_return(p):
    '''
    check_return : empty
    '''
    global currFuncId, hasReturn
    funcType = FD.getFuncType(currFuncId)
    if (funcType != CONV['void']):
        quads.checkReturn(hasReturn)
    else:
        pass

def p_reset_return(p):
    '''
    reset_return : empty
    '''
    global hasReturn
    hasReturn = False

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
    global currType, currFuncId
    if (p[1] == 'void'):
        currType = CONV['void']
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

# accesing variables
def p_variable(p):
    '''
    variable : ID variable_1 
    '''
    global currType, currId
    currId = p[1]
    address = FD.getVarAddress(p[1])
    currType = FD.getVarType(p[1])
    quads.insertOpAndType(address, currType)

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

# var assignment 
def p_assignment(p):
    '''
    assignment : variable EQUAL assignment_1 
    '''

def p_assignment_1(p):
    '''
    assignment_1 : std_func assign_std_func
                 | push_to_operator_stack exp assign_var SEMICOL 
                 | CTE_CHAR push_string_operand assign_var SEMICOL
                 | sp_func assign_sp_func
                 | c_input assign_input
    '''
                 # | factor push_to_operand_stack assign_var SEMICOL

# read user input
def p_c_input(p):
    '''
    c_input : INPUT get_stmnt_id push_print_and_input LPAREN RPAREN generate_st_func
    '''

# print to console
def p_c_print(p):
    '''
    c_print : PRINT get_stmnt_id LPAREN c_print_1 RPAREN 
    '''

def p_c_print_1(p):
    '''
    c_print_1 : exp push_print_and_input generate_st_func c_print_2 
              | CTE_CHAR push_string_operand push_print_and_input generate_st_func c_print_2 
    '''

def p_c_print_2(p):
    '''
    c_print_2 : COMMA c_print_1
              | empty
    '''
# conditional
def p_condition(p):
    '''
    condition : IF LPAREN exp RPAREN insert_f_goto LCURLY block RCURLY condition_1
    '''

def p_condition_1(p):
    '''
    condition_1 : ELSE fill_gotof insert_goto_if LCURLY block RCURLY 
                | fill_gotof empty
    '''

# while loops
def p_while_loop(p):
    '''
    while_loop : WHILE LPAREN exp RPAREN insert_f_goto LCURLY block RCURLY insert_goto fill_gotof_while
    '''

# for loops
def p_for_loop(p):
    '''
    for_loop : FOR update_seen LPAREN for_loop_1 assign_counter COMMA exp push_jump COMMA for_loop_1 push_jump RPAREN insert_f_goto_for\
             LCURLY block RCURLY fill_f_goto_for insert_goto_for move_counter_quads 
    '''

def p_update_seen(p):
    '''
    update_seen : empty
    '''
    global seenFor
    seenFor += 1

def p_for_loop_1(p):
    '''
    for_loop_1 : ID EQUAL exp 
    '''
    address = FD.getVarAddress(p[1])
    varType = FD.getVarType(p[1])
    quads.insertOpAndType(address, varType)

# standard functions
def p_std_func(p):
    '''
    std_func : ID push_func_id generate_era LPAREN std_func_1 RPAREN generate_func_call reset_param_counter
    '''

def p_std_func_1(p):
    '''
    std_func_1 : exp insert_func_call_param std_func_2
               | empty
    '''

def p_std_func_2(p):
    '''
    std_func_2 : COMMA exp insert_func_call_param std_func_2
               | empty
    '''

def p_insert_func_call_param(p):
    '''
    insert_func_call_param : empty
    '''
    '''
    TODO: add variable address (far assignment)
    # address = quads.getOperand()
    # quads.insertOperand(address)
    '''
    # print("insert_func_call_param")
    # quads.printStacks()
    quads.generateParam()


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
    return_func : RETURN push_to_operator_stack exp generate_return SEMICOL
    '''

# file functions
def p_file_func(p):
    '''
    file_func : open_file
              | write_file
              | close_file
    '''
              # | read_file

# cryptography functions
def p_crypto_func(p):
    '''
    crypto_func : encrypt_func 
                | decrypt_func
                | hash_sha_256 
                | hash_md5 
    '''

# file manipulation
def p_open_file(p):
    '''
    open_file : OPEN get_module_id LPAREN open_file_1 RPAREN insert_open 
    '''

def p_insert_open(p):
    '''
    insert_open : empty
    '''
    global currModuleId, currType
    address = FD.addTmpVariable(currType)
    quads.insertOperator(CONV[currModuleId])
    quads.generateOpen(address)

def p_open_file_1(p):
    '''
    open_file_1 : CTE_CHAR insert_string_param 
                | ID insert_param 
    '''

def p_write_file(p):
    '''
    write_file : WRITE get_module_id LPAREN CTE_CHAR insert_string_param COMMA ID insert_file_id RPAREN insert_file_func
    '''

def p_close_file(p):
    '''
    close_file : CLOSE get_module_id LPAREN ID insert_file_id RPAREN insert_file_func 
    '''

# cryptography functions
def p_generate_key_func(p):
    '''
    generate_key_func : GENERATE_KEY get_module_id LPAREN RPAREN insert_generate_key
    '''

def p_insert_generate_key(p):
    '''
    insert_generate_key : empty
    '''
    address = FD.addTmpVariable(CONV['char'])
    quads.generateGKey(address)

def p_encrypt_func(p):
    '''
    encrypt_func : ENCRYPT get_module_id LPAREN encrypt_func_1 COMMA ID push_to_operand_stack RPAREN insert_encrypt_decrypt_func
    '''

def p_encrypt_func_1(p):
    '''
    encrypt_func_1 : CTE_CHAR push_string_operand
                   | ID push_to_operand_stack
    '''

def p_decrypt_func(p):
    '''
    decrypt_func : DECRYPT get_module_id LPAREN decrypt_func_1 COMMA ID push_to_operand_stack RPAREN insert_encrypt_decrypt_func
    '''

def p_insert_encrypt_decrypt_func(p):
    '''
    insert_encrypt_decrypt_func : empty
    '''
    operator = CONV[currModuleId]
    key = quads.popOperand()
    keyType = quads.popType()
    file = quads.popOperand()
    fileType = quads.popType()
    address = FD.addTmpVariable(fileType)
    quads.generateEncryptDecrypt(operator, key, keyType, file, fileType, address)

def p_decrypt_func_1(p):
    '''
    decrypt_func_1 : CTE_CHAR push_string_operand
                   | ID push_to_operand_stack
    '''

def p_hash_sha_256(p):
    '''
    hash_sha_256 : HASH_SHA256 get_module_id LPAREN hash_sha_256_1 RPAREN insert_hash
    '''

def p_hash_sha_256_1(p):
    '''
    hash_sha_256_1 : CTE_CHAR push_string_operand
                   | ID push_to_operand_stack  
    '''

def p_hash_md5(p):
    '''
    hash_md5 : HASH_MD5 get_module_id LPAREN hash_md5_1 RPAREN insert_hash
    '''

def p_hash_md5_1(p):
    '''
    hash_md5_1 : CTE_CHAR push_string_operand
               | ID push_to_operand_stack  
    '''

def p_insert_hash(p):
    '''
    insert_hash : empty
    '''
    global currModuleId
    operator = CONV[currModuleId]
    operand = quads.popOperand()
    operandType = quads.popType()
    tmpAddress = FD.addTmpVariable(operandType)
    quads.generateHash(operator, operand, operandType, tmpAddress)

# expressions
def p_exp(p):
    '''
    exp : t_exp exp_1 solve_exp 
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

def p_g_exp(p):
    '''
    g_exp : m_exp g_exp_1 solve_g_exp  
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
    m_exp : term solve_m_exp m_exp_1 
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
           | variable
           | CTE_INT push_int_operand
           | CTE_FLOAT push_float_operand
           | std_func
    '''


# ------------------------------------------------------------------------------
## VARS-------------------------------------------------------------------------
def p_set_scope(p):
    '''
    set_scope : empty
    '''
    global currScope
    currScope = CONV['local']

def p_get_id(p):
    '''
    get_id : empty
    '''
    global currId
    currId = p[-1]

def p_get_stmnt_id(p):
    '''
    get_stmnt_id : empty
    '''
    global currStmntId
    currStmntId = p[-1]

def p_get_module_id(p):
    '''
    get_module_id : empty
    '''
    global currModuleId
    currModuleId = p[-1]
    
def p_get_func_id(p):
    '''
    get_func_id : empty
    '''
    global currFuncId
    currFuncId = p[-1]

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
    currXDims = 1
    currYDims = 3

def p_assign_var(p):
    '''
    assign_var : empty
    '''
    operator = quads.popOperator()
    rightType = quads.popType()
    leftType = quads.popType()
    resType = quads.checkTypeMismatch(leftType, rightType, operator)
    tmpAddress = FD.addTmpVariable(resType)
    quads.generateQuad(operator, rightType, leftType, resType, tmpAddress)

def p_assign_sp_func(p):
    '''
    assign_sp_func : empty
    '''
    global currModuleId
    quads.insertOperator(CONV[currModuleId])
    quads.assignSpFunc()

def p_assign_std_func(p):
    '''
    assign_std_func : empty
    '''
    '''
    TODO: checar si func también
    '''
    global currFuncId
    address = FD.getVarAddress(currFuncId)
    quads.insertOpAndType(address, FD.getFuncType(currFuncId))
    quads.assignStdFunc()

def p_assign_input(p):
    '''
    assign_input : empty
    '''
    global currType
    address = quads.popAddress() #FD.addTmpVariable(currType)
    quads.assignInput(address)

def p_generate_st_func(p):
    '''
    generate_st_func : empty
    '''
    printType = quads.popType()
    address = FD.addTmpVariable(printType)
    quads.generateStFunc(address)

## FUNCS------------------------------------------------------------------------
def p_create_main(p):
    '''
    create_main : empty
    '''
    global currFuncId, currType
    FD.addFunc(currFuncId, CONV['void'])

def p_create_func(p):
    '''
    create_func : empty
    '''
    global currFuncId, currType
    FD.addFunc(currFuncId, currType)

def p_add_param(p):
    '''
    add_param : empty
    '''
    global  currScope, currId, currType, currFuncId, currXDims, currYDims
    tmpVar = V.addVar(currId, currType, currXDims, currYDims, 0)
    FD.addParam(currFuncId, currId, currType)
    FD.addVariable(currScope, tmpVar)

def p_reset_param_counter(p):
    '''
    reset_param_counter : empty
    '''
    quads.resetParamCounter()


def p_add_variable(p):
    '''
    add_variable : empty
    '''
    global currScope, currType, currId, currXDims, currYDims, currFuncId
    tmpVar = V.addVar(currId, currType, currXDims, currYDims, 0)
    FD.addVariable(currScope, tmpVar)

def p_generate_era(p):
    '''
    generate_era : empty
    '''
    # address = FD.getVarAddress(currFuncId)
    # quads.insertOperand(address)
    quads.generateEra()
    # print("generate era")
    # quads.printStacks()

def p_generate_return(p):
    '''
    generate_return : empty
    '''
    global currFuncId
    global hasReturn
    hasReturn = True
    quads.insertFuncType(FD.getFuncType(currFuncId))
    quads.generateReturn()

def p_generate_func_call(p):
    '''
    generate_func_call : empty
    '''
    global currFuncId
    params = FD.getFuncParams(currFuncId)
    pointer = FD.getFuncPointer(currFuncId)
    address = FD.getVarAddress(currFuncId)
    quads.insertOperand(address)
    quads.insertOperand(pointer)
    # tmpAddress = FD.getVarAddress(currFuncId)
    quads.insertOperand(currFuncId)
    quads.generateFuncCall(params)

def p_push_func_id(p):
    '''
    push_func_id : empty
    '''
    global currFuncId
    currFuncId = p[-1]
    # address = FD.getVarAddress(currFuncId)
    quads.insertOperand(currFuncId)

def p_update_fund_dir(p):
    '''
    update_func_dir : empty
    '''
    FD.updatePointer(currFuncId, quads.getQuadPointer())

def p_update_func_type(p):
    '''
    update_func_type : empty
    '''
    global currType, currFuncId, currXDims, currYDims
    FD.updateFuncType(currFuncId, currType)

## SP FUNCS---------------------------------------------------------------------
# def p_insert_crypto_func(p):
#     '''
#     insert_crypto_func : empty
#     '''
#     global currModuleId
#     quads.insertOperator(CONV[currModuleId])
#     tmpAddress = FD.addTmpVariable()
#     quads.generateCryptoFunc()

def p_insert_file_func(p):
    '''
    insert_file_func : empty
    '''
    global currModuleId
    quads.insertOperator(CONV[currModuleId])
    quads.generateFileFunc()

def p_insert_param(p):
    '''
    insert_param : empty
    '''
    global currType
    currType = CONV['char']
    address = FD.getVarAddress(p[-1])
    currType = FD.getVarType(p[-1])
    quads.insertOpAndType(address, currType)

def p_insert_string_param(p):
    '''
    insert_string_param : empty
    '''
    global currType
    currType = CONV['char']
    address = FD.addConstant(CONV['constant'], p[-1],CONV['char'])
    quads.insertOpAndType(address, CONV['char'])

def p_insert_file_id(p):
    '''
    insert_file_id : empty
    '''
    address = FD.getVarAddress(p[-1])
    varType = FD.getVarType(p[-1])
    quads.insertOpAndType(address, varType)
    # global currScope
    # quads.insertOpAndType(p[-1], FD.getVarType(p[-1]))

## EXPRESSIONS-----------------------------------------------------------------
def p_push_to_operator_stack(p):
    '''
    push_to_operator_stack : empty
    '''
    quads.insertOperator(CONV[p[-1]])

def p_push_print_and_input(p):
    '''
    push_print_and_input : empty
    '''
    quads.insertOperator(CONV[currStmntId])

def p_push_to_operand_stack(p):
    '''
    push_to_operand_stack : empty
    '''
    address = FD.getVarAddress(p[-1])
    varType = FD.getVarType(p[-1])
    quads.insertOpAndType(address, varType)

def p_push_float_operand(p):
    '''
    push_float_operand : empty
    '''
    address = FD.addConstant(CONV['constant'], p[-1],CONV['float'])
    varType = FD.getVarType(p[-1])
    quads.insertOpAndType(address, CONV['float'])

def p_push_int_operand(p):
    '''
    push_int_operand : empty
    '''
    address = FD.addConstant(CONV['constant'], p[-1],CONV['int'])
    quads.insertOpAndType(address, CONV['int'])


def p_push_string_operand(p):
    '''
    push_string_operand : empty
    '''
    address = FD.addConstant(CONV['constant'], p[-1],CONV['char'])
    quads.insertOpAndType(address, CONV['char'])
 
def p_solve_m_exp(p):
    '''
    solve_m_exp : empty
    '''
    # + or -
    if (quads.getOperator() == CONV['+'] or quads.getOperator() == CONV['-']):
        operator = quads.popOperator()
        rightType = quads.popType()
        leftType = quads.popType()
        resType = quads.checkTypeMismatch(leftType, rightType, operator)
        tmpAddress = FD.addTmpVariable(resType)
        quads.generateQuad(operator, rightType, leftType, resType, tmpAddress)

def p_solve_term(p):
    '''
    solve_term : empty
    '''
    # * or /
    if (quads.getOperator() == CONV['*'] or quads.getOperator() == CONV['/']):
        operator = quads.popOperator()
        rightType = quads.popType()
        leftType = quads.popType()
        resType = quads.checkTypeMismatch(leftType, rightType, operator)
        tmpAddress = FD.addTmpVariable(resType)
        quads.generateQuad(operator, rightType, leftType, resType, tmpAddress)

def p_solve_t_exp(p):
    '''
    solve_t_exp : empty
    '''
    if (quads.getOperator() == CONV['and']):
        operator = quads.popOperator()
        rightType = quads.popType()
        leftType = quads.popType()
        resType = quads.checkTypeMismatch(leftType, rightType, operator)
        tmpAddress = FD.addTmpVariable(resType)
        quads.generateQuad(operator, rightType, leftType, resType, tmpAddress)
        FD.addConstant(CONV['local'],False,CONV['bool'])


def p_solve_g_exp(p):
    '''
    solve_g_exp : empty
    '''
    ops = [CONV['-gt'],CONV['-ge'],CONV['-lt'],CONV['-le'],CONV['-eq'],CONV['-ne']]
    if (quads.getOperator() in ops):
        operator = quads.popOperator()
        rightType = quads.popType()
        leftType = quads.popType()
        resType = quads.checkTypeMismatch(leftType, rightType, operator)
        tmpAddress = FD.addTmpVariable(resType)
        quads.generateQuad(operator, rightType, leftType, resType, tmpAddress)
        FD.addConstant(CONV['local'],False,CONV['bool'])

def p_solve_exp(p):
    '''
    solve_exp : empty
    '''
    if (quads.getOperator() == CONV['or']):
        operator = quads.popOperator()
        rightType = quads.popType()
        leftType = quads.popType()
        resType = quads.checkTypeMismatch(leftType, rightType, operator)
        tmpAddress = FD.addTmpVariable(resType)
        quads.generateQuad(operator, rightType, leftType, resType, tmpAddress)
        FD.addConstant(CONV['local'],False,CONV['bool'])

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
        operator = quads.popOperator()
        rightType = quads.popType()
        leftType = quads.popType()
        resType = quads.checkTypeMismatch(leftType, rightType, operator)
        tmpAddress = FD.addTmpVariable(resType)
        quads.generateQuad(operator, rightType, leftType, resType, tmpAddress)
    quads.popParen()

## GOTOs------------------------------------------------------------------------

def p_insert_goto_if(p):
    '''
    insert_goto_if : empty
    '''
    quads.generateGotoIf()
    
def p_push_jump(p):
    '''
    push_jump : empty
    '''
    quads.insertJump()

def p_insert_f_goto(p):
    '''
    insert_f_goto : empty
    '''
    quads.generateGotoF()

def p_insert_goto(p):
    '''
    insert_goto : empty
    '''
    quads.generateGoto()

def p_insert_goto_for(p):
    '''
    insert_goto_for : empty
    '''
    global seenFor
    if (seenFor == 2):
        quads.generateGotoFor(seenFor)
        seenFor = 0
    else:
        quads.generateGotoFor(0)

def p_fill_gotof(p):
    '''
    fill_gotof : empty
    '''
    mod = 0
    if (p[-1] == "else"):
        mod = 1
    quads.fillGotoF(mod)

def p_fill_gotof_while(p):
    '''
    fill_gotof_while : empty
    '''
    quads.fillGotoFWhile()

def p_insert_f_goto_for(p): 
    '''
    insert_f_goto_for : empty
    '''
    # address = FD.getVarAddress(p[1])
    # currType = FD.getVarType(p[1])
    # quads.insertOpAndType(address, currType)
    quads.generateForQuad()

def p_fill_f_goto_for(p):
    '''
    fill_f_goto_for : empty
    '''
    quads.fillFGotoFor()

def p_assign_counter(p):
    '''
    assign_counter : empty
    '''
    quads.generateForCounter()

def p_move_counter_quads(p):
    '''
    move_counter_quads : empty
    '''
    quads.moveCounterQuads()

# ------------------------------------------------------------------------------
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
    exit()


# ------------------------------------------------------------------------------

parser = yacc.yacc()

try:
    with open (filename, "r") as file:
        data = file.read()
        result = parser.parse(data)

    with open('data.obj', 'wb') as file:
        pickle.dump(
                {"quadruples": quads.quads, "funcDir": FD.funcDirectory, "memory": FD.memory }, file)

    print("-----------QUADS-----------")
    quads.printStacks()
    print("---------------------------")
    quads.printTheQuads()
    print("---------------------------")
    # FD.printFuncDir()
    # print("***************************")
    # FD.printVars()
    # print("---------------------------")
    FD.printMemory()
    print("---------------------------")


except EOFError:
    print(EOFError)
