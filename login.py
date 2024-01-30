from tkinter import *

def get_val():
    print(user_value.get())
    print(password_value.get())

root = Tk()
root.geometry("500x335")
root.title("Login Page")
Label(root, text = "Welcome To Login Page", font = "comicsansms 13 bold" ).grid(row = 0, column = 3)


user = Label(root,text = "Username")
password = Label(root,text = "Password")
user.grid()
password.grid()

user_value = StringVar()
password_value = StringVar() 
remember_me = IntVar()

user_entry = Entry(root,textvariable = user_value)
password_entry = Entry(root,textvariable = password_value)

#packing
user_entry.grid(row = 1, column = 1)
password_entry.grid(row = 2, column = 1)

Button(text = "Submit",command = get_val).grid()
remember_me = Checkbutton(text = "Remember Me", variable= remember_me)
remember_me.grid(row=4,column = 2)
root.mainloop()