my_money = float(input('How much money do you have? \n£'))
hours = 3
venue_cost_per_hour = 200 * hours
deposit = venue_cost_per_hour / 10
total_cost = venue_cost_per_hour + deposit
if my_money >= total_cost:
    print('You can afford the venue.')
else:
    print('You cannot afford the venue.')