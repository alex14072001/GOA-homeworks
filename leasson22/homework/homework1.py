#შექმინთ 2 სია  , პირველი სია ინქება ცარიელი  ხოლო მეროე სია ინქება სახელებით სავსე მინიმუმ 5 , თქვენი დავალებაა ამ სიიდან  ჩაამოტომ მეორე სიაში სახელელბი რომელიც  4 სიმბოლოზე ნაკლებია

list_one = []


list_two = ["Anna", "John", "Kate", "Leo", "Mike", "Sam", "Max"]


list_one = [name for name in list_two if len(name) < 4]


print("პირველი სია:", list_one)
print("მეორე სია:", list_two)
