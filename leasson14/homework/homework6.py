# დაბეჭდეთ რიცხვები, რომლებიც იყოფა 3-ზე და 5-ზე 1-დან 100-მდე
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:  # გამოტოვება, თუ რიცხვი 3-ზე და 5-ზე იყოფა
        print(i)
