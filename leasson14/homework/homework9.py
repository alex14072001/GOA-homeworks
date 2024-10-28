# შემოატანინეთ მომხმარებელს მისი ასაკი თუ მისი ასაკი 18 წელზე მეტია დაუპრინტეთ “you are adult” თუ 18 წელზე ნაკლები “you are virgin”
age = int(input("შეიყვანეთ თქვენი ასაკი: "))  
if age > 18:
    print("You are an adult.")
elif age < 18:
    print("You are a virgin.")
else:
    print("You are 18 years old.")
