from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title('Denomination counter')
root.configure(bg='light blue')
root.geometry('650x400')

upload = Image.open("img-2.jpg")

upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='light blue')
label.place(x=180, y=20)

label1 = Label(root
               text="hi, Welcome", 
               bg='light blue')
label.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    MsgBox = messagebox.showinfo(
        "Alert", "do you want to calculate"
    )
    if MsgBox == 'ok':
        topwin()


button1 = Button(root, 
                  text="Let's get started",
                  command=msg,
                  bg='brown',
                  fg='white')
button1.place(x=260, y=360)


def topwin():
    top = Toplevel()
    top.title("Denominations calculator")
    top.configure('light grey')
    top.geometry("600x360+50+50")



    label = Label(top, text="enter total amount", bg='light grey')
    entry = Entry(top)
    lbl = Label(top, text= "Here are no. of notes", bg='light grey')

    l1 = Label(top, text="2000", bg='light grey')
    l1 = Label(top, text="500", bg='light grey')
    l1 = Label(top, text="100", bg='light grey')