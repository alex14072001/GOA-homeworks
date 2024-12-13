# შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა რიცხვებით სავსე სია ამ ფუნქციამ კი უნდა დააბრუნოს ამ სიის რიცხვების ჯამი

def sum_of_list(numbers):
    return sum(numbers)


numbers = [1, 2, 3, 4, 5]  
print(f"ჯამი: {sum_of_list(numbers)}")
