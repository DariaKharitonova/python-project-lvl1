from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'
MAX_NUMBER = 50
MIN_NUMBER = 1


def generate_number():
    return randint(MIN_NUMBER, MAX_NUMBER)


def get_question_and_answer():
    first_number = generate_number()
    second_number = generate_number()
    question = f'{first_number} {second_number}'
    answer = gcd(first_number, second_number)
    return question, str(answer)


def gcd(first_number, second_number):
    """Euclidean algorithm https://en.wikipedia.org/wiki/Euclidean_algorithm"""
    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number %= second_number
        else:
            second_number %= first_number
    return first_number + second_number
