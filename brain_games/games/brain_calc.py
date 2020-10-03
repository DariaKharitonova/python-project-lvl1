from random import choice, randint
import operator
from brain_games.general_functions import question_prefix

operations = {'+': operator.add, '-': operator.sub, '*': operator.mul}

DESCRIPTION = 'What is the result of the expression?'
MAX_NUMBER = 100
MIN_NUMBER = 1


def generate_number():
    return randint(MIN_NUMBER, MAX_NUMBER)


def generate_operation():
    return choice(list(operations.keys()))


def correct_answer(first_number, operation, second_number):
    return str(operations[operation](first_number, second_number))


def generate_question():
    first_number = generate_number()
    second_number = generate_number()
    operation = generate_operation()
    task = f'{question_prefix()} {first_number} {operation} {second_number}'
    answer = correct_answer(first_number, operation, second_number)
    return task, answer
