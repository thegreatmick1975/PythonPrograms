## Python Interest Calculator

from tkinter import *

root = Tk()
root.title('Simple Interest Calculator')
root.geometry("500x300")

def Calculate():
    prin = int(principalentry.get())
    rat = float(rateentry.get())
    tim = int(timeentry.get())
    if timeunit.get() == "Months":
        tim /= 12
    amount = (prin * rat * tim) / 100
    total = prin + amount
    Label(text=f"Total amount: {total:.2f}", font="arial 30 bold").place(x=150, y=220)



principal=Label(root,text="Principal:", font="arial 15")
rate=Label(root, text= "Rate of Interest:", font="arial 15")
time=Label(root, text= "Time:", font= "arial 15")

principal.place(x=50, y=20)
rate.place(x=50, y=90)
time.place(x=50, y=160)

interest=Label(root, text="Interest:", font="arial 15")
interest.place(x=50, y=230)

principalvalue=StringVar()
ratevalue=StringVar()
timevalue=StringVar()

principalentry=Entry(root, textvariable=principalvalue, font= "arial 20", width=8)
rateentry=Entry(root, textvariable=ratevalue, font= "arial 20", width=8)
timeentry=Entry(root, textvariable=timevalue, font="arial 20", width=8)

principalentry.place(x=200, y=20)
rateentry.place(x=200, y=90)
timeentry.place(x=200, y=160)

timeunit = StringVar()
timeunit.set("Months")
timemenu = OptionMenu(root, timeunit, "Months", "Years")
timemenu.config(font="arial 15", width=8)
timemenu.place(x=350, y=160)


Button(text="Calculate", font="arial 15", command=Calculate).place(x=350, y=20)
Button(root, text="Exit", command=lambda:exit(), font="arial 15", width=8).place(x=350, y=90)


root.mainloop()













