
class attribute:

    def __init__(self, attributes, index, name):
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

    #used to check and see the boolean value of an attribute's value.
    def searchVal(self, attribute):
        print("in searchVal now, attribute is " + attribute)
        if attribute == self.attributes[0]:
            print("Returning false -> " + attribute + " : " + self.attributes[0])
            return False
        elif attribute == self.attributes[1]:
            print("Returning true -> " + attribute + " : " + self.attributes[1])
            return True
        else:
            print(attribute + " doesn't match " + self.attributes[0] + ", or " + self.attributes[1] + ". Returning -1")
            return -1
