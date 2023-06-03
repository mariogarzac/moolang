import json 
from cube import CONV
from VirtualMemory import * 

class Variable:
    def __init__ (self):
        self.varAttributes = {}

    def addVar(self, varId, varType, varXDims = 0 , varYDims = 0, address = 0):
        self.varAttributes = {varId :{"vType" : varType, "vXDims" : varXDims , "vYDims" : varYDims, "address": address}}

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
        self.memory = VirtualMemory()

    # <INSERTS>
    def addFunc(self, funcId, funcType):
        for name in self.funcDirectory.keys():
            if funcId == name:
                if funcType == self.funcDirectory[name]["fType"]:
                    print(f"ERROR: Function {funcId} with type {self.convertOp(funcType)} has already been declared")
                    exit()

        # Add function to function dictionary
        self.funcDirectory[funcId] = {}
        self.funcDirectory[funcId]["fType"] = funcType
        self.funcDirectory[funcId]["pointer"] = 0
        self.funcDirectory[funcId]["fResources"] = {CONV['int']:0, CONV['float']:0, CONV['char']:0, CONV['file']:0, CONV['bool']:0 },
        self.funcDirectory[funcId]["fParams"] = []
        self.funcDirectory[funcId]["fParamId"] = []


        # Add global variable with function name
        self.vars[CONV['local']]["fName"] = funcId
        self.vars[CONV['global']]["vars"][funcId] = {}
        self.vars[CONV['global']]["vars"][funcId].update({"vType" : funcType})
        
        # Set the address for the function variable
        address = self.setAddress(CONV['global'], funcId, funcType)
        self.vars[CONV['global']]["vars"][funcId].update({"address" : address})

    def addParam(self,funcId,paramId, paramType): 
        self.funcDirectory[funcId]["fParamId"].append(paramId)
        self.funcDirectory[funcId]["fParams"].append(paramType)

    def addVariable(self, scope, newVar):
        # get var id from newvar dictionary 
        varId = list(newVar.keys())[0]
        if (self.findVariable(scope,varId)):
            print(f"ERROR: A variable with name {varId} has already been declared.")
            exit()
        else:
            self.vars[scope]["vars"][varId] = {}
            self.vars[scope]["vars"][varId].update(newVar[varId])

            varType = self.vars[scope]["vars"][varId]["vType"]
            address = self.setAddress(scope, varId, varType)
            self.vars[scope]["vars"][varId]["address"] = address

    def findVariable(self,scope, varId):
        # find in local scope
        try:
            self.vars[scope]["vars"][varId]
            return True
        except KeyError:
            existsLocal = False
            pass

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
        try:
            return self.funcDirectory[funcId]["fParams"][:]
        except KeyError:
            print(f"ERROR: Functions with name {funcId} does not exist.")
            exit()

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
        try:
            return self.funcDirectory[funcId]["fType"]
        except KeyError:
            print(f"ERROR: Functions with name {funcId} does not exist.")
            exit()


    def getFuncPointer(self, funcId):
        return self.funcDirectory[funcId]["pointer"]

    # VIRTUAL MEMORY
    def setAddress(self, scope,varId, varType):
        try:
            xDims = self.vars[scope]["vars"][varId]["vXDims"]
            yDims = self.vars[scope]["vars"][varId]["vYDims"]
            size = xDims * yDims
        except KeyError:
            size = 1

        address = self.memory.createMoreMemory(scope, varType, size)
        self.vars[scope]["vars"][varId]["address"] = address
        return address

    def addConstant(self,scope, value, varType):
        if (scope == CONV['local']):
            address = self.memory.createMemory(scope, varType)
            self.memory.addToLocalMemory(address, varType)
        else:
            if (scope == CONV['constant']):
                constant = self.memory.findConstant(value)
                if (constant == None):
                    address = self.memory.createMemory(scope, varType)
                    self.memory.addToConstantMemory(address, value)
                else:
                    return constant
        return address
    
    def addTmpVariable(self, varType):
        return self.memory.createMemory(CONV['local'], varType)

    def addToMemory(self,scope):
        if (scope == CONV['global']):
            self.memory.addToGlobalMemory(address,varType)
        elif (scope == CONV['local']):
            self.memory.addToLocalMemory(address,varType)
        else:
            print("ERROR: Unknown scope")
            exit()

    def getVarAddress(self, varId):
        existsLocal = True
        try:
            return self.vars[CONV['local']]["vars"][varId]["address"] 
        except KeyError:
            existsLocal = False
            pass

        # find in global scope
        if (not existsLocal):
            try:
                return self.vars[CONV['global']]["vars"][varId]["address"]
            except KeyError:
                self.printVars()
                print(f"ERROR: Variable {varId} does not exist.")
                exit()

    def getFuncs(self):
        with open("func.json", "w") as file:
            json.dump(self.funcDirectory, file)

    def popLocalMemory(self):
        self.memory.popLocalMemory()

    # HELPER FUNCTIONS
    def clearVarTable(self):
        self.vars[CONV['local']] = {"fName" : 0, "vars" :{}}
        
    def printFuncDir(self):
        print(json.dumps(self.funcDirectory, indent=4, sort_keys=False))

    def printVars(self):
        print(json.dumps(self.vars, indent=4, sort_keys=False))
        
    def printMemory(self):
        self.memory.printMem()

    def convertOp(self, op):
            return list(CONV.keys())[list(CONV.values()).index(op)]
