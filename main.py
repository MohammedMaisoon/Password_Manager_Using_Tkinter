from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_text_button():
    website_get = web_entry.get()
    email_get = email_entry.get()
    password_get = pass_entry.get()

    if len(website_get) == 0 or len(password_get) == 0:
        messagebox.showinfo(title="Oops",message="Please Make Sure you haven't left any fields empty.")
    else:
        is_ok=messagebox.askokcancel(title="website", message=f"These are the Details Entered: \nEmail:{email_get}" 
        f"\nPassword:{password_get}\n is it ok to save?")

        if is_ok:
            with open("data.txt", "a") as file:
                name = file.write(f"{website_get} | {email_get} | {password_get}\n")
                web_entry.delete(0,END)
                pass_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

Web = Label(text="Website:")
Web.grid(row=1,column=0)

Email = Label(text="Email/Username:")
Email.grid(row=2, column=0)

Pass = Label(text="Password:")
Pass.grid(row=3, column=0)

web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, columnspan=2)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "username@gmail.com")

pass_entry = Entry(width=21)
pass_entry.grid(row=3,column=1)

Gen_pass = Button(text="Generate Password", command=generate_password)
Gen_pass.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=add_text_button)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()