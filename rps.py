#!/usr/bin/python

import random


def askUser():
    answer = raw_input("Rock, Paper, Scissors? ")
    return answer


def askForNumberOfGames():
    answer = None
    while answer == None:
        try:
            answer = int(
                raw_input('How many number of games would you like to play? '))
        except ValueError:
            print('Not a valid number. Try again.')

    return answer


def validateAnswer(answer, options):
    answer = answer.strip().capitalize()
    if answer in options:
        return True

    print('Not a valid option')
    return False


def pickRandom(options):
    choice = random.randint(0, (len(options) - 1))

    return options[choice]


def determineWinner(player1, player2):
    if player1 == player2:
        return 3
    elif player1 == 'Rock':
        if player2 == 'Paper':
            return 2
        elif player2 == 'Scissors':
            return 1
    elif player1 == 'Paper':
        if player2 == 'Rock':
            return 1
        elif player2 == 'Scissors':
            return 2
    elif player1 == 'Scissors':
        if player2 == 'Rock':
            return 2
        elif player2 == 'Paper':
            return 1


def oneOrSeveral(amount, word):
    if amount != 1:
        word += 's'

    return word


options = ['Rock', 'Paper', 'Scissors']

games = askForNumberOfGames()

gamesPlayed = 0
ties = 0

player1Wins = 0
player2Wins = 0

while games > gamesPlayed:
    userChoice = askUser().capitalize()
    computerChoice = pickRandom(options)

    if validateAnswer(userChoice, options):
        result = determineWinner(userChoice, computerChoice)
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

print
print('Player 1: %d %s.' % (player1Wins, oneOrSeveral(player1Wins, 'win')))
print('Player 2: %d %s.' % (player2Wins, oneOrSeveral(player2Wins, 'win')))
print('%d %s played.' % (gamesPlayed, oneOrSeveral(gamesPlayed, 'game')))
print('%d %s.' % (ties, oneOrSeveral(ties, 'tie')))
print
