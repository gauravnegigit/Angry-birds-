import math 
import pymunk 
import pygame
import pymunk.pygame_util
from pymunk import Vec2d

from constants import ELASTICITY , FRICTION , WOOD , WOOD2


class Polygon :
    def __init__(self , pos , width , height , space , mass = 5) -> None:
        moment = 1000
        body = pymunk.Body(mass , moment)
        body.position = pos 
        shape = pymunk.Poly.create_box(body , (width , height ))
        shape.color = (0 , 0 , 255 , 100)
        shape.friction = FRICTION
        shape.elasticity = 0.5
        shape.collision_type = 2
        space.add(body , shape)
        rect = pygame.Rect(251 , 357 , 86 , 22)
        self.beam_image = WOOD.subsurface(rect).copy()
        rect = pygame.Rect(16 , 252 , 22 , 84)
        self.column_image = WOOD2.subsurface(rect).copy()

        self.shape , self.body = shape , body

    
    def draw_poly(self , element , screen):
        """Blittinhg beams and columns on the screen """

        poly = self.shape 
        ps = poly.get_vertices()
        ps.append(ps[0])
        
        ps = list(ps)
        color = (255 , 0 , 0)
        pygame.draw.lines(screen , color , False , ps)

        p = poly.body.position
        p  = Vec2d(p[0] , p[1])
        angle_degrees = math.degrees(poly.body.angle) + 180

        if element == "beams" :
            rotated_img = pygame.transform.rotate(self.beam_image , angle_degrees)
        if element == "columns":
            rotated_img = pygame.transform.rotate(self.column_image , angle_degrees)
        
        offset = Vec2d(*rotated_img.get_size()) // 2
        p -= offset

        screen .blit(rotated_img , (p.x , p.y))

        
        