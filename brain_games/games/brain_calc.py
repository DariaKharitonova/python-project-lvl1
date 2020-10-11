import random
import operator

operations = {'+': operator.add, '-': operator.sub, '*': operator.mul}

DESCRIPTION = 'What is the result of the expression?'
MAX_NUMBER = 10
MIN_NUMBER = 1


def generate_number():
    return random.randint(MIN_NUMBER, MAX_NUMBER)


def generate_operation():
    return random.choice(list(operations.items()))


def get_correct_answer(first_number, operation, second_number):
    return str(operation[1](first_number, second_number))


def get_question_and_answer():
    first_number = generate_number()
    second_number = generate_number()
    operation = generate_operation()
    task = f'{first_number} {operation[0]} {second_number}'
    answer = get_correct_answer(first_number, operation, second_number)
    return task, answer
