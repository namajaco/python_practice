def hello_world():
    print("Hello, World!")

hello_world()

def calculate_vat(amount):
    return print(amount * 1.2)
calculate_vat(100)

def changeString(string):
    print(string.upper())
    print(string.lower())
    first_letter = string[0].lower()
    last_letter = string[-1].lower()
    print(first_letter == last_letter)
    print(string.lower().replace(first_letter,"[REDACTED]"))

changeString("abcd")

input_str = "practice"
print(input_str[4::-2])
def removeFirstAndLastCharacter(str):
    str = str[1:]
    str = str[:-1]
    return print(str)

removeFirstAndLastCharacter("abcd")

students = ["Chloe", "Anna", "Lauren", "Shreya", "Siobhan"]
print(sorted(students)[0])

