# credits:https://www.udemy.com/course/100-days-of-code/
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [letters[i] for i in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)
    Password_entry.insert(0, password)
    print(f"password is:{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data_to_file():
    website = website_entry.get()
    email = Email_entry.get()
    password = Password_entry.get()
    if website == "" or password == "":
        messagebox.showwarning(title="Alert!", message=f"Don't leave fields empty")
        return
    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered \n{email},\n{password}")
    if is_ok:
        with open("data.txt", "a") as f:
            f.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            Password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=YELLOW)

# title_label = Label(text="Password Manager", font=(FONT_NAME, 25, "bold"), fg=RED, bg=YELLOW)
# title_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)
pwd_mng_img = PhotoImage(file="logo.png")
canvas.create_image(100, 110, image=pwd_mng_img)
canvas.grid(row=1, column=1)

website_label = Label(text="Website:", font=(FONT_NAME, 15), fg="black", bg=YELLOW)
website_label.grid(row=2, column=0)

website_entry = Entry(width=50)
website_entry.grid(row=2, column=1, columnspan=2)
website_entry.focus()

Email_label = Label(text="Email/Username:", font=(FONT_NAME, 15), fg="black", bg=YELLOW)
Email_label.grid(row=3, column=0)

Email_entry = Entry(width=50)
Email_entry.insert(0, "raviaahlad@gmail.com")
Email_entry.grid(row=3, column=1, columnspan=2)

Password_label = Label(text="Password:", font=(FONT_NAME, 15), fg="black", bg=YELLOW)
Password_label.grid(row=4, column=0)

Password_entry = Entry(width=32)
Password_entry.grid(row=4, column=1)

Generate_Password_Button = Button(text="Generate Password", command=generate_password)
Generate_Password_Button.grid(row=4, column=2)

Add_Button = Button(text="Add", width=36, command=save_data_to_file)
Add_Button.grid(row=5, column=1, columnspan=2)

# Compulsory
window.mainloop()
