#მომხმარებლის შემოტანილი რიცხვი შეამოწმე, არის თუ არა 20-ის ჯერადი და დადებითი:

number = int(input("შეიტანეთ რიცხვი: "))

if number > 0 and number % 20 == 0:
    print("რიცხვი არის 20-ის ჯერადი და დადებითი.")
else:
    print("რიცხვი არ არის 20-ის ჯერადი ან არ არის დადებითი.")