from game_data import data
from art import logo, vs
import random


is_game_finished = True
score = 0


def acc_details(acc):
    name = acc['name']
    job = acc['description']
    country = acc['country']
    return f"{name}, a {job}, from {country}"


def check_answer(guess, a_account, b_account):
    if guess == 'a' and a_account > b_account:
        return True
    elif guess == 'a' and a_account < b_account:
        return False
    elif guess == 'b' and b_account > a_account:
        return True
    elif guess == 'b' and b_account < a_account:
        return False


account_b = random.choice(data)
print("WELCOME TO HIGHER LOWER GAME!!")

# To randomly choose datas and print it
while is_game_finished:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)
    print(logo)
    print(f"Compare A: {acc_details(account_a)}")
    print(vs)
    print(f"Against B: {acc_details(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_acc_follower = account_a['follower_count']
    b_acc_follower = account_b['follower_count']

    if check_answer(guess, a_acc_follower, b_acc_follower):

        score += 1
        print(f"Your Right! Your Score: {score} ")
    else:
        is_game_finished = False
        print(f"Sorry your wrong, Final score: {score}")
