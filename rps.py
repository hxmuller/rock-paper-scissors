#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Rock, Paper, Scissors Game

This program plays a game of Rock, Paper, Scissors between two
Players, and reports both Player's scores each round.
"""

# imports TODO: Remove comment when done
import random
import itertools

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


class RandomPlayer(Player):
    """The RandomPlayer subclass selects a move randomly"""

    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    """The HumanPlayer requests validated input"""
    
    def move(self):
        human_input = ""
        while human_input not in moves:
            human_input = input("Rock, paper, scissors? > ")
        return human_input


class ReflectPlayer(Player):
    """The ReflectPlayer remembers opponent's last move, playing
    that during the current move"""

    def __init__(self):
        self.last_move = random.choice(moves)

    def move(self):
        return self.last_move

    def learn(self, my_move, their_move):
        self.last_move = their_move
        

class CyclePlayer(Player):
    """The CyclePlayer remembers its last move, and cycles through
    the moves"""

    def __init__(self):
        self.last_move = random.choice(moves)

    def move(self):
        if self.last_move == 'rock':
            return 'paper'
        elif self.last_move == 'paper':
            return 'scissors'
        else:
            return 'rock'

    def learn(self, my_move, their_move):
        self.last_move = my_move


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
        self.p1.round_score = 0
        self.p2.round_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        self.score_round(move1, move2)

    # TODO: print:
    #       - which player won
    #       - final scores
    def play_rounds(self, rounds):
        print("Rock Paper Scissors, Go!")
        for round in range(rounds):
            print(f"Round {round + 1} --")
            self.play_round()
        if self.p1.round_score == self.p2.round_score:
            print("** ROUNDS PLAY WINNER: TIE **")
        elif self.p1.round_score > self.p2.round_score:
            print("** ROUNDS PLAY WINNER: Player 1 **")
        else:
            print("** ROUNDS PLAY WINNER: Player 2 **")
        print("** FINAL SCORES: **")
        print(f"** Player 1: {self.p1.round_score} Rounds Won **")
        print(f"** Player 2: {self.p2.round_score} Rounds Won **")
        print("Game over!")

    def score_round(self, move1, move2):
        if move1 == move2:
            print("** TIE **")
        elif beats(move1, move2):
            self.p1.round_score+= 1
            print("** PLAYER ONE WINS **")
        else:
            self.p2.round_score += 1
            print("** PLAYER TWO WINS **")
        print(f"Score: Player One {self.p1.round_score}, Player Two {self.p2.round_score}")
    

    # TODO: define configure() method
    #       - win after 3 rounds
    #       - human player types quit
    #       - one player ahead 3 points

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def main():
    """Launcher."""
    game = Game(ReflectPlayer(), ReflectPlayer())
    game.play_rounds(1000000)

if __name__ == '__main__':
    main()

# TODO: test code by running, import to test functions/methods

# TODO: run pycodestyle against code

# TODO: final check against project documentation and rubric
