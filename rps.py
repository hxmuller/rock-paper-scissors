#!/usr/bin/env python3

""" Rock, Paper, Scissors Game

This program plays a game of Rock, Paper, Scissors between two
Players, and reports both Player's scores each round.
"""

# imports

# global variables
moves = ['rock', 'paper', 'scissors']


# class definitions
class Player:
    """The Player class is the parent class for all of the Players
    in this game"""


    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


# function definitions
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def main():
    """Launcher."""
    game = Game(Player(), Player())
    game.play_game()

if __name__ == '__main__':
    main()

