receipt = {
"apple": 0.20,
"milk": 2,
"bread": 1.50,
"eggs": 3
}

def dictPrice(dict):
    total_price = float(sum(dict.values()))
    print("The total price of your items is: £{:.2f}".format(total_price))

dictPrice(receipt)


shop = {
    'book': 2,
    'chair': 10,
    'shoes': 15,
    'table': 30
}

print(shop)

item = input('What is your item? ')
if item in shop:
    print(f'Price is: £{shop[item]}')
else:
    print('This item does not exist.')