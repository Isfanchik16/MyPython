import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

numb_letters = int(input("How many letters should the password have? "))
numb_numbers = int(input("How many numbers should the password have? "))
numb_symbols = int(input("How many symbols should the password have? "))

your_password = []

for x in range(numb_letters):
    random_letters = random.choice(letters)
    your_password.append(random_letters)

for x in range(numb_numbers):
    random_numbers = random.choice(numbers)
    your_password.append(random_numbers)

for x in range(numb_symbols):
    random_symbols = random.choice(symbols)
    your_password.append(random_symbols)

result = "".join(your_password)
print(f"Your desired passport is -{result}-")