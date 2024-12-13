#შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა რიცხვი შემდეგ კი მან უნდა დაგვიბრუნოს ეს რიცხვი დადებითია თუ უარყოფითი

def positive_or_negative(number):
    if number > 0:
        return "დადებითი"
    elif number < 0:
        return "უარყოფითი"
    else:
        return "ნული"


number = float(input("შეიყვანეთ რიცხვი: "))
print(f"რიცხვი არის: {positive_or_negative(number)}")
