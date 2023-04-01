
class attribute:

    def __init__(self, index, attributes, name):
        self.index = index
        self.attributes = attributes
        self.name = name

    def getIndex(self):
        return self.index

    def getVal(self, boolVal):
        if boolVal == False:
            return self.attributes[0]
        else:
            return self.attributes[1]
    
    def getName(self):
        return self.name
