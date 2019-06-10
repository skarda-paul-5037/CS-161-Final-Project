'''
Creating my own notepad program
To do list:
-creat help and about me file menu options
-get Open option working properly
-save files as .txt properly
-change color of title bar
-change icon in title bar
-create tool bar with button icons(text will do until then)
'''

import tkinter
import tkinter.filedialog as dialog
from tkinter import *


def open(root, text):
    filename = dialog.askopenfilename()
    

def save(root, text):
    data = text.get('0.0', tkinter.END)
    filename = dialog.asksaveasfilename(
        parent=root,
        filetypes=[('Text', '*.txt')],
        title='Save as...')
    writer = open(filename, 'w')
    writer.write(data)
    writer.close()

def quit(root):
    root.destroy()

def help(window, text):
    print("Did the USS OREGON need help dispaching the Spanish fleet outside the Cuban harbor? Nope!! And neither do you! ;-)")
    #m = PanedWindow(orient=VERTICAL)
    #m.pack(fill=BOTH, expand=1)

    #top = Label(m, text="top pane")
    #m.add(top)

    #bottom = Label(m, text="bottom pane")
    #m.add(bottom)

def about(window, text):
    print("Version 0.10")
    print("by Paul Skarda")
    #p = PanedWindow(orient=VERTICAL)
    #p.pack(fill=BOTH, expand=1)

    #top = Label(p, text="Version 0.1")
    #p.add(top)

    #bottom = Label(p, text="Paul Skarda")
    #p.add(bottom)
    

window = tkinter.Tk() #creating the gui/window
window.title("Basic Notepad+") #window title
window.geometry("300x300")
text = tkinter.Text(window)
text.pack()

menubar = tkinter.Menu(window)
filemenu = tkinter.Menu(menubar)
filemenu.add_command(label='Open', command=lambda : open(window, text))
filemenu.add_command(label='Save', command=lambda : save(window, text))
filemenu.add_command(label='Quit', command=lambda : quit(window))

helpmenu = tkinter.Menu(menubar)
helpmenu.add_command(label='Help F1', command=lambda : help(window, text))
helpmenu.add_command(label='About...', command=lambda : about(window, text))

menubar.add_cascade(label = 'File', menu=filemenu)
menubar.add_cascade(label = 'Help', menu=helpmenu)
window.config(menu=menubar)
#window.config(bg='black', fg='orange')

window.mainloop()
