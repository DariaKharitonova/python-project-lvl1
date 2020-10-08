from random import randint

DESCRIPTION = 'What number is missing in the progression?'
PROGRESSION_LENGHT = 10
MAX_NUMBER = 100
MIN_NUMBER = 1
MIN_PROGRESSION_STEP = 1
MAX_PROGRESSION_STEP = 10


def create_progression():
    first_number = randint(MIN_NUMBER, MAX_NUMBER)
    step = randint(MAX_PROGRESSION_STEP, MAX_PROGRESSION_STEP)
    max_number = first_number + (PROGRESSION_LENGHT * step)
    return range(first_number, max_number, step)


def get_question_answer():
    progression = create_progression()
    hidden_element_index = randint(0, len(progression) - 1)
    hidden_element = progression[hidden_element_index]
    result_progression = ' '.join([
        '..' if num == hidden_element else str(num) for num in progression
    ])
    question = f'{result_progression}'
    return question, str(hidden_element)
