# File: lBlock.py
# Author: Tyrone Hou (tyroneh@bu.edu)
# Purpose: ADT representing l-shaped blocks

(L,R,U,D) = (-1,1,1,-1)


class lBlock:
    def __init__(self, x, y, orientation):
        """ Defines a unique block on a Cartesian plane from
            x, y coords and a given orientation.
                    x,y -- x and y coords of the center of the center block.
            orientation -- a tuple recording the two orientation of the corner blocks:
                           The first element is left/right, the second is up/down
                           1 - right or up -1 - left or down
            """

        self.x = x
        self.y = y

        if orientation == (R, U):    
            self.orientation = 1
        elif orientation == (L, U):
            self.orientation = 2
        elif orientation == (L, D):
            self.orientation = 3
        elif orientation == (R, D):
            self.orientation = 4

    #def draw(self):

    def getBlock(self):
        
        
    def rotateCC(self):
        """Rotates the lBlock 90 degrees clockwise"""

        self.orientation = (self.orientation + 1) % 4;

    def rotateCCW(self):
        """ Rotates the lBlock 90 degrees counterclockwise"""

        self.orientation = (self.orientation - 1) % 4;
