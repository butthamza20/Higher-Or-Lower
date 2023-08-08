import random
from replit import clear
from game_data import data
from game_art import logo, vs


def random_person(data_list):
    person = random.choice(data_list)
    return person


def format_data(account):
    """Format the account data into a printable format."""
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(choice, account_a, account_b):
    """Takes the user's guess and checks to see if they got it right."""
    followers_A = account_a['follower_count']
    followers_B = account_b['follower_count']
    if followers_A > followers_B:
        return choice == 'a'
    else:
        return choice == 'b'


print(logo)
score = 0
game_should_continue = True
account_B = random_person(data)
while game_should_continue:
    account_A = account_B
    account_B = random_person(data)
    while account_A == account_B:
        account_B = random_person(data)

    print(f"Compare A: {format_data(account_A)}")
    print(vs)
    print(f"Compare B: {format_data(account_B)}")

    guess = input("Who has more followers? A or B: ").lower()
    is_correct = check_answer(guess, account_A, account_B)

    print(clear())

    if is_correct:
        score += 1
        print(f"Your are right! Current score = {score}.")
    else:
        print(f"You are wrong! Final Score = {score}")
        game_should_continue = False

