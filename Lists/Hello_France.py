collection_of_items = input().split('|')
budget = float(input())
selling_price_list = []
ticket = 150
total_shopping_sum = 0
total_selling_sum = 0

for item in collection_of_items:
    new_item = item.split("->")
    current_item = new_item[0]
    current_price = float(new_item[1])

    if current_item == 'Clothes' and current_price <= 50.00 and budget >= current_price:
        budget -= current_price
        total_shopping_sum += current_price
        selling_price = current_price * 1.40
        total_selling_sum += selling_price
        selling_price_list.append(f'{selling_price:.2f}')

    elif current_item == 'Shoes' and current_price <= 35.00 and budget >= current_price:
        budget -= current_price
        total_shopping_sum += current_price
        selling_price = current_price * 1.40
        total_selling_sum += selling_price
        selling_price_list.append(f'{selling_price:.2f}')

    elif current_item == 'Accessories' and current_price <= 20.50 and budget >= current_price:
        budget -= current_price
        total_shopping_sum += current_price
        selling_price = current_price * 1.40
        total_selling_sum += selling_price
        selling_price_list.append(f'{selling_price:.2f}')

final_budget = budget + total_selling_sum
print(' '.join(selling_price_list))

profit = total_selling_sum - total_shopping_sum
print(f'Profit: {profit:.2f}')
if final_budget >= ticket:
    print('Hello, France!')
else:
    print('Not enough money.')
