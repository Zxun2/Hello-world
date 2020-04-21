

import random
import time

total_tries = 0
possible_answers = ['R', 'P', 'S']

user = 0
user_points = 0
comp_points = 0


def game() :
    global user, user_points, comp_points

    print('Welcome to a game of Rock, Scissors, Paper !')
    print('Please input the number of tries (from 1-10) you wish to play')
    tries = input()
    if int(tries) > 10 :
        print('Invalid Input!')
        print('Try again?')
        answer = input()
        if answer == 'Yes' :
            game()
    elif int(tries) == 0 :
            print('Ok, goodbye!')
    else:
        total_tries = int(tries)
        print('Lets begin!')
        while user < total_tries :
            user_input = input('Please choose an element: ')
            user += 1
            computer = random.choices(possible_answers)
            if user_input == 'R' :
                print('You have chosen Rock!')
                time.sleep(1)
                if computer == 'P' :
                    time.sleep(1)
                    print('The computer have chosen Paper!')
                    print('You have lost! Noob')
                    comp_points +=1
                elif computer == 'R' :
                    time.sleep(1)
                    print('The computer have chosen Rock!')
                    print('No one wins! -_-')
                else:
                    time.sleep(1)
                    print('The computer have chosen Scissors! ')
                    print('You won!')
                    user_points += 1
            elif user_input == 'S' :
                print('You have chosen Scissors!')
                time.sleep(1)
                if computer == 'P':
                    print('The computer have chosen Paper!')
                    time.sleep(1)
                    print('You have won!')
                    user_points += 1
                elif computer == 'R':
                    time.sleep(1)
                    print('The computer have chosen Rock!')
                    print('You have lost! Noob')
                    comp_points += 1
                else:
                    time.sleep(1)
                    print('The computer have chosen Scissors! ')
                    print('No one wins....!')
            elif user_input == 'P' :
                print('You have chosen Paper')
                time.sleep(1)
                if computer == 'P':
                    time.sleep(1)
                    print('The computer have chosen Paper!')
                    print('No one won!')
                elif computer == 'R':
                    time.sleep(1)
                    print('The computer have chosen Rock!')
                    print('You have won!')
                    time.sleep(1)
                    user_input += 1
                else:
                    time.sleep(1)
                    print('The computer have chosen Scissors! ')
                    print('You lost! Noob')
                    time.sleep(1)
                    comp_points += 1
            time.sleep(1)
            print('User:', user_points)
            print('Computer:',comp_points)

    if user_points > comp_points :
        print('You have won the game!')
    elif user_points == comp_points :
        print('It\'s a draw!')
    else:
        print('You have lost the game!')

    print('Would you like to play again?')
    player =input()
    if player == 'Yes':
        total_tries = 0
        user = 0
        comp_points = 0
        user_points = 0
        game()
    elif player == 'No' :
        print('Thank you and goodbyee!')



