from tkinter import *

def click(event):
    global scvalue

    text = event.widget.cget("text")
    print(text)

    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    elif text =="BS":
        c=scvalue.get()
        scvalue.set(c[:-1])
        screen.update
    
    
    
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("520x500")  
root.minsize(520, 500)
root.maxsize(520, 500)
root.title("Project Calculator")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipady=20, ipadx=5, pady=5, padx=5)

buttons = [
    "C", "=", "%", "7", "8", "9",
    "-", "+", "*", "4", "5","6",
    "." , "/", "0", "1", "2", "3","BS",
    "00","(",")","[","]"
]


def pack_buttons(buttons, frame):
    for symbol in buttons:
        b = Button(frame, text=symbol, padx=0, pady=0, font="lucida 20 
                   ", width=4, height=2, fg="white", bg="black")
        b.pack(side=LEFT, padx=5, pady=5)
        b.bind("<Button-1>", click)
    frame.pack()


rows = [buttons[i:i+6] for i in range(0, len(buttons), 6)]

for row in rows:
    f = Frame(root,bg ="gray")
    pack_buttons(row, f)

root.mainloop()