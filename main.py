from tkinter import *
from tkinter import messagebox
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
def generate():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    pass_input.insert(0, password)
    pyperclip.copy("The text to be copied to clipboard")





# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_input.get()
    email = email_input.get()
    password = pass_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Message", message="Please don't leave the fields empty")


    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n "
                                                              f"Email: {email}\n Password: {password}\n Is it ok to save? ")

        if is_ok:
            with open("data.txt", "a") as f:
                f.write(f"{website} | {email} | {password}\n")
            web_input.delete(0, END)
            pass_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

web_label = Label(text="Website: ")
web_label.grid(column=0, row=1)

web_input = Entry(width=35)
web_input.grid(column=1, row=1, columnspan=2)
web_input.focus()

email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "zoha@email.com")

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

pass_input = Entry(width=21)
pass_input.grid(column=1, row=3)

button_gen_pass = Button(text="Generate Password", command=generate)
button_gen_pass.grid(column=2, row=3)

button_add = Button(text="Add", width=36, command=save)
button_add.grid(column=1, row=4, columnspan=2)

# save()

window.mainloop()
