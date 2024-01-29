from tkinter import *
root = Tk()
root.title('button')
root.geometry("500x300")

global is_on
is_on = False

my_label = Label(root, text="Colorblind Mode", fg='green', font=('Helvetica', 32))
my_label.pack(pady=20)


def switch():
    global is_on
    if is_on:
        on_button.config(image=off)
        is_on = False
    else:
        on_button.config(image=on)
        is_on = True

off = PhotoImage(file='images/off1.png')
on = PhotoImage(file='images/on1.png')


on_button = Button(root, image=off, bd=0, command=switch)
on_button.pack(pady=50)

root.mainloop()