from random import randint
import prompt

ROUNDS = 3


def get_user_name():
    return prompt.string('May I have your name? ')


def welcome_user():
    user_name = get_user_name()
    greeting = f'Hello, {user_name}!'
    print(greeting)
    return user_name


def generate_number():
    return randint(1, 100)


def answer_check(user_answer, correct_answer):  # checking user's answers
    if user_answer == correct_answer:
        message = 'Correct!'
        return True, message
    message = "'{wrong}' is wrong answer ;(. Correct answer was '{correct}'."
    return False, message.format(wrong=user_answer, correct=correct_answer)


def start_game(game):  # run game
    if not game:
        return
    print('Welcome to the Brain Games!')
    print(game.RULES)
    print()
    user_name = welcome_user()
    print()
    game_process(user_name, game.generate_question)


def get_user_answer():
    return prompt.string('Your answer: ')


def game_process(user_name, play):
    correct_answers = 0
    while correct_answers < ROUNDS:
        question, correct_answer = play()
        print(question)
        res, msg = answer_check(get_user_answer(), correct_answer)
        print(msg)
        if not res:
            print(f"Let's try again, {user_name}!")
            return
        correct_answers += 1
    print(f'Congratulations, {user_name}!')
