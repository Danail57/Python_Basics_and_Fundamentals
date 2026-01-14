countries = input().split(", ")
capitals = input().split(", ")
geography_dictionary = {countries[index] : capitals[index] for index in range(len(countries))}
for country, capital in geography_dictionary.items():
    print(f'{country} -> {capital}')
