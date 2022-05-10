import tkinter

window = tkinter.Tk()
window.title("Kavi")

topFrame = tkinter.Frame(window).pack()
bottomFrame = tkinter.Frame(window).pack(side="bottom")

btn1 = tkinter.Button(topFrame, text="button1", fg="red").pack()  # foreground color --> fg
bt2 = tkinter.Button(bottomFrame, text="button2", fg="white", bg="black").pack(side="left")


window.mainloop()
