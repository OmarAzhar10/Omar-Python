# from tkinter import *


# root = Tk()
# root.title("My first Tkinter window😎")
# root.geometry("400x300")
# root.configure(bg="light green")

# entry = Entry(root)
# entry.place(x= 100, y=100)

# root.mainloop()






from tkinter import *
root = Tk()
root.title("grid example")

def hello():
    print("Hello your form has been submitted")

label1 = Label(root, text="username:")
label1.grid(row=0, column=0, padx=5, pady=5)

entry1 = Entry(root)
entry1.grid(row=0, column=1, padx=5, pady=5)

label2 = Label(root, text="password")
label2.grid(row=1, column=0, padx=5, pady=5)

entry2 = Entry(root, show="*")
entry2.grid(row=1, column=1, padx=5, pady=5)


button = Button(root, text="Login", command=hello)
button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()