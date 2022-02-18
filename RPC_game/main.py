import random
import time

while True:

    choices = ['Rock', 'Paper', 'Scissors']

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input('Rock, paper or scissors? ').capitalize()

    if player == computer:
        print('Player: ' + player)
        print('Computer: ' + computer)
        print('Tie!')
    elif player == 'Rock':
        if computer == 'Paper':
            print('Player: ' + player)
            print('Computer: ' + computer)
            print('You lose!')
        elif computer == 'Scissors':
            print('Player: ' + player)
            print('Computer: ' + computer)
            print('You win!')
    elif player == 'Paper':
        if computer == 'Scissors':
            print('Player: ' + player)
            print('Computer: ' + computer)
            print('You lose!')
        elif computer == 'Rock':
            print('Player: ' + player)
            print('Computer: ' + computer)
            print('You win!')
    elif player == 'Scissors':
        if computer == 'Rock':
            print('Player: ' + player)
            print('Computer: ' + computer)
            print('You lose!')
        elif computer == 'Paper':
            print('Player: ' + player)
            print('Computer: ' + computer)
            print('You win!')

    time.sleep(1)
    play_again = None

    while play_again != 'Yes' and play_again != 'No':
        play_again = input('Play again? (yes/no) ').capitalize()
    if play_again == 'No':
        break

print('Thanks for playing, have a nice day!')