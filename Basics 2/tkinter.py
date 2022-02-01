from tkinter import *
from datetime import datetime
from tkinter import messagebox

root = Tk()
root.title('Age Calculator')
root.geometry("500x300")


def age():
    if my_entry.get():
        my_age = my_entry.get().split('/')
        year = datetime.now().year - int(my_age[0])
        month = datetime.now().month - int(my_age[1])
        day = datetime.now().day - int(my_age[2])
        messagebox.showinfo(
            "Your Age", f"Your Age Is: {year} years - {month} months - {day} days")
    else:
        messagebox.showerror("Error", "You forgot to enter your age!")


my_label = Label(
    root, text="Enter Year Born [yyyy/mm/dd]", font=("Helvetica", 24))
my_label.pack(pady=20)

my_entry = Entry(root, font=("Helvetica", 18))
my_entry.pack(pady=20)

my_button = Button(root, text="Calculate Age!",
                   font=("Helvetica", 18), command=age)
my_button.pack(pady=20)


root.mainloop()
