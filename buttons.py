import tkinter as tk
from tkinter import ttk

def button_func():
    # Get the content of the entry
    entry_text = entry.get()

    # Update the label
    # label.configure(text='some other text')
    label['text'] = entry_text
    entry['state'] = 'disabled' # disables the entry tab
   # print(label.configure)

def function2():
    entry['state'] = 'enabled'
    entry_text = entry.get()
    label['text'] = entry_text


# Window
window = tk.Tk()
window.title("Getting and setting widgets")

# Widgets
label = ttk.Label(master=window, text="Some text")
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master= window, text="Update the label", command=button_func)
button.pack()


# Exercise: add aonther button that changes the text back to 'some text' and that enables entry

button2 = ttk.Button(master=window, text='redo', command=function2)
button2.pack()

# Running
window.mainloop()