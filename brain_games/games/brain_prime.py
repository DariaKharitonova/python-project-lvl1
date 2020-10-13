import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MAX_NUMBER = 100
MIN_NUMBER = 1


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


def get_question_and_answer():
    number = generate_number()
    question = str(number)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return question, correct_answer


def generate_number():
    return random.randint(MIN_NUMBER, MAX_NUMBER)
