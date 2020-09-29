from random import randint
from brain_games.general_functions import question_prefix

RULES = 'Answer "yes" if number even otherwise answer "no".'


def generate_number():
    return randint(1, 100)


def is_even(number):  # test of even
    if number % 2 != 0:
        return False
    return True


def generate_question():
    number = generate_number()
    question = f'{question_prefix()}{number}'
    correct_answer = 'yes' if is_even(number) else 'no'
    return question, correct_answer
