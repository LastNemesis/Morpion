## Import main library
from tkinter import *

## Board creation
class Board:
    """ This is the class for the Tic-Tac-Toe Board """
    
    def __init__(self, brain):
        """ This function initializing the board """
        self.window         = Tk()
        self.title          = "Tic-Tac-Toe"

        self.height         = 400
        self.width          = int(self.height * 0.75)

        self.window.geometry(str(self.width) + "x" + str(self.height))

        self.background     = 'white'

        self.font_color     = 'black'
        self.font_family    = 'Arial'
        self.font_size      = 30

        self.buttons        = {}

        self.brain = brain

        self.canvas_init()
        self.buttons_board_placing()
        self.initialize_game()
    
    def canvas_init(self):
        """ This function creates and initialize the main canvas"""
        # Creating Canvas
        self.canvas = Canvas(self.window, width = self.width, height = self.height, bg = self.background)
        
        # Binding the user-click with the main brain function
        self.canvas.bind("<Button-1>", self.brain.user_position)

        # Placing the Canvas inside the window
        self.canvas.place(x=0, y=0)
    
    def canvas_destroy(self):
        """ This function destroys the main canvas"""
        # Detroying canvas
        self.canvas.destroy()
    
    def canvas_reset(self):
        """ This function destroys the main canvas"""
        # Destroying canvas
        self.canvas_destroy()
        
        # Restoring canvas
        self.canvas_init()
        self.buttons_board_placing()
        self.initialize_game()
        
        # Restoring the brain to its basic
        self.brain.initialize()
    
    def start(self):
        """ This function starts the Tkinter window """
        # Starting the main loop
        self.window.mainloop()

    def place_title(self):
        """ This function places the title """
        # Placing title
        self.canvas.create_text(self.width/2, self.height/8, text=self.title, fill=self.font_color, font=(self.font_family, self.font_size))

    def board(self):
        """ This function draws the board """
        # Horizontal lines
        self.canvas.create_line(0, self.height * 1/4, self.width, self.height * 1/4)
        self.canvas.create_line(0, self.height * 2/4, self.width, self.height * 2/4)
        self.canvas.create_line(0, self.height * 3/4, self.width, self.height * 3/4)
        self.canvas.create_line(0, self.height * 4/4, self.width, self.height * 4/4)
        
        # Vertical lines
        self.canvas.create_line(self.width * 0/3, self.height * 1/4, self.width * 0/3, self.height)
        self.canvas.create_line(self.width * 1/3, self.height * 1/4, self.width * 1/3, self.height)
        self.canvas.create_line(self.width * 2/3, self.height * 1/4, self.width * 2/3, self.height)
        self.canvas.create_line(self.width * 3/3, self.height * 1/4, self.width * 3/3, self.height)
    
    def initialize_game(self):
        """ This function intialize the full board """
        # Drawing the basic canvas background
        self.place_title()
        self.board()
    
    def buttons_board_placing(self):
        """ This function places the main buttons """
        # Creating the button
        self.buttons.update({'Button_reset': Button(self.window, text='reset', font=5, bg='white', command=self.canvas_reset)})
        
        # Placing the button
        self.buttons['Button_reset'].place(x=1, y=1, width=60, height=20, anchor=NW)
    
    def cross(self, x, y):
        """ This function places a cross on the given coordinates """
        # Drawing a cross
        self.canvas.create_line((x*100) + 25, (y*100) + 125, (x*100) + 75, (y*100) + 175)
        self.canvas.create_line((x*100) + 75, (y*100) + 125, (x*100) + 25, (y*100) + 175)

    def circle(self, x, y):
        """ This function places a circle on the given coordinates """
        # Drawing a circle
        self.canvas.create_oval((x*100) + 25, (y*100) + 125, (x*100) + 75, (y*100) + 175, fill=self.background, outline=self.font_color)

    def winner(self, player):
        """ This function displays the winner """
        # Window
        self.canvas.create_rectangle(self.width * 1/12, self.height * 1/3.2, self.width * 11/12, self.height * 3/3.2, fill=self.background, outline=self.font_color)

        # Text
        self.canvas.create_text(int(self.width * 1/2), int(self.height * 7/16), text='You won !',fill=self.font_color, font=(self.font_family, self.font_size))
        self.canvas.create_text(int(self.width * 1/2), int(self.height * 12/16), text='is the winner',fill=self.font_color, font=(self.font_family, int(self.font_size * 2/3)))

        # Placing the player in the middle
        if (player == 1):
            
            # Winner is the cross
            self.cross(1,1)
        else:
            # Winner is the circle
            self.circle(1,1)

    def draw(self):
        """ This function displays the draw page """
        # Window
        self.canvas.create_rectangle(self.width * 1/12, self.height * 1/3.2, self.width * 11/12, self.height * 3/3.2, fill=self.background, outline=self.font_color)

        # Text
        self.canvas.create_text(int(self.width * 1/2), int(self.height * 8/16), text='Draw',fill=self.font_color, font=(self.font_family, self.font_size))
        self.canvas.create_text(int(self.width * 1/2), int(self.height * 10/16), text='Reset the game',fill=self.font_color, font=(self.font_family, int(self.font_size * 2/3)))