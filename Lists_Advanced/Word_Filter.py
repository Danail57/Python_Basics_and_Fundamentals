words = input().split()
word_list_filtered = [word for word in words if len(word) % 2 == 0]
print('\n'.join(word_list_filtered))
