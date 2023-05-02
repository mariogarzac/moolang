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

    def addVar(self, varId, varType, varScope, varValue, varXDims = None, varYDims = None):
        self.varAttributes = {varId :{"varType" : varType, "varScope" : varScope, "varValue" : varValue,\
                "varXDims" : varXDims , "varYDims" : varYDims}}

        # #self.funcDirectory[self.funcCounter]["funcVars"]= {}
        # self.varAttributes = {}
        # self.varAttributes[varId] = {}
        # self.varAttributes[varId]["varType"] = varType
        # self.varAttributes[varId]["varScope"] = varScope
        # self.varAttributes[varId]["varValue"] = varValue
        # self.varAttributes[varId]["varXDims"] = varXDims
        # self.varAttributes[varId]["varYDims"] = varYDims
        return self.varAttributes

class FunctionDirectory:

    def __init__ (self):
        # define main function as init
        # since functions will be addressed by number instead of name,
        # we start at 0
        self.funcCounter = 0
        self.funcDirectory = {self.funcCounter: { "funcType" : 0, "funcParams": {}, "funcVars" : {} } }

    def addFunc(self, funcId, funcType, funcParams = None, funcVars = None):
        # funcParams is a dictionary
        # funcVars is a dictionary
        self.funcCounter += 1

        self.funcDirectory[self.funcCounter] = {}
        self.funcDirectory[self.funcCounter]["funcType"] = funcType
        self.funcDirectory[self.funcCounter]["funcParams"] = funcParams
        self.funcDirectory[self.funcCounter]["funcVars"] = funcVars

    def addParams(self, paramId, paramType): 
        self.funcDirectory[self.funcCounter]["funcParams"].update(paramId, paramType)

    def addVariable(self, newVar):
        varId = list(newVar.keys())[0]
        self.funcDirectory[self.funcCounter]["funcVars"][varId] = {}
        self.funcDirectory[self.funcCounter]["funcVars"][varId].update(newVar[varId])
        return self.funcDirectory

    def printFuncDir(self):
        p.pprint(self.funcDirectory)
