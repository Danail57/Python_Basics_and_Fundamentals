stock_data = input().split()

stock = {}
for index in range(0, len(stock_data), 2):
    product = stock_data[index]
    quantity = int(stock_data[index + 1])
    stock[product] = quantity
products_to_search = input().split()
for product in products_to_search:
    if product in stock:
        print(f'We have {stock[product]} of {product} left')
    else:
        print(f"Sorry, we don't have {product}")
