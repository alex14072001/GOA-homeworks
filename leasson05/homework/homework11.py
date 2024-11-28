#მომხმარებელს შემოატანინეთ ორი რიცხვი, შემდეგ კი ამ ორი რიცხვისგან შეადგინეთ ოთხი მათემატიკური მოქმედება (დამატება, გამოკლება, გამრავლება, გაყოფა):

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "Undefined (cannot divide by zero)"

print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")