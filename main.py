from tkinter import *
from tkinter import messagebox
from PIL import Image

import qrcode


qr_data = {}

# Functions.


def save_link():
    qr_data["saved_link"] = link_storage.get()
    print(qr_data)
    link_entry.delete(0, END)


def save_filename():
    qr_data["file_name"] = name_storage.get()
    print(qr_data)
    name_entry.delete(0, END)


def generate_qr():
    qr_name_splitted = (qr_data.get("file_name", "QR").split(".")[0] + ".png")
    qr_img = qrcode.make(qr_data.get("saved_link"))
    qr_img.save(qr_name_splitted)
    Image.open(qr_name_splitted).show()
    messagebox.showinfo("Info", "QR code was successfully generated!")


# -------Main-Frame----------------


screen = Tk()
screen.title("QR Generator")
screen.geometry("500x400")
screen.configure(background="white")

# Setting Background Picture.
bg_picture = Canvas(screen, bg="white", height=100, width=100)
filename = PhotoImage(file="bg.png")
background_label = Label(screen, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Logo.
logo = PhotoImage(file="logo.png")
logo_label = Label(screen, image=logo)
logo_label.pack()

# ------Link-Entry---------------

# Link Info text.
text_top = Label(screen, text="Input Link to the File: ", font="none 24 bold")
text_top.pack()

# Link EntryText.
link_storage = StringVar()
link_entry = Entry(screen, width=50, bg="white", fg="black", textvariable=link_storage)
link_entry.pack()

# Link Submit Button.
link_submit_button = Button(screen, width=10, bg="white", text="Submit", command=save_link)
link_submit_button.pack()

# -----Filename-Entry--------------------

# Filename EntryText.
text_link = Label(screen, text="Input Desired Filename: ", font="none 24 bold")
text_link.pack()

# Filename Entry.
name_storage = StringVar()
name_entry = Entry(screen, width=50, bg="white", fg="black", textvariable=name_storage)
name_entry.pack()

# Name Submit Button.
name_submit_button = Button(screen, width=10, bg="white", text="Submit", command=save_filename)
name_submit_button.pack()

# test
generate_qr_button = Button(screen, width=10, bg="white", text="Generate", command=generate_qr)
generate_qr_button.pack()


screen.mainloop()
