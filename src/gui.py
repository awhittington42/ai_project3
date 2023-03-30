from tkinter import *
import tkinter as tk
import sys
sys.path.append("..")
class ProjectGui:

    #instanceInfo = StringVar(value="No instance detected")
    def createinstance(self):
        print("createinstance invoked!")

    def loadinstance(self):
        print("loadinstance called!")
        self.loadInstanceTextVar.set("Enter attributes filename.")
        self.fname = StringVar()
        fname_entry = tk.Entry(self.mainframe, width=10, textvariable=fname)
        fname_entry.focus()
        fname_entry.grid(row=1, column=1, sticky=(W, E))
        self.root.bind("<Return>", self.parseAttributes)

    def quitgui(self):
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
        self.mainframe = tk.Frame(self.root)
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        #root.mainloop()
        self.createInstanceTextVar = StringVar(value ="Create Instance")
        self.createInstanceBtn = tk.Button(self.mainframe, textvariable=self.createInstanceTextVar, command=self.createinstance).grid(row=0, column=0, sticky=(W, E))
        self.loadInstanceTextVar = StringVar(value = "Load Instance")
        self.loadInstanceBtn = tk.Button(self.mainframe, textvariable=self.loadInstanceTextVar, command=self.loadinstance).grid(row=1, column=0, sticky=(W, E))
        self.quitButton = tk.Button(self.mainframe, text='Quit', command=self.quitgui).grid(row=2, column=0, sticky=(W, W))
        self.instanceLabel = tk.Label(self.mainframe, text='Current Instance --> ').grid(row=3, column=0, sticky=(W, E))
        self.existenceButton = tk.Button(self.mainframe, text='Existence', command=self.existence)
        self.exempButton = tk.Button(self.mainframe, text='Exemplification', command=self.exemp)
        self.optimizeButton = tk.Button(self.mainframe, text='(Omni)optimization', command=self.optimize)
        self.instanceInfo = StringVar(value="No Instance Detected")
        self.instanceText = tk.Label(self.mainframe, textvariable=self.instanceInfo).grid(row=3, column=1, sticky=(W, E))
        self.root.mainloop()

    def parseAttributes(self):
        self.attributes = []
        # File input gathering and parsing to do here
