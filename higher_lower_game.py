from art import logo, vs
from gam_data import data
import os
import random


clear = lambda: os.system('cls') #clearing console

#display art

score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    print(logo)
    #generate a random account from game data

    #making accoun_b new account_a
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    #formating account data
        
    def format_data(account):
        """Takes the data and returns the printable format"""
        account_name = account["name"]
        account_description = account["description"]
        account_country = account["country"]

        return f"{account_name}, a {account_description} from {account_country}"

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    def check_answer(guess, a_followers, b_followers):
        """Use if statement to check if user is correct"""
        # if a_followers > b_followers:
        #     if guess == "a":
        #         return True
        #     else:
        #         return False
            
        # if a_followers < b_followers:
        #     if guess == "b":
        #         return True
        #     else:
        #         return False

        if a_followers > b_followers:
            return guess == "a" #it will return True if guess is "a" and False if "b"
        else:
            return guess == "b" #it will return True if guess is "b" and False if "a"



    #ask user for quess

    guess = input("Who has more followers? A or B: ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    clear()

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, You're wrong! Final score is {score}")
        game_should_continue = False
    