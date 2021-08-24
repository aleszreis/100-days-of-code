PLACEHOLDER = "[name]"


with open("./Input/Names/invited_names.txt") as file:
    nomes = file.readlines()

with open("./Input/Letters/starting_letter.docx", encoding='UTF-8') as file:
    content = file.read()

for nome in nomes:
    nome_sem_espaco = nome.strip()
    nova_carta = content.replace(PLACEHOLDER, nome_sem_espaco)

    with open(f"./Output/ReadyToSend/letter_for_{nome_sem_espaco}.txt", mode="w") as completed_letter:
        completed_letter.write(nova_carta)
