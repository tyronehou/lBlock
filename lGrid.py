from lBlock import *    

# helper function
#def getCenter():
    

class lGrid:
    def __init__(self, x, y, length, n):
        """ Initializes a grid with a center (x,y)
            consisting of 2^n by 2^n squares.

            length -- distance from center to side of grid
            n -- a nonnegative integer
        """
        
        self.x = x
        self.y = y
        self.length = length

        self.n = n
        
    def __str__(self):
        size = str(2**self.n) + "x" + str(2**self.n) + " grid"
        center = "Center: (" + str(self.x) + ", " + str(self.y) + ")"
        length = "Side length: " + str(self.length)

        hline = "-" * max(len(size), len(center), len(length))
        
        return size + "\n" + hline + "\n" + center + "\n" + length
        
        '''
    def tile(self, win):
        if:
            
        else:
            for i in range(1, 5):
                quarter = lGrid(
                self.tileCorner(corner)
                
    def tileCorner(self, corner):
        if self.length == 2: # base case
            block = lBlock(self.x, self.y, corner, win     
        '''

def test():
    grid = lGrid(100, 100, 50, 2)
    
    print("Initializing lGrid...")
    print(grid)

    print()

    
    
    win = GraphWin()
    win.close()
    

if __name__ == '__main__':
    test()
