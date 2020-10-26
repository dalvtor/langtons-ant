import time
from termcolor import colored
from src.direction import Direction
from src.settings import GRID_COLORS, TIME_TO_SLEEP, GRID_CHARACTER


class LangtonsAnt:

    def __init__(self, grid, starting_position):
        """
        :param grid: A two-dimensional matrix of booleans representing the grid
        :param starting_position: A tuple of positive integers representing the (x, y) starting coordinates of the ant
        """

        # We need to check that the starting position is valid.
        if not isinstance(starting_position, tuple) or len(starting_position) != 2:
            raise TypeError('The starting position of the ant must be a tuple of coordinates')

        start_pos_x, start_pos_y = starting_position

        if start_pos_x < 0 or start_pos_y < 0 or start_pos_x >= len(grid) or start_pos_y >= len(grid[0]):
            raise TypeError('The given starting position is out of range')

        self.grid = grid
        self.position = {
            'x': start_pos_x,
            'y': start_pos_y
        }
        self.direction = 0

    @property
    def state(self):
        return self.grid

    def next(self):
        """
        Flips the cell and moves one step forward according to the game rules
        """
        try:
            # Negative indexes are considered invalid in this case
            if self.position['x'] < 0 or self.position['y'] < 0:
                raise IndexError

            # Check if we should rotate clockwise on anticlockwise
            if not self.grid[self.position['x']][self.position['y']]:
                self.rotate_clockwise()
            else:
                self.rotate_anticlockwise()
            direction_x, direction_y = Direction.get_direction(self.direction).value
            self.flip_color(self.position['x'], self.position['y'])

            # Updates the position
            self.position['x'] += direction_x
            self.position['y'] += direction_y
        except IndexError:
            print("A wall was hit. We can't move further.")
            exit(0)

    def flip_color(self, x, y):
        """
        :param x: x coordinate
        :param y: y coordinate

        Flips the value of the cell
        """
        self.grid[x][y] = not self.grid[x][y]

    def draw_grid(self):
        """
        Draws the current grid to the standard output
        """
        output = ''
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                output += (colored(GRID_CHARACTER, GRID_COLORS[self.grid[i][j]]))
            output += '\n'
        print(output)

    def rotate_clockwise(self):
        """
        Rotates the ant 90 degrees clockwise
        """
        self.direction = (self.direction + 1) % 4

    def rotate_anticlockwise(self):
        """
        Rotates the ant 90 degrees anticlockwise
        """
        self.direction = (self.direction - 1) % 4

    def simulate(self, steps):
        """
        :param steps: number of steps

        Simulates and prints N steps at once
        """
        for i in range(steps):
            print(f"Iteration: {i + 1}")
            self.next()
            self.draw_grid()
            time.sleep(TIME_TO_SLEEP)
