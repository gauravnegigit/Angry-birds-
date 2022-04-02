import pymunk 
from pymunk import Vec2d 
from constants import ELASTICITY , FRICTION 


class Bird :
    def __init__(self , distance , angle , x , y , space) -> None:
        self.life = 20 
        mass = 5
        radius = 12 
        moment = pymunk.moment_for_circle(mass , 0 , radius , (0 , 0))
        body = pymunk.Body(mass , moment)
        body.position = x ,y 
        power = distance * 60 
        body.apply_impulse_at_local_point(Vec2d(power , 0).rotated(angle))
        shape = pymunk.Circle(body , radius , (0 , 0))
        shape.elasticity = ELASTICITY 
        shape.friction = FRICTION
        shape.collision_type = 0 
        space.add(body , shape)

        self.body = body 
        self.shape = shape 


class Pig :
    def __init__(self , x , y, space) -> None:
        self.life = 20 
        mass = 5
        radius = 14 
        moment = pymunk.moment_for_circle(mass , 0 , radius , (0 , 0))
        body = pymunk.Body(mass , moment )
        body.position = x , y 
        shape = pymunk.Circle(body , radius , (0 , 0))
        shape.elasticity = ELASTICITY
        shape.friction = FRICTION
        shape.collision_type = 1
        space.add(body , shape)
        
        self.body , self.shape = body , shape

