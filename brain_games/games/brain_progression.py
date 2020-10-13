import random

DESCRIPTION = 'What number is missing in the progression?'
PROGRESSION_LENGHT = 10
MAX_NUMBER = 100
MIN_NUMBER = 1
MIN_PROGRESSION_STEP = 1
MAX_PROGRESSION_STEP = 10


def create_progression(first_number, max_number, step):
    return range(first_number, max_number, step)


def get_question_and_answer():
    first_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    step = random.randint(MIN_PROGRESSION_STEP, MAX_PROGRESSION_STEP)
    max_number = first_number + (PROGRESSION_LENGHT * step)
    progression = create_progression(first_number, max_number, step)
    hidden_element_index = random.randint(0, len(progression) - 1)
    hidden_element = progression[hidden_element_index]
    result_progression = ' '.join([
        '..' if index == hidden_element_index else str(item)
        for index, item in enumerate(progression)
    ])
    question = result_progression
    return question, str(hidden_element)
