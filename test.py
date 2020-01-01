#from tkinter import Tk, filedialog, Button,Label,messagebox
from tkinter import *
from tkinter import filedialog, messagebox
from functools import partial
import os

root = Tk()
root.title("Python Tkinter tutorial")
'''
top_frame = Frame(root)
top_frame.pack(side='top')
bottom_frame = Frame(root)
bottom_frame.pack(side='bottom')
currdir = os.getcwd()
def browse():
   tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
   if len(tempdir) > 0:
    messagebox.showinfo("filename","You chose %s" % tempdir)

label1 = Label(root, text="This is a test",bg="black",fg="red")
label1.pack(fill=Y)
button1 = Button(root,text = "Browse",bg="grey",fg="green",command=browse)
button1.pack(side='bottom')
'''
def login(user):
    messagebox.showinfo("Log IN",f"Logged in as {user}")
def leftClick(Event):
    print("Left")
def donothing():
    print("I won't")

# Menu 
menu = Menu(root)
root.config(menu=menu)

option1 = Menu(menu)
menu.add_cascade(label="File", menu=option1)
option1.add_command(label="open", command=donothing)
option1.add_command(label="Save", command=donothing)
option1.add_separator()
option1.add_command(label='exit', command=donothing)

option2 = Menu(menu)
menu.add_cascade(label="Edit", menu=option2)
option2.add_command(label="copy", command=donothing)
option2.add_command(label="paste", command=donothing)

#TOOLBAR
toolbar =  Frame(root, bg="blue")
insert_button =Button(toolbar, text="Insert", command=donothing)
insert_button.pack(side=LEFT, padx=2, pady=2)
toolbar.pack(side=TOP, fill=X)

#Main body
mainbody = Frame(root)
username_label = Label(mainbody, text='username')
password_label = Label(mainbody, text='Password')
remembe_me = Checkbutton(mainbody, text='Remember Me')
username = Entry(mainbody)
password = Entry(mainbody)

username_label.grid(row=1,column=0)
password_label.grid(row=2, column=0)
username.grid(row=1, column=1)
password.grid(row=2, column=1)
remembe_me.grid(row=3, columnspan=2)

login_msg = login(username)

#root.withdraw() #use to hide tkinter window
button1 = Button(mainbody,text = "Log In",bg="grey",fg="green", command=lambda : login(username.get()))

button1.grid(row=4)
button2 = Button(mainbody,text = "Register",bg="grey",fg="red")
button2.grid(row=4, column=2)
button2.bind("<Button-1>",leftClick)

mainbody.pack(side=TOP)

#status bar
status = Label(root, text="proessing", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

answer = messagebox.askquestion("Survey","DO you like this app?")
if answer == "yes":
    print("Welldone")
else:
    print("Improve")
'''
#canvas_frame = Frame(root)
canvas = Canvas(root, width=200, height=100)
canvas.pack(side=LEFT)
canvas.create_line(0, 0, 200, 100)
canvas.create_line(0, 100, 200 , 100)
#canvas_frame.pack(side=LEFT, fill=X)
'''
root.mainloop()