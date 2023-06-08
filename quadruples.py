from cube import CUBE
from cube import CONV

class Quadruple:
    def __init__(self, operator, leftOperand, rightOperand, address):
        self.operator = operator
        self.leftOperand = leftOperand
        self.rightOperand = rightOperand
        self.address = address

    def printContents(self):
        #pretty print op
        try:
            operator = (list(CONV.keys())[list(CONV.values()).index(self.operator)]) 
            print(f"{operator} {self.leftOperand} {self.rightOperand} {self.address}")
        except ValueError:
            print(f"{self.operator} {self.leftOperand} {self.rightOperand} {self.address}")
    
    def getLeftOperand(self):
        return self.leftOperand

    def getRightOperand(self):
        return self.rightOperand
    
    def getOperator(self):
        return self.operator

    def getAddress(self):
        return self.address

class QuadrupleTable:

    # These stacks will hold the essential items to generate quadruples
    # The quadPointer will point to the next quadruple to be generated
    def __init__(self):
        self.typeStack = []
        self.operandStack = []
        self.operatorStack = []
        self.jumpStack = []
        self.quads = []
        self.paramCounter = 0
        self.quadPointer = 0
        self.eraTable = [0,0,0,0,0]

    # <INSERT INTO STACK>
    def insertOpAndType(self,newOperand, newType):
        # newType is a number so we use it to index the list
        self.eraTable[newType - 1] += 1
        self.typeStack.append(newType)
        self.operandStack.append(newOperand)

    def insertOperand(self, newOperand):
        self.operandStack.append(newOperand)

    def insertOperator(self, newOp):
        self.operatorStack.append(newOp)

    def insertJump(self):
        self.jumpStack.append(self.quadPointer)
        
    def insertFuncType(self, funcType):
        self.typeStack.append(funcType)

    # <POP POPS>
    def popOperator(self):
        return self.operatorStack.pop()

    def popOperand(self):
        return self.operandStack.pop()

    def popType(self):
        return self.typeStack.pop()

    def popJump(self):
        return self.jumpStack.pop()

    def popParen(self):
        try:
            self.operatorStack.pop(self.operatorStack.index(CONV['(']))
        except ValueError:
            print("Not Found")

    # <GET FROM STACK OR GET POINTER>
    def getOperator(self):
        try:
            return self.operatorStack[-1]
        except IndexError:
            pass

    def getOperand(self):
        return self.operandStack[-1]

    def getType(self):
        return self.typeStack[-1]

    def getJump(self):
        return self.jumpStack[-1]

    def getQuadPointer(self):
        return self.quadPointer

    def getParamCounter(self):
        return self.paramCounter

    # <TYPE CHECKING>
    def checkTypeMismatch(self, leftType, rightType, operator):
        try:
            if (CUBE[leftType][rightType][operator]):
                return CUBE[leftType][rightType][operator]
        except:
            lT = self.convertOp(leftType)
            rT = self.convertOp(rightType)
            self.printTheQuads()
            print(f"ERROR: TypeMismatch <{lT}, {rT}>")
            exit()

    # <PRINTS AND MISC>
    def printTheQuad(self):
        self.quads[len(self.quads) - 1].printContents()

    def printTheQuads(self):
        for i in range(0, len(self.quads)):
            print(i, end=" ") 
            self.quads[i].printContents()

    def printStacks(self):
        print("TYPESTACK",self.typeStack)
        print("OPERANDSTACK",self.operandStack)
        print("OPERATORSTACK",self.operatorStack)
        print("JUMPS",self.jumpStack)
        print("\n")

    def convertOp(self, op):
        return list(CONV.keys())[list(CONV.values()).index(op)]

    # QUADS---------------------------------------------------------------------
    # <HIT THE QUADS>
    def generateQuad(self,operator, resType, tmpAddress):

        if (operator == CONV['=']):
            res = self.popOperand()
            var = self.popOperand()
            self.quads.append(Quadruple(operator, res, None, var))
        else:
            rightOperand = self.popOperand()
            leftOperand = self.popOperand()

            self.quads.append(Quadruple(operator, leftOperand, rightOperand, tmpAddress))

            # After generating the quadruple, add the new value and type
            self.insertOpAndType(tmpAddress, resType)

        self.quadPointer += 1

    '''
    TODO: Validate vartypes with input types
    '''
    # <FUNCS>
    def generateStFunc(self, tmpAddress):
        operator = self.popOperator()
        if (operator == CONV['print']):
            operand = self.popOperand()
            self.quads.append(Quadruple(operator, None, None, operand))
        elif (operator == CONV['input']):
            self.quads.append(Quadruple(operator, None, None, tmpAddress))

        self.quadPointer += 1

    def generateEra(self):
        funcName = self.popOperand()
        self.quads.append(Quadruple(CONV['era'], None, None, funcName))
        self.quadPointer += 1

    def getEraTable(self):
        return self.eraTable

    def resetEra(self):
        self.eraTable = [0,0,0,0,0]

    def resetParamCounter(self):
        self.paramCounter = 0

    def incrementParamCounter(self):
        self.paramCounter += 1

    def generateParam(self):
        varName = self.popOperand()
        operand = self.popOperand()
        paramAddress = self.popOperand()
        self.quads.append(Quadruple(CONV['param'], paramAddress, None, operand))
        self.quadPointer += 1

    def verifyParams(self, fParams):
        # compare the amount of parameters sent and expected
        if (self.paramCounter == len(fParams)):
            while (fParams):
                argumentType = self.popType()
                paramType = fParams.pop()
                if (paramType != argumentType):
                    print(f"ERROR: Param is type {self.convertOp(paramType)} and argument is type {self.convertOp(argumentType)}.")
                    exit()
        else:
            print(f"ERROR: Expected {len(fParams)} and recieved {self.paramCounter}")
            exit()

    def checkReturn(self, hasReturn):
        if (not hasReturn):
            print("ERROR: Non-void functions need a return")
            exit()

    def generateReturn(self):
        funcType = self.popType()
        if (funcType == CONV['void']):
            print("ERROR: Void functions cannot have a return value.")
            exit()
        else:
            # Verify return type and function type before generating the quad
            returnType = self.popType()
            if (funcType == returnType):
                operator = self.popOperator()
                tmpAddress = self.popOperand()
                try:
                    funcAddress = self.popOperand()

                    self.quads.append(Quadruple(operator, funcAddress, None, tmpAddress))
                    self.quadPointer += 1
                except IndexError:
                    self.quads.append(Quadruple(operator, None, None, tmpAddress))
                    self.quadPointer += 1
            else:
                print(f"ERROR: Function is type {self.convertOp(funcType)} and return is type {self.convertOp(returnType)}.")
                exit()

    def generateFuncCall(self):
        pointer = self.popOperand() 
        funcName = self.popOperand() 
        tmpAddress = self.popOperand()
        
        self.quads.append(Quadruple(CONV['gosub'], None, funcName, f"${pointer}"))
        self.quadPointer += 1

        self.quads.append(Quadruple(CONV['='], funcName, None, tmpAddress))
        self.quadPointer += 1

    def assignStdFunc(self):
        funcName = self.popOperand()
        var = self.popOperand()

        funcType = self.popType()
        varType = self.popType()
        operator = self.popOperator()
        
        self.checkTypeMismatch(varType, funcType, operator)
        self.quads.append(Quadruple(operator, funcName, None, var))
        self.quadPointer += 1
    # -------------------------------------------------------------------------
    # <SPECIAL FUNCS>
    def generateOpen(self, tmpAddress):
        operator = self.popOperator()
        operand = self.popOperand()
        self.quads.append(Quadruple(operator, None, operand, tmpAddress))
        self.quadPointer += 1

    def generateFileFunc(self):
        operator = self.popOperator()

        if (operator == CONV['write']):
            # pop variables to keep stack clean
            varType = self.popType()
            self.popType()

            if (varType == CONV['file']):
                file = self.popOperand()
                string = self.popOperand()
                self.quads.append(Quadruple(operator, string, None, file))
                self.quadPointer += 1
            else:
                print("ERROR: Only files can be written")
                exit()

        elif (operator == CONV['close']):
            varType = self.popType()
            if (varType == CONV['file']):
                operand = self.popOperand()
                self.quads.append(Quadruple(operator, None, None, operand))
                self.quadPointer += 1
            else:
                print("ERROR: Only files can be closed")
                exit()

    def generateGKey(self,tmpAddress):
        self.quads.append(Quadruple(CONV['generate_key'], None, None, tmpAddress))
        self.quadPointer += 1

    def generateEncryptDecrypt(self,operator, key, keyType, file, fileType, tmpAddress):
        if (fileType == CONV['file'] or fileType == CONV['char']):
            self.quads.append(Quadruple(operator, file, key, file))
            self.quadPointer += 1
        else:
            if (operator == CONV['encrypt']):
                print("ERROR: Data to encrypt must be a string or a file.")
                exit()
            elif(operator == CONV['decrypt']):
                print("ERROR: Data to decrypt must be a string or a file.")
                exit()

    def generateHash(self,operator, operand, operandType, tmpAddress):
        if(operandType == CONV['file'] or operandType == CONV['char']):
            self.quads.append(Quadruple(operator, operand, None, tmpAddress))
            self.quadPointer += 1
        else: 
            print(f"ERROR: {operator} must have a string or file as an argument.")
            exit()

    def assignSpFunc(self):
        spFunc = self.popOperator()
        var = self.popOperand()
        address = self.quads[self.quadPointer - 1].address

        ops = [CONV['generate_key'], CONV['hash_md5'], CONV['hash_sha256'], CONV['encrypt'], CONV['decrypt']]

        if(spFunc == CONV['open']):
            argumentType = self.popType()
            if (argumentType == CONV['char']):
                varType = self.popType()
                if (varType == CONV['file'] or varType == CONV['char']):
                    self.quads.append(Quadruple(CONV['='], address, None, var))
                    self.quadPointer += 1
                else:
                    print("ERROR: Variable type must be file or string")
                    exit()
            else: 
                print(f"ERROR: Argument for open must be of type string, not {self.convertOp(argumentType)}")
                exit()

        elif(spFunc in ops):
            varType = self.popType()
            if (varType == CONV['char']):
                self.quads.append(Quadruple(CONV['='], address, None, var))
                self.quadPointer += 1
            else:
                print("ERROR: Var must be type char")
                exit()
    '''
    TODO: Check if tmpaddress is needed
    '''
    def assignInput(self, tmpAddress):
        operand = self.popOperand()
        operator = self.popOperator()
        self.quads.append(Quadruple(operator, tmpAddress, None, operand))
        self.quadPointer += 1


    # -------------------------------------------------------------------------
    # <GOTOs>
    def generateGotoF(self):
        resType = self.popType()
        # if (resType == CONV['bool']):
        res = self.popOperand()
        self.quads.append(Quadruple(CONV['gotof'], res, None, None))
        self.jumpStack.append(self.quadPointer) # jump back here
        self.quadPointer += 1
        # else:
        #     print(f"ERROR: Expression type must be of type bool, not {self.convertOp(resType)}.")
        #     exit()

    def generateGoto(self):
        gotof = self.popJump()
        self.quads.append(Quadruple(CONV['goto'],None, None, f"${gotof - 1}"))
        self.jumpStack.append(gotof) # to fill gotof while for
        self.quadPointer += 1
    
    # IF
    def generateGotoIf(self):
        self.quadPointer += 1
        self.quads.append(Quadruple(CONV['goto'],None, None, f"${self.quadPointer}"))

    def fillGotoIf(self):
        jump = self.popJump()
        self.quads[jump].address = f"${self.quadPointer}"

    def fillGotoF(self , mod):
        quadToFill = self.popJump()
        self.quads[quadToFill].address = f"${self.quadPointer +  mod}"

    # WHILE
    def fillGotoFWhile(self):
        quadToFill = self.popJump()
        self.quads[quadToFill].address = f"${self.quadPointer}"
 
    # FOR
    # generates control variable expression (first part)
    def generateForCounter(self):
       valueType = self.popType()
       varType = self.popType()
       if (self.checkTypeMismatch(valueType, varType, CONV['='])):
           variable = self.popOperand()
           value = self.popOperand()
           self.quads.append(Quadruple(CONV['='],value, None, variable))
           self.quadPointer += 1

    def generateForQuad(self):
        #validate types
        varType = self.popType()
        modType = self.popType()
        expType = self.popType()
        if (expType == CONV['bool']):
            variable = self.popOperand()
            modifier = self.popOperand()
            rLimit = self.popOperand()

            if (varType == modType):
                # initialize variable
                expression = self.popJump() - 2
                res = self.quads[expression].address

                prevRes = self.quads[self.quadPointer - 1].address

                # creates modifier quadruple
                self.quads.append(Quadruple(CONV['='], prevRes, None, variable))
                self.quadPointer += 1

                # create gotof quadruple
                self.quads.append(Quadruple(CONV['gotof'],res, None, None))
                self.insertJump() # insert quad of expression
                self.quadPointer += 1
            else: 
                print(f"ERROR: Control variable is type {self.convertOp(varType)} and modifier is type {self.convertOp(modType)}")
                exit()
        else:
            print(f"ERROR: For loop parameters must be of type int") 
            exit()

    def fillFGotoFor(self, seenFor):
        quadToFill = self.popJump()
        if (seenFor == 2):
            self.quads[quadToFill].address = f"${len(self.quads) - 1}"
        else:
            self.quads[quadToFill].address = f"${len(self.quads) + 1}"

        self.jumpStack.append(quadToFill -  2) 

    def generateGotoFor(self, seen):
        gotof = self.popJump()
        if (seen == 2):
            self.quads.append(Quadruple(CONV['goto'],None, None, f"${gotof - 3}"))
            # self.jumpStack.append(gotof) # to fill gotof while for
        else:
            self.quads.append(Quadruple(CONV['goto'],None, None, f"${gotof - 1}"))
        self.quadPointer += 1


    # moves the for control variable before the goto
    def moveCounterQuads(self):
        # Gets the quad position
        quadToMove = self.popJump() 

        # Pop quads
        expQuad = self.quads.pop(quadToMove)
        assignmentQuad = self.quads.pop(quadToMove)
        # assignmentQuad.address = expQuad.address
        
        # Insert quads into new position
        newPosition = len(self.quads) - 1
        self.quads.insert(newPosition, assignmentQuad)
        self.quads.insert(newPosition, expQuad)

    # -------------------------------------------------------------------------
    # ARRAYS
    def generateVerifyDims(self, xDim, yDim):
        self.popType()
        operand = self.getOperand()
        self.quads.append(Quadruple(CONV['ver'], f"${xDim}", f"${yDim}", operand))


    def addConstantK(self, tmpAddress):
        operand = self.popOperand()
        self.quads.append(Quadruple(CONV['+'], operand, None, tmpAddress))

    # -------------------------------------------------------------------------
    # MAIN and ENDFUNC
    def generateGotoMain(self):
        self.quads.append(Quadruple(CONV['main'], None, None, None))
        self.quadPointer += 1

    def fillGotoMain(self):
        self.quads[0].address = f"${self.quadPointer}"

    def generateEndfunc(self):
        self.quads.append(Quadruple(CONV['endfunc'], None, None, None))
        self.quadPointer += 1

    def generateEndprog(self):
        self.quads.append(Quadruple(CONV['endprog'], None, None, None))
        self.quadPointer += 1

    # # DEBUGGING
    # def clearQuads(self):
    #     self.typeStack = []
    #     self.operandStack = []
    #     self.operatorStack = []
    #     self.jumpStack = []
    #     self.eraTable = [0,0,0,0,0]
    #     self.quads = []
    #     self.quadPointer = 1
