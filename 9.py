items = {
    'bag': 30,
    'shoes': 150,
    'hat': 10
}

customer_money = 100
purchase_tries = 0

def MaxPurchase():
    SystemExit('You have reached maximum purchase attempts.')

if purchase_tries == 3:
    raise MaxPurchase()
def print_items():
    for item, price in items.items():
        print(f'{item.capitalize()}: £{price}')

print('Welcome to the shop 🛒\nItems are:')
print_items()

customer_option = input('Input your chosen item here, or to exit type e: ').lower()

if customer_option == 'e':
    raise SystemExit('You have exited the shop.')

if customer_option not in items:
    raise ValueError('Invalid input')


if customer_option == 'bag' and customer_money >= items.get('bag'):
    print(f'Here’s your {customer_option}!')
    raise SystemExit('Thank you for shopping.')
elif customer_option == 'bag' and not customer_money >= items.get('bag'):
    more_money = input(f'You cannot afford the {customer_option}\nDo you have more money? (y/n): ').lower()
    if more_money == 'y':
        add_money = float(input('Add to balance: £'))
        try:
            add_money > 0
        except:
            print('Cannot add input to balance.')

        customer_money += add_money
        print(f'Your balance is now £{customer_money:.2f}')
    elif customer_option == 'n':
        purchase_tries += 1

def is_above_zero(num):
    """
    Function that accepts a number and returns true if above 0
    :param num:
    :return: Boolean
    """
    if num > 0:
        return True
    else:
        return False