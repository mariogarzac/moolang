from cube import CONV
import json
'''
global
0 - 2999
int       0 -  999 
float  1000 - 1999 
char  2000 - 2499
file  2500 - 2749 
bool  2750 - 2999

local
3000 - 5999
int   3000 - 3999 
float 4000 - 4999 
char  5000 - 5499 
file  5500 - 5749 
bool  5750 - 5999 

const
6000 - 9999 
int   6000 - 6999 
float 7000 - 7999 
char  8000 - 8999 
file  9000 - 9499
bool  9500 - 9999 
'''
class VirtualMemory:

    def __init__(self): 
        # Set limits for the variables
        # GLOBAL
        self.local ={}
        self.constAndGlobal = {}

        self.globalIntStart = 0 
        self.globalIntEnd = 999 

        self.globalFloatStart =  1000 
        self.globalFloatEnd = 1999 

        self.globalCharStart =  2000 
        self.globalCharEnd = 2499 

        self.globalFileStart =  2500
        self.globalFileEnd = 2749 

        self.globalBoolStart =  2750 
        self.globalBoolEnd = 2999 

        # LOCAL
        self.localIntStart =  3000 
        self.localIntEnd = 3999 

        self.localFloatStart = 4000 
        self.localFloatEnd = 4999 

        self.localCharStart = 5000 
        self.localCharEnd = 5499 

        self.localFileStart = 5500 
        self.localFileEnd = 5749 

        self.localBoolStart = 5750 
        self.localBoolEnd = 5999 
        
        # CONSTANTS
        self.constIntStart = 6000 
        self.constIntEnd = 6999 

        self.constFloatStart = 7000 
        self.constFloatEnd = 7999 

        self.constCharStart = 8000  
        self.constCharEnd = 8999 

        self.constFileStart = 9000 
        self.constFileEnd = 9499 

        self.constBoolStart = 9500 
        self.constBoolEnd = 9999 

        # Initialize counters at the first available address
        # GLOBAL
        self.globalIntCounter = self.globalIntStart
        self.globalFloatCounter = self.globalFloatStart  
        self.globalCharCounter = self.globalCharStart
        self.globalFileCounter = self.globalFileStart
        self.globalBoolCounter = self.globalBoolStart

        # LOCAL
        self.localIntCounter = self.localIntStart  
        self.localFloatCounter = self.localFloatStart  
        self.localCharCounter = self.localCharStart  
        self.localFileCounter = self.localFileStart  
        self.localBoolCounter = self.localBoolStart  
        
        # CONSTANTS
        self.constIntCounter = self.constIntStart  
        self.constFloatCounter = self.constFloatStart  
        self.constCharCounter = self.constCharStart   
        self.constFileCounter = self.constFileStart  
        self.constBoolCounter = self.constBoolStart  
    
    #--------------------------------------------------------------------------
    # FUNCTIONS TO CREATE A SPACE IN MEMORY
    def createGlobalInt(self):
        if (self.globalIntCounter <= self.globalIntEnd):
            self.globalIntCounter += 1
            return self.globalIntCounter - 1
        else:
            print("There are no more global int variables left.")
            exit()

    def createGlobalFloat(self):
        if (self.globalFloatCounter <= self.globalFloatEnd):
            self.globalFloatCounter += 1
            return self.globalFloatCounter - 1
        else:
            print("There are no more global float variables left.")

    def createGlobalChar(self):
        if (self.globalCharCounter <= self.globalCharEnd):
            self.globalCharCounter += 1
            return self.globalCharCounter - 1
        else:
            print("There are no more global char variables left.")

    def createGlobalBool(self):
        if (self.globalBoolCounter <= self.globalBoolEnd):
            self.globalBoolCounter += 1
            return self.globalBoolCounter - 1
        else:
            print("There are no more global bool variables left.")

    def createGlobalFile(self):
        if (self.globalFileCounter <= self.globalFileEnd):
            self.globalFileCounter += 1
            return self.globalFileCounter - 1
        else:
            print("There are no more global file variables left.")

    def createLocalInt(self):
        if (self.localIntCounter <= self.localIntEnd):
            self.localIntCounter += 1
            return self.localIntCounter - 1
        else:
            print("There are no more local int variables left.")

    def createLocalFloat(self):
        if (self.localFloatCounter <= self.localFloatEnd):
            self.localFloatCounter += 1
            return self.localFloatCounter - 1
        else:
            print("There are no more local float variables left.")

    def createLocalChar(self):
        if (self.localCharCounter <= self.localCharEnd):
            self.localCharCounter += 1
            return self.localCharCounter - 1
        else:
            print("There are no more local char variables left.")

    def createLocalBool(self):
        if (self.localBoolCounter <= self.localBoolEnd):
            self.localBoolCounter += 1
            return self.localBoolCounter - 1
        else:
            print("There are no more local bool variables left.")

    def createLocalFile(self):
        if (self.localFileCounter <= self.localFileEnd):
            self.localFileCounter += 1
            return self.localFileCounter - 1
        else:
            print("There are no more local file variables left.")

    def createConstantInt(self):
        if (self.constIntCounter <= self.constIntEnd):
            self.constIntCounter += 1
            return self.constIntCounter - 1
        else:
            print("There are no more const int variables left.")

    def createConstantFloat(self):
        if (self.constFloatCounter <= self.constFloatEnd):
            self.constFloatCounter += 1
            return self.constFloatCounter - 1
        else:
            print("There are no more const float variables left.")

    def createConstantChar(self):
        if (self.constCharCounter <= self.constCharEnd):
            self.constCharCounter += 1
            return self.constCharCounter - 1
        else:
            print("There are no more const char variables left.")

    def createConstantBool(self):
        if (self.constBoolCounter <= self.constBoolEnd):
            self.constBoolCounter += 1
            return self.constBoolCounter - 1
        else:
            print("There are no more const bool variables left.")

    def createConstantFile(self):
        if (self.constFileCounter <= self.constFileEnd):
            self.constFileCounter += 1
            return self.constFileCounter - 1
        else:
            print("There are no more const file variables left.")

    # FUNCTION THAT USES OTHER CREATE FUNCTIONS TO MAKE A SPACE IN MEMORY
    def createMemory(self, scope, varType):
        address = 0
        if (scope == CONV['global']):
            if (varType == CONV['int']):
                address = self.createGlobalInt()
                self.addToGlobalMemory(address, varType)
            elif (varType == CONV['float']):
                address = self.createGlobalFloat()
                self.addToGlobalMemory(address, varType)
            elif (varType == CONV['char']):
                address = self.createGlobalChar()
                self.addToGlobalMemory(address, varType)
            elif (varType == CONV['file']):
                address = self.createGlobalFile()
                self.addToGlobalMemory(address, varType)
            elif (varType == CONV['bool']):
                address = self.createGlobalBool()
                self.addToGlobalMemory(address, varType)

        elif (scope == CONV['local']):
            if (varType == CONV['int']):
                address = self.createLocalInt()
                self.addToLocalMemory(address, varType)
            elif (varType == CONV['float']):
                address = self.createLocalFloat()
                self.addToLocalMemory(address, varType)
            elif (varType == CONV['char']):
                address = self.createLocalChar()
                self.addToLocalMemory(address, varType)
            elif (varType == CONV['file']):
                address = self.createLocalFile()
                self.addToLocalMemory(address, varType)
            elif (varType == CONV['bool']):
                address = self.createLocalBool()
                self.addToLocalMemory(address, varType)

        elif (scope == CONV['constant']):
            if (varType == CONV['int']):
                address = self.createConstantInt()
                self.addToConstantMemory(address, varType)
            elif (varType == CONV['float']):
                address = self.createConstantFloat()
                self.addToConstantMemory(address, varType)
            elif (varType == CONV['char']):
                address = self.createConstantChar()
                self.addToConstantMemory(address, varType)
            elif (varType == CONV['file']):
                address = self.createConstantFile()
                self.addToConstantMemory(address, varType)
            elif (varType == CONV['bool']):
                address = self.createConstantBool()
                self.addToConstantMemory(address, varType)
        else:
            print(f"ERROR: Unknown scope")
            exit()
        return address
        
    #--------------------------------------------------------------------------
    # GETTERS
    def getType(self, address):
        if ((address >= self.localIntStart and address <= self.localIntEnd) or (address >= self.globalIntStart and address <= self.globalIntEnd) or (address >= self.constIntStart and address <= self.constIntEnd)):
            return CONV['int']
        elif ((address >= self.localFloatStart and address <= self.localFloatEnd) or (address >= self.globalFloatStart and address <= self.globalFloatEnd) or (address >= self.constFloatStart and address <= self.constFloatEnd)):
            return CONV['float']
        elif ((address >= self.localCharStart and address <= self.localCharEnd) or (address >= self.globalCharStart and address <= self.globalCharEnd) or (address >= self.constCharStart and address <= self.constCharEnd)):
            return CONV['char']
        elif ((address >= self.localBoolStart and address <= self.localBoolEnd) or (address >= self.globalBoolStart and address <= self.globalBoolEnd) or (address >= self.constBoolStart and address <= self.constBoolEnd)):
            return CONV['bool']
        elif ((address >= self.localFileStart and address <= self.localFileEnd) or (address >= self.globalFileStart and address <= self.globalFileEnd) or (address >= self.constFileStart and address <= self.constFileEnd)):
            return CONV['file']
        else:
            print("WHAT?! Atte. Your friendly neighborhood vars :*")
            exit()

    def getScope(self,address):
        if (address >= self.localIntStart and address <= self.localBoolEnd):
            return CONV['global']
        elif (address >= self.globalIntStart and address <= self.globalBoolEnd):
            return CONV['local']
        elif (address >= self.constIntStart and address <= self.constBoolEnd):
            return CONV['constant']
        else:
            print("WHAT?! Atte. Your friendly neighborhood vars :*")
            exit()

    # THIS FUNCTION WILL BE USED BY ARRAYS
    def createMoreMemory(self, scope, varType, size=1):
        firstAddress = self.createMemory(scope, varType)

        for i in range(1,size):
            self.createMemory(scope,varType)

        return firstAddress
    #--------------------------------------------------------------------------
    # FUNCTIONS TO ADD A VARIABLE TO THE MEMORY
    def addToLocalMemory(self,address, varType):
        if (varType == CONV['float']):
            self.local.update({address : 0.0})
        elif (varType == CONV['bool']):
            self.local.update({address : False})
        elif (varType == CONV['char']):
            self.local.update({address: ""})
        else:
            self.local.update({address : 0})

    def addToGlobalMemory(self, address, varType):
        if (varType == CONV['float']):
            self.constAndGlobal.update({address : 0.0})
        elif (varType == CONV['bool']):
            self.constAndGlobal.update({address : False})
        elif (varType == CONV['char']):
            self.constAndGlobal.update({address: ""})
        else:
            self.constAndGlobal.update({address : 0})

    def addToConstantMemory(self, address, value):
        self.constAndGlobal.update({address : value})

    #--------------------------------------------------------------------------
    # PRINT MEMORY
    def printMem(self):
        print(json.dumps(self.local, indent=4, sort_keys=False))
        print(json.dumps(self.constAndGlobal, indent=4, sort_keys=False))


