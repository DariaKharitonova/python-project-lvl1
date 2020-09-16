import prompt


def welcome_user(gamer_name):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name?\n')
    print('Hello, %s!' % user_name)
    return user_name
