from tkinter import *


root = Tk()
root.geometry("300x300")
root.title("HELLO NAME")

def display():
    
    text_to_display = "Hello " + entry1.get()
    Label(root, text = text_to_display, fg ="green", font =(30)).pack()


label1 = Label(root, text ="Enter your name here")
label1.pack()
entry1 = Entry(root)
entry1 .pack()
Button(text="click here", command = display).pack()

root.mainloop()