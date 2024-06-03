import tkinter as tk

def click(event):
    # Gives button that was clicked
    # cget: extracts text from widget
    
    global scvalue

    text = event.widget.cget("text")
    print(text)
    if text == "=":
        try:
            result = eval(scvalue.get())
            scvalue.set(result)
        except Exception as e:
            scvalue.set("Error")
    elif text == "C":
        scvalue.set("")
    else:
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
frame_buttons = tk.Frame(root, bg="grey")
frame_buttons.pack()

# Define button labels
button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Create and place the buttons in the frame
row_val = 0
col_val = 0

for text in button_texts:
    button = tk.Button(frame_buttons, text=text, font="lucida 20 bold", width=4, height=2)
    button.grid(row=row_val, column=col_val, padx=5, pady=5)
    button.bind("<Button-1>", click)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop() # Event loop
