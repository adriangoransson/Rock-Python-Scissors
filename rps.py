#!/usr/bin/env python3

import random


def askUser():
    answer = input("Rock, Paper, Scissors? ")
    return answer


def askForNumberOfGames():
    answer = None
    while answer == None:
        try:
            answer = int(
                input('How many number of games would you like to play? '))
        except ValueError:
            print('Not a valid number. Try again.')

    return answer


def validateAnswer(answer, options):
    if answer in options:
        return True

    print('Not a valid option')
    return False


def pickRandom(options):
    options = list(options)
    choice = random.randint(0, (len(options) - 1))

    return options[choice]


def determineWinner(player1, player2, options):
    if player1 == player2:
        return 3
    elif options[player1] == player2:
        return 1
    elif options[player2] == player1:
        return 2


def oneOrSeveral(amount, word):
    if amount != 1:
        word += 's'

    return word

# options and what option they beat
options = {'Rock': 'Scissors', 'Paper': 'Rock', 'Scissors': 'Paper'}

games = askForNumberOfGames()

gamesPlayed = 0
ties = 0

player1Wins = 0
player2Wins = 0

while games > gamesPlayed:
    userChoice = askUser().strip().capitalize()
    computerChoice = pickRandom(options)

    if validateAnswer(userChoice, options):
        result = determineWinner(userChoice, computerChoice, options)
        if result == 3:
            ties += 1
            print('%s - %s. Tie!' % (userChoice, computerChoice))
        else:
            if result == 1:
                player1Wins += 1
            elif result == 2:
                player2Wins += 1
            print('%s - %s. Player %d wins!'
                  % (userChoice, computerChoice, result))
            gamesPlayed += 1

print('')
print('Player 1: %d %s.' % (player1Wins, oneOrSeveral(player1Wins, 'win')))
print('Player 2: %d %s.' % (player2Wins, oneOrSeveral(player2Wins, 'win')))
print('%d %s played.' % (gamesPlayed, oneOrSeveral(gamesPlayed, 'game')))
print('%d %s.' % (ties, oneOrSeveral(ties, 'tie')))
print('')
