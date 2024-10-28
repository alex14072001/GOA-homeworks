#მთელმა გუნდმა ერთად შეასრულეთ ერთი დიდი მთლიანი პროექტი რაზეც გაკვეთილზე ვისაუბრეთ აბა თქვენ იცით დაუკავშირდით ერთმანეთს არავინ დაიზაროთ
bank = print("Hello How Can I Help You?")

bank_money = 155000551

Client = input("Hello i want to: ")
while True:
    if Client == "withdraw money":
        money_1 = float(input("How much?: "))
        bank_money = bank_money - money_1

        response = input("would you add somethings?:")
        if response == "no":
            print("okay goodbye")
        elif response == "create card":
            card_type = input("what kind of card? debit or students?:")
            name = input("your name?")
            lastname = input("lastname?")
            privat_number = int(input("your privat number?"))
            mob_number = int(input("your mobile number?"))
            print("your card will be ready soon.")
        elif response == "take loan":
            loan = float(input("how much?"))
            bank_money = bank_money - loan 
    elif Client == "create card":
        card_type = input("what kind of card? debit or students?:")
        name = input("your name?")
        lastname = input("lastname?")
        privat_number = int(input("your privat number?"))
        mob_number = int(input("your mobile number?"))
        print("your card will be ready soon.")
        
        response = input("would ypu add somethings?:")
        
        if response == "no":
            print("okay goodbye")
        elif response == "take loan":
            loan = float(input("how much?"))
            bank_money = bank_money - loan 


    elif Client == "take loan":
        loan = float(input("how much?"))
        bank_money = bank_money - loan 

        response = input("would ypu add somethings?:")

        if response == "no":
            print("okay goodbye")
        elif response == "create card":
            card_type = input("what kind of card? debit or students?:")
            name = input("your name?")
            lastname = input("lastname?")
            privat_number = int(input("your privat number?"))
            mob_number = int(input("your mobile number?"))
            print("your card will be ready soon.")
        elif response == "withdrow money":
            money_1 = float(input("How much?: "))
            bank_money = bank_money - money_1
