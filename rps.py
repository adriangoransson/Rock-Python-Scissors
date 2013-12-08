#!/usr/bin/env python3

import random


def askUser():
    """Promt user for a choice"""
    answer = input("Rock, Paper, Scissors? ")
    return answer


def askForNumberOfGames():
    """Ask for and validate user input saying how many games are to be played"""
    answer = None
    while answer == None:
        try:
            answer = int(
                input('How many number of games would you like to play? '))
        except ValueError:
            print('Not a valid number. Try again.')

    return answer


def validateAnswer(answer, options):
    """Make sure that the answer is in supplied options dict or list"""
    if answer in options:
        return True

    print('Not a valid option')
    return False


def pickRandom(options):
    """Choose a random key from options dict or list. If dict, extract keys"""
    options = list(options)
    choice = random.randint(0, (len(options) - 1))

    return options[choice]


def determineWinner(player1, player2, options):
    """Use options (must be a dictionary) to determine if player1 choice beats player2"""
    if player1 == player2:
        return 3
    elif options[player1] == player2:
        return 1
    elif options[player2] == player1:
        return 2


def oneOrSeveral(amount, word):
    """Append an "s" to the end of word if amount is not 1"""
    if amount != 1:
        word += 's'

    return word

def presentResults(player1Wins, player2Wins, gamesPlayed, ties, padding=False):
    """Present player wins, how many games have been played and the number of ties"""
    # Empty line above and below makes it look a bit nicer.
    if padding:
        print()
    print('Player 1: %d %s.' % (player1Wins, oneOrSeveral(player1Wins, 'win')))
    print('Player 2: %d %s.' % (player2Wins, oneOrSeveral(player2Wins, 'win')))
    print('%d %s played.' % (gamesPlayed, oneOrSeveral(gamesPlayed, 'game')))
    print('%d %s.' % (ties, oneOrSeveral(ties, 'tie')))
    if padding:
        print()

def main():
    # options and what option they beat
    options = {'Rock': 'Scissors', 'Paper': 'Rock', 'Scissors': 'Paper'}

    games = askForNumberOfGames()

    gamesPlayed = 0
    ties = 0

    player1Wins = 0
    player2Wins = 0

    # iterate over number of games chosen by user
    # if a player wins the round, increment gamesPlayed and playerXWins
    # else, increment ties
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

    # present results with padding
    presentResults(player1Wins, player2Wins, gamesPlayed, ties, True)

# be nice, do not run if not explicitly told so
if __name__ == '__main__':
    main()