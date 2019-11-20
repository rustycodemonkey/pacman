"""
Write a module docstring here
"""

__author__ = "Phillip Kim"

import os
import sys


class Pacman:
    def __init__(self, board_dimension, initial_position, walls):
        self.board_dimension = board_dimension
        self.initial_position = initial_position
        self.walls = walls
        self.current_position = initial_position
        self.path_taken = [initial_position]
        self.coins_collected = 0

    def move(self, movement):
        print(self.board_dimension)
        print(self.walls)
        print(self.current_position)
        print(self.path_taken)
        print(movement)
        print("###################")

        if movement == 'N':
            pass

        elif movement == 'S':
            pass

        elif movement == 'E':
            pass

        elif movement == 'W':
            pass

        else:
            print("Incorrect movement {}. Exiting...".format(movement))
            sys.exit()

    def calc_coins(self):
        pass

    def results(self):
        return self.current_position[0], self.current_position[1], self.coins_collected


def pacman(input_file):
    """ Use this function to format your input/output arguments. Be sure not to change the order of the output arguments. 
    Remember that code organization is very important to us, so we encourage the use of helper fuctions and classes as you see fit.
    
    Input:
        1. input_file (String) = contains the name of a text file you need to read that is in the same directory, includes the ".txt" extension
           (ie. "input.txt")
    Outputs:
        1. final_pos_x (int) = final x location of Pacman
        2. final_pos_y (int) = final y location of Pacman
        3. coins_collected (int) = the number of coins that have been collected by Pacman across all movements
    """

    # Check if input file exists
    if not os.path.isfile(input_file):
        print("Input file {} does not exist. Exiting...".format(input_file))
        sys.exit()

    # Read input file
    with open(input_file) as fp:
        input_file_list = fp.read().splitlines()

        # Board dimension
        board_dimension = int(input_file_list[0].split(' ')[0]), int(input_file_list[0].split(' ')[1])

        # Initial position
        initial_position = int(input_file_list[1].split(' ')[0]), int(input_file_list[1].split(' ')[1])

        # Movements
        movements = list(input_file_list[2])

        # Walls
        walls_list = input_file_list[3:]
        walls = [(int(wall.split(' ')[0]), int(wall.split(' ')[1])) for wall in walls_list]

        # (10, 10)
        # (13, 13)
        # ['N', 'N', 'N', 'E', 'S', 'E', 'N', 'N', 'W', 'E', 'S', 'E', 'S', 'S', 'W', 'S', 'S', 'E', 'N', 'N', 'E', 'N', 'N', 'E', 'E', 'E', 'E', 'S', 'E', 'S', 'S', 'W', 'W', 'S', 'W', 'S', 'E', 'S', 'S']
        # [(1, 7), (1, 8), (2, 5), (3, 4), (3, 5), (3, 6), (3, 7), (5, 6), (5, 7), (7, 3), (8, 4), (9, 4)]
        # print(board_dimension)
        # print(initial_position)
        # print(movements)
        # print(walls)
        # print("###############################")

    # Initialise a Pacman object using inputs
    pm = Pacman(board_dimension, initial_position, walls)

    # Move Pacman according to input movements
    for movement in movements:
        pm.move(movement)

    # Calculate the coins collected
    pm.calc_coins()

    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    # return final_pos_x, final_pos_y, coins_collected
    return pm.results()