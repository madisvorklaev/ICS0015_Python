import tkinter
from tkinter import ttk, scrolledtext, filedialog, messagebox
from tkinter import *

window = Tk()
window.title('Notes')
window.geometry('960x540')

# Using a scrolled Text
scrollW = 960
scrollH = 540
scr = scrolledtext.ScrolledText(window, width = scrollW, height = scrollH, wrap = tkinter.WORD)

class menu_items():
    def __init__(self, scr):
        self.scr = scr
        self.filename = ' '
        
    def _new(self):
        scr.delete('1.0', END)
        scr.grid(column = 0, columnspan = 3)
        self.filename = ' '

    def _open(self):
        filename =  filedialog.askopenfilename(initialdir = 'C:\ ', title = 'Select file', filetypes = (('Text Documents','*.txt'),('All Files','*.*')))
        if filename:
            f = open(filename, 'r+')
            text = f.read()
            f.close()
            scr.delete('1.0', END)
            scr.insert(tkinter.INSERT, text)
            scr.grid(column = 0, columnspan = 3)
            self.filename = filename
            
    def _save(self):
        if self.filename != ' ':
            try:
                f = open(self.filename, 'w')
            except FileNotFoundError as error:
                print('The file name was not specified')
        else:
            filename =  filedialog.asksaveasfilename(initialdir = 'C:\ ',title = 'Select file',filetypes = (('Text Documents','*.txt'),('All Files','*.*')), defaultextension = '.txt')
            try:
                f = open(filename, 'w')
                self.filename = filename
            except FileNotFoundError as error:
                print('The file name was not specified')
            else:
                contents = scr.get(1.0, END)
                f.write(contents)
                f.close
        

    def _saveas(self):
        filename =  filedialog.asksaveasfilename(initialdir = 'C:\ ',title = 'Select file',filetypes = (('Text Documents','*.txt'),('All Files','*.*')), defaultextension = '.txt')
        if filename:
            f = open(filename, 'w')
            contents = scr.get(1.0, END)
            f.write(contents)
            f.close

    def _quit(self):
        window.quit()
        window.destroy()
        exit()

    def _about(self):
        messagebox.showinfo("Notes v1.0", "Notes by Madis Võrklaev")

#creating Menu Bar
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

# Starting main window (root window)
window.mainloop()
