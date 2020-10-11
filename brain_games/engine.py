import prompt

NUMBER_OF_ROUNDS = 3
PREFIX = 'Question:'


def get_user_name():
    return prompt.string('May I have your name? ')


def welcome_user():
    user_name = get_user_name()
    greeting = f'Hello, {user_name}!'
    print(greeting)
    return user_name


def run_game(game):
    print('Welcome to the Brain Games!')
    print(game.DESCRIPTION)
    print()
    user_name = welcome_user()
    print()
    run_game_loop(user_name, game.get_question_and_answer)


def get_user_answer():
    return prompt.string('Your answer: ')


def run_game_loop(user_name, get_qa):
    for _ in range(NUMBER_OF_ROUNDS):
        question, correct_answer = get_qa()
        print(f'{PREFIX} {question}')
        user_answer = get_user_answer()
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. \'"
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return
        print('Correct!')
    print(f'Congratulations, {user_name}!')
