import random
rolled_numbers = []
for i in range(101):
    dice_roll = random.randint(2,12)
    #print(i, dice_roll)
    rolled_numbers.append(dice_roll)
print(rolled_numbers)

number = int(input('You have two dice, what number do you want to get? '))
probability = int((rolled_numbers.count(number) / 100) * 100)
print(f'The chance of you getting {number} is {probability}%')