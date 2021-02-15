#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Rock, Paper, Scissors Game

This program plays a game of Rock, Paper, Scissors between two
Players, and reports both Player's scores each round.
"""

# imports TODO: Remove comment when done

# global variables TODO: Remove comment when done
# NOTE: this is the only global variable 
moves = ['rock', 'paper', 'scissors']


# class definitions TODO: Remove comment when done
class Player:
    """The Player class is the parent class for all of the Players
    in this game"""


    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


# TODO: test each Player subclass against HumanPlayer


# TODO: define RandomPlayer subclass
#       - chooses move randomly


# TODO: define HumanPlayer subclass
#       - include move method requesting input (see demo)
#       - move method should also validate input (see demo)


# TODO: define ReflectPlayer subclass
#       - remembers opponent's last move, playing that during
#           current move
#         - implemented in learn() method which saves info
#             in instance variable
#       - what to do for first move?


# TODO: define CyclePlayer subclass
#       - remembers its last move, cycles through moves
#         - implemented in learn() method which saves info
#             in instance variable
#       - what to do for first move?


# TODO: update Game class to display:
#       - outcome of each round
#       - keep score for both players
#
#       use beats() function
#
#       handle ties
#
#       configure to play RandomPlayer vs RandomPlayer
#
#       configure to play HumanPlayer vs RandomPlayer
#
#       call each players move method once per round
#
#       after each round, call learn method to tell each
#         payer what the other player's move was
#
#       some Players do not need to remember, method should pass
#
#       method to play single round
#
#       method to play match
#
#       score and number of rounds played are instance variables
class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    # TODO: call learn() method on each player object
    #
    #       print results of round
    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    # TODO: print:
    #       - which player won
    #       - final scores
    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")

    # TODO: define configure() method
    #       - win after 3 rounds
    #       - human player types quit
    #       - one player ahead 3 points

# function definitions TODO: Remove comment when done
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


# TODO: define input() function for human player


def main():
    """Launcher."""
    game = Game(Player(), Player())
    game.play_game()

if __name__ == '__main__':
    main()

# TODO: test code by running, import to test functions/methods

# TODO: run pycodestyle against code

# TODO: final check against project documentation and rubric
