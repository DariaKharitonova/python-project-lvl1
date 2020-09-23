from brain_games.general_functions import generate_number

RULES = 'Find the greatest common divisor of given numbers.'


def ask_question():
    first_number = generate_number()
    second_number = generate_number()
    question = f'Question: {first_number} {second_number}'
    answer = gcd(first_number, second_number)
    return question, str(answer)


def gcd(first_number, second_number):  # Euclidean algorithm
    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number %= second_number
        else:
            second_number %= first_number
    return first_number + second_number
