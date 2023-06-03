from cryptography.fernet import Fernet, InvalidToken
import hashlib
import os
import pickle
from cube import CONV


class VirtualMachine:
    def __init__(self,quads, funcs, memory):
        self.quads = quads
        self.funcs = funcs
        self.memory = memory
        self.ip = 0
        self.control = 0
        self.file = ""
        self.fileNames = {}

        # for i in range(len(self.quads)):
        #     print(self.quads[i].operator, self.quads[i].leftOperand,self.quads[i].rightOperand, self.quads[i].address)

    def parseQuads(self, quad):
        rightOperand = 0
        leftOperand = 0
        address = 0
        
        operator = quad[self.ip].operator
        # print(self.quads[self.ip].operator, self.quads[self.ip].leftOperand,self.quads[self.ip].rightOperand, self.quads[self.ip].address)
        if (quad[self.ip].leftOperand != None):
            scope = self.memory.getScope(quad[self.ip].leftOperand)
            leftOperand = self.memory.getValue(scope, quad[self.ip].leftOperand)

        if (quad[self.ip].rightOperand != None):
            scope = self.memory.getScope(quad[self.ip].rightOperand)
            rightOperand = self.memory.getValue(scope, quad[self.ip].rightOperand)

        if (quad[self.ip].address != None):
            if ('$' in str(quad[self.ip].address)):
                address = int(quad[self.ip].address.replace('$', ''))
            else:
                address = quad[self.ip].address
                # scope = self.memory.getScope(quad[self.ip].rightOperand)
                # rightOperand = self.memory.getValue(scope, quad[self.ip].rightOperand)

        return operator, leftOperand, rightOperand, address

    def initialize(self):
        while (self.ip < len(self.quads)):
            atts = self.parseQuads(self.quads)
            operator = atts[0]
            leftOperand = atts[1]
            rightOperand = atts[2]
            address = atts[3]

            # print(f"now parsing quad {self.ip} with {atts}")
            if (operator == CONV['main']):
                self.ip = address - 1

            elif (operator == CONV['+']):
                value = leftOperand + rightOperand
                scope = self.memory.getScope(address)
                self.memory.setValue(scope, address, value)
                # print("address is +", address)

            elif(operator == CONV['-']):
                value = leftOperand - rightOperand
                scope = self.memory.getScope(address)
                self.memory.setValue(scope, address, value)
                # print("address is -", address)

            elif(operator == CONV['*']):
                value = leftOperand * rightOperand
                scope = self.memory.getScope(address)
                self.memory.setValue(scope, address, value)
                # print("address is *", address)

            elif(operator == CONV['/']):
                try:
                    value = leftOperand / rightOperand
                    scope = self.memory.getScope(address)
                    self.memory.setValue(scope, address, value)
                except ZeroDivisionError:
                    print("ERROR: Division by zero")
                    exit()

            elif(operator == CONV['=']):
                # print(f"value is {leftOperand}")
                scope = self.memory.getScope(address)
                self.memory.setValue(scope, address, leftOperand)

            elif(operator == CONV['print']):
                scope = self.memory.getScope(address)
                value = self.memory.getValue(scope, address)
                
                if(type(value) == bytes):
                        print(value)
                elif(type(value) == str):
                    if (value[1:-1] == r"\n"):
                        print("\n")
                    else:
                        print(value.replace('"', ''), end="")
                else:
                    print(value, end="")
                
            elif(operator == CONV['input']):
                scope = self.memory.getScope(address)
                typeToBe = self.memory.getType(address)
                value = input()
                if (typeToBe == CONV['int']):
                    self.memory.setValue(scope, address, int(value))
                elif (typeToBe == CONV['float']):
                    self.memory.setValue(scope, address, float(value))
                elif (typeToBe == CONV['char']):
                    self.memory.setValue(scope, address, float(value))

            # <RELATIONAL OPERATORS>
            elif(operator == CONV['-gt']):
                    value = leftOperand > rightOperand
                    scope = self.memory.getScope(address)
                    self.memory.setValue(scope, address, value)
            elif(operator == CONV['-ge']):
                    value = leftOperand >= rightOperand
                    scope = self.memory.getScope(address)
                    self.memory.setValue(scope, address, value)
            elif(operator == CONV['-lt']):
                    value = leftOperand < rightOperand
                    scope = self.memory.getScope(address)
                    self.memory.setValue(scope, address, value)
            elif(operator == CONV['-le']):
                    value = leftOperand <= rightOperand
                    scope = self.memory.getScope(address)
                    self.memory.setValue(scope, address, value)
            elif(operator == CONV['-eq']):
                if (leftOperand == rightOperand):
                    value = True
                else:
                    value = False
                scope = self.memory.getScope(address)
                self.memory.setValue(scope, address, value)
            elif(operator == CONV['-ne']):
                if (leftOperand != rightOperand):
                    value = True
                else:
                    value = False
                scope = self.memory.getScope(address)
                self.memory.setValue(scope, address, value)
            elif(operator == CONV['and']):
                    value = leftOperand and rightOperand
                    scope = self.memory.getScope(address)
                    self.memory.setValue(scope, address, value)
            elif(operator == CONV['or']):
                    value = leftOperand or rightOperand
                    scope = self.memory.getScope(address)
                    self.memory.setValue(scope, address, value)

            # <GOTOs>
            elif(operator == CONV['goto']):
                self.ip = address - 1

            elif(operator == CONV['gotof']):
                if (leftOperand == False):
                    self.ip = address - 1
            
            # <SPECIAL FUNCTIONS>
            elif(operator == CONV['open']):
                try:
                    self.file = open(rightOperand[1:-1], "rb+")
                    scope = self.memory.getScope(address)
                    self.memory.setValue(scope, address, self.file.read())
                    self.fileNames.update({address : rightOperand[1:-1]})

                except FileNotFoundError:
                    print("ERROR: File does not exist.")
                    exit()
            elif(operator == CONV['write']):
                if (not self.file.closed):
                    self.file.write(leftOperand[1:-1])
                else:
                    print("ERROR: Could not write to file. ")
                    exit()

            elif(operator == CONV['close']):
                try: 
                    self.file.close()
                    scope = self.memory.getScope(address)
                    self.memory.popAddress(scope, address)
                except ValueError:
                    pass

            elif(operator == CONV['encrypt']):
                try:
                    key = rightOperand
                    target = leftOperand

                    # If target is a string
                    if (type(target) == str):
                        newTarget = target.encode('utf-8')
                        encrypted_contents = Fernet(key).encrypt(newTarget)
                        scope = self.memory.getScope(address)
                        self.memory.setValue(scope, address, encrypted_contents)

                    # If target is a file
                    else:
                        fileName = self.memory.findKey(target)
                        file = self.fileNames[fileName]
                        if (file is not None):
                            with open (file, "wb") as fileToEncrypt:
                                fileToEncrypt.write(encrypted_contents)
                except TypeError:
                    print("ERROR: Value must be bytes or a string. Are you passing the file correctly?")
                    exit()
                except InvalidToken:
                    print(f"ERROR: Invalid token {target}.")
                    exit()


                    
            elif(operator == CONV['decrypt']):
                try:
                    key = rightOperand
                    target = leftOperand

                    decrypted_contents = Fernet(key).decrypt(target)

                    with open ("decrypted_file.txt", "wb") as fileToDecrypt:
                        fileToDecrypt.write(decrypted_contents)

                    scope = self.memory.getScope(address)
                    self.memory.setValue(scope, address, decrypted_contents)
                except TypeError:
                    print("ERROR: Value must be bytes or a string. Are you passing the file correctly?")
                    exit()
                except InvalidToken:
                    print(f"ERROR: Invalid token {target}.")
                    exit()
                    
            elif(operator == CONV['hash_md5']):
                try:
                    target = leftOperand
                    hash = hashlib.sha256()

                    hash.update(target)
                    hash_digest = hash.hexdigest()

                    scope = self.memory.getScope(address)
                    self.memory.setValue(scope, address, hash_digest)
                except TypeError:
                    print(f"ERROR: Unable to calculate the hash with current parameters.")
                    exit()

            elif(operator == CONV['hash_sha256']):
                try:
                    target = leftOperand
                    hash = hashlib.md5()

                    hash.update(target)
                    hash_digest = hash.hexdigest()

                    scope = self.memory.getScope(address)
                    self.memory.setValue(scope, address, hash_digest)
                except TypeError:
                    print(f"ERROR: Unable to calculate the hash with current parameters.")
                    exit()

            elif(operator == CONV['generate_key']):
                scope = self.memory.getScope(address)
                key = Fernet.generate_key()
                self.memory.setValue(scope, address, key)
            
            self.ip += 1
                                    

with open ('data.obj', 'rb') as file:
    data = pickle.load(file)

quads = data['quadruples']
funcs = data['funcDir']
memory  = data['memory']

vm = VirtualMachine(quads, funcs, memory)
vm.initialize()

# elif(operator == CONV['void']):
# elif(operator == CONV['int']):
# elif(operator == CONV['float']):
# elif(operator == CONV['char']):
# elif(operator == CONV['file']):
# elif(operator == CONV['bool']):

# elif(operator == CONV['local']):
# elif(operator == CONV['global']):
# elif(operator == CONV['constant']):



# elif(operator == CONV['return']):
# elif(operator == CONV['main']):
# elif(operator == CONV['gosub']):
# elif(operator == CONV['era']):
# elif(operator == CONV['param']):
# elif(operator == CONV['endfunc']):
