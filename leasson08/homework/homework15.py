#დაწერე პროგრამა, რომელიც ამოწმებს, არის თუ არა რიცხვი ერთდროულად 50-ზე ნაკლები და 10-ის ჯერადი:

number = int(input("შეიტანეთ რიცხვი: "))

if number < 50 and number % 10 == 0:
    print("რიცხვი არის 50-ზე ნაკლები და 10-ის ჯერადი.")
else:
    print("რიცხვი არ არის 50-ზე ნაკლები ან არ არის 10-ის ჯერადი.")