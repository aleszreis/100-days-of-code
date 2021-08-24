from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [random.choice(letters) for letter in range(random.randint(6, 8))]
    pass_symbols = [random.choice(symbols) for symbol in range(random.randint(2, 4))]
    pass_numbers = [random.choice(numbers) for number in range(random.randint(2, 4))]

    password_list = pass_letters + pass_symbols + pass_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "senha": password,
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops!", message="Não é possível salvar se houver campos vazios.")
    else:
        try:
            with open("data.json") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file)

        except json.decoder.JSONDecodeError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file)

        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file)

        finally:
            password_entry.delete(0, END)
            email_entry.delete(0, END)
            website_entry.delete(0, END)

# ---------------------------- SEARCH TOOL ------------------------------- #
def search_website():
    site_title = website_entry.get()
    try:
        with open("data.json") as file:
            dictionary = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Erro", message=f"Arquivo não encontrado.")
    else:
        if site_title in dictionary:
            email = dictionary[site_title]["email"]
            senha = dictionary[site_title]["senha"]
            messagebox.showinfo(title=f"{site_title}", message=f'Email: {email}\nSenha: {senha}')
        else:
            messagebox.showinfo(title="Oops!", message=f"Não foi encontrada correspondência para o site '{site_title}'.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Gerenciador de senhas")
window.config(padx=35, pady=35)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=1)

website_label = Label(text="Site:")
website_label.grid(column=0, row=2)
website_entry = Entry(width=18)
website_entry.focus()
website_entry.grid(column=1, row=2,)


email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=3)
email_entry = Entry(width=38)
email_entry.grid(column=1, row=3, columnspan=2)


password_label = Label(text="Senha:")
password_label.grid(column=0, row=4)
password_entry = Entry(width=18)
password_entry.grid(column=1, row=4)


gen_button = Button(text="Gerar senha aleatória", command=generate_password)
gen_button.grid(column=2, row=4)

add_button = Button(text="Salvar", width=32, command=save)
add_button.grid(column=1, row=5, columnspan=2)

search_button = Button(text="Buscar", width=16, command=search_website)
search_button.grid(column=2, row=2)


window.mainloop()