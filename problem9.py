
from tkinter import *
root = Tk()			
root.geometry('200x100')
btn = Button(root, text = 'Click me !', bd = '5',
						command = root.destroy)

btn.pack(side = 'top')
root.mainloop()
