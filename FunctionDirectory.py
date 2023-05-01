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
        self.varAttributes[varId] = {}
        self.varAttributes[varId]["varType"] = varType
        self.varAttributes[varId]["varScope"] = varScope
        self.varAttributes[varId]["varValue"] = varValue
        self.varAttributes[varId]["varXDims"] = varXDims
        self.varAttributes[varId]["varYDims"] = varYDims
        return self.varAttributes

    def getVars(self):
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

    def addVariable(self, var): # varType, varScope, varValue, varXDims = None, varYDims = None
        self.funcDirectory[self.funcCounter]["funcVars"] = var
        return self.funcDirectory

        # self.funcDirectory[funcCounter][funcVars].update(varId) 
        # return vars.addVar(varId, varType, varScope, varValue, varXDims, varYDims)

    def printFuncDir(self):
        # pretty = json.dumps(self.funcDirectory, indent=4)
        # print(pretty)
        p.pprint(self.funcDirectory)


vars = Variable()
funcs = FunctionDirectory()
funcs.addVariable(vars.addVar(1,2,3,4))
vars.addVar(5,6,7,8)
vars.addVar(9,10,11,12)
funcs.addFunc("func1", "int", None, vars.getVars())
funcs.printFuncDir()

        # self.varAttributes.update({varId :
        #                         {"varType" : varType ,
        #                          "varScope" : varScope,
        #                          "varValue" : varValue,
        #                          "varXDims" : varXDims,
        #                          "varYDims" : varYDims,
        #                         }
        #                      })
