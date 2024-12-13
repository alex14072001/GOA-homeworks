#შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა რიცხვი შემდეგ კი ფუნქციამ უნდა დაგვიბრუნოს მისი საპირისპირო რიცხვი
 
 
def opposite_number(number):
    return -number


number = float(input("შეიყვანეთ რიცხვი: "))
print(f"რიცხვი {number} არის მისი საპირისპირო: {opposite_number(number)}")
