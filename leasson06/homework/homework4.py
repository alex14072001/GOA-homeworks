#შემოიტანე 2 input, შეამოწმე, არის თუ არა ორი რიცხვის ჯამი 100-ზე მეტი:

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 + num2 > 100:
    print("The sum of the numbers is greater than 100.")
else:
    print("The sum of the numbers is less than or equal to 100.")