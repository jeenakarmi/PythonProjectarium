import tkinter as tk

def click(event):
    #gives button that was clicked
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

#GUI logic 

#width x height
root.geometry("350x900")
root.title("Calculator")
root.wm_iconbitmap("D:/Codespot/Calculator/1.ico")


#width and height
root.minsize(300,500)
root.maxsize(700,500)

scvalue = tk.StringVar()
scvalue.set("")
screen= tk.Entry(root,textvar =scvalue, font="lucida 40 bold")
screen.pack(fill=tk.X, ipadx=8, pady=10, padx=10)

frame1 = tk.Frame(root, bg= "grey")
button = tk.Button(frame1, text="9", font= "lucida 35 bold")
button.pack(side="left")
button.bind("<Button-1>", click)
frame1.pack()

frame2 = tk.Frame(root, bg= "grey")
button = tk.Button(frame1, text="8", font= "lucida 35 bold")
button.pack(side="left")
button.bind("<Button-1>", click)
frame2.pack()

frame3 = tk.Frame(root, bg= "grey")
button = tk.Button(frame1, text="7", font= "lucida 35 bold")
button.pack(side="left")
button.bind("<Button-1>", click)
frame3.pack()
root.mainloop() #eventloop

