import prompt

NUMBER_OF_ROUNDS = 3
PREFIX_STRING = 'Question:'


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
    play_game(user_name, game.get_question_and_answer)


def get_user_answer():
    return prompt.string('Your answer: ')


def play_game(user_name, play):
    for _ in range(NUMBER_OF_ROUNDS):
        question, correct_answer = play()
        print(f'{PREFIX_STRING} {question}')
        user_answer = get_user_answer()
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. \'"
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return
        print('Correct!')
    print(f'Congratulations, {user_name}!')
