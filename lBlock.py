# File: lBlock.py
# Author: Tyrone Hou (tyroneh@bu.edu)
# Purpose: ADT representing l-shaped blocks

from graphics import *

(L,R,U,D) = (-1,1,1,-1)


class lBlock(Polygon):
    def __init__(self, x, y, orientation, length):
        """ Defines a unique block on a Cartesian plane from
            x, y coords and a given orientation.
                    x,y -- x and y coords of the smallest square that circumscribes the lBlock.
            orientation -- a tuple recording the two orientation of the corner blocks:
                           The first element is left/right, the second is up/down
                           1 - right or up -1 - left or down
            """
        
        self.x = x
        self.y = y
        self.length = length
        self.orientation = orientation
        Polygon.__init__(self.calcPoints())
        
    def calcPoints(self):
        """ Calculates and returns a list of the vertices of the L-shaped tile"""

        vertices = []
        
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i, j) is not orientation:
                    vertices += [( self.x+(length*i), self.y+(length*j) )]

        return vertices
