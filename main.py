'''
# RULE
# Rocks crushes scissors, scissors cuts paper and paper wins rock

'''

# player input
from random import randint

player_win_count = 0
cpu_win_count = 0

while True:
    player_choice = input("rock... paper... scissors?")
    possible_choices = ('rock', 'paper', 'scissors')

    if player_choice not in possible_choices:
        print('Invalid choice!, enter rock, paper or scissors')
        print(" ")
    elif player_choice == 'quit':
        break
    else:
        cpu_choice = possible_choices[randint(0, 2)]

        def score_board(player_score, cpu_score):
            '''
              prints game score and starts new round
            '''
            print(f'Score: You ({player_score}) : ({cpu_score}) CPU')
            print("Enter quit to stop the game. STARTING ANOTHER ROUND...")
            print("_________________________________________________")
            print(" ")

        if (player_choice == 'rock' and cpu_choice == 'scissors') or (player_choice == 'scissors' and cpu_choice == 'paper') or (player_choice == 'paper' and cpu_choice == 'rock'):
            player_win_count += 1
            print(
                f'You won!. Your choice: {player_choice}, CPU choice: {cpu_choice}')
            score_board(player_win_count, cpu_win_count)

        elif (cpu_choice == 'rock' and player_choice == 'scissors') or (cpu_choice == 'scissors' and player_choice == 'paper') or (cpu_choice == 'paper' and player_choice == 'rock'):
            cpu_win_count += 1
            print(
                f'CPU won!. Your choice: {player_choice}, CPU choice: {cpu_choice}')
            score_board(player_win_count, cpu_win_count)
        else:
            print(
                f'DRAW!. Your choice: {player_choice}, CPU choice: {cpu_choice}')
            score_board(player_win_count, cpu_win_count)
