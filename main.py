from tkinter import *
#from functions import display
import functions.display as display

root = Tk()
root.title('ETERNITY - Calculator')
root.geometry('400x556')
root.resizable(0, 0)
root.configure(background='grey90')
newRoot = Frame(root, relief='sunken', bg='grey90')
newRoot.pack(fill=BOTH, expand=True, padx=0, pady=5)

display.configureWindow(newRoot)

root.mainloop()
