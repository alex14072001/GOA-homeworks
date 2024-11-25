#შექმენით სია რომელშიც იქნება სახელები შემდეგ კი შექმენით პროგრამა რომელიც ამოშლის ყველა სახელს რომელიც "t" ასოზე იწყება და ჩაამატებს ახალ სიაში

names = ["Tina", "Aleko", "Teona", "Bero", "Tinatin", "Luna", "Tina", "Nika"]


new_list = [name for name in names if not name.lower().startswith("t")]


print("ახალი სია (სახელები, რომლებსაც არ აქვთ 't' დასაწყისში):", new_list)
