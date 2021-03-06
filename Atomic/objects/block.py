from pygame import sprite, Surface
from atom import Atom 

class Block(sprite.Sprite): 
    BLOCK_WIDTH, BLOCK_HEIGHT = 25, 25

    def __init__(self, x, y): 
        super().__init__() 

        self.x = x 
        self.y = y 
        
        self.width = Block.BLOCK_WIDTH 
        self.height = Block.BLOCK_HEIGHT 

        self.surface = Surface((Block.BLOCK_WIDTH, Block.BLOCK_HEIGHT))
        self.surface.fill((255, 0, 0))

    def setX(self, x): 
        self.x = x 

    def setY(self, y): 
        self.y = y 

    def burst(self): 
        """  """
        pass 


