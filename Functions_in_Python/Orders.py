def total_sum(product, quantity):
    if product == 'coffee':
        price = 1.50
    elif product == 'coke':
        price = 1.40
    elif product == 'water':
        price = 1.00
    elif product == 'snacks':
        price = 2.00
    return price * quantity

product = input()
quantity = int(input())

result = (total_sum(product, quantity))
print(f'{result:.2f}')
