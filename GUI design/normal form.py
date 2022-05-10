import tkinter

w = tkinter.Tk()
w.title("Form")
w.resizable(100, 200)


tkinter.Label(w, text="Enter your name", fg="black", bg="white").grid(row=1)
tkinter.Entry(w).grid(row=1, column=1)

tkinter.Label(w, text="Enter Password", fg="black", bg="white").grid(row=2)
tkinter.Entry(w).grid(row=2, column=1)

tkinter.Checkbutton(w, text="Agree").grid(columnspan=2)

w.mainloop()