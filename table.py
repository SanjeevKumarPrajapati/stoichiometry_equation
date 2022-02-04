from tkinter import *
import tkinter
from PIL import ImageTk, Image

a=Tk()
a.title("Periodic Table")
a.maxsize(1024,576)
a.minsize(1024,576)
image1 = Image.open('ColorfulPeriodicTable118-1024x576.png').resize((1024,576))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=0, y=0)
a.mainloop()

