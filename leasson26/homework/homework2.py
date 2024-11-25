# სახელები
names = ["Aleko", "Tinatin", "Bero", "Aleko", "Nika", "Aleko", "Teona"]

# სახელი, რომლის გამეორებასაც ვთვლით
name_to_count = "Aleko"

# ინიცირება count-ის ცვლადი 0-ით
count = 0


for name in names:
    if name == name_to_count:  # თუ სახელი ემთხვევა ჩვენს მითითებულ სახელს
        count += 1  # დავამატოთ 1

# შედეგის გამოტანა
print("სახელი '{}' მეორდება {}-ჯერ.".format(name_to_count, count))
