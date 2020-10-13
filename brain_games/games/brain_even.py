import random

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'
MAX_NUMBER = 100
MIN_NUMBER = 1


def get_question_and_answer():
    number = generate_number()
    question = str(number)
    correct_answer = 'yes' if is_even(number) else 'no'
    return question, correct_answer


def is_even(number):
    return number % 2 == 0


def generate_number():
    return random.randint(MIN_NUMBER, MAX_NUMBER)
