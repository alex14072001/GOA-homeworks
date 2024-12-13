
# მომხმარებელს შეეკითხეთ ორი რიცხვი შემდეგ კი შექმენით ფუნქცია რომელსაც არგუმენტად გადასცემთ ამ ორ რიცხვს ხოლო ფუნქცია დააბრუნებს ამ ორი რიცხვის ჯამს, ასევე გააკეთე ასეთი 4 ფუნქცია სხვადასხვა მათემატიკური მოქმედებებისთვის, გამოიყენეთ პარამეტრები და არგუმენტად გადაეცით მომხარებლის შემოტანილი რიცხვები

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b if b != 0 else "არ შეიძლება ნულით გაყოფა"

a = float(input("შეიყვანეთ პირველი რიცხვი: "))
b = float(input("შეიყვანეთ მეორე რიცხვი: "))

print(f"ჯამი: {addition(a, b)}")
print(f"სხვაობა: {subtraction(a, b)}")
print(f"ნამრავლი: {multiplication(a, b)}")
print(f"ნაწილობა: {division(a, b)}")
