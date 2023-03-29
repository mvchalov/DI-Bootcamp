# Challenge 1
letters = {}
user_word = input("Enter a word: ")


def letter_check(indata):
    i, data = indata
    if data in letters.keys():
        letters[data].append(i)
    else:
        letters[data] = [i]


for item in enumerate(list(user_word)):
    letter_check(item)
print(letters)

# Challenge 2
indata = [
    {
        'items_purchase':
            {
                "Water": "$1",
                "Bread": "$3",
                "TV": "$1,000",
                "Fertilizer": "$20"
            },
        'wallet': "$300"
    },
    {
        'items_purchase':
            {
                "Apple": "$4",
                "Honey": "$3",
                "Fan": "$14",
                "Bananas": "$4",
                "Pan": "$10",
                "Spoon": "$2"
            },
        'wallet': "$100"
    },
    {
        'items_purchase':
            {
                "Phone": "$999",
                "Speakers": "$300",
                "Laptop": "$5,000",
                "PC": "$1200"
            },
        'wallet': "$1"
    }
]


def price_correction(price):
    return int(''.join(list(filter(lambda e: e.isdigit(), price))))


for test_set in indata:
    current_items = {}
    for key, value in test_set['items_purchase'].items():
        current_items[key] = price_correction(value)
    current_items = sorted(current_items.items(), key=lambda e: e[1], reverse=True)
    current_money = price_correction(test_set['wallet'])
    purchases = []
    while len(current_items) > 0 and current_money - current_items[-1][1] > 0:
        current_index = 0
        while (current_money - current_items[current_index][1] < 0):
            current_index += 1
        purchases.append(current_items[current_index][0])
        current_money -= current_items[current_index][1]
        del current_items[current_index]
    print(', '.join(purchases) or "There's nothing to buy")
