import random

point_user=0
point_computer=0

while True:

    user_input=input("Enter your choice [rock,paper,scissors]: ")
    possible_choices=['rock','paper','scissors']
    computer_choices=random.choice(possible_choices)

    print(f'You choose {user_input},computer choose {computer_choices}')

    if user_input==computer_choices:
        print(f"The game ended in a draw both players selected the same option {user_input}")
    elif user_input=='rock':
        if computer_choices=='scissors':
            print(f"The user wins because {user_input} breaks scissors.")
            point_user +=1
        else:
            print(f"The computer wins because {computer_choices} covers the rock.")
            point_computer +=1
    elif user_input=='scissors':
        if computer_choices=='rock':
            print(f"The computer wins {computer_choices} breaks scissors.")
            point_computer +=1
        else:
            print(f"The user wins {user_input} cut the paper")
            point_user +=1
    elif user_input=='paper':
        if computer_choices=='rock':
            print(f"User wins {user_input} covers rock")
            point_user +=1
        else:
            print(f"Computer wins {computer_choices} cut the Paper")
            point_computer +=1

    playagain=input('Do you want to play again? (y/n): ')
    if playagain !='y':
        break
print(f'User points are: {point_user}, computer: {point_computer}')
print("Game Over!")
