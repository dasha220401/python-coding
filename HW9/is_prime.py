from cmath import sqrt


def is_prime(number):
    if number % 2 == 0 and number !=2:
        return False
    if number == 0 or number == 1:
        return False
    for i in range(3, int(sqrt(number).real) + 1, 2):
        if number % i == 0:
            return False
    return True
