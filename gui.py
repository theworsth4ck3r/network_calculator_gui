import tkinter as tk
from tkinter import messagebox

class GUIApplication:

    def __init__(self):        
        self.createAndConfigureRootWindow()
        self.createAndConfigureMainFrame()
        self.buildMainFrameLayout()
        self.createAndConfigureCalculateButton()
        self.createAndConfigureResultEntry()
        
        self.rootWindow.mainloop()
        

    def createAndConfigureRootWindow(self):
        self.rootWindow = tk.Tk()
        self.rootWindow.geometry('800x500')
        self.rootWindow.grid_columnconfigure(0, weight=1)
        

    def createAndConfigureMainFrame(self):
        self.mainFrame = tk.Frame(self.rootWindow)
        self.mainFrame.columnconfigure(0, weight=1)
        self.mainFrame.columnconfigure(1, weight=1)
        
    def buildMainFrameLayout(self):
        ipAddressLabel = tk.Label(self.mainFrame, text="IP Address", font=('Arial', 14))
        ipAddressLabel.grid(row=0, column=0, padx=10)

        self.ipAddressInput = tk.Entry(self.mainFrame)
        self.ipAddressInput.grid(row=1, column=0, sticky=tk.W + tk.E, padx=10)

        subnetMaskLabel = tk.Label(self.mainFrame, text="Subnet Mask", font=('Arial', 14))
        subnetMaskLabel.grid(row=0, column=1, padx=10)

        self.subnetMaskInput = tk.Entry(self.mainFrame)
        self.subnetMaskInput.grid(row=1, column=1, sticky=tk.W + tk.E, padx=10)

        self.mainFrame.pack(fill='x', padx=20, pady=20)
        
    def createAndConfigureCalculateButton(self):
        self.calculateButton = tk.Button(self.rootWindow, text="Calculate", command=self.handleCalculateButtonClick)
        self.calculateButton.pack()
        
    def createAndConfigureResultEntry(self):
        self.resultEntry = tk.Label(self.rootWindow, font=('Arial', 16), justify='left').pack(pady=20)
        
    def handleCalculateButtonClick(self):
        res = '''
------------------------------------------------------
Adres sieci                            1
Adres rozgłoszeniowy                   2
Maksymalna liczba urządzeń             3
Adres IP pierwszego urządzenia         4
Adres IP ostatniego urządzenia         5
------------------------------------------------------
        '''
    
    
    def createAndDisplayErrorMessages(self, errorMessage):
        pass