from random import randint
from brain_games.general_functions import question_prefix

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_number():
    return randint(1, 100)


def is_prime(number):
    if number < 2:
        return False
    return all(number % i for i in range(2, number))


def generate_question():
    number = generate_number()
    question = f'{question_prefix()} {number}'
    correct_answer = 'yes' if is_prime(number) else 'no'
    return question, correct_answer
