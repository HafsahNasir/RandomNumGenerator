from random import randint, random

play_again = True

def random_num_game ():
    generated_num = randint(1,10)
    user_num = input("Enter a number between 1 and 10: ")
    if int(user_num) == generated_num:
        print("good job! your guess was correct")
        return True
    else:
        print("your guess was incorrect. The number was", generated_num)
        return False

random_num_game()

while play_again == True:
    user_input = input("would you like to play again (y/n): ")
    if user_input == "y":
        play_again = True
        random_num_game()
    elif user_input == "n":
        play_again = False
        print("thank you for playing! <3")
        break
    else:
        print("incorrect input")
        user_input = input("would you like to play again (y/n): ")
        random_num_game()