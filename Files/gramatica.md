# Mario Garza Chapa
# A01720245

#### **PROGRAM**
PROG &rarr; PROG' PROG'' main lbracket BLOCK rbracket
PROG' &rarr; DEC_VAR  PROG' | empty
PROG'' &rarr; FUNCTION PROG'' | empty

#### **DEC_VAR**
DEC_VAR &rarr; VARS DEC_ARR |  ARR DEC_ARR | empty

#### **VARS**
VARS &rarr; var VAR' id VAR'' semicol
VARS' &rarr; SP_TYPE | SMP_TYPE
VARS'' &rarr;  comma id VAR'' | empty
 
#### **ARR**
ARR &rarr; var SMP_TYPE id lsbracket cte_i rsbracket ARR' semicol
ARR' &rarr; lsbracket cte_i rsbracket | empty

#### **SMP_TYPE**
SMP_TYPE &rarr; int | float | char 

#### **SMP_TYPE**
SMP_TYPE &rarr; file

#### **FUNCTION**
FUNCTION &rarr; func id lparentheses  PARAM rparentheses minus gtsym FUNCTION'
FUNCTION' &rarr; FUNCTION_TS | FUNCTION_VOID

#### **FUNCTION_TS**
FUNCTION_TS &rarr; SMP_TYPE lbracket DEC_VARS BLOCK return EXP semicol rbracket

#### **FUNCTION_VOID**
FUNCTION_VOID &rarr; void lbracket DEC_VARS BLOCK rbracket

#### **PARAM**
PARAM &rarr; SMP_TYPE id PARAM' 
PARAM' &rarr; comma id PARAM'| empty

#### **BLOCK**
BLOCK &rarr; STATUS BLOCK | empty 

#### **STATUS**
STATUS &rarr; ASSIGNMENT | C_INPUT | C_PRINT | CONDITION | FOR_LOOP | WHILE_LOOP | FUNC_CALL 

#### **ASSIGNMENT**
ASSIGNMENT &rarr; VARIABLE equal EXP FUNC_CALL semicol 

#### **C_INPUT**
C_INPUT &rarr; input VARIABLE semicol

#### **C_PRINT**
C_PRINT &rarr; print lparentheses C_PRINT' rparentheses semicol
C_PRINT' &rarr; EXP C_PRINT'' | cte_c C_PRINT''
C_PRINT'' &rarr; comma C_PRINT' | empty

#### **CONDITION**
CONDITION &rarr; if lparentheses EXP rparentheses lbracket BLOCK rbracket CONDITION'
CONDITION' &rarr; else lbracket BLOCK rbracket | empty

#### **FOR_LOOP**
FOR_LOOP &rarr; for id in range lparentheses EXP, EXP rparentheses lbracket BLOCK rbracket

#### **WHILE_LOOP**
WHILE_LOOP &rarr; while lparentheses EXP rparentheses lbracket BLOCK rparentheses

#### **VARIABLE**
VARIABLE &rarr; id VARIABLE'
VARIABLE' &rarr;  lsbracket EXP rsbracket VARIABLE'' | empty
VARIABLE'' &rarr;  lsbracket EXP rsbracket

#### **FUNC_CALL**
FUNC_CALL &rarr; STD_FUNC | SP_FUNC

#### **STD_FUNC**
STD_FUNC &rarr; id lparentheses STD_FUNC' rparentheses
STD_FUNC' &rarr; EXP STD_FUNC'' | empty
STD_FUNC'' &rarr; comma EXP STD_FUNC'' | empty

#### **FUNC_ESP**
FUNC_ESP &rarr; GENERATE_KEY_FUNC | FILE_FUNC | CRYPTO_FUNC

#### **FILE_FUNC**
FILE_FUNC &rarr; OPEN_FILE | WRITE_FILE | READ_FILE | CLOSE_FILE

#### **CRYPTO_FUNC**
CRYPTO_FUNC &rarr; ENCRYPT_FUNC | DECRYPT_FUNC | HASH_SHA256 | HASH_MD5 

#### **GENERATE_KEY_FUNC**
GENERATE_KEY_FUNC &rarr; generate_key lparentheses rparentheses

#### **ENCRYPT_FUNC**
ENCRYPT_FUNC &rarr; encrypt lparentheses ENCRYPT_FUNC' comma id rparentheses
ENCRYPT_FUNC' &rarr; cte_c | id

#### **DECRYPT_FUNC**
DECRYPT_FUNC &rarr; decrypt lparentheses DECRYPT_FUNC' comma id rparentheses
DECRYPT_FUNC' &rarr; cte_c | id

#### **HASH_SHA256**
HASH_SHA256 &rarr; hash_sha265 lparentheses HASH_SHA256'  rparentheses
HASH_SHA256' &rarr; cte_c | id

#### **HASH_MD5**
HASH_MD5 &rarr; HASH_MD5 lparentheses HASH_MD5' rparentheses
HASH_MD5' &rarr; cte_c | id

#### **OPEN_FILE**
OPEN_FILE &rarr; open lparentheses cte_c rparentheses

#### **READ_FILE**
READ_FILE &rarr; read lparentheses id rparentheses

#### **WRITE_FILE**
WRITE_FILE &rarr; write lparentheses cte_c comma id rparentheses

#### **CLOSE_FILE**
CLOSE_FILE &rarr; close lparentheses id rparentheses

#### **EXP**
EXP &rarr; T_EXP EXP'
EXP' &rarr; or T_EXP | empty

#### **T_EXP**
T_EXP &rarr; G_EXP T_EXP'
T_EXP' &rarr; and T_EXP | empty

#### **G_EXP**
G_EXP &rarr; M_EXP G_EXP
G_EXP' &rarr; G_EXP'' M_EXP | empty
G_EXP'' &rarr; -gt | -lt | -ge | -le | -eq | -ne

#### **M_EXP**
M_EXP &rarr; TERM M_EXP'
M_EXP' &rarr; M_EXP'' M_EXP | empty
M_EXP'' &rarr; plus | minus 

#### **TERM**
TERM &rarr; FACTOR TERM'
TERM' &rarr; TERM'' TERM | empty
TERM'' &rarr;  TIMES | DIVIDE 

#### **FACTOR**
FACTOR &rarr;  lparentheses EXP rparentheses | FACTOR'
FACTOR' &rarr; cte_i | cte_f | cte_c | VARIABLE | FUNC_CALL | empty

