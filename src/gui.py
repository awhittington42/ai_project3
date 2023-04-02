from tkinter import *
import tkinter as tk
import sys
import os
import fnmatch
import itertools
import attribute
import driver
import random

sys.path.append("..")
class ProjectGui:

    allObjects = []
    user_attributes = []
    user_constraints = []
    penalty_preferences = []
    possi_preferences = []
    quali_preferences = []
    feasible_objects = []

    def createinstance(self):
        print("createinstance invoked!")

    def getConstraints(self):
        return ProjectGui.user_constraints

    def getObjects(self):
        return ProjectGui.allObjects

    def getAttributes(self):
        return ProjectGui.user_attributes

    def getPenalty(self):
        return ProjectGui.penalty_preferences

    def getPoss(self):
        return ProjectGui.possi_preferences

    def getQual(self):
        return ProjectGui.quali_preferences

    def clean():
        ProjectGui.allObjects = []
        ProjectGui.user_attributes = []
        ProjectGui.user_constraints = []
        ProjectGui.penalty_preferences = []
        ProjectGui.possi_preferences = []
        ProjectGui.quali_preferences = []

    def loadWidgets(self, root):
        self.mainframe = tk.Frame(self.root)
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.createInstanceTextVar = StringVar(value ="Create Instance")
        self.createInstanceBtn = tk.Button(self.mainframe, textvariable=self.createInstanceTextVar, command=self.createinstance)
        self.createInstanceBtn.grid(row=0, column=0, sticky=(W, E))
        self.loadInstanceTextVar = StringVar(value = "Load Instance")
        self.loadInstanceBtn = tk.Button(self.mainframe, textvariable=self.loadInstanceTextVar, command=self.loadinstance)
        self.loadInstanceBtn.grid(row=1, column=0, sticky=(W, E))
        quitButton = tk.Button(self.mainframe, text='Quit', command=ProjectGui.quitgui)
        quitButton.grid(row=2, column=0, sticky=(W, W))
        self.instanceLabelTextVar = StringVar(value = "Current Instance: ")
        self.instanceLabel = tk.Label(self.mainframe, textvariable=self.instanceLabelTextVar)
        self.instanceLabel.grid(row=3, column=0, sticky=(W, E))
        self.existenceButton = tk.Button(self.mainframe, text='Existence', command=self.existence)
        self.exempButton = tk.Button(self.mainframe, text='Exemplification', command=self.exemp)
        self.optimizeButton = tk.Button(self.mainframe, text='(Omni)optimization', command=self.optimize)
        self.instanceInfo = StringVar(self.mainframe, value="No Instance Detected")
        self.instanceText = tk.Label(self.mainframe, textvariable=self.instanceInfo)
        self.instanceText.grid(row=3, column=1, sticky=(N, W, E, S))

    def loadinstance(self):
        print("loadinstance called!")
        ProjectGui.clean()
        self.existenceButton.grid_forget()
        self.exempButton.grid_forget()
        self.optimizeButton.grid_forget()
        self.instanceLabel.grid_forget()
        self.instanceText.grid_forget()
        self.loadInstanceBtn.grid_forget()
        self.loadInstanceTextVar.set("Enter Filename & click me.")
        self.fname = StringVar()
        self.fname_entry = tk.Entry(self.mainframe, width=10, textvariable=self.fname)
        self.loadInstanceBtn.configure(command=self.parseAttributes)
        self.loadInstanceBtn.grid(row=1, column=1, sticky=(W,E))
        self.fname_entry.focus()
        self.fname_entry.grid(row=1, column=0, sticky=(W, E))
        self.createInstanceTextVar.set("Enter attribute filename below")
        #self.root.bind("<Return>", lambda: self.parseAttributes(fname))

    def instanceLoaded(self):
        self.fname_entry.delete(0, END)
        self.fname_entry.grid_forget()
        self.loadInstanceBtn.grid_forget()
        self.loadInstanceTextVar.set("Load New Instance")
        self.loadInstanceBtn.configure(command=self.loadinstance)
        self.loadInstanceBtn.grid(row=1, column=0, sticky=(W,E))
        self.createInstanceTextVar.set("Create New Instance")
        self.createInstanceBtn.grid(row=0, column=0, sticky=(W,E))
        self.pref_label.destroy()
        self.pref_type1.destroy()
        self.pref_type2.destroy()
        self.pref_type3.destroy()
        self.existenceButton.grid(row=0, column=1, sticky=(W,E))
        self.exempButton.grid(row=1, column=1, sticky=(W,E))
        self.optimizeButton.grid(row=2, column=1, sticky=(W,E))
        self.updateInstanceInfo()

        #reversing order of combos so it starts with 0/false.
        temp = []
        ctr = len(ProjectGui.allObjects) - 1
        while ctr >= 0:
            temp.append(ProjectGui.allObjects[ctr])
            ctr -= 1
        ProjectGui.allObjects = temp
        #print(ProjectGui.allObjects)

    def updateInstanceInfo(self):
        info = []
        attCount = 0
        info.append("Attributes")
        #want to have attributes listed, number of objects, etc..
        for a in ProjectGui.user_attributes:
            if ProjectGui.user_attributes.index(a) % 3 == 0:
                attCount += 1
                info.append(a)

        #now we have all attributes housed in list, with "Attributes" preceeding
        #now add constraints info
        info.append("Constraints")
        for c in ProjectGui.user_constraints:
            info.append(c)

        #now time to gather preference info.
        info.append("Penalty Logic")
        for p in ProjectGui.penalty_preferences:
            info.append(p)
        info.append("Possibilistic Logic")
        for i in ProjectGui.possi_preferences:
            info.append(p)
        info.append("Qualitative Choice Logic")
        for q in ProjectGui.quali_preferences:
            info.append(q)

        #Now populate bottom of Gui with info.
        holderString1 = ""
        string2 = False
        holderString2 = ""
        constraintCtr = 1
        for item in info:
            if type(item) == list:
                for x in item:
                    if string2:
                        holderString2 += x + ", "
                    else:
                        if constraintCtr == 2:
                            holderString1 += x + ", "
                            constraintCtr = 1
                        else:
                            holderString1 += x + " OR "
                            constraintCtr += 1
            elif item == "Attributes" or item == "Constraints":
                holderString1 += "\n" + item
                holderString1 += ":\n"
            elif item == "Penalty Logic":
                string2 = True
                holderString2 += "\n" + item
                holderString2 += ":\n"
            elif item == "Possibilistic Logic" or item == "Qualitative Choice Logic":
                string2 = True
                holderString2 += "\n" + item
                holderString2 += ":\n"
            elif string2:
                holderString2 += item + ", "
            else:
                holderString1 += item + ", "

        self.instanceLabelTextVar.set(holderString1)
        #self.instanceInfo.set(holderString2)
        #self.instanceText.grid(row=3, column=1, sticky=(N,W,E,S))
        self.instanceLabel.grid(row=3, column=0, sticky=(N,W,E,S))


    def quitgui():
        #print("quitgui called!")
        sys.exit(0)

    def existence(self):
        #print("existence called!")
        """
        # existence means figure out what objects out of all possible combos satisfy
        # the constraints.
        # So I need to begin by taking in the constraints and actually parsing them.
        # Need to add functionality to recognize logic and NOT etc...
        # Raw idea: Go through the object list, and assign the truth value of each
        # tuple index to their respective attribute type. So in this 3 attribute
        # example, we have dissert correspond to first tuple index, drink will be
        the 2nd tuple index, and main will be the third. Go through each tuple and
        build out a comparison between the truth values of each attribute, and the
        constraints. This means the program will need to recognize attribute names
        and that a NOT in front of that attribute means False essentially.
        """
        attObjects = []
        nameCtr = 0
        atname = ""
        temp = []
        ctr = 0
        #First I need to get the attributes and build out a list of attribute objcts
        for a in ProjectGui.user_attributes:
            if ctr == 2:
                at = attribute.attribute(temp, nameCtr - 1, atname)
                temp = []
                #print("Appending " + atname)
                attObjects.append(at)
                atname = ""
                ctr = 0
            if ProjectGui.user_attributes.index(a) % 3 == 0:
                atname += str(a)
                nameCtr += 1
            else:
                #print("Appending " + str(a) + " to temp")
                temp.append(a)
                ctr+= 1
        at = attribute.attribute(temp, nameCtr - 1, atname)
        attObjects.append(at)

        # To get attribute values from constraints:
        # First loop into the main list, where you will access each sublist
        # which each contain the two parts of a clause that are implicitly
        # linked with an OR
        # boolConstraints will house the attribute value
        boolConstraints = []
        for li in ProjectGui.user_constraints:
            tmp = li[0][0:3]
            if tmp == "NOT":
                #print("In Not conditional")
                tmpAtt = li[0][4:]
                tpl = self.findAttribute(attObjects, tmpAtt)
                a = tpl[0]
                # truthval = complement of the attribute's truth value, since NOT
                if tpl[1] == False:
                    #print("false truth value in NOT conditional, change to True.")
                    truthVal = True
                elif tpl[1] == True:
                    #print("true truth value in NOT conditional, change to False.")
                    truthVal = False
                else:
                    pass
                    #print("Error, unexpected truthVal")
                #print(a.getName() + " is attribute, " + str(truthVal) + " is truthVal, " + tmpAtt + " is tmpAtt, adding to boolConstraints")
                boolConstraints.append(a)
                boolConstraints.append(truthVal)
            else:
                tpl = self.findAttribute(attObjects, li[0])
                a = tpl[0]
                truthVal = tpl[1]
                #print(a.getName() + " is attribute, " + str(truthVal) + " is truthVal, " + li[0] + " is li[0], adding to boolConstraints")
                boolConstraints.append(a)
                boolConstraints.append(truthVal)
                #print("a is " + a.getName() + ", li[0] is " + li[0])

            # now for 2nd element, seperate with OR.
            boolConstraints.append("OR")
            tmp = li[1][0:3]
            if tmp == "NOT":
                #print("In NOT conditional")
                tmpAtt = li[1][4:]
                tpl = self.findAttribute(attObjects, tmpAtt)
                a = tpl[0]
                if tpl[1] == False:
                    #print("false truth value in NOT conditional, change to true")
                    truthVal = True
                elif tpl[1] == True:
                    #print("true truth value in NOT conditional, change to false")
                    truthVal = False
                else:
                    pass
                    #print("unexpected truthVal, error.")
                #print(a.getName() + " is attribute, " + str(truthVal) + " is truthVal, " + tmpAtt + " is tmpAtt, adding to boolConstraints")
                boolConstraints.append(a)
                boolConstraints.append(truthVal)
            else:
                tpl = self.findAttribute(attObjects, li[1])
                a = tpl[0]
                truthVal = tpl[1]
                #print(a.getName() + " is attribute, " + str(truthVal) + " is truthVal, " + li[1] + " is li[1], adding to boolConstraints")
                boolConstraints.append(a)
                boolConstraints.append(truthVal)

        # Loop through all objects, compare each to all constraint elements, if they
        # match, then it is feasible, otherwise it's not.

        feasible = []
        #boolFlag = True
        #print(str(len(ProjectGui.allObjects)))
        for x in ProjectGui.allObjects:
            temp = []
            boolCtr = 0
            boolFlag = True
            #print("In outer loop")
            for y in boolConstraints:
                #print("In inner loop")
                if boolFlag == False:
                    #print("boolFlag is false, breaking out of inner loop")
                    break
                #print("checking if type - " + str(type(y)) + " is equal to bool")
                if type(y) == bool:
                    #print("Type was bool, incrementing boolCtr from " + str(boolCtr) + ", to " + str(boolCtr + 1) + " and appending y")
                    boolCtr += 1
                    temp.append(y)
                else:
                    temp.append(y)
                if boolCtr ==2:
                    #print("BoolCtr is 2, calling logicCompare.")
                    #print("temp is")
                    #print(temp)
                    # Compare constraints to object
                    boolFlag = self.logicCompare(temp, x)
                    boolCtr = 0
                    temp = []
            #print("Made it through inner loop, checking if boolFlag is still True")
            if boolFlag == True:
                #print("it was, adding x and its index to feasible")
                feasible.append(x)
                feasible.append(ProjectGui.allObjects.index(x))

        #Have feasible, now just need to transform the list
        #into the corresponding attribute truth values
        new_feasible = []

        for f in feasible:
            temp = []
            tmpInt = -1
            for a in attObjects:
                if type(f) == tuple:
                    temp.append(a.getVal(f[a.getIndex()]))
                else:
                    tmpInt = f
            if len(temp) > 0:
                new_feasible.append(temp)
            if tmpInt >= 0:
                new_feasible.append(tmpInt)


        #print(feasible)
        #print(new_feasible)

        ProjectGui.feasible_objects = new_feasible

        print("Feasible:")
        listTemp = ""
        for item in new_feasible:
            indexTemp = ""
            if type(item) == list:
                for x in item:
                    #print(x)
                    listTemp += x + " "
                    #print("listTemp is " + listTemp)
            if type(item) == int:
                #print(str(item))
                indexTemp +=str(item) + ": "
                #print("indexTemp is " + indexTemp)
                print("o" + indexTemp + listTemp)
                listTemp = ""

            #fullString = indexTemp + listTemp
            #print(fullString)

    def logicCompare(self, constraints, obj):
        index = constraints[0].getIndex()
        val = constraints[1]
        #print("In logicCompare. index is " + str(index) + ", val is " + str(val))
        #print("Comparing " + str(obj[index]) + " to " + str(val))
        if str(obj[index]) == str(val):
            #print("It was true, returning true")
            return True
        else:
            #print("It was false, checking next clause")
            # first clause is false, check 2nd, since it's an OR
            index = constraints[3].getIndex()
            val = constraints[4]
            #print("in next clause, index is " + str(index) + ", val is " + str(val))
            #print("Comparing " + str(obj[index]) + " to " + str(val))
            if str(obj[index]) == str(val):
                #print("It was true, returning true.")
                return True
            else:
                #print("2nd clause was also false, returning false")
                return False

    def findAttribute(self, attObjects, name):
        # reverse lookup an attribute based on one of their values.
        #print("Finding attribute:")
        for a in attObjects:
            val = a.searchVal(name)
            if val == -1:
                #print(name + " is not in " + str(a.getName()) + "going to next")
                next
            else:
                #print("findAttribute either returned false or true, returning " + a.getName())

                return (a, val)
        # If couldn't find attribute, return -1
        #print("Couldn't find the attribute, returning -1.")
        return -1

    def exemp(self):
        print("exemp called!")
        # exemplification means to generate two random feasible objects, and
        # then display the preference relationship between the two objects.
        # First need to randomly select two feasible objects from the list.
        # Then need to look at all the preferences to see what relationship exists between them

        if len(ProjectGui.feasible_objects) == 0:
            #Not enough feasible objects, exemp impossible
            print("Impossible to generate 2 feasible objects")
        else:

            random_num1 = random.randint(0, len(ProjectGui.feasible_objects) - 1)
            random_num2 = random.randint(0, len(ProjectGui.feasible_objects) - 1)
            #print(ProjectGui.feasible_objects)
            rand_feasible1 = ProjectGui.feasible_objects[random_num1]
            rand_feasible2 = ProjectGui.feasible_objects[random_num2]
            while type(rand_feasible1) == int or type(rand_feasible2) == int or rand_feasible1 == rand_feasible2:
                rand_num = random.randint(0, len(ProjectGui.feasible_objects))
                if type(rand_feasible1) == int:
                    rand_feasible1 = ProjectGui.feasible_objects[rand_num]
                else:
                    rand_feasible2 = ProjectGui.feasible_objects[rand_num]
            print("Random feasible object # 1 generated: ")
            print(rand_feasible1)

            print("Random feasible object # 2 generated: ")
            print(rand_feasible2)

            print("Penalty Logic \n")
            print(ProjectGui.penalty_preferences)
            print("Possibility Logic \n")
            print(ProjectGui.possi_preferences)
            print("Qualitative Choice Logic \n")
            print(ProjectGui.quali_preferences)

            # Now I can start comparing preference info to the
            # Two objects and see which gets better scores
            feas1_penalty_score = 0
            feas1_possi_score = 0.0
            feas2_penalty_score = 0
            feas2_possi_score = 0.0
            feas1_true = False
            feas2_true = False
            andOperator = False
            #Penalty Logic
            for p in ProjectGui.penalty_preferences:
                if "AND" in p[0]:
                    print("AND detected, splitting with AND")
                    splitList = p[0].split("AND")
                    print(splitList)
                    andOperator = True
                else:
                    print("OR detected, splitting with OR")
                    splitList = p[0].split("OR")
                    print(splitList)
                    andOperator = False
                literal1 = splitList[0].strip()
                literal2 = splitList[1].strip()
                if andOperator:
                    print("AND operator detected")
                    if literal1 in rand_feasible1 and literal2 in rand_feasible1:
                        feas1_true = True
                    if literal1 in rand_feasible2 and literal2 in rand_feasible2:
                        feas2_true = True
                else:
                    print("OR operator detected")
                    if literal1 in rand_feasible1 or literal2 in rand_feasible1:
                        feas1_true = True
                    if literal1 in rand_feasible2 or literal2 in rand_feasible2:
                        feas2_true = True
                if feas1_true == False:
                    feas1_penalty_score += int(p[1])
                if feas2_true == False:
                    feas2_penalty_score += int(p[1])
            print("End of penalty logic:")
            print("feas1 penalty score: " + str(feas1_penalty_score))
            print("feas2 penalty score: " + str(feas2_penalty_score))


            # Possibilistic Logic
            for p in ProjectGui.possi_preferences:
                if "AND" in p[0]:
                    print("AND detected, splitting with AND")
                    splitList = p[0].split("AND")
                    print(splitList)
                    andOperator = True
                else:
                    print("OR detected, splitting with OR")
                    splitList = p[0].split("OR")
                    print(splitList)
                    andOperator = False
                literal1 = splitList[0].strip()
                literal2 = splitList[1].strip()
                if andOperator:
                    print("AND operator detected")
                    if literal1 in rand_feasible1 and literal2 in rand_feasible1:
                            feas1_true = True
                    if literal1 in rand_feasible2 and literal2 in rand_feasible2:
                            feas2_true = True
                else:
                    print("OR operator detected")
                    if literal1 in rand_feasible1 or literal2 in rand_feasible1:
                        feas1_true = True
                    if literal1 in rand_feasible2 or literal2 in rand_feasible2:
                        feas2_true = True
                if feas1_true == False:
                    feas1_possi_score = 1.0 - float(p[1])
                if feas2_true == False:
                    feas2_possi_score = 1.0 - float(p[1])
            print("End of possibilistic logic:")
            print("feas1 possibilistic score: " + str(feas1_possi_score))
            print("feas2 possibilistic score: " + str(feas2_possi_score))

            """
            # Qualitative Choice Logic
            qualList = []
            preferredList1 = []
            preferredList2 = []
            for p in ProjectGui.quali_preferences:
                for x in p:
                    qualList.append[x]
                #now all parts of first clause is gathered.
                print(qualList[-1])
                if qualList[-1] == "IF":
                    #Last element is if, so applies to all.
                    for q in qualList:
                        if q in rand_feasible1:
                            preferredList1.append(q)
                        if q in rand_feasible2:
                            preferredList2.append(q)
                else:
                    pass
            """







    def optimize(self):
        print("optimize called!")
        # optimize is two buttons in one. So first need to get user input to see
        # if user wants to just optimize, that is, find one optimal Object, or
        # if user wants to omni-optimize, which means finding ALL optimal objects.
        self.createInstanceTextVar.set("Omnioptimization")
        self.createInstanceBtn.configure(command = self.omniopt)
        self.createInstanceBtn.grid(row=3, column=1, sticky = (W,E))
        self.optimizeButton.configure(text='Optimization', command=self.opt)

    def omniopt(self):
        pass

    def opt(self):
        pass

    #create initial frame and set up grid, to then create and place buttons within
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("CAP4630 Project 3")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.loadWidgets(self.root)
        self.root.mainloop()

    def parseAttributes(self):
        fName = self.fname.get()
        self.fname_entry.delete(0, END)
        attributes = []
        attributeNames = []
        #getting other directory path for TestCase files

        cur_path = os.path.dirname(__file__)
        print(str(cur_path))
        filePath = os.path.join(cur_path, '..', 'TestCase', fName)
        #print("successfully reached parseAttributes, path is" + str(filePath))
        with open(filePath, "r") as infile:
            for line in infile:
                rawAttributes = []
                #First split to get attribute type and then options.
                rawAttributes = line.split(":")
                print(rawAttributes)
                # if the list length is only 1, then there is an error in the file syntax
                print(str(len(rawAttributes)))
                if len(rawAttributes) == 2:
                    #now get the actual attributes, in the 2nd index(1) of the rawAttributes list.
                    temp  = rawAttributes[1].split(",")
                    for item in temp:
                        item = item.replace("\n", "")
                        item = item.replace(" ", "")
                        attributes.append(item)
                    print(attributes)
                    attributeNames.append(rawAttributes[0])
                    print(attributeNames)
                else:
                    print("Error - Invalid file syntax. Please ensure the files follow the form of \'Name: item1, item2, ...\'")
                    sys.exit(-1)

        #Add attribute name and attributes to global user_attributes variable
        nameCtr = 0
        for item in attributes:
            if len(ProjectGui.user_attributes) % 3 == 0:
                #Attribute Name
                ProjectGui.user_attributes.append(attributeNames[nameCtr])
                nameCtr += 1
            ProjectGui.user_attributes.append(item)

        #print(ProjectGui.user_attributes)
        self.createInstanceTextVar.set("Now Enter Constraints filename:")
        self.loadInstanceBtn.configure(command=self.parseConstraints)
        #self.loadInstanceBtn.grid(row=1, column=1, sticky=(W, E))

    def parseConstraints(self):
        fName = self.fname.get()
        self.fname_entry.delete(0, END)
        cur_path = os.path.dirname(__file__)
        filePath = os.path.join(cur_path, '..', 'TestCase', fName)
        #print("successfully reached parseConstraints, path is" + str(filePath))

        with open(filePath, "r") as infile:
            for line in infile:
                rawConstraints = []
                rawConstraints = line.split("OR")
                constraints = [s.strip() for s in rawConstraints]
                ProjectGui.user_constraints.append(constraints)

        #print(ProjectGui.user_constraints)

        self.createInstanceTextVar.set("Now Enter Preferences filename:")
        self.loadInstanceBtn.configure(command=self.parsePreferences)
        #self.loadInstanceBtn.grid(row=1, column=1, sticky=(W, E))

    def parsePreferences(self, flag=False):
        fName = self.fname.get()
        preferences = []
        #self.choice = tk.IntVar()
        #First, need to check and see what kind of preference file we're using.
        #Check flag to see if getting the rest of preferences.
        if flag:
            self.pref_label.configure(text="Please select next preference file type after entering its filename.")
            self.createInstanceTextVar.set("Please enter next preference filename.")
        else:
            self.choice = tk.IntVar()
            self.pref_label = tk.Label(self.mainframe, text="Please Select Preference Type of File")
            self.pref_label.grid(row=0, column=1, sticky=(W, E))
            self.pref_type1 = tk.Radiobutton(self.mainframe, text="Penalty Logic", variable=self.choice, value=1, command=self.preferenceType)
            self.pref_type1.grid(row=1, column=1, sticky=(W, E))
            self.pref_type2 = tk.Radiobutton(self.mainframe, text="Possibilistic Logic", variable=self.choice, value=2, command=self.preferenceType)
            self.pref_type2.grid(row=2, column=1, sticky=(E, W))
            self.pref_type3 = tk.Radiobutton(self.mainframe, text="Qualitative Choice Logic", variable=self.choice, value=3, command=self.preferenceType)
            self.pref_type3.grid(row=3, column=1, sticky=(W, E))

    def preferenceType(self):
        #print("successfully reached parsePreferences")
        user_choice = self.choice.get()
        if user_choice == 1:
            #print("Penalty logic selected")
            self.parsePenalty()
        elif user_choice == 2:
            #print("Possibilistic logic selected")
            self.parsePossibilistic()
        elif user_choice == 3:
            #print("Qualitative choice logic selected")
            self.parseQualitative()

    def parsePenalty(self):
        fName = self.fname.get()
        self.fname_entry.delete(0, END)

        cur_path = os.path.dirname(__file__)
        filePath = os.path.join(cur_path, '..', 'TestCase', fName)
        #print("successfully reached parsePenalty, path is" + str(filePath))
        with open(filePath, "r") as infile:
            rawPenalty = []
            for line in infile:
                line = line.replace("\n", "")
                rawPenalty = line.split(",")
                temp = rawPenalty[1].strip()
                rawPenalty[1] = temp
                print(rawPenalty)
                ProjectGui.penalty_preferences.append(rawPenalty)
        print(ProjectGui.penalty_preferences)
        self.objectsBuilder()

    def parsePossibilistic(self):
        fName = self.fname.get()
        self.fname_entry.delete(0, END)

        cur_path = os.path.dirname(__file__)
        filePath = os.path.join(cur_path, '..', 'TestCase', fName)
        #print("successfully reached parsePossibilistic, path is" + str(filePath))
        with open(filePath, "r") as infile:
            rawPoss = []
            for line in infile:
                rawPoss = line.replace("\n", "").split(",")
                print(rawPoss)
                temp = rawPoss[1].strip()
                rawPoss[1] = temp
                ProjectGui.possi_preferences.append(rawPoss)
        print(ProjectGui.possi_preferences)
        self.objectsBuilder()


    def parseQualitative(self):
        fName = self.fname.get()
        self.fname_entry.delete(0, END)

        cur_path = os.path.dirname(__file__)
        filePath = os.path.join(cur_path, '..', 'TestCase', fName)
        #print("successfully reached parseQualitative, path is" + str(filePath))
        with open(filePath, "r") as infile:
            rawQual = []
            for line in infile:
                temp = line.replace("\n", "")
                line = temp
                rawQual = line.split("BT")
                print(rawQual)
                tempQual = []
                for i in rawQual:
                    tempQual.append(i.strip())
                ProjectGui.quali_preferences.append(tempQual)
        print(ProjectGui.quali_preferences)
        ProjectGui.splitList(ProjectGui.quali_preferences)
        print(ProjectGui.quali_preferences)
        self.objectsBuilder()


    def splitList(l):
        temp = []
        ctr = 0
        for x in l:
            for y in x:
                if "IF" in y:
                    #idea is to split based off spaces, and then add the new list items to current list
                    splitTemp = y.split(" ")
                    temp.append(splitTemp)
                else:
                    temp.append(y)
        print(temp)
        lastSplit = []
        prev_item = []
        next_item = []
        for item in temp:
            if type(item) == list:
                newList = []
                newList.append(prev_item)
                for i in item:
                    newList.append(i)
                lastSplit.append(newList)
            prev_item = item
        ProjectGui.user_preferences = lastSplit

    def objectsBuilder(self):
        category_counter = 0
        for a in ProjectGui.user_attributes:
            if ProjectGui.user_attributes.index(a) % 3 == 0:
                category_counter += 1
        #print("Number of attributes: " + str(category_counter))
        #print("Using itertools to build out all combinations.")

        combinations = [seq for seq in itertools.product((True, False), repeat = category_counter)]
        #print("Combinations generated, now printing: \n")
        #print(combinations)
        #Can use itertools.product to yield a list of tuples with all the binary combos needed. Then I can map them to each object created.

        ProjectGui.allObjects = combinations
        if ProjectGui.penalty_preferences and ProjectGui.possi_preferences and ProjectGui.quali_preferences:
            self.pref_label.grid_remove()
            self.pref_type1.grid_remove()
            self.pref_type2.grid_remove()
            self.pref_type3.grid_remove()
            self.instanceLoaded()
        else:
            self.choice.set(0)
            self.parsePreferences(True)
