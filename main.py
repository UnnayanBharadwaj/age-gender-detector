import tkinter as tk
from os import startfile

class Home(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()
        self.createScreen()
        
    def createScreen(self):
        self.title = tk.Label(self, text = "Gender Detector\n", fg = "red", font = ("Courier", 20))
        self.title.pack(side = "top")
        
        self.live = tk.Button(self, text = "Start Detection", command = lambda :startfile('ageGenderDetector.py'), width = 25, height = 3)
        self.live.pack(side = "top")
        
        self.credit = tk.Button(self, text = "Credits", command = self.credits, width = 25, height = 3)
        self.credit.pack(side = "top")
        
        self.quit = tk.Button(self, text="Quit", command=root.destroy, width = 25, height = 3)
        self.quit.pack(side="bottom")
        
    def credits(self):
        self.live.forget()
        self.quit.forget()
        self.credit.forget()
        
        self.title = tk.Label(self, text = "Credits\n", font = ("Courier"))
        self.title.pack(side = "top")

        self.details = tk.Label(self, text = "Developed By: Pradyumna Tripathi,\n"
                                +"pradyumnatripathi99@gmail.com\n"
                                +"THANK YOU!\n")
        self.details.pack()
        self.back = tk.Button(self, text = "Back", command = self.createNewScreen)
        self.back.pack()
        
    def createNewScreen(self):
        self.forget()
        self.__init__(None)

root = tk.Tk()
root.title("Gender Detect")
root.minsize(300,300)
start = Home(root)
start.mainloop()