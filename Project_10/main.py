def plus(num1,num2):
    return num1+num2
def minus(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2
def rem(num1,num2):
    return num1%num2
def square(num1,num2):
    return num1+num2

is_running=True
while is_running:
    num1 = float(input("Enter first number : "))
    op = input('Chose method "+", "-", "*", "/", "%", "**" : ')
    num2 = float(input("Enter second number : "))
    if op == "+":
        print("You chose '+' method and the outcome is {}".format(plus(num1,num2)))
    elif op == "-":
        print("You chose '-' method and the outcome is {}".format(minus(num1,num2)))
    elif op == "*":
        print("You chose '*' method and the outcome is {}".format(mul(num1,num2)))
    elif op == "/":
        print("You chose '/' method and the outcome is {}".format(div(num1,num2)))
    elif op == "%":
        print("You chose '%' method and the outcome is {}".format(rem(num1,num2)))
    elif op == "**":
        print("You chose '**' method and the outcome is {}".format(square(num1,num2)))
    else:print("Unknown method!")
    quit = input("Do you wanna calculate again? (Yes or No) : ").lower()
    if quit=="yes":is_running=True
    else:is_running=False