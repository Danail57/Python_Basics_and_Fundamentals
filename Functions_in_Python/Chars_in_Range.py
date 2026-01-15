def characters(first_symbol: str, second_symbol:str):
    characters = []
    for current_character_as_digit in range(ord(first_symbol) + 1, ord(second_symbol)):
        characters.append(chr(current_character_as_digit))
    return characters

first_symbol = input()
second_symbol = input()
all_characters = characters(first_symbol, second_symbol)
print(' '.join(all_characters))
