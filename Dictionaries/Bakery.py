data = input().split(" ")

stock = {}
for item in range(0, len(data), 2):
    food = data[item]
    quantity = data[item + 1]
    stock[food] = int(quantity)
print(stock)
