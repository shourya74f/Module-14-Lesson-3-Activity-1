from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

r=Tk()
r.title("Denomination Counter")
r.configure(bg="light blue")
r.geometry("650x400")

u=Image.open("images-2.jpeg")
u=u.resize((300, 300))
i=ImageTk.PhotoImage(u)
l=Label(r, image=i, bg="light blue")
l.place(x=100, y=20)

l1=Label(r, text="Welcome to the Denomination Counter", bg="light blue")
l1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    b=messagebox.showinfo("Do you want to calculate the Denomination count?")
    if b=="ok":
        tw()

b=Button(r, text="Let's get started!", command=msg, bg="brown", fg="white")
b.place(x=260, y=360)

def tw():
    t=Toplevel()
    t.title("Denominations Calculator")
    t.configure(bg="light grey")
    t.geometry("600x350+50+50")

    l=Label(t, text="Enter total amount: ", bg="light grey")
    e=Entry(t)
    lb=Label(t, text="Here are the number of notes for each denomination", bg="light grey")

    l1=Label(t, text="2000", bg="light grey")
    l2=Label(t, text="500", bg="light grey")
    l3=Label(t, text="100", bg="light grey")

    t1=Entry(t)
    t2=Entry(t)
    t3=Entry(t)

    def c():
        try:
            global a
            a=int(e.get())
            n2000=a//2000
            a%=2000
            n500=a//500
            a%=500
            n100=a//100
            a%=100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, str(n2000))
            t1.insert(END, str(n500))
            t1.insert(END, str(n100))
        except ValueError:
            messagebox.showerror("Error",  "Please enter a valid number")

    b1=Button(t, text="Calculate", command=c, bg="purple", fg="red")

    l.place(x=230, y=50)
    e.place(x=200, y=80)
    b1.place(x=240, y=120)
    lb.place(x=140, y=170)

    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)

    t.mainloop()

r.mainloop()