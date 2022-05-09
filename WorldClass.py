#2022 Fall
#CS-212
#Practical Python
#Version 2
#Sunday, 17 April 2022
#Oscar Michua-Zarate

#Description: This class contains tkinter to create a canvas for my program
import tkinter as tk
from EncrClass import *
from DecrClass import *
from BruteForceCLass import *

#import BruteForceCLass

class World:
    """
        Purpose: To set up the canvas (GUI) for the program
        Responsibilities: Will be responsible for creating the canvas for the user. 
                          Will also have to incorporate all other classes in here to 
                          do sorts of calculations and encryptions. 
    """
    def CreateWindow():
        """
            Description: So far only makes a GUI with a text block for string 
                         and another text box for key
            Inputs: None
            Outputs: None
        """
        root= tk.Tk()

        #get string to modify
        def printTxtString():
            """
                Description: gets the input from inputstring box
                Inputs: None
                Outputs: inp
                        inp: gets the input from inputstring box
            """
            inp = inputtxtString.get(1.0, "end-1c")
            return inp

        #get key
        def GetKey():
            """
                Description: gets the input from inputkey box
                Inputs: None
                Outputs: inp
                         inp: gets the input from inputkey box
            """
            inp = inputtxtKey.get(1.0, "end-1c")
            inp = int(inp)
            return inp

        #Creates the Scrolling section for the bruteforce method
        scrollbar = tk.Scrollbar(root)
        scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
        mylist = tk.Listbox(root, yscrollcommand = scrollbar.set )
        mylist.pack( side = tk.RIGHT, fill = tk.BOTH )
        scrollbar.config( command = mylist.yview )

        #Create GUI canvas with specific measurements
        canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
        canvas1.pack()

        #Creates Title for GUI
        Title1 = tk.Label(root, text='Caesar Cypher')
        Title1.config(font=('helvetica', 14))
        canvas1.create_window(200, 20, window=Title1)

        #Shows a string input section in GUI for a text box
        stringLabel = tk.Label(root, text = 'Input a String: ')
        stringLabel.config(font=('helvetica', 10))
        canvas1.create_window(75, 70, window = stringLabel)

        #Shows a key string input section in GUI for a text box
        KeyLabel = tk.Label(root, text = 'Input your Key: ')
        KeyLabel.config(font=('helvetica', 10))
        canvas1.create_window(73, 115, window = KeyLabel)

        #Creates modified string text
        ModifiedString = tk.Label(root, text = 'Modified String: ')
        ModifiedString.config(font=('helvetica', 10))
        canvas1.create_window(73, 205, window = ModifiedString)

        #Creates modified string text input
        ModifiedString = tk.Text(root, height= 1, width= 20)
        ModifiedString.pack()
        canvas1.create_window(200, 205, window=ModifiedString)

        #Creates a text box for InputString
        inputtxtString = tk.Text(root, height= 1, width= 20)
        inputtxtString.pack()
        canvas1.create_window(200, 70, window=inputtxtString)

        #Creates a text box for key value
        inputtxtKey = tk.Text(root, height= 1, width= 10)
        inputtxtKey.pack()
        canvas1.create_window(160, 115, window=inputtxtKey)

        def CommandEncrypt():
            """
                Description: Sends the modified string into a encrypted form
                Inputs: None
                Outputs: None
            """
            key = GetKey()
            text = printTxtString()
            p1 = EncryptClass.EncryptFunc(key,text)
            #print(p1)
            ModifiedString.insert(tk.END, p1)

        def CommandDecrypt():
            """
                Description: Sends the modified string into a decrypted form
                Inputs: None
                Outputs: None
            """
            key = GetKey()
            text = printTxtString()
            p1 = DecryptClass.DecryptFunc(key,text)
            #print(p1)
            ModifiedString.insert(tk.END, p1)

        def CommandBrute():
            """
                Description: Gets all possible combinations of encryption for a string
                Inputs: None
                Outputs: None
            """
            key = GetKey()
            text = printTxtString()
            for key in range(26):
                p2 = (EncryptClass.EncryptFunc(key,text))
                mylist.insert(tk.END, p2)

        def ClearAll():
            """
                Description: Clears all text boxes in the GUI
                Inputs: None
                Outputs: None
            """
            ModifiedString.delete('1.0', tk.END)
            inputtxtString.delete('1.0', tk.END)
            inputtxtKey.delete('1.0', tk.END)
            mylist.delete('0', tk.END)
        
        #Creates Encrypt Button
        EncryptButton = tk.Button(root,text = 'Encrypt', command=CommandEncrypt)
        EncryptButton.config(font=('helvetica', 10))
        canvas1.create_window(73, 160, window=EncryptButton)

        #Creates Decrypt Button
        DecryptButton = tk.Button(root,text = 'Decrypt', command=CommandDecrypt)
        DecryptButton.config(font=('helvetica', 10))
        canvas1.create_window(180, 160, window=DecryptButton)

        #Creates BruteForce Button
        BruteForceButton = tk.Button(root,text = 'BruteForce', command=CommandBrute)
        BruteForceButton.config(font=('helvetica', 10))
        canvas1.create_window(290, 160, window=BruteForceButton)

        #Create Clear Button
        ClearButton = tk.Button(root,text = 'Clear', command = ClearAll)
        ClearButton.config(font=('helvetica', 10))
        canvas1.create_window(73, 290, window=ClearButton)        
        #Runs root
        root.mainloop()

World.CreateWindow()

