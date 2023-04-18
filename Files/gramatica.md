# Mario Garza Chapa
# A01720245

#### **PROGRAMA**
PROG &rarr; PROG' main lbracket BLOQUE rbracket
PROG' &rarr; DEC_VAR | FUNCIONES | PROG' | empty

#### **DEC_VARS**
DEC_VARS &rarr;  var DEC_VAR | DEC_ARR

#### **DEC_VAR**
DEC_VAR &rarr; var DEC_VAR' id DEC_VAR'' semicol
DEC_VAR' &rarr; TIPO_COMP | TIPO_SIMPLE
DEC_VAR'' &rarr;  comma id DEC_VAR'' | empty
 
#### **DEC_ARR**
DEC_ARR &rarr; var TIPO_SIMPLE id lsbracket cte i rsbracket DEC_ARR' semicol
DEC_ARR' &rarr; lsbracket cte i rsbracket 

#### **FUNCTION**
FUNCTION &rarr; func id lparentheses  FUNCTION' rparentheses minus gt FUNCTION''
FUNCTION' &rarr; PARAM
FUNCTION'' &rarr; FUNCTION_TS | FUNCTION_VOID

#### **FUNCTION_VOID**
FUNCTION_VOID &rarr; void lbracket FUNCTION_VOID' BLOQUE rbracket
FUNCTION_VOID' &rarr; DEC_VARS FUNCTION_VOID' | empty

#### **FUNCTION_TS**
FUNCTION_TS &rarr; TIPO_SIMPLE lbracket FUNCTION_TS' BLOQUE return EXP semicol rbracket
FUNCTION_TS' &rarr; DEC_VARS FUNCTION_TS' | empty

#### **BLOQUE**
BLOQUE &rarr; ESTATUTO BLOQUE | empty 

#### **TIPO_SIMPLE**
TIPO_SIMPLE &rarr; int | float | char 

#### **TIPO_COMPUESTO**
TIPO_COMPUESTO &rarr; file

#### **PARAM**
PARAM &rarr; TIPO_SIMPLE id PARAM' 
PARAM' &rarr; comma id PARAM'| empty

#### **ESTATUTO**
ESTATUTO &rarr; ASIGNACION | LECTURA | ESCRITURA | CONDICION | FOR | WHILE | LLAMADA FUNC_ESP

#### **ASIGNACIÓN**
ASIGNACIÓN &rarr; VARIABLE equal EXP semicol 

#### **LECTURA**
LECTURA &rarr; input VARIABLE semicol

#### **ESCRITURA**
ESCRITURA &rarr; print lparentheses ESCRITURA' rparentheses semicol
ESCRITURA' &rarr; EXP ESCRITURA'' | cte c ESCRITURA''
ESCRITURA'' &rarr; comma ESCRITURA' | empty

#### **CONDICIÓN**
CONDICIÓN &rarr; if lparentheses EXP rparentheses lbracket BLOQUE rbracket CONDICION'
CONDICIÓN' &rarr; else lbracket BLOQUE rbracket | empty

#### **FOR**
FOR &rarr; for VARIABLE in range lparentheses EXP, EXP rparentheses lbracket BLOQUE rbracket

#### **WHILE**
WHILE &rarr; while lparentheses EXP rparentheses lbracket BLOQUE rparentheses

#### **LLAMADA**
LLAMADA &rarr; id lparentheses EXP LLAMADA' rparentheses
LLAMADA' &rarr; comma EXP LLAMADA' | empty

#### **FUNC_ESP**
FUNC_ESP &rarr; GENERAR_LLAVE | CIFRAR | DESCIFRAR | HASH_SHA256 | HASH_MD5 | LEER_ARCH | ESCRIBIR_ARCH | ABRIR_ARCH | CERRAR_ARCH

#### **GENERAR_LLAVE**
GENERAR_LLAVE &rarr; generate_key lparentheses rparentheses

#### **CIFRAR**
CIFRAR &rarr; encrypt lparentheses CIFRAR' comma cte c rparentheses
CIFRAR' &rarr; cte c | file

#### **DESCIFRAR**
DESCIFRAR &rarr; decrypt lparentheses DESCIFRAR' comma cte c rparentheses
DESCIFRAR' &rarr; cte c | file

#### **HASH_SHA256**
HASH_SHA256 &rarr; hash_sha265 lparentheses HASH_SHA256' comma cte c rparentheses
HASH_SHA256' &rarr; cte c | file

#### **HASH_MD5**
HASH_MD5 &rarr; HASH_MD5 lparentheses HASH_MD5' comma cte c rparentheses
HASH_MD5' &rarr; cte c | file

#### **LEER_ARCH**
LEER_ARCH &rarr; read lparentheses cte c rparentheses

#### **ESCRIBIR_ARCH**
ESCRIBIR_ARCH &rarr; write lparentheses cte c, EXP rparentheses

#### **ABRIR_ARCH**
ABRIR_ARCH &rarr; open lparentheses cte c rparentheses

#### **CERRAR_ARCH**
CERRAR_ARCH &rarr; close lparentheses cte c rparentheses

#### **EXP**
EXP &rarr; T_EXP EXP'
EXP' &rarr; or T_EXP | empty

#### **T_EXP**
T_EXP &rarr; G_EXP T_EXP'
T_EXP' &rarr; and T_EXP | empty

#### **G_EXP**
G_EXP &rarr; M_EXP G_EXP
G_EXP' &rarr; G_EXP'' M_EXP | empty
G_EXP'' &rarr; -gt | -lt | -ge | -le | -eq | -ne | empty

#### **M_EXP**
M_EXP &rarr; T M_EXP'
M_EXP' &rarr; M_EXP'' M_EXP | empty
M_EXP'' &rarr; plus | minus | empty

#### **T**
T &rarr; F T'
T' &rarr; T'' T | empty
T'' &rarr; \* | / | empty

#### **F**
F &rarr; F' | lparentheses EXP rparentheses
F' &rarr; cte i | cte f | cte c | VARIABLE | LLAMADA | empty

