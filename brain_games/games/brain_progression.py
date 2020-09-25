from random import randint

RULES = 'What number is missing in the progression?'
PROGRESSION_LENGHT = 10


def generate_number():
    return randint(1, 100)


def create_progression():
    first_number = randint(1, 100)
    step = randint(1, 10)
    max_number = first_number + (PROGRESSION_LENGHT * step)
    return range(first_number, max_number, step)


def ask_question():
    progression = create_progression()
    hidden_element_index = randint(0, PROGRESSION_LENGHT - 1)
    hidden_element = progression[hidden_element_index]
    result_progression = ' '.join([
        '..' if num == hidden_element else str(num) for num in progression
    ])
    question = f'Question: {result_progression}'
    return question, str(hidden_element)
