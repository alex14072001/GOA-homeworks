import random

# პირველი სია: 10 რენდომი რიცხვი
first_list = [random.randint(1, 100) for _ in range(10)]

# მეორე სია: მხოლოდ ლუწი რიცხვები
even_list = [num for num in first_list if num % 2 == 0]

# შედეგი
print("პირველი სია:", first_list)
print("მეორე სია (ლუწი რიცხვები):", even_list)
