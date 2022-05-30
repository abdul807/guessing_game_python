import random
from game_data import data
from art import logo,vs
import os,sys


clear = lambda : os.system('cls')




score=0
is_game = True
def check_guess(guess,a_followers,b_followers):
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'


    # if a_followers > b_followers :
    #     if guess == 'a':
    #         return 'You won'
    #     else:
    #         return 'You lost'
    # elif b_followers > a_followers:
    #     if guess == 'b':
    #         return 'You Won'
    #     else:
    #         return 'You lost'

            # OR

    # if a_followers > b_followers and guess == 'a':
    #     return 'You won'
    # elif a_followers < b_followers and guess == 'a':
    #     return 'You lost'
    # elif b_followers > a_followers and guess == 'b':
    #     return 'You won'
    # elif b_followers < a_followers and guess == 'b':
    #     return 'You lost'




def formatted_data(account):
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']

    return f'{account["name"]},a {account["description"]} from {account["country"]}'

print(logo)


account_b = random.choice(data)

while is_game:
    account_a= account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f'Compare A :{formatted_data(account_a)}')
    print(vs)
    print(f'Against B :{formatted_data(account_b)}')

    # print(account_a['follower_count'])
    # print(account_b['follower_count'])


    guess = input('Who has more followers? Type "A" or "B" :').lower()

    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']



    is_correct = check_guess(guess,a_follower_count,b_follower_count)
    clear()
    print(logo)

    if is_correct:
        score += 1 #score declared on line 8
        print(f'You won, your score is {score}')
    else:
        
        is_game = False
        print(f'You losst, your score is {score}')

# print(check_guess(guess,a_follower_count,b_follower_count))
