import tkinter

w = tkinter.Tk()
w.title("Images & icon")

img = tkinter.PhotoImage(file="D:\wallpaper\d312dac6e71b17141a3adf5127339bd2.jpg")

l = tkinter.Label(w, image=img)
l.pack()

w.mainloop()
