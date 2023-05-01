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
   
    def getVar(self):
        return self.varAttributes

    def addVar(self, varId, varType, varScope, varValue, varXDims = None, varYDims = None):
        self.varAttributes[varId] = {}
        self.varAttributes[varId]["varType"] = varType
        self.varAttributes[varId]["varScope"] = varScope
        self.varAttributes[varId]["varValue"] = varValue
        self.varAttributes[varId]["varXDims"] = varXDims
        self.varAttributes[varId]["varYDims"] = varYDims
        return self.varAttributes
    
    
    def printVars(self):
        pretty = json.dumps(self.varAttributes, indent=4)
        print(pretty)

class FunctionDirectory:

    def __init__ (self):
        # define main function as init
        # since functions will be addressed by number instead of name,
        # we start at 0
        self.funcCounter = 0
        self.funcDirectory = {self.funcCounter: 
                               {
                                "funcType" : 0,
                                "funcParams": {None},
                                "funcVars" : {None}
                               }
                              }

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
        self.funcDirectory[self.funcCounter]["funcVars"].update(newVar)
        # self.funcDirectory[self.funcCounter]["funcVars"]= howdy[varId]
        # self.funcDirectory[self.funcCounter]["funcVars"][varId]["varType"] =  howdy[varId]
        # self.funcDirectory[self.funcCounter]["funcVars"][varId]["varScope"] = howdy[varId][varScope]
        # self.funcDirectory[self.funcCounter]["funcVars"][varId]["varValue"] = howdy[varId][varValue]
        # self.funcDirectory[self.funcCounter]["funcVars"][varId]["varXDims"] = howdy[varId][varXDims]
        # self.funcDirectory[self.funcCounter]["funcVars"][varId]["varYDims"] = howdy[varId][varYDims]
        return self.funcDirectory

    def printFuncDir(self):
        p.pprint(self.funcDirectory)


vars = Variable()
funcs = FunctionDirectory()
tmp = vars.addVar("hello",1,20,4, None, None)
funcs.addVariable(tmp)
funcs.printFuncDir()





# funcs.addVariable("howdy",1,20,4, None, None)
# funcs.addVariable("greetings",1,20,4, None, None)
