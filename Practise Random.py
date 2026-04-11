# Create a project using random module that generates strong password. 
# The password should be 8 characters long with 3 digits, 3 letters and 2 special characters.

import random

# letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "V", "w", "x", "y", "z"]
# digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
# special_char = ["!", "(", ")", "[", "]", "{", "}", "£", ":", "@"]

# rand_digits_1 = random.choice(digits)
# rand_digits_2 = random.choice(digits)
# rand_digits_3 = random.choice(digits)

# rand_letters_1 = random.choice(letters)
# rand_letters_2 = random.choice(letters)
# rand_letters_3 = random.choice(letters)

# rand_special_1 = random.choice(special_char)
# rand_special_2 = random.choice(special_char)

# password = rand_digits_1 + rand_digits_2 + rand_digits_3 + rand_letters_1 + rand_letters_2 + rand_letters_3 + rand_special_1 + rand_special_2#
# print(password)



# -------------


# Create a rock, paper, scissors game. The player picks one of the three objects and the computer randomly picks one of the three objects. Then these rules are applied to see who has won that round:
# Paper wraps (beats) Rock
# Scissors cut (beat) Paper
# Rock blunts (beats) Scissors
# Repeat it to have 3 rounds.
# Add score to the game.
# Declare the final winner.

rounds = 0
items = ["rock", "paper", "scissors"]



user_points = 0
computer_points = 0

while rounds <3:

    user_choice = input("Choose between Rock, Paper and Scissors")
    user_choice = user_choice.lower()
    computer_choice = random.choice(items)

    if user_choice == "paper" and computer_choice == "rock":
        print("The computer has played {} and you won that round because paper wraps the rock.".format(computer_choice))
        user_points = user_points + 1
        rounds = rounds + 1
    elif user_choice == "rock" and computer_choice == "paper":
        print("The computer has played {} and they won that round because paper wraps the rock.".format(computer_choice))
        computer_points = computer_points + 1
        rounds = rounds + 1

    elif user_choice == "scissors" and computer_choice == "paper":
        print("The computer has played {} and you won that round because scisscors cuts the paper.".format(computer_choice))
        user_points = user_points + 1
        rounds = rounds + 1    
    elif user_choice == "paper" and computer_choice == "scissors":
        print("The computer has played {} and they won that round because scisscors cuts the paper.".format(computer_choice))
        computer_points = computer_points + 1
        rounds = rounds + 1

    elif user_choice == "rock" and computer_choice == "scissors":
        print("The computer has played {} and you won that round because rock blunts the scissors.".format(computer_choice))
        user_points = user_points + 1
        rounds = rounds + 1    
    elif user_choice == "scissors" and computer_choice == "rock":
        print("The computer has played {} and they won that round because rock blunts the scissors.".format(computer_choice))
        computer_points = computer_points + 1
        rounds = rounds + 1
    else:
        print("It is a draw")
        rounds = rounds + 1
if computer_points > user_points:
    print("The computer won the game.")
    print("The computer scored {} and you scored {}".format(computer_points, user_points))
elif user_points > computer_points:
    print("You won the game!")
    print("The computer scored {} and you scored {}".format(computer_points, user_points))
else:
    print("The game was a draw.")