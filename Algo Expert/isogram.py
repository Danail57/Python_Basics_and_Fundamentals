def is_isogram(string):
    string = string.lower()
    seen_letters = {}

    for char in string:
        if char in seen_letters:
            return False
        seen_letters[char] = True
    return True