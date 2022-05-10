import tkinter

w = tkinter.Tk()
w.title("mouse click event")


def say(event):
    tkinter.Label(w, text="Hi").pack()


btn1 = tkinter.Button(w, text="Click Here")
btn1.bind("<Button-1>", say)
btn1.pack()

w.mainloop()
