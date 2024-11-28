#მომხმარებელს შემოატანინეთ პაროლი, შემდეგ კითხეთ ხელახლა, რომ გაიმეოროს პაროლი და შეამოწმეთ უდრის თუ არა ისინი ერთმანეთს:

password = input("Enter your password: ")
confirm_password = input("Confirm your password: ")

if password == confirm_password:
    print("The passwords match.")
else:
    print("The passwords do not match.")