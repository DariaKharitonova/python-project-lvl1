import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MAX_NUMBER = 100
MIN_NUMBER = 1


def generate_number():
    return random.randint(MIN_NUMBER, MAX_NUMBER)


def is_prime(number):
    if number > 1:
        for i in range(2, number - 1):
            if (number % i) == 0:
                return False
    else:
        return False
    return True


def get_question_and_answer():
    number = generate_number()
    question = f'{number}'
    correct_answer = 'yes' if is_prime(number) else 'no'
    return question, correct_answer
