## Import main library
from tkinter import *

## Board creation
class Game:
    """ This is the class for the Game """

    def __init__(self, board, width, height):
        """ This function initialize the game """

        self.grid       = [[ 0, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ]]

        self.count      = 0
        self.turn       = 1

        self.board      = board

        self.width      = width
        self.height     = height

        self.key        = 1
    
    def main(self, event):
        """ This function is the main game logic function """

        # Getting the click coordinates
        X=event.x
        Y=event.y

        # Height loop
        for y in range(3):
            
            # Width loop
            for x in range(3):

                    # Checking if the click is in a cell
                    if (X > (100 * x)) and (X < (100 + 100 * x)) and (Y > (100 + 100 * y)) and (Y < (200 + 100 * y)) and (self.grid[y][x] == 0) and (self.key == 1):

                        # Depending on the turn, drawing a cross or a circle
                        if (self.turn%2 ==0):
                            
                            # Drawing a cross
                            self.board.cross(x,y)
                        
                        else:
                            # Drawing a circle
                            self.board.circle(x,y)
        
                        # Adding one to the counter
                        self.count += 1

                        # Adding one to board
                        self.grid[y][x] = (self.turn + 1)

                        # Changing the player
                        self.turn = (self.turn + 1) % 2
        
        # Checking if there is a winner (after minimum four moves)
        if (self.count > 4):
            self.winner_check()
        
        # Checking if there is a draw
        if (self.count > 7) and (self.key == 1):
            self.draw_check()

    def winner_check(self):
        """ This function checks if there is a winner """

        # For each row/column
        for i in range(3):

            # Vertical check
            if (self.grid[i][0] == self.grid[i][1] == self.grid[i][2] != 0):
                
                self.winner_display()
            
            # Horizontal check
            if (self.grid[0][i] == self.grid[1][i] == self.grid[2][i] != 0):
                
                self.winner_display()
            
        # Diagonal checks
        if (self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != 0):
                
                self.winner_display()
        
        if (self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != 0):
                
                self.winner_display()
    
    def winner_display(self):
        """ This function launches the winner display and cut-off the click function"""

        # Winner display
        self.board.winner(self.turn)

        # Cut-off
        self.key = 0
    
    def draw_check(self):
        """ This function check is the grid is full, then declares Draw """

        counter = 0

        # Height loop
        for y in range(3):
            
            # Width loop
            for x in range(3):

                # Checking if the cell is empty
                if (self.grid[y][x] != 0):

                    counter += 1
        
        # Checking if the grid is full
        if (counter == 9):
            
            # Displaying the draw page
            self.board.draw()

            # Cut-off
            self.key = 0