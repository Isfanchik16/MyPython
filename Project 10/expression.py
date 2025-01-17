def plus(num1,num2):
    return num1+num2
def minus(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def division(num1,num2):
    return num1/num2
def remainder(num1,num2):
    return num1%num2
def square(num1,num2):
    return num1,num2

is_running=True

while is_running:
    value1=int(input("Enter first number : "))
    op = input('Chose method "+", "-", "*", "/", "%" "**" : ')
    value2=int(input("Enter second number : "))
    if op=="+":
        print(f"You chose '+' method and the outcome is {plus(value1,value2)}")
    elif op=="-":
        print(f"You chose '-' method and the outcome is {minus(value1,value2)}")
    elif op=="*":
        print(f"You chose '*' method and the outcome is {multiply(value1,value2)}")
    elif op=="/":
        print(f"You chose '/' method and the outcome is {division(value1,value2)}")
    elif op=="%":
        print(f"You chose '%' method and the outcome is {remainder(value1,value2)}")
    elif op=="**":
        print(f"You chose '**' method and the outcome is {square(value1,value2)}")
    else:
        print("Unknown method!")

    quit = input("Do you wanna calculate again? (Yes or No) : ").lower()
    if quit == "yes":
        is_running = True
    else:
        is_running= False