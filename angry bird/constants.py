import pygame

# main screen cosntants
WIDTH , HEIGHT = 1200 , 600 
WIN  = pygame.display.set_mode((WIDTH , HEIGHT))

# game constants 
SLING_X , SLING_Y = 135, 450
SLING2_X, SLING2_Y = 160, 450

# attributes for physical pymunk objects
ELASTICITY = 0.85
FRICTION = 1

# image constants
WOOD = pygame.image.load("assets/images/wood.png").convert_alpha()
WOOD2 = pygame.image.load("assets/images/wood2.png").convert_alpha()
REDBIRD = pygame.image.load("assets/images/red-bird3.png").convert_alpha()
BACKGROUDND = pygame.image.load("assets/images/background3.png").convert_alpha()
SLING_IMAGE = pygame.image.load("assets/images/sling-3.png").convert_alpha()
FULL_SPRITE = pygame.image.load("assets/images/full-sprite.png").convert_alpha()

# some misc. images 
rect = pygame.Rect(181 , 1050 , 50 , 50)
cropped = FULL_SPRITE.subsurface(rect).copy()
PIG = pygame.transform.scale(cropped , (30 , 30))
BUTTONS = pygame.image.load("assets/images/selected-buttons.png").convert_alpha()
PIG_HAPPY = pygame.image.load("assets/images/pig_failed.png").convert_alpha()
STARS = pygame.image.load("assets/images/stars-edited.png").convert_alpha()
rect = pygame.Rect(0 , 0 , 200 , 200)
STAR1 = STARS.subsurface(rect).copy()
rect = pygame.Rect(204 , 0 , 200 , 200)
STAR2 = STARS.subsurface(rect).copy()
rect = pygame.Rect(426 , 0 , 200 , 200)
STAR3 = STARS.subsurface(rect).copy()
rect = pygame.Rect(164 , 10 , 60 , 60)
PAUSE = BUTTONS.subsurface(rect).copy()
rect = pygame.Rect(24 , 4 , 100 , 100)
REPLAY = BUTTONS.subsurface(rect).copy()
NEXT = BUTTONS.subsurface(pygame.Rect(142 , 365 , 130 , 100)).copy()
PLAY = BUTTONS.subsurface(pygame.Rect(18 , 212 , 100 , 100)).copy()

# color constants
RED =(255 , 0 , 0)
GREEN = (0 , 255 ,0)
BLUE = (0 , 0 , 255)
WHITE = (255 , 255 , 255)
BLACK = (0 , 0 , 0)
