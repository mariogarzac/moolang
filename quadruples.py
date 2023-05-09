from cube import CUBE
from cube import CONV


class Quadruple:
    def __init__(self, operator, leftOperand, rightOperand, temp):
        self.operator = operator
        self.leftOperand = leftOperand
        self.rightOperand = rightOperand
        self.temp = temp

    def printContents(self):
        print(f"{self.operator} {self.leftOperand} {self.rightOperand} {self.temp}")

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

    def popParen(self):
        try:
            self.operatorStack.pop(self.operatorStack.index(10))
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
        return quadPointer

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

    def printStacks(self):
        print("TYPESTACK",self.typeStack)
        print("OPERANDSTACK",self.operandStack)
        print("OPERATORSTACK",self.operatorStack)
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

            self.temp += 1
            operator = (list(CONV.keys())[list(CONV.values()).index(operator)]) #pretty print op
            self.quads.append(Quadruple(operator, leftOperand, rightOperand, self.temp))

            # After generating the quadruple, add the new value and type
            self.insertOpAndType(self.temp, resType)

        elif (operator == CONV['=']):
            res = self.popOperand()
            var = self.popOperand()
            self.quads.append(Quadruple(operator, res, None, var))
            self.operandStack.append(var)
            self.operandStack.append(res)

        self.printTheQuad()
        self.quadPointer += 1
