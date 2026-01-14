total_energy = 100
total_coins = 100

working_day_events = input().split('|')

for event in working_day_events:
    event_name, number = event.split('-')
    number = int(number)

    if event_name == 'rest':
        gained_energy = min(number, 100 - total_energy)
        total_energy += gained_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")

    elif event_name == 'order':
        if total_energy >= 30:
            total_energy -= 30
            total_coins += number
            print(f"You earned {number} coins.")
        else:
            total_energy += 50
            print("You had to rest!")

    else:
        if total_coins >= number:
            total_coins -= number
            print(f"You bought {event_name}.")
        else:
            print(f"Closed! Cannot afford {event_name}.")
            break
else:
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")
