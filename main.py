import tkinter as tk

def click(event):
    # Gives button that was clicked
    # cget: extracts text from widget
    
    global scvalue

    text = event.widget.cget("text")
    print(text)
    if text == "=":
        pass
    elif text == "C":
        pass
    else:
        # showing in screen
        scvalue.set(scvalue.get() + text)
        screen.update()

root = tk.Tk()

# GUI logic 

# Width x height
root.geometry("350x900")
root.title("Calculator")
root.wm_iconbitmap("D:/Codespot/Calculator/1.ico")

# Width and height
root.minsize(300,500)
root.maxsize(700,500)

scvalue = tk.StringVar()
scvalue.set("")
screen = tk.Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=tk.X, ipadx=8, pady=10, padx=10)

# Create a frame for the digits
frame_digits = tk.Frame(root, bg="grey")
frame_digits.pack()

# Define digits 0 to 9
digits = list(range(10))

# Create and place the buttons for digits
for digit in digits:
    # Calculate row and column for each digit
    row = 3 - (digit - 1) // 3  # Distribute digits over 3 rows
    column = (digit - 1) % 3  # Distribute digits over 3 columns
    if digit == 0:
        row = 4
        column = 1
    button = tk.Button(frame_digits, text=str(digit), font="lucida 35 bold")
    button.grid(row=row, column=column, padx=5, pady=5)
    button.bind("<Button-1>", click)

root.mainloop()  # Event loop
