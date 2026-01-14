phonebook = {}

while (command := input()) != "search":
    name, phone_number = command.split("-")
    phonebook[name] = phone_number

while True:
    name = input()
    if name == 'Stop':
        break
    if name not in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")
