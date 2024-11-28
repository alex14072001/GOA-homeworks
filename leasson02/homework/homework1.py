# ოთხი ცვლადის შექმნა განსხვავებული რიცხვებით
a = 3
b = 4
c = 5
d = 6

# ცვლადების სია
numbers = [a, b, c, d]

# ყველა შესაძლო წყვილზე მოქმედებების შესრულება
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        x = numbers[i]
        y = numbers[j]
        
        # მოქმედებების ბეჭდვა
        print(f"{x} + {y} = {x + y}")  # მიმატება
        print(f"{x} - {y} = {x - y}")  # გამოკლება
        print(f"{y} - {x} = {y - x}")  # საპირისპირო მიმართულებით გამოკლება
        print(f"{x} * {y} = {x * y}")  # გამრავლება
        if y != 0:  # გაყოფა (თუ გამყოფი ნულია,)
            print(f"{x} / {y} = {x / y:.2f}")  # x / y
        if x != 0:  
            print(f"{y} / {x} = {y / x:.2f}")  # y / x