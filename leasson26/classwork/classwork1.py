# შექმენით ერთი სია რომელშიც შეიტანთ სახელებს შემდეგ შექმენით მეორე სია რომელშიც იქნება ისევ სხვადასხვა სახელები გააერთიანეთ ეს ორი სია ჩაამატეთ 5 ინდექსზე ახალი სახელი დაითვალეთ გაერთიანებული სიის სიგრძე და დაითვალეთ თქვენი სახელი რამდენჯერ გვხვდება ამ სიაში, ასევე დაბეჭდეთ რომელ ინდექსზე დგას თქვენი სახელი


list1 = ["თეო", "გიორგი", "ნიკა", "თაკო", "ელენე"]
list2 = ["ანა", "დათო", "ლუკა", "მარი", "ლევანი"]


combined_list = list1 + list2
combined_list.insert(5, "შოთა")


list_length = len(combined_list)
name_count = combined_list.count("თეო")
name_indices = [index for index, name in enumerate(combined_list) if name == "თეო"]


print(combined_list)
print(list_length)
print( name_count, )
print( name_indices)
