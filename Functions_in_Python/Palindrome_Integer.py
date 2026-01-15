def palindrome_integer():
    positive_integers = input().split(', ')

    for current_integer in positive_integers:
        if current_integer == current_integer[::-1]:
            print('True')
        else:
            print('False')
palindrome_integer()
