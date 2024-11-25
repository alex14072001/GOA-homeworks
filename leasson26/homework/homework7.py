import random

# პირველი სია: 10 რენდომი რიცხვი
random_list = [random.randint(1, 100) for _ in range(10)]

# ამოშლილია ყველა ლუწი რიცხვი
random_list = [num for num in random_list if num % 2 != 0]

# შედეგი
print("რენდომი რიცხვები (ლუწი რიცხვების გარეშე):", random_list)
