from tkinter import *
from PIL import ImageTk, Image
window = Tk()
window.title("kevin is better")
window.geometry("700x500")

top = Toplevel()
label = Label(top, text = "Hello, world").pack()
mainloop()
