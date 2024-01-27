# Basic Widgets in tkinter

# Importing the libraries
import tkinter as tk
from tkinter import ttk

# Creating  a function for the button
def button_function():
    print("A button was pressed")

# Creating a function for the exercise button
def hello():
    print("Hello")

# Creating the window
window = tk.Tk()
window.title('Window and widgets')
window.geometry('800x500')

# ttk label
label = ttk.Label(master=window, text='This is a test')
label.pack()

# tk text
text = tk.Text(master= window)
text.pack()

# ttk entry
entry = ttk.Entry(master=window)
entry.pack()

# Exercise label
secondlabel = ttk.Label(master=window, text='my label')
secondlabel.pack()

# ttk button
button = ttk.Button(master=window, text='A Button', command=button_function)
button.pack()

# Exercise button
#button_2 = ttk.Button(master=window, text='print Hello', command=hello)
button_2 = ttk.Button(master=window, text='print Hello', command=lambda: print("hello"))
button_2.pack()

# Exercise
# Add one more text label and a button with the function to print hello
# The label should say "my label" and be between the entry widget and the button

# Running
window.mainloop()