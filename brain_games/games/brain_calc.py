import random
import operator

operations = {'+': operator.add, '-': operator.sub, '*': operator.mul}

DESCRIPTION = 'What is the result of the expression?'
MAX_NUMBER = 10
MIN_NUMBER = 1


def get_question_and_answer():
    first_number = generate_number()
    second_number = generate_number()
    symbol, operation = generate_operation()
    task = f'{first_number} {symbol} {second_number}'
    answer = str(operation(first_number, second_number))
    return task, answer


def generate_operation():
    symbol, operation = random.choice(list(operations.items()))
    return symbol, operation


def generate_number():
    return random.randint(MIN_NUMBER, MAX_NUMBER)
