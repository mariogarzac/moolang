import pprint as p
import json 


'''
TODO:
    - Fix varaibles not appending to dict
    - Fix params not appending 
'''

class Variable:
    def __init__ (self):
        self.varAttributes = {}

    def addVar(self, varId, varType, varScope, varValue, varXDims = 0 , varYDims = 0):
        self.varAttributes = {varId :{"vType" : varType, "vScope" : varScope, "vValue" : varValue,\
                "vXDims" : varXDims , "vYDims" : varYDims}}

        return self.varAttributes

    def printVars(self):
        print(self.varAttributes)

class FunctionDirectory:

    def __init__ (self):
        # define main function as init
        # since functions will be addressed by number instead of name,
        # we start at 0
        self.funcCounter = 0
        self.funcDirectory = {self.funcCounter: {"fName": 0, "fType" : 0, "fParams": {}, "fVars" : {} } }

    def addFunc(self, funcId, funcType):
        # funcParams is a dictionary
        # funcVars is a dictionary
        self.funcCounter += 1

        self.funcDirectory[self.funcCounter] = {}
        self.funcDirectory[self.funcCounter]["fName"] = funcId
        self.funcDirectory[self.funcCounter]["fType"] = funcType
        self.funcDirectory[self.funcCounter]["fParams"] = {}
        self.funcDirectory[self.funcCounter]["fVars"] = {}

    def addParam(self, paramId, paramType): 
        self.funcDirectory[self.funcCounter]["fParams"].update({paramId : paramType})

    def addVariable(self, newVar):
        varId = list(newVar.keys())[0]
        self.funcDirectory[self.funcCounter]["fVars"][varId] = {}
        self.funcDirectory[self.funcCounter]["fVars"][varId].update(newVar[varId])
        return self.funcDirectory

    def assignValue(self,varId, value):
        self.funcDirectory[self.funcCounter]["fVars"][str(varId)]["vValue"] = value

    def getVarType(self, varId):
        id = str(varId)
        try:
            return self.funcDirectory[self.funcCounter]["fVars"][id]["vType"]
        except KeyError:
            print("ERROR: Variable does not exist")
            exit()
    

    def printFuncDir(self):
        print(json.dumps(self.funcDirectory, indent=4, sort_keys=False))
