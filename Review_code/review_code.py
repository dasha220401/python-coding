import random
from array import array


# ф-ция возвращает True если выиграли, False- если нет
def game_loop(dices_sum):
    for i in range(10):
        input_str = input("Guess the number: ")
        if input_str == "":
            return False

        try:
            guess_number = int(input_str)
        except ValueError:
            print("Not a number! Try again.")
            continue

        if guess_number == dices_sum:
            print("You won")
            return True
        elif guess_number > dices_sum:
            print("Try less!")
        elif guess_number < dices_sum:
            print("Try greater!")

    return False


def get_continue_condition(res1, res2):
    return 'yes' if res1 == res2 else input("Would you like to continue? (yes/no) ")


res1 = 0
res2 = 0
guessed_numbers = array('i')
continue_condition = 'yes'
while continue_condition == 'yes':
    dices_sum = random.randint(10, 60)
    guessed_numbers.append(dices_sum)

    if game_loop(dices_sum):
        res1 += dices_sum
    else:
        res2 += dices_sum

    print("scores of player 1 = " + str(res1))
    print("scores of player 2 = " + str(res2))
    continue_condition = get_continue_condition(res1, res2)


