import pprint as p
import json 
from cube import CONV

class Variable:
    def __init__ (self):
        self.varAttributes = {}

    def addVar(self, varId, varType, varXDims = 0 , varYDims = 0):
        self.varAttributes = {varId :{"vType" : varType, "vXDims" : varXDims , "vYDims" : varYDims}}

        return self.varAttributes

    def printVars(self):
        print(self.varAttributes)

    def clearV(self):
        self.varAttributes = {}

class FunctionDirectory:

    def __init__ (self):
        # set initial function entry as global
        self.funcDirectory = {"global" : {"fType":0, "pointer":0, "fResources":{CONV['int']:0, CONV['float']:0, CONV['char']:0, CONV['file']:0, CONV['bool']:0 }, "fParams": []}} 
        self.vars = {
                     CONV['global'] : {"fName" : "global", "vars" :{}},
                     CONV['local'] : {"fName" : 0, "vars" :{}}
                    }

    # <INSERTS>
    def addFunc(self, funcId, funcType):
        for name in self.funcDirectory.keys():
            if funcId == name:
                if funcType == self.funcDirectory[name]["fType"]:
                    print(f"ERROR: Function {funcId} with type {self.convertOp(funcType)} has already been declared")
                    exit()

        self.funcDirectory[funcId] = {}
        self.funcDirectory[funcId]["fType"] = funcType
        self.funcDirectory[funcId]["pointer"] = 0
        self.funcDirectory[funcId]["fResources"] = {CONV['int']:0, CONV['float']:0, CONV['char']:0, CONV['file']:0, CONV['bool']:0 },
        self.funcDirectory[funcId]["fParams"] = []
        self.vars[CONV['local']]["fName"] = funcId
        self.vars[CONV['global']]["vars"][funcId] = {}
        self.vars[CONV['global']]["vars"][funcId].update({"vType" : funcType})

    def addParam(self, scope, funcId, paramId, paramType): 
        self.funcDirectory[funcId]["fParams"].append(paramType)
        self.vars[scope]["vars"][paramId] = {}
        self.vars[scope]["vars"][paramId].update({"vType" : paramType})

    def addVariable(self, scope, newVar):
        # get var id from newvar dictionary 
        varId = list(newVar.keys())[0]
        self.vars[scope]["vars"][varId] = {}
        self.vars[scope]["vars"][varId].update(newVar[varId])

    def updateFuncType(self,funcId, fType):
        self.funcDirectory[funcId]["fType"] = fType

    def updatePointer(self,funcId, pointer):
        self.funcDirectory[funcId]["pointer"] = pointer

    def updateEra(self, funcId, eraTable):
        self.funcDirectory[funcId]["fResources"] =  {
                 CONV['int']   : eraTable[0], 
                 CONV['float'] : eraTable[1], 
                 CONV['char']  : eraTable[2],
                 CONV['file']  : eraTable[3], 
                 CONV['bool']  : eraTable[4]
                 }
                

    def getFuncParams(self, funcId):
        size = len(self.funcDirectory[funcId]["fParams"])
        return self.funcDirectory[funcId]["fParams"]

    # GET IT
    def getVarType(self,varId):
        # find in local scope
        existsLocal = True
        try:
            return self.vars[CONV['local']]["vars"][varId]["vType"]
        except KeyError:
            existsLocal = False
            pass

        # find in global scope
        if (not existsLocal):
            try:
                return self.vars[CONV['global']]["vars"][varId]["vType"]
            except KeyError:
                print(f"ERROR: Variable {varId} does not exist")
                exit()

    def getFuncName(self, scope):
        return self.vars[scope]["fName"]

    def getFuncType(self,funcId):
        return self.funcDirectory[funcId]["fType"]

    # HELPER FUNCTIONS
    def clearVarTable(self):
        self.vars[CONV['local']] = {"fName" : 0, "vars" :{}}
        
    def printFuncDir(self):
        print(json.dumps(self.funcDirectory, indent=4, sort_keys=False))

    def printVars(self):
        print(json.dumps(self.vars, indent=4, sort_keys=False))

    def convertOp(self, op):
            return list(CONV.keys())[list(CONV.values()).index(op)]

    # DEBUGGING
    def clearFD(self):
        self.funcDirectory = {"global" : {"fType":0, "pointer":0, "fResources":{}, "fParams": []}} 
        self.vars = {
                     CONV['global'] : {"fName" : "global", "vars" :{}},
                     CONV['local'] : {"fName" : 0, "vars" :{}}
                    }
