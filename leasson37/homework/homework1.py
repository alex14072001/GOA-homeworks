 #გააკეთეთ random student generator რომელსაც გადაეცემა ჯგუფის მოსწავლეებით სავსე სია და დაგვიბრუნებს რენდომულად განაწილებულ გუნდებს მზგავსად როგორც გავაკეთეთ წინა გაკვეთილზე

import random

def random_student_generator(students, team_size):
    random.shuffle(students)  
    teams = [students[i:i + team_size] for i in range(0, len(students), team_size)]
    return teams


students = ['sofia', 'nika', 'giorgi', 'ana', 'gabrieli', 'mariami']
team_size = 2
teams = random_student_generator(students, team_size)
print(teams)
