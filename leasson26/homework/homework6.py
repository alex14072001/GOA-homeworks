import random

# პირველი სია: რენდომი რიცხვები
first_list = [random.randint(1, 100) for _ in range(10)]

# მეორე სია: მხოლოდ ლუწი რიცხვები
even_list = [num for num in first_list if num % 2 == 0]

print("პირველი სია:", first_list)
print("მეორე სია (ლუწი რიცხვები):", even_list)
