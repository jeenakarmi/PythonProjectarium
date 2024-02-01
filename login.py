from tkinter import *

def get_val():
    print(f"{user_value.get() , password_value.get()}")

    with open("records.txt", "a") as f:
        f.write(f"{user_value.get(), (password_value.get())} \n")

def toggle_password_visibility():
    if show_password.get():
        password_entry.config(show="")
        show_password_label.config(text="👀")
    else:
        password_entry.config(show="*")
        show_password_label.config(text="😎")

def load_credentials(): # need to modify
    try:
        with open("records.txt", "r") as f:
            lines = f.readlines()
            if lines:
                last_line = lines[-1]
                username, password = last_line.strip().split(', ')
                user_value.set(username)
                password_value.set(password)
                remember_me.set(0)  # Check the "Remember Login" checkbox
    except FileNotFoundError:
        # Display an error message if the file is not found
        print("Error: File 'records.txt' not found.")
    except Exception as e:
        # Handle other exceptions and display an error message
        print(f"An error occurred: {e}")

root = Tk()
root.geometry("500x335")
root.minsize(500, 275)
root.maxsize(600, 200)
root.title("Login Page")

# Centering everything
root.columnconfigure(0, weight=1)
root.columnconfigure(3, weight=2)
root.rowconfigure(0, weight=0)
root.rowconfigure(7, weight=0)

Label(root, text="Welcome To Login Page", font="comicsansms 13 bold", pady=20).grid(row=0, column=2, sticky="nsew")

user = Label(root, text="Username")
password = Label(root, text="Password")
user.grid(row=1, column=1, sticky="nsew")
password.grid(row=2, column=1, sticky="nsew")

user_value = StringVar()
password_value = StringVar()
remember_me = IntVar()
show_password = IntVar()

user_entry = Entry(root, textvariable=user_value)
password_entry = Entry(root, textvariable=password_value, show="*")

# packing
user_entry.grid(row=1, column=2, sticky="nsew")
password_entry.grid(row=2, column=2, sticky="nsew")

Button(text="Submit", command=get_val, bg="blue", fg="white").grid(row=6, column=2, sticky="nsew")

load_credentials()
remember_me = Checkbutton(text="Remember Login", variable=remember_me)
remember_me.grid(row=4, column=2, sticky="nsew")

show_password_label = Label(root)
show_password_label.grid(row=2, column=3, sticky="w", padx=(0, 10))  # Adjust padx to move the emoji closer to the password entry

show_password_checkbox = Checkbutton(text="Show  Password", variable=show_password, command=toggle_password_visibility)
show_password_checkbox.grid(row=5, column=2, sticky="nsew")

root.mainloop()
