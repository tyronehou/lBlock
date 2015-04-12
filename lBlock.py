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

def eraseLine(p1, p2, win):
    """ Draws over a line by covering it with a white line
        p1 & p2 are (x,y) tuples rep. the endpoints
    """
    l = Line(p1, p2)
    l.setOutline('white')
    l.draw(win)
    

def getDiagonal(x, y, d, s):
    """ Calculates the endpoint of a diagonal of
        a square of side length s given the other endpoint and the
        direction the endpoint faces. Returns a double value.
        d -- direction vector
        corner -- (x,y) coordinate tuple
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
        
        self.x = x
        self.y = y
        self.center = Point(x, y)
        self.length = length          
        self.orientation = directions[orient]


    def __str__(self):
        length = "Length: " + str(self.length)
        center = "Center: (" + str(self.x) + ", " + str(self.y) + ")"
        orientation = "Orientation: " + str(self.orientation)
        
        return length + "\n" + center + "\n" + orientation + "\n"

    
    def draw(self, win):
        diagonals = self.getDiagonals()

        # Draws three minisquares to get the form of the blocks
        for p1, p2 in diagonals:
            Rectangle(p1, p2).draw(win)
            
        # Erases the two extraneous inner lines
        dx, dy = self.orientation
        p1 = Point(self.x - (dx * self.length), self.y) # endpoint 1
        q1 = Point(self.x, self.y - (dy * self.length)) # endpoint 2

        eraseLine(self.center, p1, win)
        eraseLine(self.center, q1, win)
        
        
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
    print("Initializing lBlock...")
    block = lBlock(100, 100, 1, 50)
    print(block)
    
    print("Testing getCenters:")
    print("(50, 150) (50, 50) (150, 50)")
    for diag in block.getDiagonals():
        p = diag[1]
        x, y = p.getX(), p.getY()
        print("(" + str(x) + ", " + str(y) + ")", end = " ")

    print()
        
    print("Drawing lBLock...")
    win = GraphWin()
    block.draw(win)
    win.getMouse()
    win.close()

if __name__ == '__main__':
    test()

    
