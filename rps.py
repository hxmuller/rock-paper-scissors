#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Rock, Paper, Scissors Game

This program plays a game of Rock, Paper, Scissors between two
Players, and reports both Player's scores each round.
"""

import random
import itertools

moves = ['rock', 'paper', 'scissors']


class Player:
    """The Player class is the parent class for all of the Players
    in this game"""


    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


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


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1.rounds_won = 0
        self.p2.rounds_won = 0
        self.p1.sets_won = 0
        self.p2.sets_won = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        self.score_round(move1, move2)

    def match_play(self):
        print("Match Play")
        print("- First to win 2 rounds wins set")
        print("- First to win 2 sets wins the match\n")
        print("Rock Paper Scissors, Go!\n")
        round = 0
        set = 1
        while self.p1.sets_won < 2 and self.p2.sets_won < 2:
            while self.p1.rounds_won < 2 and self.p2.rounds_won < 2:
                print(f"Round {round + 1} --")
                self.play_round()
                round += 1
                if self.p1.rounds_won == 2:
                    print(f"** Player 1 WINS SET {set} **\n")
                    set += 1
                    self.p1.sets_won += 1
                elif self.p2.rounds_won == 2:
                    print(f"** Player 2 WINS SET {set} **\n")
                    set += 1
                    self.p2.sets_won += 1
            round = 0
            if self.p1.sets_won  == 2:
                print("** MATCH PLAY WINNER: Player 1 **")
            elif self.p2.sets_won == 2:
                print("** MATCH PLAY WINNER: Player 2 **")
            self.p1.rounds_won = 0
            self.p2.rounds_won = 0
        print("** FINAL SCORES: **")
        print(f"** Player 1: {self.p1.sets_won} Sets Won **")
        print(f"** Player 2: {self.p2.sets_won} Sets Won **")
        print("\nGame over!")


    def rounds_play(self, rounds):
        print(f"Rounds Play: playing {rounds} rounds\n")
        print("Rock Paper Scissors, Go!\n")
        for round in range(rounds):
            print(f"Round {round + 1} --")
            self.play_round()
        if self.p1.rounds_won == self.p2.rounds_won:
            print("** ROUNDS PLAY WINNER: TIE **")
        elif self.p1.rounds_won > self.p2.rounds_won:
            print("** ROUNDS PLAY WINNER: Player 1 **")
        else:
            print("** ROUNDS PLAY WINNER: Player 2 **")
        print("** FINAL SCORES: **")
        print(f"** Player 1: {self.p1.rounds_won} Rounds Won **")
        print(f"** Player 2: {self.p2.rounds_won} Rounds Won **")
        print(f"** Ties: {rounds - self.p1.rounds_won - self.p2.rounds_won} **")
        print("\nGame over!")

    def score_round(self, move1, move2):
        if move1 == move2:
            print("** TIE **")
        elif beats(move1, move2):
            self.p1.rounds_won += 1
            print("** PLAYER ONE WINS **")
        else:
            self.p2.rounds_won += 1
            print("** PLAYER TWO WINS **")
        print(f"Score: Player One {self.p1.rounds_won}, Player Two {self.p2.rounds_won}\n")
    

def select_players():
    players = ["One", "Two"]
    for idx, player in enumerate(players):
        choice = ""
        print(f"Player {player} Selection Menu:")
        print("1 - simple (always plays rock)")
        print("2 - random (selects random move)")
        print("3 - reflect (plays opponents last move)")
        print("4 - human (keyboard driven)")
        while choice not in ["1", "2", "3", "4"]:
            choice = input(f"Select Player {player} type: ")
        if choice == "1":
            player_type = Player()
        if choice == "2":
            player_type = RandomPlayer()
        if choice == "3":
            player_type = ReflectPlayer()
        if choice == "4":
            player_type = HumanPlayer()
        if idx == 0:
            player_1 = player_type
        if idx == 1:
            player_2 = player_type
    return Game(player_1, player_2)


def select_game(game):
    choice = ""
    rounds = 0
    print("Game Selection Menu:")
    print("1 - Rounds Play")
    print("2 - Match Play")
    while choice not in ["1", "2" ]:
        choice = input("Select game: ")
    if choice == '1':
        while True:
            number = input("Enter number of rounds to play: ")
            try:
                rounds = int(number)
                if rounds <= 0:
                    continue
                break
            except ValueError:
                continue
        game.rounds_play(rounds)
    if choice == '2':
        game.match_play()



def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def main():
    """Launcher."""
    game = select_players()
    select_game(game)

if __name__ == '__main__':
    main()

# TODO: test code by running, import to test functions/methods

# TODO: run pycodestyle against code

# TODO: final check against project documentation and rubric
