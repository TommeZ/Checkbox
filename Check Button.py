# Import Library from Tkinter Python's de-facto standard GUI
from tkinter import *
# Messagebox library
from tkinter import messagebox

#Python List                            
services = []

# Function to use when button is clicked displaying info from checkbox
def showInfo():
    for i in range(len(services)):
        selected=""
        #Get services variable
        if services[i].get()>=1:
            selected += str(i)
            #External Window
            messagebox.showinfo(message="You selected Checkbox " + selected)            

# Create new root window                        
window = Tk()
# Root window title
window.title("Checkbox Buttons")
                            
for i in range(4):
    # Append int variables for each checkbox
    option = IntVar()
    option.set(0)
    services.append(option)

# Check widget used to display a number of toggle buttons/boxes for different options                       
Checkbutton(window, text= "Checkbox 0",
#Pack manages our widgets in blocks before placing them onto our root window (Widget button or checkbox)
variable=services[0]).pack()

Checkbutton(window, text= "Checkbox 1",
variable=services[1]).pack()

Checkbutton(window, text= "Checkbox 2",
variable=services[2]).pack()

Checkbutton(window, text= "Checkbox 3",
variable=services[3]).pack()

# Create External Window using function show info from selected checkbox                       
Button(window, text="Ok",
command=showInfo).pack()

#Halt execution of program                            
window.mainloop()
