# Mario Garza Chapa
# A01720245
---

<h1 align="center"> Sintaxis moo </h1>

#### **PROG**
prog : prog1 prog2 MAIN LPAREN RPAREN LCURLY block RCURLY 

#### **PROG1**
prog1 : dec_vars
      | empty 

#### **PROG2**
prog2 : function prog2
      | empty 

#### **DEC_VARS**
dec_vars : VAR dec_vars1 

#### **DEC_VARS1**
dec_vars1 : smp_type ID LBRACKET exp RBRACKET dec_vars3 SEMICOL dec_vars4
          | smp_type ID dec_vars2 SEMICOL dec_vars4
          | sp_type ID dec_vars2 SEMICOL dec_vars4

#### **DEC_VARS2**
dec_vars2 : COMMA ID dec_vars2
          | empty

#### **DEC_VARS3**
dec_vars3 : LBRACKET exp RBRACKET
          | empty

#### **DEC_VARS4**
dec_vars4 : dec_vars
          | empty

#### **SMP_TYPE**
smp_type : INT
         | FLOAT
         | CHAR

#### **SP_TYPE**
sp_type : FILE

#### **FUNCTION**
function : FUNC ID LPAREN param RPAREN ARROW smp_type LCURLY function1 block RETURN exp SEMICOL RCURLY
         | FUNC ID LPAREN param RPAREN ARROW VOID LCURLY function1 block RCURLY

#### **FUNCTION1**
function1 : dec_vars
          | empty

#### **PARAM**
param : smp_type ID param1
      | empty

#### **PARAM1**
param1 : COMMA smp_type ID param1 
       | empty

#### **BLOCK**
block : statement block 
      | empty

#### **STATEMENT**
statement : assignment
          | c_input
          | c_print
          | condition
          | for_loop
          | while_loop
          | std_func
          | sp_func

#### **ASSIGNMENT**
assignment : variable EQUAL assignment1 SEMICOL 

#### **ASSIGNMENT1**
assignment1 : exp
            | sp_func

#### **VARIABLE**
variable : ID variable1 

#### **VARIABLE1**
variable1 : LBRACKET exp RBRACKET variable2
          | empty

#### **VARIABLE2**
variable2 : LBRACKET exp RBRACKET 
          | empty

#### **C_INPUT**
c_input : INPUT variable c_input1 SEMICOL

#### **C_INPUT1**
c_input1 : COMMA variable c_input1
         | empty

#### **C_PRINT**
c_print : PRINT LPAREN c_print1 RPAREN SEMICOL

#### **C_PRINT1**
c_print1 : exp c_print2 
         | CTE_CHAR c_print2

#### **C_PRINT2**
c_print2 : COMMA c_print1
         | empty

#### **CONDITION**
condition : IF LPAREN exp RPAREN LCURLY block RCURLY condition1

#### **CONDITION1**
condition1 : ELSE LCURLY block RCURLY
           | empty

#### **FOR_LOOP**
for_loop : FOR ID IN RANGE LPAREN exp COMMA exp RPAREN LCURLY block RCURLY

#### **WHILE_LOOP**
while_loop : WHILE LPAREN exp RPAREN LCURLY block RCURLY

#### **STD_FUNC**
std_func : ID LPAREN std_func1 RPAREN 

#### **STD_FUNC1**
std_func1 : exp std_func2
          | empty

#### **STD_FUNC2**
std_func2 : COMMA exp std_func2
          | empty

#### **SP_FUNC**
sp_func : generate_key_func
        | file_func
        | crypto_func

#### **FILE_FUNC**
file_func : open_file
          | read_file
          | write_file
          | close_file

#### **CRYPTO_FUNC**
crypto_func : encrypt_func 
            | decrypt_func
            | hash_sha256 
            | hash_md5 

#### **GENERATE_KEY_FUNC**
generate_key_func : GENERATE_KEY LPAREN RPAREN 

#### **OPEN_FILE**
open_file : OPEN LPAREN CTE_CHAR RPAREN

#### **READ_FILE**
read_file : READ LPAREN ID RPAREN 

#### **WRITE_FILE**
write_file : WRITE LPAREN CTE_CHAR ID RPAREN

#### **CLOSE_FILE**
close_file : CLOSE LPAREN ID RPAREN

#### **ENCRYPT_FUNC**
encrypt_func : ENCRYPT LPAREN encrypt_func1 COMMA ID RPAREN

#### **ENCRYPT_FUNC1**
encrypt_func1 : CTE_CHAR
              | ID

#### **DECRYPT_FUNC**
decrypt_func : DECRYPT LPAREN decrypt_func1 COMMA ID RPAREN

#### **DECRYPT_FUNC1**
decrypt_func1 : CTE_CHAR
              | ID

#### **HASH_SHA256**
hash_sha256 : HASH_SHA256 LPAREN hash_sha2561 RPAREN

#### **HASH_SHA2561**
hash_sha2561 : CTE_CHAR
             | ID

#### **HASH_MD5**
hash_md5 : HASH_MD5 LPAREN hash_md51 RPAREN

#### **HASH_MD51**
hash_md51 : CTE_CHAR
          | ID

#### **EXP**
exp : t_exp exp1

#### **EXP1**
exp1 : OR exp
     | empty

#### **T_EXP**
t_exp : g_exp t_exp1

#### **T_EXP1**
t_exp1 : AND t_exp
       | empty

#### **G_EXP**
g_exp : m_exp g_exp1

#### **G_EXP1**
g_exp1 : GT m_exp 
       | LT m_exp 
       | GE m_exp 
       | LE m_exp 
       | EQ m_exp 
       | NE m_exp 
       | empty

#### **M_EXP**
m_exp : term m_exp1 

#### **M_EXP1**
m_exp1 : PLUS m_exp
       | MINUS m_exp
       | empty


#### **TERM**
term : factor term1

#### **TERM1**
term1 : TIMES term
      | DIVIDE term
      | empty

#### **FACTOR**
factor : LPAREN exp RPAREN
       | variable
       | std_func
       | CTE_INT
       | CTE_FLOAT
