from random import randint
from brain_games.general_functions import question_prefix

RULES = 'What number is missing in the progression?'
PROGRESSION_LENGHT = 10
MAX_NUMBER = 100
MIN_NUMBER = 1


def generate_number():
    return randint(MIN_NUMBER, MAX_NUMBER)


def create_progression():
    first_number = randint(1, 100)
    step = randint(1, 10)
    max_number = first_number + (PROGRESSION_LENGHT * step)
    return range(first_number, max_number, step)


def generate_question():
    progression = create_progression()
    hidden_element_index = randint(0, len(progression) - 1)
    hidden_element = progression[hidden_element_index]
    result_progression = ' '.join([
        '..' if num == hidden_element else str(num) for num in progression
    ])
    question = f'{question_prefix()} {result_progression}'
    return question, str(hidden_element)
