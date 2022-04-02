import random
from re import X
from debugpy import is_client_connected
from pymunk import Poly
from characters import Pig 
from polygon import Polygon
from constants import WIDTH , HEIGHT

class Level :
    def __init__(self , pigs , columns , beams , space) -> None:
        self.pigs = pigs 
        self.beams = beams 
        self.columns = columns 
        self.space = space 
        self.number_of_birds = 4
        
        self.prev = 0  # tracks the previous level of the game
        self.curr = 0 
        # stars for winning the game according to the scores
        self.one_star = 20000
        self.two_star = 40000
        self.three_star = 60000
        self.bool_space =   False 

    def open_flat(self , x , y , n):
        """This method is used for creating an open flat structure in the game ."""

        Y = y 

        for i in range(n):
            y = y + 100

            # adding 2 columns and then a beam in bwteen 
            p  = (x , HEIGHT - y)
            self.columns.append(Polygon(p , 20 , 85 , self.space))

            p = (x + 60 , HEIGHT - y )
            self.beams.append(Polygon(p , 85 , 20 , self.space))

            p = (x + 30 , HEIGHT - y - 50)
            self.beams.append(Polygon(p , 85 , 20 , self.space))
        
    def closed_flat(self , x , y , n):
        """This method would be used for creating a closed flat structure """

        Y = y 

        for i in range(n):
            y = y + 100

            # adding 2 columns and then a 2 beams in bwteen 
            p = (x ,  HEIGHT - (y + 22))
            self.columns.append(Polygon(p , 20 , 85 , self.space))
            p = (x + 60 ,HEIGHT - ( y + 22))
            self.columns.append(Polygon(p , 20 , 85 , self.space))
            p = (x + 30 ,HEIGHT - ( y + 70))
            self.beams.append(Polygon( p , 85 , 20 , self.space))
            p = (x + 30 , HEIGHT - (y - 30))
            self.beams.append(Polygon(p , 85 , 20 , self.space))
    
    def vertical_pile(self , x , y , n):
        y -= 10
        for i in range(n):
            p = (x, HEIGHT - (y+85+i*85))
            self.columns.append(Polygon(p, 20, 85, self.space))

    def build_0(self):
        """This method will handle the level 2 for the game 
        return : None 
        """

        pig1 = Pig(WIDTH - 520 , HEIGHT - 100 , self.space)
        pig2 = Pig(WIDTH - 510 , HEIGHT - 180  , self.space)
        self.pigs.append(pig1)
        self.pigs.append(pig2)

        # creating bemas and columns for the game 
        w , h = WIDTH , HEIGHT
        p = (w - 550 , h - 80)
        self.columns.append(Polygon(p , 20 , 85 , self.space))
        p = (w - 490 , h - 80)
        self.columns.append(Polygon(p , 20 , 85 , self.space))
        p = (w - 520 , h - 150)
        self.beams.append(Polygon (p , 85 , 20 , self.space))
        p = (w - 550 , h - 200)
        self.columns.append(Polygon(p , 20 , 85 , self.space))
        p = (w - 490 , h - 200)
        self.columns.append(Polygon(p , 20 , 85 , self.space))
        p = (w - 520 , h - 240)
        self.beams.append(Polygon(p , 85 , 20 , self.space))
        self.number_of_brids = 4 

        if self.bool_space :
            self.number_of_brids = 0 

    def build_1(self):
        pig = Pig(WIDTH - 500 , HEIGHT - 100 , self.space)

        self.pigs.append(pig)
        p = (WIDTH - 600 , HEIGHT - 80)
        self.columns.append(Polygon(p , 20 , 85 , self.space))
        p = (WIDTH - 650 , HEIGHT - 80)
        self.columns.append(Polygon(p , 20 , 85 , self.space))
        p = (WIDTH - 650 , HEIGHT - 150)
        self.columns.append(Polygon(p , 20 , 85 , self.space))
        p = (WIDTH - 450 , HEIGHT - 150)
        self.columns.append(Polygon(p , 20 , 85 , self.space))
        p = (WIDTH - 395 , HEIGHT - 210)
        self.beams.append(Polygon(p , 85 , 20 , self.space))

        self.number_of_birds = 4
        if self.bool_space :
            self.number_of_birds = 8 
    
    def build_2(self):
        self.pigs.append(Pig(WIDTH - 650 , HEIGHT - 180 , self.space))
        self.pigs.append(Pig(WIDTH - 500 , HEIGHT - 230 , self.space))
        
        p = (WIDTH - 650 , HEIGHT - 80)
        self.columns.append(Polygon(p , 20 , 85 , self.space))
        p = (WIDTH - 650 , HEIGHT - 150)
        self.beams.append(Polygon(p , 85 , 20 , self.space))
        p = (WIDTH - 500 , HEIGHT - 80)
        self.columns.append(Polygon(p , 85 , 20 , self.space))
        p = (WIDTH - 500 , HEIGHT - 180)
        self.columns.append(Polygon(p , 20 , 85 , self.space))
        p = (WIDTH - 500 , HEIGHT - 210)
        self.beams.append(Polygon(p , 85 , 20 , self.space))
        self.number_of_birds = 4

        if self.bool_space :
            self.number_of_birds = 8 
    
    def build_3(self):
        """level 3"""
        pig = Pig(950, 320, self.space)
        pig.life = 25
        self.pigs.append(pig)
        pig = Pig(885, HEIGHT - 225, self.space)
        pig.life = 25
        self.pigs.append(pig)
        pig = Pig(1005, HEIGHT - 225, self.space)
        pig.life = 25
        self.pigs.append(pig)
        p = (1100, HEIGHT - 100)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1070, HEIGHT - 152)
        self.beams.append(Polygon(p, 85, 20, self.space))
        p = (1040, HEIGHT - 100)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (980, HEIGHT - 100)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (920, HEIGHT - 100)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (950, HEIGHT - 152)
        self.beams.append(Polygon(p, 85, 20, self.space))
        p = (1010, HEIGHT - 180)
        self.beams.append(Polygon(p, 85, 20, self.space))
        p = (860, HEIGHT - 100)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (800, HEIGHT - 100)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (830, HEIGHT - 152)
        self.beams.append(Polygon(p, 85, 20, self.space))
        p = (890, HEIGHT - 180)
        self.beams.append(Polygon(p, 85, 20, self.space))
        p = (860, HEIGHT - 223)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (920, HEIGHT - 223)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (980, HEIGHT - 223)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1040, HEIGHT - 223)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (890, HEIGHT - 280)
        self.beams.append(Polygon(p, 85, 20, self.space))
        p = (1010, HEIGHT - 280)
        self.beams.append(Polygon(p, 85, 20, self.space))
        p = (950, HEIGHT - 300)
        self.beams.append(Polygon(p, 85, 20, self.space))
        p = (920, HEIGHT - 350)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (980, HEIGHT - 350)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (950, HEIGHT - 400)
        self.beams.append(Polygon(p, 85, 20, self.space))
        self.number_of_birds = 4
        if self.bool_space:
            self.number_of_birds = 8

    def build_4(self):
        pig = Pig(900, HEIGHT - 300, self.space)
        self.pigs.append(pig)
        pig = Pig(1000, HEIGHT - 500, self.space)
        self.pigs.append(pig)
        pig = Pig(1100, HEIGHT - 400, self.space)
        self.pigs.append(pig)
        self.number_of_birds = 4
        if self.bool_space:
            self.number_of_birds = 8 

    def build_5(self) :
        """level 5"""
        pig = Pig(900, HEIGHT - 70, self.space)
        self.pigs.append(pig)
        pig = Pig(1000, HEIGHT - 152, self.space)
        self.pigs.append(pig)
        for i in range(9):
            p = (800, 300+i*21)
            self.beams.append(Polygon(p, 85, 20, self.space))
        for i in range(4):
            p = (1000, 300+i*21)
            self.beams.append(Polygon(p, 85, 20, self.space))
        p = (970, HEIGHT - 176)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1026, HEIGHT - 176)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1000, HEIGHT - 230)
        self.beams.append(Polygon(p, 85, 20, self.space))
        self.number_of_birds = 4
        if self.bool_space:
            self.number_of_birds = 8
    
    def build_6(self):
        pig = Pig(920, HEIGHT - 533, self.space)
        pig.life = 40
        self.pigs.append(pig)
        pig = Pig(820, HEIGHT - 533, self.space)
        self.pigs.append(pig)
        pig = Pig(720, HEIGHT - 633, self.space)
        self.pigs.append(pig)
        self.closed_flat(895, 423, 1)
        self.vertical_pile(900, 0, 5)
        self.vertical_pile(926, 0, 5)
        self.vertical_pile(950, 0, 5)
        self.number_of_birds = 4
        if self.bool_space:
            self.number_of_birds = 8

    def build_7(self):
        """level 7"""
        pig = Pig(1000, HEIGHT - 180, self.space)
        pig.life = 20
        self.pigs.append(pig)
        pig = Pig(900, HEIGHT - 180, self.space)
        pig.life = 20
        self.pigs.append(pig)
        self.open_flat(1050, 0, 3)
        self.open_flat(963, 0, 2)
        self.open_flat(880, 0, 2)
        self.open_flat(790, 0, 3)
        self.number_of_birds = 4
        if self.bool_space:
            self.number_of_birds = 8
    
    def load_level(self , l = None  ):
        
        total_levels = 8
        self.number_of_birds = 4

        if l is None  : 
            x = random.randint(0 , total_levels - 1)

            while x == self.prev : 
                x = random.randint(0 , total_levels - 1)

            build_name = "build_" + (str(x))

        else :
            x = l  
            build_name = "build_" + (str(x))
        
        self.curr = x  # storing the current level 

        getattr(self , build_name)()
        return x 
        
