import tkinter
from tkinter import ttk
from tkinter import scrolledtext

window = tkinter.Tk()
window.title('Notes')
window.geometry('1920x1080')
# window.withdraw()
# window.iconbitmap(r'C:\Python27\DLLs\pyc.ico')

window.resizable(0, 0)

# Using a scrolled Text
scrolW = 30
scrolH = 4
scr = scrolledtext.ScrolledText(window, width = scrolW, height = scrolH, wrap = tkinter.WORD)

txt = '''This is just a matter of time before you become expert in programming.
good luck and never lose hope.'''
scr.insert(tkinter.INSERT,txt)
scr.grid(column = 0, columnspan = 3)

#Call back function for Exit menu
def _quit():
	window.quit()
	window.destroy()
	exit()

#creating Menu Bar
menuBar = tkinter.Menu(window) 
window.config(menu = menuBar)
fileMenu = tkinter.Menu(menuBar, tearoff = 0)
fileMenu.add_command(label = 'New')
menuBar.add_cascade(label = 'File', menu = fileMenu)
fileMenu.add_separator()
fileMenu.add_command(label = 'Exit', command = _quit) 

helpMenu = tkinter.Menu(menuBar, tearoff = 0)
helpMenu.add_command(label = '?')
helpMenu.add_command(label ='About')
menuBar.add_cascade(label = 'Help', menu = helpMenu)

# Starting main window (root window)
window.mainloop()
