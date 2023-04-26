
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
    def insertNewIdAndType(self, newType, newId):
        self.typeStack.append(newType)
        self.operandStack.append(newId)

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
        self.quads[0].printContents()

    def checkTypeMismatch(self, leftType, rightType, operator):
        try:
            if (CUBE[leftType][rightType][operator]):
                print("Types are valid")
                return CUBE[leftType][rightType][operator]
        except:
            print("ERROR: TypeMismatch")
            exit()

    # <HIT THE QUADS>
    def generateQuad(self):
        leftType = self.popType()
        leftOperand = self.popOperand()

        rightType = self.popType()
        rightOperand = self.popOperand()

        operator = self.popOperator()

        self.checkTypeMismatch(leftType, rightType, operator)
        
        self.quads.append(Quadruple(operator, leftOperand, rightOperand, self.temp))

        self.quadPointer += 1


q = QuadrupleTable()

q.insertNewIdAndType('int', 'x')
q.insertOperator('+')
q.insertNewIdAndType('int', 's')
print(q.typeStack)
print(q.operandStack)
print(q.operatorStack)
q.generateQuad()
q.printTheQuads()
