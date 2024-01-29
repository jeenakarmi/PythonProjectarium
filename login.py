from tkinter import *

def get_val():
    print(user_value.get())
    print(password_value.get())

root = Tk()
root.geometry("655x333")
root.title("Login Page")

user = Label(root,text = "Username",padx= 15)
password = Label(root,text = "Password")
user.grid()
password.grid()

user_value = StringVar()
password_value = StringVar()

user_entry = Entry(root,textvariable = user_value)
password_entry = Entry(root,textvariable = password_value)

#packing
user_entry.grid(row = 0, column = 1)
password_entry.grid(row = 1, column = 1)

Button(text = "Submit",command = get_val).grid()
root.mainloop()