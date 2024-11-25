#კომენტარებით ახსენით რას შვება pop append

my_list = []

# append: ამატებს ელემენტს სიაში ბოლოში
my_list.append(5)  # სიაში დაემატა 5
my_list.append(10)  # სიაში დაემატა 10
print("სიაში დამატების შემდეგ:", my_list)

# pop: შლის ბოლო ელემენტს სიიდან და აბრუნებს მას
last_item = my_list.pop()  # შლის 10-ს
print("სიიდან ამოღების შემდეგ:", my_list)
print("ამოღებული ელემენტი:", last_item)
