
'''
TODO: Revisar cubo con la maestra
 - asingaciones
 - char
 - bools
'''

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
    'goto':          21,
    'gotof':         22,
    'gotov':         23,
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
    'generate_key':  34,
    'print':         35,
    'input':         36,
    'endfunc':       37
}



CUBE = {

        # int
        1: {
            1 : {
                6:   1,
                7:   1,
                8:   1,
                9:   2,
                12:  1,
                13:  5,
                14:  5,
                15:  5,
                16:  5,
                17:  5,
                18:  5,
                }, 

            2: {
                6:   2,
                7:   2,
                8:   2,
                9:   2,
                13:  5,
                14:  5,
                15:  5,
                16:  5,
                17:  5,
                18:  5,
                },

            3: {
                6:   3,
                7:   3,
                8:   3,
                9:   3,
                13:  5,
                14:  5,
                15:  5,
                16:  5,
                17:  5,
                18:  5,
                }
            }, 

        # float
        2: {
            1 : {
                6:   2,
                7:   2,
                8:   2,
                9:   2,
                12:  2,
                13:  5,
                14:  5,
                15:  5,
                16:  5,
                17:  5,
                18:  5,
                },

            2: {
                6:   2,
                7:   2,
                8:   2,
                9:   2,
                12:  2,
                13:  5,
                14:  5,
                15:  5,
                16:  5,
                17:  5,
                18:  5,
                },

            3: {
                6:   3,
                7:   3,
                8:   3,
                9:   3,
                13:  5,
                14:  5,
                15:  5,
                16:  5,
                17:  5,
                18:  5,
                }
            }, 

        # char
        3 : {
                1 : {
                    6:   3,
                    7:   3,
                    8:   3,
                    9:   3,
                    13:  5,
                    14:  5,
                    15:  5,
                    16:  5,
                    17:  5,
                    18:  5,
                    },

                2: {
                    6:   3,
                    7:   3,
                    8:   3,
                    9:   3,
                    13:  5,
                    14:  5,
                    15:  5,
                    16:  5,
                    17:  5,
                    18:  5,
                    },

                3: {
                    6:   3,
                    7:   3,
                    8:   3,
                    9:   3,
                    12:  3,
                    13:  5,
                    14:  5,
                    15:  5,
                    16:  5,
                    17:  5,
                    18:  5,
                   }
            },
           # File
           4: {
                3: {
                    12 : 4,
                    28 : 3
                   }
              },

           # File
           5: {
                5: {
                    13 : 5,
                    14 : 5,
                    15 : 5,
                    16 : 5,
                    17 : 5,
                    18 : 5,
                    19 : 5,
                    20 : 5,
                   }
              }

} # end

 

