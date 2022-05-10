from tkinter import *

# Driver code
if __name__ == "__main__":
    # Create a GUI window
    w = Tk()

    w.title("Form")  # Set title of GUI window
    w.configure(background="light blue")  # Set background color of GUI window
    w.geometry("480x380")  # set size of GUI window

    # Creating form & grid method (like table)
    heading = Label(w, text="Registration Form", bg="light blue", font=("bold", 14)).grid(columnspan=2)

    name = Label(w, text="Enter your name", bg="light blue").grid(row=1, column=0)
    nm = Entry(w).grid(row=1, column=1, ipadx=100)  # ipadx --> width of entry

    age = Label(w, text="Enter your age", bg="light blue").grid(row=2, column=0)
    ag = Entry(w).grid(row=2, column=1, ipadx=100)

    addr = Label(w, text="Enter address", bg="light blue").grid(row=3, column=0)
    ad = Entry(w).grid(row=3, column=1, ipadx=100)

    ph = Label(w, text="Enter your mobile num", bg="light blue").grid(row=4, column=0)
    p = Entry(w).grid(row=4, column=1, ipadx=100)

    em = Label(w, text="Enter your Email", bg="light blue").grid(row=5, column=0)
    eml = Entry(w).grid(row=5, column=1, ipadx=100)

    gen = Label(w, text="Select gender", bg="light blue").grid(row=6, column=0)  # radio button
    var = IntVar()
    rbm = Radiobutton(w, text="Male", bg="light blue", padx=5, variable=var, value=1).place(x=170, y=132)
    rbf = Radiobutton(w, text="Female", bg="light blue", padx=20, variable=var, value=2).place(x=230, y=132)

    country = Label(w, text="Select country", bg="light blue").grid(row=8, column=0)
    list1 = ['Canada', 'India', 'AUS']
    c = StringVar()
    droplist = OptionMenu(w, c, *list1).grid(row=8, column=1)
    # droplist.config(width=15)
    c.set("Select your country")

    btn_submit = Button(w, text="SUBMIT", bg="black", fg="light blue").grid(columnspan=2)  # button

    w.mainloop()
