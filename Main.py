# Import the built-in tkinter library, available on Python 3.7+
from tkinter import *
import tkinter
from tkinter import Tk, Label, Button, Toplevel


# The tk function is initialized to create a window 
# Title is given, and the min size has been defined
root = Tk()
root.title("Vehicle Registration")
# root.iconbitmap("icon.ico")
root.geometry("500x500")

# this funcion generate the new-registration page
# it calls for the following function to print success as a label
# 2 sets of name; vin; address; phone; label and entry. Submit and exit button
def new_registration():  
    # global name_entry
    # global vin_entry
    # global page1
    # global address_entry
    # global phone_entry
    page1 = Toplevel()
    page1.geometry("800x800")
    new_welcome_note = Label(page1, text= "Welcome to New Vehicle Registration Form \n Please fill the following information", font=(20))
    new_welcome_note.pack()
    Label(page1, text="Enter your full name").pack()
    name_entry = Entry(page1, highlightthickness = 7, bg="white").pack()
    Label(page1, text="Enter your VIN").pack()
    vin_entry = Entry(page1, highlightthickness = 7, bg="white").pack()
    Label(page1, text="Enter your Address").pack()
    address_entry = Entry(page1, highlightthickness = 7, bg="white").pack()
    Label(page1, text="Enter your Phone Number").pack()
    phone_entry = Entry(page1, highlightthickness = 7, bg="white").pack()
    Button(page1, text = "Submit!", state=ACTIVE, command=new_application_success).pack()
    Button(page1, text="Exit", command=page1.destroy).pack()
# Display successful submission
def new_application_success():
    Label(page1, text="Application Submitted Successfully!", fg="green", font=(28)).pack()

# welcome
welcome_note="Welcome to Vehicle Registration Form! \n Please select a service"
welcome_label = Label(root, text=welcome_note,font=(20), pady = 30)
welcome_label.pack()

# 2 buttons on the home page, 1 exit button
new_button = Button(root, command=new_registration, text = "New Registration",width = 20, font = (20), pady=30)
new_button.pack(pady=20)

renew_button= Button(root, text = "Re-new Registration", width = 20, font = (20), pady=30)
renew_button.pack()

Button(root, text="Exit", command=root.destroy).pack()


# execute in the main loop.
root.mainloop()
