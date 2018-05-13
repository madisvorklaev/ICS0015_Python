# The network part is from https://www.youtube.com/watch?v=D0SLpD7JvZI
# https://medium.com/swlh/lets-write-a-chat-app-in-python-f6783a9ac170

import socket
import threading
import sys
import tkinter
from tkinter import ttk, scrolledtext, filedialog, messagebox
from tkinter import *

def send_message():
    m = message_field.get()
    message_field.delete(0, END)
    s.send(bytes(m+ '\n', 'utf8'))
    if m == '/quit':
        s.close()
        window.quit()

def receive_message():
    while True:
        data = s.recv(1024)
        if not data:
            break
        print(str(data, 'utf-8'))
        message_show.insert(tkinter.END, data)
        message_show.see(END)

window = Tk()
window.title('Chat')
window.geometry('960x540')

frame = tkinter.Frame()
message_show = scrolledtext.ScrolledText(window, wrap = tkinter.WORD)
frame.pack()
message_show.pack(side = LEFT, fill = BOTH, expand = YES)
message_field = tkinter.Entry(frame)
message_field.pack()
send_button = tkinter.Button(frame, text='SEND', command = send_message)
send_button.pack()
addr = ('127.0.0.1', 5000)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(addr)

receive_thread = threading.Thread(target=receive_message)
receive_thread.start()

tkinter.mainloop()



