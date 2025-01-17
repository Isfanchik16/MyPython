Capputhino_price = 1.5
Latte_price = 2.0
Espresso_price = 2.5

coffee_choice = int(input("""What kinds of coffee  Capputhino = $1.5 Latte = $2 Espresso = $2.5. PLease Choose: 
Capputhino (1),Latte (2),Exspreso (3) Do you prefer? """))

if coffee_choice==1:
    print(f"You have to pay ${Capputhino_price}")
elif coffee_choice==2:
    print(f"You have to pay ${Latte_price}")
elif coffee_choice==3:
    print(f"You have to pay ${Espresso_price}")

ten = int(input(" How many 10 cents do you want to pay? "))
twenty_five = int(input(" How many 25 cents do you want to pay? "))
fifty = int(input(" How many 50 cents do you want to pay? "))
total_money = (ten*0.1)+(twenty_five*0.25)+(fifty*0.50)
print(f"Your total money is ${total_money}")

pay = input("Do you want to pay? (Yes or No) >> ").lower()
if pay == "yes":
    if coffee_choice == 1:
        if Capputhino_price <= total_money:
            print("Here is your Capputhino come again!")
            if total_money-Capputhino_price !=0:print(f"You payed a bit more here is your ${total_money-Capputhino_price}")
            else:print("You have payed successfully!")
        else:print(f"You have to pay ${Capputhino_price} and You don't have enought money!")
    if coffee_choice == 2:
        if Latte_price <= total_money:
            print("Here is your Latte come again!")
            if total_money-Latte_price !=0:print(f"You payed a bit more here is your ${total_money-Latte_price}")
            else:print("You have payed successfully!")
        else:print(f"You have to pay ${Latte_price} and You don't have enought money!")
    if coffee_choice == 3:
        if Espresso_price <= total_money:
            print("Here is your Espresso come again!")
            if total_money-Espresso_price !=0:print(f"You payed a bit more here is your ${total_money-Espresso_price}")
            else:print("You have payed successfully!")
        else:print(f"You have to pay ${Espresso_price} and You don't have enought money!")
else:
    print("Okey! 👍")

