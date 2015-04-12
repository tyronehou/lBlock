# File: lBlock.py
# Author: Tyrone Hou (tyroneh@bu.edu)
# Purpose: ADT representing l-shaped blocks
from graphics import *

directions = {
    1: (1, 1),
    2: (-1, 1),
    3: (-1, -1),
    4: (1, -1)
}

# Helper functions

def eraseLine(p1, p2, win, color):
    """ Draws over a line. p1 & p2 are (x,y) coordinates rep. the endpoints
    """
    l = Line(p1, p2)
    l.setOutline(color)
    l.draw(win)
    

def getDiagonal(x, y, d, s):
    """ Calculates the endpoint of a diagonal of
        a square of side length s given the other endpoint and the
        direction the endpoint faces. Returns a double value.
        d -- direction vector
        s -- side length
    """

    dx, dy = d
    return (x + s*dx, y + s*dy)


class lBlock:
    def __init__(self, x, y, orient, length):
        """ Defines a unique block of given side length
            from x, y coords and a given orientation.
            x,y -- x and y coords of the smallest square that circumscribes the lBlock.
            orientation -- a tuple recording the two orientation of the corner blocks:
                           The first element is left/right, the second is up/down
                           1 - right or up -1 - left or down
            """

        # spatial data
        self.x = x
        self.y = y
        self.center = Point(x, y)
        self.length = length          
        self.orientation = directions[orient]

        # color data
        self.fill = 'white'
        self.outline  = 'black'


    def __str__(self):
        length = "Length: " + str(self.length)
        center = "Center: (" + str(self.x) + ", " + str(self.y) + ")"
        orientation = "Orientation: " + str(self.orientation)
        
        return length + "\n" + center + "\n" + orientation + "\n"

    
    def draw(self, win):
        diagonals = self.getDiagonals()

        # Draws three minisquares to get the form of the blocks
        for p1, p2 in diagonals:
            r = Rectangle(p1, p2)
            r.setFill(self.fill)
            r.setOutline(self.outline)
            r.draw(win)
            
        # Erases the two extraneous inner lines
        dx, dy = self.orientation
        p1 = Point(self.x - (dx * self.length), self.y) # endpoint 1
        q1 = Point(self.x, self.y - (dy * self.length)) # endpoint 2

        eraseLine(self.center, p1, win, self.fill)
        eraseLine(self.center, q1, win, self.fill)

    def undraw(self, win):
        """ undraws lBlock from given window
        """
        diagonals = self.getDiagonals()

        for p1, p2, in diagonals:
            r = Rectangle(p1, p2)
            r.setFill('white')
            r.setOutline('white')
            r.draw(win)

    def setFill(self, fill):
        """ Sets inner color for lBlock from given window
            fill -- string variable
        """
        self.fill = fill

    def setOutline(self, outline):
        """ Sets inner color for lBlock from given window
            outline -- string variable
        """
        self.outline = outline

    def getDiagonals(self):
        """ Calculates and returns the endpoints of a diagonal
            of each of the 3 subsquares of the tile"""
        
        diagonals = []
        for i in range(1,5):
                d = directions[i] # possible orientation
                
                if d != self.orientation:
                    diagonal = getDiagonal(self.x, self.y, d, self.length)
                    Dx, Dy = diagonal

                    diagonals += [(self.center, Point(Dx, Dy))]
                                
        return diagonals # returns the vertices of the lBlock


def test():
    #Initializing and printing
    print("Initializing lBlocks...")
    block1 = lBlock(60, 60, 1, 40)
    block2 = lBlock(140, 60, 2, 40)
    block3 = lBlock(140, 140, 3, 40)
    block4 = lBlock(60, 140, 4, 40)

    print("block1")
    print(block1)
    
    print("block2")
    print(block2)
    
    print("block3")
    print(block3)
    
    print("block4")
    print(block4)

    # shell methods
    print("Testing getDiagonal(0, 0, directions[4], .5):")
    print("(0.5, -0.5)")
    print(getDiagonal(0, 0, directions[4], .5))

    print()

    print("Testing getDiagonal(-1, 23, directions[3], 200):")
    print("(-202, -177)")
    print(getDiagonal(-2, 23, directions[3], 200))

    print()

    print("Testing getDiagonal(-1, 23, directions[2], 0):")
    print("(-1, 23)")
    print(getDiagonal(-1, 23, directions[3], 0))

    print()

    print("Testing getDiagonal(-1, -1, directions[1], 3):")
    print("(2, 2)")
    print(getDiagonal(-1, -1, directions[1], 3))

    print()
    
    print("Testing getDiagonals for block1:")
    print("(20, 100) (20, 20) (100, 20)")
    for diag in block1.getDiagonals():
        p = diag[1]
        x, y = p.getX(), p.getY()
        print("(" + str(x) + ", " + str(y) + ")", end = " ")

    print("\n")

    # Drawing test
    
    print("Drawing lBLock...")
    win = GraphWin(autoflush = False)
    win.setCoords(0, 0, 200, 200)

    # Cycle through the four blocks
    block1.draw(win)
    
    win.getMouse()

    block1.undraw(win)
    block2.draw(win)
    
    win.getMouse()
        
    block2.undraw(win)
    block3.draw(win)
    
    win.getMouse()
    
    block3.undraw(win)
    block4.draw(win)
    
    win.getMouse()
    
    block4.undraw(win)

    # Draw the windows symbol (sort of) :]
    block1.setFill('blue')
    block2.setFill('yellow')
    block3.setFill('green')
    block4.setFill('red')

    block1.setOutline('blue')
    block2.setOutline('yellow')
    block3.setOutline('green')
    block4.setOutline('red')    
    
    block1.draw(win)
    block2.draw(win)
    block3.draw(win)
    block4.draw(win)

    print("It's Windows!")
    
    # Wait for user response
    win.getMouse()

    print("I'm Done")
    
    # exit test
    win.close()

if __name__ == '__main__':
    test()

    
