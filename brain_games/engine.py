import prompt

NUMBER_OF_ROUNDS = 3
TASK_PREFIX = 'Question:'


def run_game(game):
    print('Welcome to the Brain Games!')
    print(game.DESCRIPTION)
    print()
    user_name = prompt.string('May I have your name? ')
    print()
    print(f'Hello, {user_name}!')
    run_game_loop(user_name, game.get_question_and_answer)


def run_game_loop(user_name, get_question_and_answer):
    for _ in range(NUMBER_OF_ROUNDS):
        question, correct_answer = get_question_and_answer()
        print(f'{TASK_PREFIX} {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. \'"
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return
        print('Correct!')
    print(f'Congratulations, {user_name}!')
