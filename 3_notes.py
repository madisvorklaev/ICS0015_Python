import tkinter
from tkinter import ttk, scrolledtext, filedialog, messagebox
from tkinter import *

window = Tk()
window.title('Notes')
window.geometry('960x540')
# window.withdraw()
# window.iconbitmap(r'C:\Python27\DLLs\pyc.ico')

#window.resizable(0, 0)

# Using a scrolled Text
scrollW = 960
scrollH = 540
scr = scrolledtext.ScrolledText(window, width = scrollW, height = scrollH, wrap = tkinter.WORD)

##txt = '''This is just a matter of time before you become expert in programming.
##good luck and never lose hope.'''
##scr.insert(tkinter.INSERT,txt)
##scr.grid(column = 0, columnspan = 3)

#Call back function for menus
def _new():
    contents = ''
    scr.insert(tkinter.INSERT, contents)
    scr.grid(column = 0, columnspan = 3)

def _open():
    filename =  filedialog.askopenfilename(initialdir = 'C:\ ', title = 'Select file', filetypes = (('Text Documents','*.txt'),('All Files','*.*')))
    f = open(filename)
    text = f.read()
    f.close()
    scr.delete('1.0', END)
    scr.insert(tkinter.INSERT, text)
    scr.grid(column = 0, columnspan = 3)
        
##def _save():
##   # https://python-forum.io/Thread-save-acts-like-save-as
##    filename =  filedialog.asksaveasfilename(initialdir = 'C:\ ',title = 'Select file',filetypes = (('Text Documents','*.txt'),('All Files','*.*')))
##    f = open(filename, 'w')
##    contents = scr.get(1.0, END)
##    f.write(contents)
##    f.close

def _saveas():
    filename =  filedialog.asksaveasfilename(initialdir = 'C:\ ',title = 'Select file',filetypes = (('Text Documents','*.txt'),('All Files','*.*')))
    f = open(filename, 'w')
    contents = scr.get(1.0, END)
    f.write(contents)
    f.close

def _quit():
    window.quit()
    window.destroy()
    exit()

def _about():
    messagebox.showinfo("Notes v1.0", "Notes by Madis Võrklaev")

#creating Menu Bar
menuBar = tkinter.Menu(window) 
window.config(menu = menuBar)
fileMenu = tkinter.Menu(menuBar, tearoff = 0)
fileMenu.add_command(label = 'New', command = _new)
fileMenu.add_command(label = 'Open', command = _open)
##fileMenu.add_command(label = 'Save', command = _save)
fileMenu.add_command(label = 'Save as', command = _saveas)
menuBar.add_cascade(label = 'File', menu = fileMenu)
fileMenu.add_separator()
fileMenu.add_command(label = 'Exit', command = _quit) 

helpMenu = tkinter.Menu(menuBar, tearoff = 0)
helpMenu.add_command(label ='About', command = _about)
menuBar.add_cascade(label = 'Help', menu = helpMenu)

# Starting main window (root window)
window.mainloop()
