class Item:
    def __init__(self, name, expiry_days, is_almost_empty):
        self.is_almost_empty = is_almost_empty
        self.expiry_days = expiry_days
        self.name = name

items = [
        Item("Jam", 5, False),
        Item("Milk", 2, True),
        Item("Butter", 10, False)
    ]

def fridge_organizer(items):
    valid_items = [item for item in items if item.expiry_days >= 0]
    valid_items.sort(key = lambda x: (not x.is_almost_empty, x.expiry_days, x.name))
    return [item.name for item in valid_items]

print(fridge_organizer(items))
