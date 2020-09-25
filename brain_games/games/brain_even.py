from random import randint

RULES = 'Answer "yes" if number even otherwise answer "no".'


def generate_number():
    return randint(1, 100)


def generate_question():
    number = generate_number()
    question = f'Question: {number}'
    answer = correct_answer(number)
    return question, answer


def correct_answer(number):  # rules of even
    if number % 2 == 0:
        return 'yes'
    return 'no'
