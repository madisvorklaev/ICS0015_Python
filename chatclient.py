# The network part is from https://www.youtube.com/watch?v=D0SLpD7JvZI
# https://medium.com/swlh/lets-write-a-chat-app-in-python-f6783a9ac170

import socket
import threading
import sys
import tkinter
from tkinter import ttk, scrolledtext, filedialog, messagebox
from tkinter import *

def send_message(event = None):
    m = message_field.get()
    message_field.delete(0, END)
    s.send(bytes(m+ '\n', 'utf8'))
    if m == '/quit':
        callback()

def receive_message():
    while True:
        data = s.recv(1024)
        q = str(data, 'utf-8')
        if q == ('/quit'):
            print("Sorry, only 5 connections allowed, Chat will exit now")
            s.close()
            root.quit()
            break
        if not data:
            break
        message_show.insert(tkinter.END, data)
        message_show.see(END)

def callback():
    if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
        root.destroy()
        s.close()

root = Tk()
root.protocol("WM_DELETE_WINDOW", callback)
root.title('Chat')
root.geometry('200x100')

frame = tkinter.Frame()
message_show = scrolledtext.ScrolledText(root, wrap = tkinter.WORD)
message_show.insert(END, 'Welcome to Chat! For exit, type /quit')
frame.pack()
message_show.pack(side = LEFT, fill = BOTH, expand = YES)
message_field = tkinter.Entry(frame)
message_field.bind('<Return>', send_message)
message_field.pack()
send_button = tkinter.Button(frame, text='SEND', command = send_message)
send_button.pack()
addr = ('127.0.0.1', 5000)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(addr)

receive_thread = threading.Thread(target=receive_message)
receive_thread.start()

tkinter.mainloop()



