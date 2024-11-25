#გააკეთეთ სია სადაც იქნება 10 ინტეჯერი , ინტეჯერები რომელიბ იქნება 10 ზე ნაკლები append ის დახმარებით შეიყვანეთ ახალ ცხრილში 

original_list = [4, 15, 8, 23, 2, 9, 11, 6, 18, 3]


new_list = []


for num in original_list:
    if num < 10:
        new_list.append(num)


print("ორიგინალური სია:", original_list)
print("ახალი სია (10-ზე ნაკლები):", new_list)
