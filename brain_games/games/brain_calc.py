import random
import operator

operations = {'+': operator.add, '-': operator.sub, '*': operator.mul}

DESCRIPTION = 'What is the result of the expression?'
MAX_NUMBER = 10
MIN_NUMBER = 1


def generate_number():
    return random.randint(MIN_NUMBER, MAX_NUMBER)


def generate_operation():
    operation_symbol = random.choice(list(operations.items()))
    return operation_symbol[0], operation_symbol[1]


def get_correct_answer(first_number, operation_symbol, second_number):
    return str(operation_symbol(first_number, second_number))


def get_question_and_answer():
    first_number = generate_number()
    second_number = generate_number()
    symbol, operation = generate_operation()
    task = f'{first_number} {symbol} {second_number}'
    answer = get_correct_answer(first_number, operation, second_number)
    return task, answer
