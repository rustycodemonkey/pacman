"""
The module takes a text file as an input and runs a Pacman like game producing an output
Please run the pacman function as per its docstring.
Last Modified: November 21, 2019
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

        self.perimeter = self.__get_perimeter_position()

    def __get_perimeter_position(self):
        perimeter_points = []

        # Get top and bottom perimeter points
        for x in range(self.board_dimension[0] + 1):
            perimeter_points.append((x, 0))
            perimeter_points.append((x, self.board_dimension[1]))

        # Get left and right perimeter points
        for y in range(self.board_dimension[1] + 1):
            perimeter_points.append((0, y))
            perimeter_points.append((self.board_dimension[0], y))

        # Remove duplicate perimeter points at rectangle vertices and then sort for readability
        perimeter_points = sorted(list(set(perimeter_points)))

        return perimeter_points

    def init_pos_out_of_bounds(self):
        # Check if initial_position is outside of 2-dimensional board
        if self.initial_position[0] >= self.board_dimension[0] or self.initial_position[0] <= 0 or \
                self.initial_position[1] >= self.board_dimension[1] or self.initial_position[1] <= 0:
            return True
        # Check if initial_position is a wall
        elif self.initial_position in self.walls:
            return True
        else:
            return False

    def move(self, movement):
        print("##### Start of a move #####")
        print("board_dimension: {}".format(self.board_dimension))
        print("initial_position: {}".format(self.initial_position))
        print("walls: {}".format(self.walls))
        print("perimeter: {}".format(self.perimeter))
        print("current_position: {}".format(self.current_position))
        print("path_taken: {}".format(self.path_taken))
        print("movement: {}".format(movement))

        if movement == 'N':
            new_position = self.current_position[0], self.current_position[1] + 1

        elif movement == 'S':
            new_position = self.current_position[0], self.current_position[1] - 1

        elif movement == 'E':
            new_position = self.current_position[0] + 1, self.current_position[1]

        elif movement == 'W':
            new_position = self.current_position[0] - 1, self.current_position[1]

        else:
            print("Incorrect movement {}. Exiting...".format(movement))
            sys.exit()

        print("new_position: {}".format(new_position))

        if new_position not in self.walls and new_position not in self.perimeter:
            self.current_position = new_position
            self.path_taken.append(new_position)
        else:
            # current_position and path_taken remains the same
            print("Bumped into a wall or a perimeter")

        print("Updated current_position: {}".format(self.current_position))
        print("Updated path_taken: {}".format(self.path_taken))
        print("##### End of a move #####")

    def calc_coins(self):
        print("path_taken: {}".format(self.path_taken))
        print("length of path_taken: {}".format(len(self.path_taken)))
        print("initial_position: {}".format(self.initial_position))

        # self.coins_collected = len(set(self.path_taken)) - 1

        # Using a temporary deep copy of path_taken so that path_taken isn't altered
        # Remove duplicates from path_taken
        temp_path_taken = list(set(self.path_taken))
        # Remove the starting point from temp_path_taken
        temp_path_taken.remove(self.initial_position)
        self.coins_collected = len(set(temp_path_taken))

        print("path_taken: {}".format(self.path_taken))
        print("length of path_taken: {}".format(len(self.path_taken)))
        print("coins_collected: {}".format(self.coins_collected))

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

        # Example breakdown of the inputs
        # print(board_dimension)
        # (10, 10)
        # print(initial_position)
        # (1, 5)
        # print(movements)
        # ['N', 'N', 'N', 'E', 'S', 'E', 'N', 'N', 'W', 'E', 'S', 'E', 'S', 'S', 'W', 'S', 'S', 'E', 'N', 'N', 'E',
        # 'N', 'N', 'E', 'E', 'E', 'E', 'S', 'E', 'S', 'S', 'W', 'W', 'S', 'W', 'S', 'E', 'S', 'S']
        # print(walls)
        # [(1, 7), (1, 8), (2, 5), (3, 4), (3, 5), (3, 6), (3, 7), (5, 6), (5, 7), (7, 3), (8, 4), (9, 4)]


    # Initialise a Pacman object using inputs
    pm = Pacman(board_dimension, initial_position, walls)

    if pm.init_pos_out_of_bounds() is True:
        return -1, -1, 0

    else:
        for movement in movements:
            pm.move(movement)

        # Calculate the coins collected
        pm.calc_coins()

        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

        # return final_pos_x, final_pos_y, coins_collected
        return pm.results()
