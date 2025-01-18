# English Language
def show_balance(balance):
    print(f"Your balance is ${balance}")

def deposit():
    money = float(input("Enter the amount to deposit: "))
    return money

def withdraw(balance):
    money = float(input("Enter the amount to withdraw: "))
    if balance >= money:
        print(f"Here is your ${money}")
        return money
    elif balance <=0:
        print("Your balance should be greater than 0!")
        return 0
    else:
        print("Insufficient Balance!")
        return 0


def english():
    balance=0.0
    is_running=True

    while is_running:
        print(''' 
+---------------------------------------------------+
|                                                   |
|            WELCOME BACK TO THE ATM!               |
|                                                   |
+---------------------------------------------------+
|                                                   |
|   1. Check Balance                                |
|   2. Deposit                                      |
|   3. Withdraw Cash                                |
|   4. Exit                                         |
+---------------------------------------------------+
''')
        select_op=int(input("Enter your choice (1-4): "))
        if select_op == 1:
            show_balance(balance)
        elif select_op == 2:
            balance += deposit()
        elif select_op == 3:
            balance -= withdraw(balance)
        elif select_op == 4:
            is_running = False
        else:
            print("This is not a valid choice!")
    print('''
+---------------------------------------------------+
|                                                   |
|            THANKS FOR USING OUR ATM!              |
|                                                   |
+---------------------------------------------------+
''')

# Russian Language
def показать_баланс(баланс):
    print(f"Твой баланс ${баланс}")

def депозит():
    деньги = float(input("Введите сумму для внесения: "))
    return деньги

def cнять(баланс):
    деньги = float(input("Введите сумму для вывода: "))
    if баланс >= деньги:
        print(f"Вот ваш ${деньги}")
        return деньги
    elif баланс <=0:
        print("Ваш баланс должен быть больше 0!")
        return 0
    else:
        print("Недостаточный баланс!")
        return 0


def russian():
    баланс=0.0
    работает=True

    while работает:
        print(''' 
+---------------------------------------------------+
|                                                   |
|         ДОБРО ПОЖАЛОВАТЬ В БАНКОМАТ СНОВА!        |
|                                                   |
+---------------------------------------------------+
|                                                   |
|   1. Проверить баланс                             |
|   2. Депозит                                      |
|   3. Снять наличные                               |
|   4. Выход                                        |
+---------------------------------------------------+
''')
        выбор=int(input("Введите свой выбор (1-4): "))
        if выбор == 1:
            показать_баланс(баланс)
        elif выбор== 2:
            баланс+= депозит()
        elif выбор == 3:
            баланс -= cнять(баланс)
        elif выбор == 4:
            работает = False
        else:
            print("Это недопустимый выбор!")
    print('''
+---------------------------------------------------+
|                                                   |
|      СПАСИБО, ЧТО ПОЛЬЗУЕТЕСЬ НАШИМ БАНКОМАТОМ!   |
|                                                   |
+---------------------------------------------------+
''')

# Uzbek Language
def balans_tekshirish(balans):
    print(f"Sizning balansingiz ${balans}")

def depozit():
    pul = float(input("Введите сумму для внесения: "))
    return pul

def olish(balans):
    pul = float(input("Введите сумму для вывода: "))
    if balans >= pul:
        print(f"Mana sizning ${pul}")
        return pul
    elif balans <=0:
        print("Balansingiz 0 dan katta bo'lishi kerak!")
        return 0
    else:
        print("Balans yetarli emas!")
        return 0


def uzbek():
    balans=0.0
    ishlaydi=True

    while ishlaydi:
        print(''' 
+---------------------------------------------------+
|                                                   |
|           ATMGA YANA Xush kelibsiz!               |
|                                                   |
+---------------------------------------------------+
|                                                   |
|   1. Balansni tekshirish                          |
|   2. Depozit                                      |
|   3. Naqd pul yechib olish                        |
|   4. Chiqish                                      |
+---------------------------------------------------+
''')
        tanlov=int(input("Tanlovingizni kiriting (1-4): "))
        if tanlov == 1:
            balans_tekshirish(balans)
        elif tanlov== 2:
            balans+= depozit()
        elif tanlov == 3:
            balans -= cнять(balans)
        elif tanlov == 4:
            ishlaydi = False
        else:
            print("Bu qabul qilib bo'lmaydigan tanlovdir!")
    print('''
+---------------------------------------------------+
|                                                   |
|   BANKOMATIMIZDAN FOYDALANGANINGIZ UCHUN RAHMAT!  |
|                                                   |
+---------------------------------------------------+
''')

if __name__ == '__main__':
    print(''' 
+---------------------------------------------------+
|                                                   |
|                 Welcome to ATM                    |
|                                                   |
+---------------------------------------------------+                                                        
|      1.English                                    |
|      2.Russian                                    |
|      3.Uzbek                                      |
+---------------------------------------------------+
''')
    chose_language = int(input("SELECT YOUR LANGUAGE: "))
    if chose_language == 1:
        english()
    elif chose_language == 2:
        russian()
    elif chose_language == 3:
        uzbek()
    else:
        print('''
+---------------------------------------------------+
|                                                   |
|          ENTER ONE OF THE GIVEN LANGUAGES!        |
|                                                   |
+---------------------------------------------------+
''')
