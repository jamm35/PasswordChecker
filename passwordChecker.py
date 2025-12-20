import re
from tkinter import * # imports everything from tkinter
import tkinter as tk

class PasswordChecker:
    
    def __init__(self, password, window):
        self.rating = 0
        self.password = password
        self.window = window
        self.file_path = "securityReport.txt"

        pass

    def length_check(self):
        if len(self.password) >= 16:
            self.length_label = tk.Label(self.window, text="good length!")
            self.length_label.place(x=100,y=0)
            self.rating+=1
        else:
            self.length_label = tk.Label(self.window, text="bad length.")
            self.length_label.place(x=100,y=0)

    def lowercase_check(self):
        lower = []
        for i in self.password:
            if i.islower():
                lower.append(i)
        if not lower:
            self.lowercase_label = tk.Label(self.window, text='bad lowercase')
            self.lowercase_label.place(x=100,y=20)
        else:
            self.lowercase_label = tk.Label(self.window, text='good lowercase')
            self.lowercase_label.place(x=100,y=20)
            self.rating+=1
    
    def uppercase_check(self):
        upper = []
        for i in self.password:
            if i.isupper():
                upper.append(i)
        if not upper:
            self.upper_label = tk.Label(self.window, text='bad uppercase')
            self.upper_label.place(x=100,y=40)
        else:
            self.upper_label = tk.Label(self.window, text='good uppercase')
            self.upper_label.place(x=100,y=40)
            self.rating+=1
    
    def number_check(self):
        numbers =  re.findall(r'\d+', self.password)
        if not numbers:
            self.numbers_label = tk.Label(self.window, text='bad numbers')
            self.numbers_label.place(x=100,y=60)
        else:
            self.numbers_label = tk.Label(self.window, text='good numbers')
            self.numbers_label.place(x=100,y=60)
            self.rating+=1
    
    def specialChar_check(self):
        special_characters = " !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
        user_sc = []
        for i in self.password:
            if i in special_characters:
                user_sc.append(i)
        if not user_sc:
            self.special_label = tk.Label(self.window, text='bad special characters')
            self.special_label.place(x=100,y=80)
        else:
            self.special_label = tk.Label(self.window, text='good special characters')
            self.special_label.place(x=100,y=80)
            self.rating+=1
    
    def rating_system(self):
        division = self.rating / 5
        percentage = division * 100
        percentage = str(percentage)
        self.rating_label = tk.Label(self.window, text=f"overall security score: {percentage}%")
        self.rating_label.place(x=100,y=100)
    
    def destroyReport(self):
        self.length_label.destroy()
        self.lowercase_label.destroy()
        self.upper_label.destroy()
        self.numbers_label.destroy()
        self.special_label.destroy()
        self.rating_label.destroy()

#test cases for PasswordChecker class
# checker = PasswordChecker()
# checker.length_check()
# checker.lowercase_check()
# checker.uppercase_check()
# checker.number_check()
# checker.specialChar_check()
# checker.rating_system()

class UserInterface:
    def __init__(self):
        self.window = Tk() #start a window
        self.window.geometry("420x420")
        self.window.title("password checker")
        self.rbuttonClicked = False
    pass

    def initialButton(self):
        self.turn_on = tk.Button(self.window, text="check your password", command=self.resultsPage)
        self.turn_on.place(x=115,y=210)
        

    def initialTextBox(self):
        self.text=Text(self.window, borderwidth=3, relief="solid", width=40, height=1)
        self.text.place(x=60, y=150)

        #prevents user from using the return key
        self.text.bind("<Return>", self.prevent_returnKey)

        #limits user to 40 characters
        self.text.bind("<KeyPress>", self.characterLimit)
    
    def resultsPage(self):
        self.password = self.text.get("1.0", "end-1c")
        #destroys previous UI
        self.turn_on.destroy()
        self.text.destroy()

        
        self.pc = PasswordChecker(self.password, self.window)
        #displays results of PasswordChecker
        self.pc.length_check()
        self.pc.lowercase_check()
        self.pc.uppercase_check()
        self.pc.number_check()
        self.pc.specialChar_check()
        self.pc.rating_system()
        

        self.label = tk.Label(self.window, text=self.password)
        self.label.place(x=150,y=150)
        #displays button to try password again
        self.rbutton = tk.Button(self.window, text="click here to try again", command=self.resetButton)
        self.rbutton.place(x=115,y=210)

        #displays fileButton
        self.fileGen = reportFile()
        self.fileGen.generateFile(self.window)
    
    def resetButton(self):
            rbuttonClicked = self.rbuttonClicked
            rbuttonInitial = rbuttonClicked
            rbuttonClicked = not rbuttonClicked
            if rbuttonInitial != rbuttonClicked:
                self.label.destroy()
                self.rbutton.destroy()
            self.initialButton()
            self.initialTextBox()
            #destroy report
            self.pc.length_label.destroy()
            self.pc.lowercase_label.destroy()
            self.pc.upper_label.destroy()
            self.pc.numbers_label.destroy()
            self.pc.special_label.destroy()
            self.pc.rating_label.destroy()

            #destroy fileButton
            self.fileGen.destroyFileButton()
    
            
            

    def prevent_returnKey(self, event):
        self.resultsPage()
        return "break"
    
    def characterLimit(self, event):
        count = len(self.text.get('1.0', 'end-1c'))

        if count >= 40 and event.keysym not in ("BackSpace", "Delete"):
            return "break"
    #^^ allow super+a at character limit ^^

class reportFile:
    
    def __init__(self):
        self.ui = ui
        pass

    def generateFile(self, window):
        self.fileButton = tk.Button(window, text="click here to generate a security report", command=self.encryptionPrompt)
        self.fileButton.place(x=65,y=250)
        pass

    def destroyFileButton(self):
        #destoys fileButton when user attempts to try another password
        self.fileButton.destroy()
        pass

    def encryptionPrompt(self):
        ui = self.ui

        # destroy results UI
        ui.label.destroy()
        ui.rbutton.destroy()
        ui.pc.destroyReport()
        self.destroyFileButton()

        #prompts user for encryption password
        

    pass

    

ui = UserInterface()
ui.initialButton()
ui.initialTextBox()
ui.window.mainloop()