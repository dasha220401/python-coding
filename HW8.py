#task1
with open ("111.txt") as file_handler:
    for line in file_handler:
        print(line)



#task 2
import json

with open('questions.json', 'r') as file:
    data = json.load(file)

    for q in data['questions']:
        q['answer'] = input(q['q'])

with open('questions.json', 'w') as file:
    json.dump(data, file, indent=4)

#task 3
import random
the_number = random.randint(1, 50)
vib = int(input("Предполагаемое вами число: "))
tries = 10
while vib != the_number:
    if vib > the_number:
        print("Попробуйте меньше ")
    else:
        print("Попробуйте больше ")
    if tries == 0:
        break
    vib = int(input("Предполагаемое вами число: "))
    tries -= 1
if vib != the_number:
     print("Попыток больше нет!")
else:
     print("Угадали!")












