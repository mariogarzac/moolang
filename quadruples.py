
'''
may a god bless your soul child
'''

from cube import CUBE

class Quadruple:
    def __init__(self, operator, leftOperand, rightOperand, temp):
        self.operator = operator
        self.leftOperand = leftOperand
        self.rightOperand = rightOperand
        self.temp = temp

    def printContents(self):
        print(f"contents: {self.operator} ,{self.leftOperand} ,{self.rightOperand} ,{self.temp}")

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

    # <POP POPS>
    def popOperator(self):
        return self.operatorStack.pop()

    def popOperand(self):
        return self.operandStack.pop()

    def popType(self):
        return self.typeStack.pop()

    def popJump(self):
        return self.jumpStack.pop()

    # <GET FROM STACK OR GET POINTER>
    def getOperator(self):
        return self.operatorStack[-1]

    def getOperand(self):
        return self.operandStack[-1]

    def getType(self):
        return self.typeStack[-1]

    def getJump(self):
        return self.jumpStack[-1]

    def getQuadPointer(self):
        return quadPointer

    def printTheQuads(self):
        for i in range(0, len(self.quads)):
            print(self.quads[i].printContents())

    def checkTypeMismatch(self, leftType, rightType, operator):
        try:
            if (CUBE[leftType][rightType][operator]):
                return CUBE[leftType][rightType][operator]
        except:
            print("ERROR: TypeMismatch")
            exit()

    def printStacks(self):
        print("TYPESTACK ", self.typeStack)
        print("OPERANDSTACK ", self.operandStack)
        print("OPERATORSTACK ", self.operatorStack)
        print("\n")


    def popParen(self):
        try:
            self.operatorStack.pop(self.operatorStack.index(10))
            self.typeStack.pop(self.typeStack.index(0))
        except ValueError:
            print("Not Found")

    def checkPending(self, op1, op2):
        length = len(self.operatorStack)
        for i in range(0, length - 1):
            if (self.operatorStack[i] == op1 or self.operatorStack[i] == op2):
                tmpPop = self.operatorStack.pop(i) 
                self.insertOperator(tmpPop)
                return
    

    # <HIT THE QUADS>
    def generateQuad(self):

        operator = self.popOperator()
        rightType = self.popType()
        leftType = self.popType()

        resType = self.checkTypeMismatch(leftType, rightType, operator)

        if (operator < 10):
            rightOperand = self.popOperand()
            leftOperand = self.popOperand()
            if (operator == 6):
                operator = '+'
                self.temp = leftOperand + rightOperand
            elif(operator == 7) :
                operator = '-'
                self.temp = leftOperand - rightOperand
            elif(operator == 8) :
                operator = '*'
                self.temp = leftOperand * rightOperand
            elif(operator == 9) :
                operator = '/'
                self.temp = leftOperand / rightOperand

            self.quads.append(Quadruple(operator, leftOperand, rightOperand, self.temp))
            self.insertOpAndType(self.temp, resType)
            print(operator, leftOperand, rightOperand, self.temp)

        else:
            if (operator == 12) :
                # Pop them to generate quad
                res = self.popOperand()
                operand = self.popOperand()

                # Reinsert them to add to variable
                self.insertOpAndType(operand, rightType)
                self.insertOpAndType(res, leftType)

                operator = '='

        self.quadPointer += 1

