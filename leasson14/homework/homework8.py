# შემოატანინეთ მომხმარებელს რიცხვი და დაადგინეთ არის თუ არა დადებითი უარყოფითი ან ნულის ტოლი 
number = float(input("შეიყვანეთ რიცხვი: ")) 

# პირობის შემოწმება
if number > 0:
    print("ეს რიცხვი არის დადებითი.")
elif number < 0:
    print("ეს რიცხვი არის უარყოფითი.")
else:
    print("ეს რიცხვი არის ნულის ტოლი.")