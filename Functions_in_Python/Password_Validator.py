def password_validator(some_password: str):
    list_with_error_messages = []
    
    if len(some_password) not in range(6, 11):
        list_with_error_messages.append("Password must be between 6 and 10 characters")
    if not some_password.isalnum():
        list_with_error_messages.append("Password must consist only of letters and digits")
    
    digits_counter = 0
    for current_character in some_password:
        if current_character.isdigit():
            digits_counter += 1
    if digits_counter < 2:
        list_with_error_messages.append("Password must have at least 2 digits")
    return list_with_error_messages

password = input()
error_messages = password_validator(password)
if not error_messages:
    print('Password is valid')
else:
    print('\n'.join(error_messages))
