#შეამოწმე, არის თუ არა ციფრი მთელი რიცხვი:

number = input("შეიტანეთ რიცხვი: ")
try:
    int_number = int(number)
    print("ციფრი არის მთელი რიცხვი.")
except ValueError:
    print("ციფრი არ არის მთელი რიცხვი.")