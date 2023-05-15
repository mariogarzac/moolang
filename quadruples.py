from cube import CUBE
from cube import CONV


class Quadruple:
    def __init__(self, operator, leftOperand, rightOperand, temp):
        self.operator = operator
        self.leftOperand = leftOperand
        self.rightOperand = rightOperand
        self.temp = temp

    def printContents(self):
        #pretty print op
        operator = (list(CONV.keys())[list(CONV.values()).index(self.operator)]) 
        print(f"{operator} {self.leftOperand} {self.rightOperand} {self.temp}")

class QuadrupleTable:

    # These stacks will hold the essential items to generate quadruples
    # The quadPointer will point to the next quadruple to be generated
    def __init__(self):
        self.typeStack = []
        self.operandStack = []
        self.operatorStack = []
        self.jumpStack = []
        self.quads = []
        self.quadPointer = 1
        self.temp = 0

    # <INSERT INTO STACK>
    def insertOpAndType(self,newOperand, newType):
        self.typeStack.append(newType)
        self.operandStack.append(newOperand)

    def insertOperator(self, newOp):
        self.operatorStack.append(newOp)

    def insertJump(self):
        # Subtract 1 because the pointer points to the next quad
        self.jumpStack.append(self.quadPointer - 1)

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

    # <TYPE CHECKING>
    def checkTypeMismatch(self, leftType, rightType, operator):
        try:
            if (CUBE[leftType][rightType][operator]):
                return CUBE[leftType][rightType][operator]
        except:
            lT = (list(CONV.keys())[list(CONV.values()).index(leftType)])            
            rT = (list(CONV.keys())[list(CONV.values()).index(rightType)])
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

    # <HIT THE QUADS>
    def generateQuad(self):
        operator = self.popOperator()
        rightType = self.popType()
        leftType = self.popType()
        resType = self.checkTypeMismatch(leftType, rightType, operator)

        if (operator != CONV['=']):
            rightOperand = self.popOperand()
            leftOperand = self.popOperand()

            self.quads.append(Quadruple(operator, leftOperand, rightOperand, self.temp))

            self.temp += 1

            # After generating the quadruple, add the new value and type
            self.insertOpAndType(self.temp, resType)

        else: # If operator is '='
            res = self.popOperand()
            var = self.popOperand()
            self.quads.append(Quadruple(operator, res, None, var))
            # self.operandStack.append(var)
            # self.operandStack.append(res)

        self.quadPointer += 1

    # <SPECIAL FUNCS>
    def generateFileFunc(self):
        operator = self.popOperator()

        if (operator == CONV['open']):
            operand = self.popOperand()
            self.quads.append(Quadruple(operator, None, operand, self.temp))

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
                self.printStacks()
            else:
                print("ERROR: Only files can be closed")
                exit()
        self.quadPointer += 1

    def assignSpFunc(self):
        operator = self.popOperator()
        var  = self.popOperand()
        self.popType()
        varType = self.popType()

        if (varType == CONV['file']):
            self.quads.append(Quadruple(operator, var, None, self.temp))
            self.temp += 1
            self.quadPointer += 1
        else:
            print("ERROR: Var type must be file")
            exit()

    def generateCryptoFunc(self):
        operator = self.popOperator()
        try:
            operand = self.popOperand()
            self.quads.append(Quadruple(operator, None, operand, self.temp))
        except IndexError:
            self.quads.append(Quadruple(operator, None, None, self.temp))
        self.temp += 1
        self.quadPointer += 1

    # <GOTOs>
    def generateGotoV(self):
        operator = self.popOperator()
        prevRes = self.popOperand()
        self.popType() # Pop the matching type to the operand
        print("goto")

    def generateGotoF(self):
        # Variables used to generate to gotoF quad
        operator = self.popOperator()
        prevRes = self.popOperand()
        self.popType() # Pop the matching type to the operand

        self.quads.append(Quadruple(operator,prevRes, None, 11))
        self.quadPointer += 1

    def generateGoto(self):
        operator = self.popOperator()
        self.quads.append(Quadruple(operator,None, None, 11))
        self.quadPointer += 1

    def fillGotoF(self):
        quadToFill = self.popJump()
        self.quads[quadToFill].temp = self.quadPointer - 1

    def fillGotoFAlt(self):
        quadToFill = self.popJump()
        self.quads[quadToFill].temp = self.quadPointer 


    def fillGoto(self):
        quadToFill = self.popJump() 
        self.quads[quadToFill].temp = self.quadPointer - 1

    def insertEndfunc(self):
        # operator = CONV['endfunc']
        self.quads.append(Quadruple(CONV['endfunc'], None, None, None))
        self.quadPointer += 1
