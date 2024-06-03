import tkinter as tk
import math 

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
    elif text == "←":
        current_value = scvalue.get()
        scvalue.set(current_value[:-1])
    elif text == "√":
        current_value = scvalue.get()
        if current_value and current_value != "Error":
            try:
                result = math.sqrt(float(current_value))
                scvalue.set(result)
            except ValueError:
                scvalue.set("Error")
        else:
             scvalue.set("Error")
    else:
        scvalue.set(scvalue.get() + text)
    screen.update()

root = tk.Tk()
root.title("Calculator")

# GUI logic 

# Width x height
# Center the window on the screen
window_width, window_height = 400, 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

# Ensure the window can be resized
root.resizable(True, True)

# Style settings
bg_color = "#ffffff"  # White background
button_color = "#dcdcdc"  # Grey for operator buttons
button_active_color = "#bdc3c7"
clear_button_color = "#e74c3c"
equal_button_color = "#2ecc71"
screen_color = "#34495e"
button_text_color = "#2c3e50"
font = "Helvetica 20"
entry_font = "Helvetica 40"

# Configure the main window background
root.configure(bg=bg_color)

# StringVar to hold the value of the screen
scvalue = tk.StringVar()
scvalue.set("")

# Entry widget for the screen
screen = tk.Entry(root, textvar=scvalue, font= entry_font)
screen.pack(fill=tk.X, ipadx=8, pady=10, padx=10)

# Frame for the buttons
frame_buttons = tk.Frame(root, bg=bg_color)
frame_buttons.pack(expand=True, fill=tk.BOTH)


# Define button labels
button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '←', '0', '.', '+', 
    'C', '=', '%', '√',  
]

# Create and place the buttons in the frame
row_val = 0
col_val = 0

for text in button_texts:
    if text in ('/', '*', '-', '+','√'):
        button_bg = button_color
    elif text in ('C', '='):
        button_bg = clear_button_color if text == 'C' else equal_button_color
    else:
        button_bg = bg_color

    button = tk.Button(
        frame_buttons, text=text, font=font, bg=button_bg, fg=button_text_color, activebackground=button_active_color,
        bd=0, highlightthickness=0, relief=tk.RAISED
    )
    button.grid(row=row_val, column=col_val, padx=10, pady=10, sticky="nsew")
    button.bind("<Button-1>", click)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Make the grid cells expand proportionally
for i in range(4):
    frame_buttons.columnconfigure(i, weight=1)
for i in range(5):
    frame_buttons.rowconfigure(i, weight=1)


root.mainloop() # Event loop
