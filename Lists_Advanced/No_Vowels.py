text = input()

sorted_text = [symbol for symbol in text if symbol.lower() not in ['a', 'o', 'u', 'e', 'i']]
print(''.join(sorted_text))
