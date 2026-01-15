def available_models():
    return {
        'Ford Fiesta': 12000,
        'Skoda Octavia': 24000,
        'Lamborghini Elemento': 100000,
        'Koenigsegg Agera': 4000000
    }
def budget():
    models = available_models()
    user_budget = int(input('Enter your budget: '))

    affordable = []
    for model, price in models.items():
        if user_budget >= price:
            affordable.append(model)

    if affordable:
        print('You can afford the following car(s):')
        for car in affordable:
            print(f'- {car}')
    else:
        print('Your budget is too low for these cars.')
budget()
