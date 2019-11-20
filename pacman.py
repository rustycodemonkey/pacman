"""
Write a module docstring here
"""

__author__ = "Phillip Kim"

import os
import sys


# class Pacman:
#     def __init__(self):


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
        movements = input_file_list[2]

        # Walls
        walls_list = input_file_list[3:]
        walls = [(int(wall.split(' ')[0]), int(wall.split(' ')[1])) for wall in walls_list]

        print(board_dimension)
        print(initial_position)
        print(movements)
        print(walls)



        # line = fp.readline()
        # print(line)
        #
        # line = fp.readline()
        # print(line)

        print("###############################")

    # pm = Pacman()

    # return final_pos_x, final_pos_y, coins_collected
    return 1, 2, 3
