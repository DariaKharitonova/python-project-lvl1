from random import randint
from brain_games.general_functions import question_prefix

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MAX_NUMBER = 100
MIN_NUMBER = 1


def generate_number():
    return randint(MIN_NUMBER, MAX_NUMBER)


def is_prime(number):
    return all(number % i for i in range(2, number))


def generate_question():
    number = generate_number()
    question = f'{question_prefix()} {number}'
    correct_answer = 'yes' if is_prime(number) else 'no'
    return question, correct_answer
