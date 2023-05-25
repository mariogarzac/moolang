import pprint as p
import json 
from cube import CONV

class Variable:
    def __init__ (self):
        self.varAttributes = {}

    def addVar(self, varId, varType, varScope, varValue, varXDims = 0 , varYDims = 0):
        self.varAttributes = {varId :{"vType" : varType, "vScope" : varScope, "vValue" : varValue,\
                "vXDims" : varXDims , "vYDims" : varYDims}}
        return self.varAttributes

    def printVars(self):
        print(self.varAttributes)

    def clearV(self):
        self.varAttributes = {}

class FunctionDirectory:

    def __init__ (self):
        # define main function as init
        # since functions will be addressed by number instead of name,
        # we start at 0
        self.funcCounter = 0
        self.funcDirectory = {self.funcCounter: {"fName": 0, "fType" : 0, "fDir" : 0,"fResources": {CONV['int']:0, CONV['float']:0, CONV['char']:0, CONV['file']:0, CONV['bool']:0}, "fPTypes": [], "fVars" : {} } }

    def addFunc(self, funcId, funcType):
        # Search for the function to see if it has already been declared
        for i in range(0,self.funcCounter + 1):
            if funcId == self.funcDirectory[i]["fName"]:
                if funcType == self.funcDirectory[i]["fType"]:
                    fType = (list(CONV.keys())[list(CONV.values()).index(funcType)]) 
                    print(f"ERROR: Function {funcId} with type {fType} has already been declared")
                    exit()

        self.funcCounter += 1
        self.funcDirectory[self.funcCounter] = {}
        self.funcDirectory[self.funcCounter]["fName"] = funcId
        self.funcDirectory[self.funcCounter]["fType"] = funcType
        self.funcDirectory[self.funcCounter]["fPTypes"] = []
        self.funcDirectory[self.funcCounter]["fParams"] = {}
        self.funcDirectory[self.funcCounter]["fVars"] = {}

    def addParam(self, paramId, paramType): 
        self.funcDirectory[self.funcCounter]["fVars"].update({paramId : paramType})
        self.funcDirectory[self.funcCounter]["fPTypes"].append(paramType)

    def addVariable(self, newVar):
        # get var id from newvar dictionary 
        varId = list(newVar.keys())[0]

        # create a new dictionary with the varId and fill
        self.funcDirectory[self.funcCounter]["fVars"][varId] = {}
        self.funcDirectory[self.funcCounter]["fVars"][varId].update(newVar[varId])
        return self.funcDirectory

    def updateFuncDir(self, pointer):
        self.funcDirectory[self.funcCounter]["fDir"] = pointer - 1

    def assignValue(self,varId, value):
        existsLocal = True
        # print(varId)
        # find in local scope
        try:
            self.funcDirectory[self.funcCounter]["fVars"][str(varId)]["vValue"] = value
        except KeyError:
            # existsLocal = False
            pass

        if (not existsLocal):
            try:
                self.funcDirectory[0]["fVars"][str(varId)]["vValue"] = value
            except KeyError:
                print(f"ERROR: Variable {varId} does not exist")
                exit()

    def getVarType(self, varId):
        id = str(varId)
        # find in local scope
        try:
            return self.funcDirectory[self.funcCounter]["fVars"][id]["vType"]
        except KeyError:
            existsLocal = False
            pass

        # find in global scope
        if (not existsLocal):
            try:
                return self.funcDirectory[0]["fVars"][id]["vType"]
            except KeyError:
                print(f"ERROR: Variable {varId} does not exist")
                exit()

    def getFuncType(self):
        return self.funcDirectory[self.funcCounter]["fType"]

    def getFuncParams(self):
        return self.funcDirectory[self.funcCounter]["fPTypes"]

    def printFuncDir(self):
        print(json.dumps(self.funcDirectory, indent=4, sort_keys=False))

    # DEBUGGING
    def clearFD(self):
        self.printFuncDir()
        self.funcCounter = 0
        self.funcDirectory = {}
        self.funcDirectory = {self.funcCounter: {"fName": 0, "fType" : 0, "fDir" : 0,"fResources": {1:0, 2:0, 3:0, 4:0, 5:0}, "fPTypes": [], "fVars" : {} } }
