from random import choice
from brain_games.general_functions import generate_number
import operator

operations = {'+': operator.add, '-': operator.sub, '*': operator.mul}

RULES = 'What is the result of the expression?'


def generate_operation():
    return choice(list(operations.keys()))


def correct_answer(first_number, operation, second_number):
    return str(operations[operation](first_number, second_number))


def ask_question():
    first_number = generate_number()
    second_number = generate_number()
    operation = generate_operation()
    question = f'Question: {first_number} {operation} {second_number}'
    answer = correct_answer(first_number, operation, second_number)
    return question, answer
