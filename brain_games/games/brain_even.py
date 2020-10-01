from random import randint
from brain_games.general_functions import question_prefix

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'
LAST_NUMBER = 100  # maximum random number


def generate_number():
    return randint(1, LAST_NUMBER)


def is_even(number):  # test of even
    return number % 2 == 0 and True or False


def generate_question():
    number = generate_number()
    question = f'{question_prefix()}{number}'
    correct_answer = 'yes' if is_even(number) else 'no'
    return question, correct_answer
