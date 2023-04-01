from tkinter import *
import tkinter as tk
import sys
import os
import fnmatch
import itertools
sys.path.append("..")
class ProjectGui:

    user_attributes = []
    user_constraints = []
    user_preferences = []

    def createinstance(self):
        print("createinstance invoked!")

    def loadWidgets(self, root):
        self.mainframe = tk.Frame(self.root)
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.createInstanceTextVar = StringVar(value ="Create Instance")
        self.createInstanceBtn = tk.Button(self.mainframe, textvariable=self.createInstanceTextVar, command=self.createinstance).grid(row=0, column=0, sticky=(W, E))
        self.loadInstanceTextVar = StringVar(value = "Load Instance")
        self.loadInstanceBtn = tk.Button(self.mainframe, textvariable=self.loadInstanceTextVar, command=self.loadinstance).grid(row=1, column=0, sticky=(W, E))
        quitButton = tk.Button(self.mainframe, text='Quit', command=ProjectGui.quitgui).grid(row=2, column=0, sticky=(W, W))
        self.instanceLabel = tk.Label(self.mainframe, text='Current Instance --> ').grid(row=3, column=0, sticky=(W, E))
        self.existenceButton = tk.Button(self.mainframe, text='Existence', command=self.existence)
        self.exempButton = tk.Button(self.mainframe, text='Exemplification', command=self.exemp)
        self.optimizeButton = tk.Button(self.mainframe, text='(Omni)optimization', command=self.optimize)
        self.instanceInfo = StringVar(value="No Instance Detected")
        self.instanceText = tk.Label(self.mainframe, textvariable=self.instanceInfo).grid(row=3, column=1, sticky=(W, E))

    def loadinstance(self):
        print("loadinstance called!")
        self.loadInstanceTextVar.set("Enter Filename & click me.")
        self.fname = StringVar()
        self.fname_entry = tk.Entry(self.mainframe, width=10, textvariable=self.fname)
        self.loadInstanceBtn = tk.Button(self.mainframe, textvariable=self.loadInstanceTextVar, command=self.parseAttributes).grid(row=1, column=1, sticky=(W,E))
        self.fname_entry.focus()
        self.fname_entry.grid(row=1, column=0, sticky=(W, E))
        self.createInstanceTextVar.set("Enter attribute filename below")
        #self.root.bind("<Return>", lambda: self.parseAttributes(fname))

    def quitgui():
        print("quitgui called!")
        sys.exit(0)

    def existence(self):
        print("existence called!")

    def exemp(self):
        print("exemp called!")

    def optimize(self):
        print("optimize called!")

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
        print("successfully reached parseAttributes, path is" + str(filePath))
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

        print(ProjectGui.user_attributes)
        self.createInstanceTextVar.set("Now Enter Constraints filename:")
        self.loadInstanceBtn = tk.Button(self.mainframe, textvariable=self.loadInstanceTextVar, command=self.parseConstraints).grid(row=1, column=1, sticky=(W, E))

    def parseConstraints(self):
        fName = self.fname.get()
        self.fname_entry.delete(0, END)
        constraints = []
        cur_path = os.path.dirname(__file__)
        filePath = os.path.join(cur_path, '..', 'TestCase', fName)
        print("successfully reached parseConstraints, path is" + str(filePath))

        with open(filePath, "r") as infile:
            for line in infile:
                rawConstraints = []
                rawConstraints = line.split("OR")
                ProjectGui.user_constraints.append(rawConstraints)

            print(ProjectGui.user_constraints)

        self.createInstanceTextVar.set("Now Enter Preferences filename:")
        self.loadInstanceBtn = tk.Button(self.mainframe, textvariable=self.loadInstanceTextVar, command=self.parsePreferences).grid(row=1, column=1, sticky=(W, E))

    def parsePreferences(self):
        fName = self.fname.get()
        preferences = []
        choice = 0
        #First, need to check and see what kind of preference file we're using.
        pref_label = tk.Label(self.mainframe, text="Please Select Preference Type of File").grid(row=0, column=1, sticky=(W, E))
        pref_type1 = tk.Radiobutton(self.mainframe, text="Penalty Logic", variable=choice, value=1, command=self.parsePenalty).grid(row=1, column=1, sticky=(W, E))
        pref_type2 = tk.Radiobutton(self.mainframe, text="Possibilistic Logic", variable=choice, value=2, command=self.parsePossibilistic).grid(row=2, column=1, sticky=(E, W))
        pref_type3 = tk.Radiobutton(self.mainframe, text="Qualitative Choice Logic", variable=choice, value=3, command=self.parseQualitative).grid(row=3, column=1, sticky=(W, E))

        print("successfully reached parsePreferences")

        if choice == 0:
            print("Error, please ensure you select a preference type from the options.")
        elif choice == 1:
            print("Penalty logic selected")
        elif choice == 2:
            print("Possibilistic logic selected")
        elif choice == 3:
            print("Qualitative choice logic selected")
        else:
            print("Error - Unexpected preference choice detected.")
            sys.exit(-1)

    def parsePenalty(self):
        fName = self.fname.get()
        self.fname_entry.delete(0, END)

        cur_path = os.path.dirname(__file__)
        filePath = os.path.join(cur_path, '..', 'TestCase', fName)
        print("successfully reached parsePenalty, path is" + str(filePath))
        with open(filePath, "r") as infile:
            rawPenalty = []
            for line in infile:
                line = line.replace("\n", "")
                rawPenalty = line.split(",")
                temp = rawPenalty[1].strip()
                rawPenalty[1] = temp
                print(rawPenalty)
                ProjectGui.user_preferences.append(rawPenalty)
        print(ProjectGui.user_preferences)

    def parsePossibilistic(self):
        fName = self.fname.get()
        self.fname_entry.delete(0, END)

        cur_path = os.path.dirname(__file__)
        filePath = os.path.join(cur_path, '..', 'TestCase', fName)
        print("successfully reached parsePossibilistic, path is" + str(filePath))
        with open(filePath, "r") as infile:
            rawPoss = []
            for line in infile:
                rawPoss = line.replace("\n", "").split(",")
                print(rawPoss)
                temp = rawPoss[1].strip()
                rawPoss[1] = temp
                ProjectGui.user_preferences.append(rawPoss)
            print(ProjectGui.user_preferences)


    def parseQualitative(self):
        fName = self.fname.get()
        self.fname_entry.delete(0, END)

        cur_path = os.path.dirname(__file__)
        filePath = os.path.join(cur_path, '..', 'TestCase', fName)
        print("successfully reached parseQualitative, path is" + str(filePath))
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
                ProjectGui.user_preferences.append(tempQual)
        print(ProjectGui.user_preferences)
        ProjectGui.splitList(ProjectGui.user_preferences)
        print(ProjectGui.user_preferences)

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

    def objectBuilder():
        objects = []

        for a in ProjectGui.attributes:
            if ProjectGui.attributes.index(a) % 3 == 0:
                #Then this is a attribute type, and the following two indices are its binary values.
                #Can use itertools.product to yield a list of tuples with all the binary combos needed. Then I can map them to each object created.
