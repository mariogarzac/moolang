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
        self.address = 0

    # <INSERT INTO STACK>
    def insertOpAndType(self,newOperand, newType):
        self.typeStack.append(newType)
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

    def incrementParamCounter(self):
        self.paramCounter += 1

    def resetParamCounter(self):
        self.paramCounter = 0

    # <TYPE CHECKING>
    def checkTypeMismatch(self, leftType, rightType, operator):
        try:
            if (CUBE[leftType][rightType][operator]):
                return CUBE[leftType][rightType][operator]
        except:
            lT = self.convertOp(leftType)
            rT = self.convertOp(rightType)
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
    def generateQuad(self):
        operator = self.popOperator()
        rightType = self.popType()
        leftType = self.popType()
        resType = self.checkTypeMismatch(leftType, rightType, operator)

        if (operator == CONV['=']):
            res = self.popOperand()
            var = self.popOperand()
            self.quads.append(Quadruple(operator, res, None, var))
        else:
            rightOperand = self.popOperand()
            leftOperand = self.popOperand()

            self.address += 1
            self.quads.append(Quadruple(operator, leftOperand, rightOperand, self.address))

            # After generating the quadruple, add the new value and type
            self.insertOpAndType(self.address, resType)

        self.quadPointer += 1

    def generateStFunc(self):
        '''
        TODO: Validate vartypes with input types
        '''
        self.popType() # Pop the type since it is not need for the print stmnt... at the moment
        operator = self.popOperator()
        if (operator == CONV['print']):
            operand = self.popOperand()
            self.quads.append(Quadruple(operator, None, None, operand))
        elif (operator == CONV['input']):
            operand = self.popOperand()
            operator = self.popOperator()
            self.quads.append(Quadruple(operator, None, operand, self.address))
            self.address += 1

        self.quadPointer += 1

    def assignInput(self):
        operator = CONV['input']#self.popOperator()
        self.quads.append(Quadruple(operator, None, None, self.address))
        self.quadPointer += 1
        self.address += 1

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
                operand = self.popOperand()
                self.quads.append(Quadruple(operator,None , None, operand))
                self.quadPointer += 1
            else:
                print(f"ERROR: Function is type {self.convertOp(funcType)} and return is type {self.convertOp(returnType)}.")
                exit()

    def generateFuncCall(self, fParams):
        # get func param types and verify types
        if (self.paramCounter == len(fParams)):
            while (fParams):
                argumentType = self.popType()
                paramType = fParams.pop()
                if (paramType != argumentType):
                    print(f"ERROR: Param is type {self.convertOp(paramType)} and argument is type {self.convertOp(argumentType)}.")
                    exit()
                else:
                    var = self.popOperand()
                    pass

            funcName = self.popOperand() 
            self.quads.append(Quadruple(CONV['gosub'], None, None, funcName))
            self.quadPointer += 1
        else:
            print(f"ERROR: Expected {len(fParams)} and recieved {self.paramCounter}")
            exit()


    # -------------------------------------------------------------------------
    # <SPECIAL FUNCS>
    def generateFileFunc(self):
        operator = self.popOperator()

        if (operator == CONV['open']):
            operand = self.popOperand()
            self.quads.append(Quadruple(operator, None, operand, self.address))
            self.quadPointer += 1

        elif (operator == CONV['write']):
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

    def generateCryptoFunc(self):
        operator = self.popOperator()

        if (operator == CONV['generate_key']):
            self.quads.append(Quadruple(operator, None, None, self.address))
            self.quadPointer += 1

        elif (operator == CONV['encrypt'] or operator == CONV['decrypt']):
            key = self.popOperand()
            keyType = self.popType()
            file = self.popOperand()
            fileType = self.popType()
            if (fileType == CONV['file'] or fileType == CONV['char']):
                self.quads.append(Quadruple(operator, file, key, self.address))
                self.address += 1
                self.quadPointer += 1
            else:
                print("ERROR: Data to encrypt must be a string or a file.")
                exit()
    
        elif (operator == CONV['hash_sha256'] or operator == CONV['hash_md5']):
            operand = self.popOperand()
            operandType = self.popType()
            if(operandType == CONV['file'] or operandType == CONV['char']):
                self.quads.append(Quadruple(operator, operand, None, self.address))
                self.quadPointer += 1
                self.address += 1
            else: 
                print(f"ERROR: {operator} must have a string or file as an argument.")
                exit()

    def assignSpFunc(self):
        spFunc = self.popOperator()
        operator = self.popOperator()
        var = self.popOperand()

        ops = [CONV['generate_key'], CONV['hash_md5'], CONV['hash_sha256']]

        if(spFunc == CONV['open']):
            argumentType = self.popType()
            if (argumentType == CONV['char']):
                varType = self.popType()
                if (varType == CONV['file']):
                    self.quads.append(Quadruple(operator, self.address, None, var))
                    self.quadPointer += 1
                    self.address += 1
                else:
                    print("ERROR: Var type must be file")
                    exit()
            else: 
                print(f"ERROR: Argument for open must be of type char, not {self.convertOp(argumentType)}")
                exit()

        elif(spFunc in ops):
            varType = self.popType()
            if (varType == CONV['char']):
                self.quads.append(Quadruple(operator, self.address, None, var))
                self.address += 1
                self.quadPointer += 1
            else:
                print("ERROR: Var must be type char")
                exit()



    # -------------------------------------------------------------------------
    # <GOTOs>
    def generateGotoF(self):
        resType = self.popType()
        if (resType == CONV['bool']):
            res = self.popOperand()
            self.quads.append(Quadruple(CONV['gotof'], res, None, None))
            self.jumpStack.append(self.quadPointer)
            self.quadPointer += 1
        else:
            print(f"ERROR: Expression type must be of type bool, not {self.convertOp(resType)}.")
            exit()

    def generateGoto(self):
        gotof = self.popJump()
        self.quads.append(Quadruple(CONV['goto'],None, None, gotof - 1))
        self.jumpStack.append(gotof)
        self.quadPointer += 1

    # IF
    def generateGotoIf(self):
        self.quads.append(Quadruple(CONV['goto'],None, None, len(self.quads)))
        self.fillGotoF()

        self.jumpStack.append(self.quadPointer)
        self.quadPointer += 1

    def fillGotoF(self):
        quadToFill = self.popJump()
        self.quads[quadToFill].address = len(self.quads)

    # WHILE
    def fillGotoFWhile(self):
        quadToFill = self.popJump()
        self.quads[quadToFill].address = self.quadPointer
 
    # FOR
    def generateForQuad(self):
        #validate types
        varType = self.popType()
        modType = self.popType()
        expType = self.popType()
        if (expType == CONV['bool']):
            variable = self.popOperand()
            modifier = self.popOperand()
            rLimit = self.popOperand()
            operator= self.popOperator()

            if (varType == modType):
                # initialize variable
                self.quads.append(Quadruple(operator, self.address, None, variable))
                self.quadPointer += 1
                self.address += 1

                # create gotof quadruple
                expression = self.popJump() 
                res = self.quads[expression].address
                self.quads.append(Quadruple(CONV['gotof'],res , None, None))
                self.insertJump() # fill goto
                self.insertJump() # fill gotof
                self.quadPointer += 1
                self.address += 1
            else: 
                print(f"ERROR: Control variable is type {self.convertOp(varType)} and modifier is type {self.convertOp(modType)}")
                exit()
        else:
            print(f"ERROR: For loop parameters must be of type int") 
            exit()

    # generates for counter expression
    def generateForCounter(self):
        valueType = self.popType()
        varType = self.popType()
        operator = self.popOperator()
        if (self.checkTypeMismatch(valueType, varType, operator)):
            variable = self.popOperand()
            value = self.popOperand()
            self.quads.append(Quadruple(operator,value, None, variable))
            self.quadPointer += 1

    def fillFGotoFor(self):
        quadToFill = self.popJump()
        self.quads[quadToFill].address = len(self.quads) + 1 
        self.jumpStack.append(quadToFill -  2) 

    def moveCounterQuads(self):
        # Gets the quad position
        quadToMove = self.popJump() 

        # Pop quads
        assignmentQuad = self.quads.pop(quadToMove)
        expQuad = self.quads.pop(quadToMove)
        
        # Insert quads into new position
        newPosition = len(self.quads) - 1
        self.quads.insert(newPosition, expQuad)
        self.quads.insert(newPosition, assignmentQuad)
        
    # -------------------------------------------------------------------------
    # MAIN and ENDFUNC
    def generateGotoMain(self):
        self.quads.append(Quadruple(CONV['main'], None, None, None))
        self.quadPointer += 1

    def fillGotoMain(self):
        self.quads[0].address = self.quadPointer - 1

    def generateEndfunc(self):
        self.quads.append(Quadruple(CONV['endfunc'], None, None, None))
        self.quadPointer += 1

    # DEBUGGING
    def clearQuads(self):
        self.typeStack = []
        self.operandStack = []
        self.operatorStack = []
        self.jumpStack = []
        self.quads = []
        self.quadPointer = 1
        self.address = 0
