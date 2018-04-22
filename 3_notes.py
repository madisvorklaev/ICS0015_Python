# Notes v1.0:
# Tested with Python 3.6.5 on Windows 10.

import tkinter
from tkinter import ttk, scrolledtext, filedialog, messagebox
from tkinter import *

# initialise a window
window = Tk()
window.title('Notes')
window.geometry('960x540')

# use the ScrolledText widget
scr = scrolledtext.ScrolledText(window, wrap = tkinter.WORD)
scr.pack(side = LEFT, fill = BOTH, expand = YES)

class menu_items():
    def __init__(self, scr):
        self.scr = scr
        self.filename = None
        self.is_saved = False
        
    def _new(self):
        scr.delete('1.0', END)
        self.filename = None

    def _open(self):
        filename =  filedialog.askopenfilename(title = 'Select file', filetypes = (('Text Documents','*.txt'),('All Files','*.*')))
        if filename:
            f = open(filename, 'r+')
            text = f.read()
            f.close()
            scr.delete('1.0', END)
            scr.insert(tkinter.INSERT, text)
            self.filename = filename
            
    def _save(self):
        if self.filename:
            try:
                f = open(self.filename, 'w')
            except FileNotFoundError as error:
                print('The file name was not specified')
                self.is_saved = False
            else:
                contents = scr.get(1.0, END)
                f.write(contents)
                f.close
                self.is_saved = True
        else:
            filename =  filedialog.asksaveasfilename(title = 'Select file',filetypes = (('Text Documents','*.txt'),('All Files','*.*')), defaultextension = '.txt')
            try:
                f = open(filename, 'w')
                self.filename = filename
            except FileNotFoundError as error:
                print('The file name was not specified')
                self.is_saved = False
            else:
                contents = scr.get(1.0, END)
                f.write(contents)
                f.close
                self.is_saved = True
        
    def _saveas(self):
        filename =  filedialog.asksaveasfilename(title = 'Select file',filetypes = (('Text Documents','*.txt'),('All Files','*.*')), defaultextension = '.txt')
        if filename:
            f = open(filename, 'w')
            contents = scr.get(1.0, END)
            f.write(contents)
            f.close

    def _quit(self):
# Save confirm from https://www.programcreek.com/python/example/57788/tkMessageBox.askyesnocancel
        if scr.compare("end-1c", "!=", "1.0"):
            message = "Do you want to save %s before closing?" % (
            self.filename or "this untitled document")
            confirm = messagebox.askyesnocancel(
            title="Save On Close",
            message=message,
            default=messagebox.YES,
            parent=self.scr)
            if confirm:
                self._save()
                if not self.is_saved:
                   return
            elif confirm is None:
                return
            else:
                reply = "no"
        window.quit()
        window.destroy()
        exit()

    def _about(self):
        messagebox.showinfo('Notes v1.0', 'Tested with Python 3.6.5 on Windows 10. \nAuthor: Madis Võrklaev')

# create a menu bar
t = menu_items(scr)
menuBar = tkinter.Menu(window) 
window.config(menu = menuBar)
fileMenu = tkinter.Menu(menuBar, tearoff = 0)
fileMenu.add_command(label = 'New', command = t._new)
fileMenu.add_command(label = 'Open', command = t._open)
fileMenu.add_command(label = 'Save', command = t._save)
fileMenu.add_command(label = 'Save as', command = t._saveas)
menuBar.add_cascade(label = 'File', menu = fileMenu)
fileMenu.add_separator()
fileMenu.add_command(label = 'Exit', command = t._quit) 

helpMenu = tkinter.Menu(menuBar, tearoff = 0)
helpMenu.add_command(label ='About', command = t._about)
menuBar.add_cascade(label = 'Help', menu = helpMenu)

# Start the main window (root window)
window.mainloop()
