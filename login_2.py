import tkinter
from tkinter import *

from PIL import Image, ImageTk

root = Tk()
root.maxsize(1200, 700)
root.minsize(1200, 700)

# Create a photoimage object of the image in the path
image1 = Image.open(r"lib.jpg")
image2 = image1.resize((1200, 700), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image2)

label1 =tkinter.Label(image=test)
label1.image = test


# Position image
label1.place(x=0, y=0)
root.mainloop()