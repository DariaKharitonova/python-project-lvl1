import random
import prompt

ROUNDS = 3


def welcome_user():  # ask user's name and greet him or her
    user_name = prompt.string('May I have your name?\n')
    print('Hello, %s!' % user_name)
    return user_name


def generate_number():
    return randint(1, 999)


def answer_check(user_answer, correct_answer):  # checking user's answers
    if user_answer == correct_answer:
        message = 'Correct!'
        return message
    message = "'{wrong}' is wrong answer ;(. Correct answer was '{correct}'."
    return message.format(wrong=user_answer, correct=correct_answer)


def start_game(game=None):  # run game
    print('Welcome to the Brain games!')
    if game:
        print(game.RULES)
    print()
    user_name = welcome_user()
    if game:
        print()
        game_process(user_name, game.ask_question)


def game_process(user_name, play):
    correct_answers = 0
    while correct_answers < ROUNDS:
        question, correct_answer = play()
        print(question)
        res, msg = check_answer(get_user_answer(), correct_answer)
        print(msg)
        if not res:
            print(f"Let's try again, {user_name}!")
            return
        correct_answers += 1
    print(f'Congratulations, {user_name}!')