"""This module runs a Pacman like game.

Pacman moves on his game board collecting coins.
The output produces the last position of Pacman's (X, Y) coordinates and the number of coins collected.

This code was cloned from https://github.com/c3ai/pacman and then modified as a solution to a technical quiz.

Note to the code reviewer:
    Debugging statements were not removed so that the code reviewer can see how the code was tested/developed.

    There is a symbolic link created in test_files/py_test directory for this file. That is, this code and
    the test cases work without moving any files around as required. However, if the provided zip file
    is unzipped on an operating system which doesn't support symbolic links then you must copy(and overwrite) this
    file into test_files/py_test directory manually to run the test cases. Having multiple copies of the same file in
    a repository is not a good code organisation practice. Hence, I did not copy this file into the testing directory.

Last Modified: November 21, 2019

"""

__author__ = "Phillip Kim"

import os
import sys


class Pacman:
    """This class represents the game Pacman.

    """

    def __init__(self, board_dimension, initial_position, walls):
        """The init function for Pacman class.

        Attributes:
            board_dimension (:obj:`tuple` of :obj:`int`): (X, Y) coordinates identifying the top right corner of the
            Pacman board. The bottom left corner of the Pacman board is represented by the coordinates (0, 0).

            initial_position (:obj:`tuple` of :obj:`int`): Starting position of Pacman in (X, Y) coordinates.

            walls (:obj:`list` of :obj:`tuple` of :obj:`int`): A list of walls in (X, Y) coordinates.

            current_position (:obj:`tuple` of :obj:`int`):  Current position of Pacman in (X, Y) coordinates.

            path_taken (:obj:`list` of :obj:`tuple` of :obj:`int`):  A list of Pacman's board positions
            in (X, Y) coordinates.

            coins_collected (:obj:`int`):  Number of coins collected by Pacman.

            perimeter (:obj:`list` of :obj:`tuple` of :obj:`int`): A list of (X, Y) coordinates which represent
            the perimeter of the game board. This list is generated by __get_perimeter_position function
            at object initialisation.

        """

        # Initialise and derive attributes from arguments
        self.board_dimension = board_dimension
        self.initial_position = initial_position
        self.walls = walls
        self.current_position = initial_position
        self.path_taken = [initial_position]
        self.coins_collected = 0
        self.perimeter = self.__get_perimeter_position()

    def __get_perimeter_position(self):
        """This function derives the perimeter of the game board from board dimensions.

        Returns:
            perimeter_points (:obj:`list` of :obj:`tuple` of :obj:`int`): A list of perimeter points
            in (X, Y) coordinates.

        """
        perimeter_points = []

        # Get top and bottom perimeter points of the game board
        for x in range(self.board_dimension[0] + 1):
            perimeter_points.append((x, 0))
            perimeter_points.append((x, self.board_dimension[1]))

        # Get left and right perimeter points of the game board
        for y in range(self.board_dimension[1] + 1):
            perimeter_points.append((0, y))
            perimeter_points.append((self.board_dimension[0], y))

        # Remove duplicate perimeter points at Pacman board vertices and then sort for readability
        perimeter_points = sorted(list(set(perimeter_points)))

        return perimeter_points

    def init_pos_out_of_bounds(self):
        """This function checks if Pacman's starting position is out of bounds.

        This function checks for two conditions:
        1. If the starting position is on the perimeter or beyond the game board
        2. If the starting position is one of the wall coordinates

        Returns:
            :obj:`Boolean`

        """
        # Check if initial_position is on the perimeter or outside of Pacman board
        if self.initial_position[0] >= self.board_dimension[0] or self.initial_position[0] <= 0 or \
                self.initial_position[1] >= self.board_dimension[1] or self.initial_position[1] <= 0:
            return True

        # Check if initial_position is one of the wall coordinates
        elif self.initial_position in self.walls:
            return True

        else:
            return False

    def move(self, movement):
        """This function moves Pacman on the game board.

        Args:
            movement(:obj:`str`): An instruction to move in cardinal directions
            e.g. 'N' means "go north" and 'E' means "go east"

        """
        # print("##### Start of a move #####")
        # print("board_dimension: {}".format(self.board_dimension))
        # print("initial_position: {}".format(self.initial_position))
        # print("walls: {}".format(self.walls))
        # print("perimeter: {}".format(self.perimeter))
        # print("current_position: {}".format(self.current_position))
        # print("path_taken: {}".format(self.path_taken))
        # print("movement: {}".format(movement))

        # Calculate temporary new position coordinate based on the movement direction
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

        # print("new_position: {}".format(new_position))

        # Only update current position and path taken if the new position is not part of the wall or the perimeter
        if new_position not in self.walls and new_position not in self.perimeter:
            self.current_position = new_position
            self.path_taken.append(new_position)
        else:
            # current_position and path_taken remains the same
            # print("Bumped into a wall or a perimeter")
            pass

        # print("Updated current_position: {}".format(self.current_position))
        # print("Updated path_taken: {}".format(self.path_taken))
        # print("##### End of a move #####")

    def calc_coins(self):
        """This function uses the record of the path taken to calculate the coins collected.

        Pacman can cross over or backtrack onto the path he has already taken so the duplicate entries in path_taken
        must be removed. Also, the starting position does not have a coin so it must be removed from path_taken before
        calculating the number of coins collected.

        """
        # print("##### Start of calc_coins #####")
        # print("path_taken: {}".format(self.path_taken))
        # print("length of path_taken: {}".format(len(self.path_taken)))
        # print("initial_position: {}".format(self.initial_position))

        # Using a temporary copy of path_taken so that path_taken attribute of the Pacman object isn't altered
        # Remove duplicates from path_taken
        temp_path_taken = list(set(self.path_taken))
        # Remove the starting point from temp_path_taken
        temp_path_taken.remove(self.initial_position)
        self.coins_collected = len(set(temp_path_taken))

        # print("path_taken: {}".format(self.path_taken))
        # print("length of path_taken: {}".format(len(self.path_taken)))
        # print("coins_collected: {}".format(self.coins_collected))
        # print("##### End of calc_coins #####")

    def results(self):
        """This function simply returns the required results.

        Returns:
            :obj:`tuple` of :obj:`int`

        """
        # return final_pos_x, final_pos_y, coins_collected
        return self.current_position[0], self.current_position[1], self.coins_collected


def pacman(input_file):
    """ Use this function to format your input/output arguments. Be sure not to change the order of the output arguments. 
    Remember that code organization is very important to us, so we encourage the use of helper functions and classes as you see fit.
    
    Args:
        1. input_file (String) = contains the name of a text file you need to read that is in the same directory, includes the ".txt" extension
           (ie. "input.txt")
    Returns:
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

        # Example breakdown of the inputs left in code as reference
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

    # Check Pacman's starting position and only proceed if his position is not out of bounds
    if pm.init_pos_out_of_bounds() is True:
        return -1, -1, 0

    else:
        # Iterate through the list movement directions and move Pacman accordingly
        for movement in movements:
            pm.move(movement)

        # Calculate the coins collected after all movements
        pm.calc_coins()

        # Run the results function to return final_pos_x, final_pos_y, coins_collected
        return pm.results()
