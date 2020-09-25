from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_number():
    return randint(1, 100)


def is_prime(number):
    counter = 3
    while counter <= number // 2:
        if not number % counter:
            return False
        counter += 1
    if number < 2:
        return False
    return True


def generate_question():
    number = generate_number()
    question = f'Question: {number}'
    correct_answer = 'yes' if is_prime(number) else 'no'
    return question, correct_answer
