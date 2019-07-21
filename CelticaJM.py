# --------------------------------------------------
# Name: Jessica  
# Program: CelticaJM.py
# --------------------------------------------------
# Program purpose: part 2 of the Celtica Game 

from graphics import *
import random


## to jump to display/gui-related functions and settings, search "GUI settings"
## to jump to game-related and background functions, search "mechanics"
## to jump to main() function, search "main()"





### ~~ GUI settings ~~ ###


# I made it playable for every size board, though it might look prettier at some settings, like 500 or 600
# this value can be changed to adjust board size; maybe in the finished game it could ask for input for board size
width = height = w = 600                                                        # "w" for width; height and width should always be equal for this game

# Purpose:          dictionary of ratio-points where the balls should arrange themselves around heboard
# Syntax:           Circle(Point(pointdict()[iterationitem][1]), Point(pointdict()[iterationitem][2])))
# Parameters:       none
# Return value:     pointdict: a dictionary mapping locations to location on the board
def pointdict():
    d = (1/10)*w                                                                # "d" for distance from sides of game board
    # board setup; these are the loactions of all the balls
    pointdict = {0:[(6/10)*w, d],
             1:[(7/10)*w, d],
             2:[(8/10)*w, d], 
             3:[w-d, d], 
             4:[w-d, (2/10)*w], 
             5:[w-d, (3/10)*w], 
             6:[w-d, (4/10)*w],
             7:[w-d, (5/10)*w], 
             8:[w-d, (6/10)*w], 
             9:[w-d, (7/10)*w], 
             10:[w-d, (8/10)*w], 
             11:[w-d, w-d], 
             12:[(8/10)*w, w-d], 
             13:[(7/10)*w, w-d], 
             14:[(6/10)*w, w-d], 
             15:[(5/10)*w, w-d], 
             16:[(4/10)*w, w-d], 
             17:[(3/10)*w, w-d], 
             18:[(2/10)*w, w-d], 
             19:[d, w-d], 
             20:[d, (8/10)*w], 
             21:[d, (7/10)*w], 
             22:[d, (6/10)*w], 
             23:[d, (5/10)*w], 
             24:[d, (4/10)*w], 
             25:[d, (3/10)*w], 
             26:[d, (2/10)*w], 
             27:[d , d], 
             28:[(2/10)*w, d], 
             29:[(3/10)*w, d], 
             30:[(4/10)*w, d], 
             31:[(5/10)*w, d], 
             32:[w/2, w/2]}
    return pointdict


# Purpose:          helper function to draw the background rectangles that are darker versions of the colors they house
# Syntax:           draw_rectangle(width/4, width/4, "purple", window)
# Parameters:       x: the x-coordinate of the anchor point
#                   y: the y-coordinate of the anchor point
#                   color: the color of the box
#                   win: the window to draw it in
# Return value:     none
def draw_rectangle(x, y, color, win):                                           # draws the rectangles that make up the background croos
    rect = Rectangle(Point(x-(width/4-25), y-(height/4-25)), Point(x+(width/4-25), y+(height/4-25)))
    rect.setFill(color)
    rect.draw(win)


# Purpose:          helper function to draw the circles that make up the marbles of Celtica
# Syntax:           draw_circle(Point(width/5, width/5), "blue", window)
# Parameters:       point: the anchor point of the circle to be drawn
#                   color: the color of the inside of the circle
#                   win: the window in wich to draw the circle
# Return value:     none
def draw_circle(point, color, win):
    circ = Circle(Point(pointdict()[point][0], pointdict()[point][1]), 20)
    circ.setOutline("white")
    circ.setWidth(1)
    circ.setFill(color)
    circ.draw(win)


# Purpose:          helper function to draw the marbles of the board consistently
# Syntax:           draw_board(list_representing_the_board, window)
# Parameters:       board: a list in the format ["G", "G", "B", ...], the same length and contents as setup_game(), though not necessarily the same order
#                   win: the window in which to draw the board
# Return value:     none
def draw_board(board, win):
    for numitem in range(33):                                                   # give each letter the appropriate colour
        if board[numitem] == "G":
            color = color_rgb(0, 250, 0)
        if board[numitem] == "Y":
            color = color_rgb(254, 250, 6)
        if board[numitem] == "R":
            color = color_rgb(255, 39, 0)
        if board[numitem] == "B":
            color = color_rgb(0, 251, 255)
        if board[numitem] == "X":
            color = "black"
        draw_circle(numitem, color, win)


# Purpose:          helper function to draw the background in one, consistent, swoop
# Syntax:           make_background(window)
# Parameters:       window: the window in which you want the background drawn
# Return value:     none
def make_background(win):                                                       # makes the background that looks like a celtic cross
    win.setBackground(color_rgb(1, 25, 148))                                    # make the background blue

    yellow = color_rgb(146, 144, 0)                                             # define dark colours of squares
    aqua = color_rgb(0, 145, 147)
    red = color_rgb(148, 17, 0)
    green = color_rgb(0, 142, 0)
    
    draw_rectangle(w/4, w/4, aqua, win)                                         # draw squares
    draw_rectangle((3/4)*w, w/4, green, win)
    draw_rectangle(w/4, (3/4)*w, yellow, win)
    draw_rectangle((3/4)*w, (3/4)*w, red, win)


# Purpose:          to draw the text that is always present on the Celtica board
# Syntax:           draw_board_text(window)
# Parameters:       win: the window in which to draw the writing
# Return value:     none
def draw_board_text(win):
    celtica = Text(Point(w/2, w/4), "Celtica")                                  # begin dawing text for "Celtica"
    celtica.setSize(25)
    celtica.setTextColor("white")
    celtica.draw(win)
    
    brb = Text(Point(w/2, (w/4)+25), "by BRB")                                  # begin drawing text for "by BRB"
    brb.setStyle("bold")
    brb.setTextColor("white")
    brb.draw(win)    





### ~~ mechanics ~~ ###


# Purpose:          helper function to setup_game() that appends something to a list 8 times
# Syntax:           append_8(item, alist)
# Parameters:       item - an item that you want to append to a list; list - the list you wish to append to
# Return value:     none
def append_8(item, alist):
    counter = 0
    while counter < 8:
        alist.append(item)
        counter = counter + 1


# Purpose:          to generate a list of balls, in order, for a game of celtica
# Syntax:           board = setup_game()
# Parameters:       none
# Return value:     board - a list of characters representing the celtica game board; ['G', 'G', 'G', 'G', 'G', ... ]
def setup_game():
    board = []
    append_8("G", board)
    append_8("R", board)
    append_8("Y", board)
    append_8("B", board)
    board.append("X")
    return board                                                                # this board should be in the winning configuration


# Purpose:          to swap two values in the game board
# Syntax:           exchange(board, 1, 7)
# Parameters:       board - a list of characters representing the celtica game board, ['G', 'G', 'G', 'G', 'G', ... ], two numbers that are indices in the list board
# Return value:     none
def exchange(board, first, second):
    board[first], board[second] = board[second], board[first]  


# Purpose:          to see if the game is over
# Syntax:           is_over = is_game_over(board)
# Parameters:       board - a list of characters representing the celtica game board, ['G', 'G', 'G', 'G', 'G', ... ]
# Return value:     True, if winning configuration; False otherwise
def is_game_over(board):   
    if board == setup_game():
        return True
    else:
        return False


# Purpose:          helper function to create a shuffled board, because I apparently hadn't done this before
# Syntax:           board_to_start_playing_with = make_random_board(setup_game)
# Parameters:       none
# Return value:     shuffled version of winboard from setup_game(), list
def make_random_board():
    newboard = setup_game()[:]
    
    for i in range(25000):                                                        
        possibletrade = random.randint(0, len(newboard)-1)                      # choose a random index in newboard
        
        if is_neighbour(whereisX(newboard), possibletrade) == True:
            exchange(newboard, whereisX(newboard), possibletrade)               # if the random index is a legal move, then switch it
        else:
            continue

    return newboard


# Purpose:          handy helper function to quickly find X in a board
# Syntax:           exchange(whereisX(board), 32)
# Parameters:       board: the board you want to find X's location in
# Return value:     the index of where X is in board
def whereisX(board):
    return board.index("X")


# Purpose:          helper function, returns true if the marble in question can be legally traded with another marble
# Syntax:           if is_neighbour(whereisX(board), board[20]) == True: ...
# Parameters:       whereXis: can actually be any location on the board, but it's most useful to do it for X
#                   newspot: another location on the board to test for validity
# Return value:     bool: True or False
def is_neighbour(whereXis, newspot):

    # neigbourdict is a dictionary of all the possible places a marble can move
    neighbourdict = {0:(31, 1), 1:(0, 2), 2:(1, 3), 3:(2, 4), 4:(3, 5), 5:(4, 6),                
                    6:(5, 7), 7:(6, 32, 8), 8:(7, 9), 9:(8, 10), 10:(9, 11), 
                    11:(10, 12), 12:(11, 13), 13:(12, 14), 14:(13, 15), 15:(14, 32, 16), 
                    16:(15, 14), 17:(16, 18), 18:(17, 19), 19:(18, 20), 20:(19, 21), 
                    21:(20, 22), 22:(21, 23), 23:(22, 32, 24), 24:(23, 25), 25:(24, 26), 
                    26:(25, 27), 27:(26, 28), 28:(27, 29), 29:(28, 30), 30:(29, 31), 
                    31:(30, 32, 0), 32:(31, 7, 23, 15)}

    if newspot in neighbourdict[whereXis]:                                      # returns True if neighbour, False if not
        return True
    else:
        return False


# Purpose:          determines if a move is legal
# Syntax:           if is_legal_move(board, 20): ...
# Parameters:       board: the board with which you're working
#                   index: the index you might want to switch to
# Return value:     bool: True or False
def is_legal_move(board, index):
    whereXis = board.index("X")
    return is_neighbour(whereXis, index)


# Purpose:          Check if a point is within the bounding box of button
# Syntax:           bool = is_clicked(point, button)
# Parameters:       point - Point object
#                   button - Rectangle object 
# Return value:     True if point is within the bounding box of button;
#                   False, otherwise
def is_clicked(point, button):
    top_left = button.getP1()
    bottom_right = button.getP2()                                               # useable as is because graphics.py has a square object for every circle object

    return (point.x >= top_left.x and point.x <= bottom_right.x and
            point.y >= top_left.y and point.y <= bottom_right.y)





### ~~ main ~~ ###


# Purpose:          runs the completed game
# Syntax:           main()
# Parameters:       none
# Return value:     none
def main():
    win = GraphWin("Celtica", width, height)                                    # make a window

    make_background(win)                                                        # set up background, text, and scrambled board
    draw_board_text(win)
    board = make_random_board()
    
    draw_board(board, win)                                                      # draw the board
    
    
    if is_game_over(board) == True:                                             # if board is in winning configuration...
        winner = Text(Point(w/2, (2/3)*w), "You win!")                          # begin drawing text for "You win!"
        winner.setSize(25)
        winner.setTextColor("white")
        winner.draw(win)
    
    while True:
        try:                                                                    # .checkMouse() may fail if the window was closed; prevent
            point = win.checkMouse()                                            # Python from crashing by placing it within a try/except block;
        except GraphicsError:                                                   # given the error, the function can return (instead of crashing)
            return
        if point == None:                                                       # if no mouse click, starts while loop all over (this try/except was copied from lab 6)
            continue
        
        for keyvalue in pointdict().items():                                    # where marbles get exchanged
            index, centerpoint = keyvalue                                       # unpack the tuple so both keys and values are useable
            if is_clicked(point, Circle(Point(centerpoint[0], centerpoint[1]), 20)):
                if is_legal_move(board, index):
                    exchange(board, whereisX(board), index)                     # if it's a legal move, exchange marbles
                    draw_board(board, win)                                      # once exchanged, redraw

    close()





main()

