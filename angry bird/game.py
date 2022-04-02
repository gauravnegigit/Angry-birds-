import time
import math 
import pymunk
import pygame 
import pymunk.pygame_util
from characters import Bird
from level import Level
from constants import *

pygame.init()

# game variables
score = 0 
game_state = 0 
bird_path = []
counter = 0 
restart_counter = False 
bonus_score_once = True 
bonus_score = 0 

# font variables
bold_font = pygame.font.SysFont("arial", 30, bold=True)
bold_font2 = pygame.font.SysFont("arial", 40, bold=True)
bold_font3 = pygame.font.SysFont("arial", 50, bold=True)


wall = False  # this variables will get turned into True if one wants teh wall to be present in the game

def draw(space , level , birds , pigs , beams , columns , counter ):
    global score , bird_path , restart_counter , mouse_dist 

    WIN.fill((130 , 200 , 100))

    # drawing background
    WIN.blit(BACKGROUDND , (0 , -50))

    # drawing the 1st part of the sling 
    rect = pygame.Rect(50 , 0 , 70 , 220)
    WIN.blit(SLING_IMAGE , (138 , 420) , rect)
    for point in bird_path :
        pygame.draw.circle(WIN , WHITE , point , 5 , 0)

    # draw the birds in the wait line 
    if level.number_of_birds > 0 :
        for i in range(level.number_of_birds - 1) :
            x = 100 - (i * 35)
            WIN.blit(REDBIRD , (x , 508))
    
    # drawing the birds 
    for bird in birds :
        if bird.shape.body.position.y < 0 :
            # removing the birds 
            space.remove(bird.shape , bird.shape.body)
            birds.remove(bird)
        
        p = bird.shape.body.position
        x , y = p
        x -= 22
        y -= 20

        WIN.blit(REDBIRD , (x , y))
        pygame.draw.circle(WIN , BLUE , p , int(bird.shape.radius) , 2)

        if counter >= 10 :
            bird_path.append(p)
            restart_counter = True 

    if restart_counter :
        counter = 0 
        restart_counter = False 

    # drawing the pigs 
    for pig in pigs :

        if pig.body.position.y > HEIGHT  :
            space.remove(pig.shape , pig.shape.body)
            pigs.remove(pig)

        pig = pig.shape 
        
        p = pig.body.position 
        x , y = p 

        angle_degrees = math.degrees(pig.body.angle)
        img = pygame.transform.rotate(PIG , angle_degrees)

        # offseting the circle and the image of the pig 
        w , h = img.get_size()
        x -= w * 0.5 
        y -= h * 0.5
        WIN.blit(img , (x , y))
        pygame.draw.circle(WIN , BLUE , p , int(pig.radius) , 2)
    
    # drawing columns and beams 

    for column in columns :
        column.draw_poly("columns" , WIN)
    
    for beam in beams :
        beam.draw_poly("beams" , WIN)

    # drawing the second part of the sling 
    rect = pygame.Rect(0 , 0 , 60 , 200)
    WIN.blit(SLING_IMAGE , (120 , 420) , rect)

    # displaysing the score in the game 
    display_score()
    WIN.blit(PAUSE , (10 , 90))

    # pause option
    if game_state == 1 :
        WIN.blit(PLAY , (WIDTH // 2 - 100 , HEIGHT //2 - 100))
        WIN.blit(REPLAY , (WIDTH // 2 - 100 , HEIGHT //2))


def display_score():
    bold_font = pygame.font.SysFont("arial" , 30 , bold = True )
    score_font = bold_font.render("SCORE : " , 1 , BLACK)
    number_font = bold_font.render(str(score) , 1 , BLACK)
    WIN.blit(score_font , (1000 , 50))
    WIN.blit(number_font , (1000 , 100))

def create_segments(space ) :
    static = [
        [(0 , 0 ) , (WIDTH , 0 )] , 
        [(0 , 0 ) , (0 , HEIGHT)] , 
        [(WIDTH - 2, 0) , (WIDTH - 2, HEIGHT)] 
    ]

    for start , end in static : 
        shape = pymunk.Segment(space.static_body , start , end , 1.0)
        shape.elasticity = ELASTICITY
        shape.friction = 0.5
        shape.color = (0 , 255 ,0 , 100)
        space.add(shape)

def floor(space):
    static_body = pymunk.Body(body_type = pymunk.Body.STATIC)
    static_lines = [pymunk.Segment(static_body , (0 , HEIGHT - 60) , (1200 ,HEIGHT - 60) , 0.0) ]
    for line in static_lines :
        line.elasticity = ELASTICITY
        line.friction = 1
        line.collision_type = 3
    space.add(static_body)
    space.add(*static_lines)

def unit_vector(p0 , p1):
    a , b = p1[0] - p0[0] , p1[1] - p0[1]
    h = ((a ** 2) + (b ** 2) ) ** 0.5 
    if h == 0 :
        h = 0.0000000001 

    x , y = a/h , b/h 

    return (x,y) 

def distance(xo, yo, x, y):
    """return : distance between points"""

    dx = x - xo
    dy = y - yo
    d = ((dx ** 2) + (dy ** 2)) ** 0.5
    return d

def sling_action(rope_length):
    """
    function for handling the sling
    return : None 
    """

    global mouse_dist , pos

    uv = unit_vector((SLING_X , SLING_Y), (pos[0] , pos[1]))
    mouse_dist = distance(SLING_X , SLING_Y , pos[0] , pos[1])
    bigger_rope = 102
    pu = (uv[0] * rope_length + SLING_X  , uv[1] * rope_length + SLING_Y )
    x_bird , y_bird = pos[0] - 20 , pos[1] - 20

    bigger_rope = 102 
    # this may be a bit tricky 
    if mouse_dist > rope_length : 
        px , py = pu 
        px -= 20 
        py -= 20 
        WIN.blit(REDBIRD , (px , py))
        pu2 = (uv[0] * bigger_rope + SLING_X , uv[1] * bigger_rope + SLING_Y) 
        pygame.draw.line(WIN , (0 , 0 , 0) , (SLING2_X , SLING2_Y) , pu2 , 5)
        #WIN.blit(REDBIRD ,(px , py))
        pygame.draw.line(WIN , (0 ,0 , 0) , (SLING_X , SLING_Y) , pu2 , 5)

    else :
        mouse_dist += 10 
        pu3 = (uv[0] * mouse_dist + SLING_X  , uv[1] * mouse_dist + SLING_Y )
        
        pygame.draw.line(WIN , (0 , 0 , 0) , (SLING2_X , SLING2_Y) ,pu3 , 5)
        WIN.blit(REDBIRD , (x_bird , y_bird))
        pygame.draw.line(WIN , (0 , 0 , 0) , (SLING_X , SLING_Y) , pu3 , 5)

    # angle of impulse 
    dy = pos[1] - SLING_Y 
    dx = pos[0] - SLING_X 
    if dx == 0 :
        dx = 0.00000000001
    angle = math.atan((float(dy))/dx)
    return angle 
    

def draw_level_failed(level , t2 , pigs):
    """function run when the level is failed"""
    global game_state
    failed = bold_font.render("Level Failed " , 1 , WHITE)
    if level.number_of_birds <= 0 and time.time() - t2 > 5 and len(pigs) > 0 :
        game_state = 3
        pygame.draw.rect(WIN , BLACK , (300 , 0 , 600 , 900))
        WIN.blit(failed , (450 , 90))
        WIN.blit(PIG_HAPPY , (380 , 120))
        WIN.blit(REPLAY , (520 , 460))

def restart(space , birds , pigs , beams , columns):
    """
    This function deletes all the objects of the level 
    return : None 
    """

    pigs_to_remove = []
    birds_to_remove = []
    columns_to_remove = []
    beams_to_remove = []

    for pig in pigs:
        pigs_to_remove.append(pig)
    for pig in pigs_to_remove:
        space.remove(pig.shape, pig.shape.body)
        pigs.remove(pig)
    for bird in birds:
        birds_to_remove.append(bird)
    for bird in birds_to_remove:
        space.remove(bird.shape, bird.shape.body)
        birds.remove(bird)
    for column in columns:
        columns_to_remove.append(column)
    for column in columns_to_remove:
        space.remove(column.shape, column.shape.body)
        columns.remove(column)
    for beam in beams:
        beams_to_remove.append(beam)
    for beam in beams_to_remove:
        space.remove(beam.shape, beam.shape.body)
        beams.remove(beam)

def draw_level_cleared(level , pigs , num):
    global game_state , score  , bonus_score_once 

    bold_font = pygame.font.SysFont("arial" , 50 , bold = True )
    level_cleared = bold_font.render("Level Cleared !" , 1 , WHITE)
    score_level = bold_font.render(str(score) , 1, WHITE)

    if level.number_of_birds >= 0 and len(pigs) == 0 :
        if bonus_score_once :
            score += (level.number_of_birds - 1) * 10000
            level.bool_space = True 

        bonus_score_once = False
        game_state = 4 
        pygame.draw.rect(WIN , BLACK , (300 , 0 , 600 , 800))

        WIN.blit(level_cleared , (450 , 90))
        if level.one_star <= score <= level.two_star :
            WIN.blit(STAR1 , (310 , 190))
        if level.two_star <= score <= level.three_star :
            WIN.blit(STAR1 , (310 , 190))
            WIN.blit(STAR2 , (500 , 170))
        
        if level.three_star <= score :
            WIN.blit(STAR1 , (310 , 190))
            WIN.blit(STAR2 , (500 , 170))
            WIN.blit(STAR3, (700  , 200))
        
        WIN.blit(score_level , (550 , 400))
        WIN.blit(REPLAY , (510 , 480))
        WIN.blit(NEXT , (620 , 480))

        level.prev = num 

def collision(space , pigs , beams , columns) :
    """
    funtion for handling collision    
    return : None 
    """

    def post_solve_bird_pig(arbiter , space , _):
        """
        This function handles the collision between the bird and the pig
        return : None 
        """

        a , b = arbiter.shapes
        bird_body = a.body 
        pig_body = b.body 
        
        r = 30 
        pygame.draw.circle(WIN , BLACK , bird_body.position , r , 4)
        pygame.draw.circle(WIN , BLACK , pig_body.position , r , 4)

        for pig in pigs :
            if pig_body == pig.body :
                pig.life -= 20 
                global score 
                score += 10000

                space.remove(pig.shape , pig.shape.body)
                pigs.remove(pig)

    def post_solve_bird_wood(arbiter , space, _):
        """handles collision between bird and wood"""
        poly_to_remove = []
        if arbiter.total_impulse.length > 1100 :
            a , b = arbiter.shapes

            for column in columns :
                if b == column.shape :
                    poly_to_remove.append(column)

            for beam in beams :
                if b == beam.shape :
                    poly_to_remove.append(beam)
            
            for poly in poly_to_remove :
                if poly in columns :
                    columns.remove(poly)
                
                if poly in beams :
                    beams.remove(poly)
            
            space.remove(b , b.body)
            global score 
            score += 5000
            
    def post_solve_pig_wood(arbiter, space, _):
        """Collision between pig and wood"""
        pigs_to_remove = []
        if arbiter.total_impulse.length > 1500:
            pig_shape, wood_shape = arbiter.shapes
            for pig in pigs:
                if pig_shape == pig.shape:
                    pig.life -= 20
                    global score
                    score += 10000
                    if pig.life <= 0:
                        pigs_to_remove.append(pig)

        for pig in pigs_to_remove:
            space.remove(pig.shape, pig.shape.body)
            pigs.remove(pig)
    
    space.add_collision_handler(0 , 1).post_solve = post_solve_bird_pig
    space.add_collision_handler(0 , 2).post_solve = post_solve_bird_wood
    space.add_collision_handler(1 , 2).post_solve = post_solve_pig_wood
    load_music()

def load_music():
    """function for loading the music
    return : None 
    """

    song1 = "assets/sounds/angry-birds.ogg"
    pygame.mixer.music.load(song1)
    pygame.mixer.music.play(-1)



def main():
    global score , game_state , counter, bird_path , restart_counter , mouse_dist , pos 

    run = True 
    clock = pygame.time.Clock()
    FPS = 60 

    # other game variables
    pigs = []
    birds = []
    beams = []
    columns = []
    rope_length  = 90 
    angle = 0
    mouse_pressed = False 

    # pymunk physics stuff 
    space = pymunk.Space()
    space.gravity = (0 , 981)
    # draw_options = pymunk.pygame_util.DrawOptions(WIN)
    dt = 1/FPS

    # handling collision 
    collision(space , pigs , beams , columns)

    level = Level(pigs , columns , beams , space)

    num = level.load_level(level.curr)

    # creating a static floor 
    floor(space)
    t1 = t2 = 0
    while run :
        clock.tick(FPS)
        space.step(dt)
        draw(space , level , birds , pigs , beams , columns , counter )
        draw_level_failed(level , t2 , pigs)
        draw_level_cleared(level , pigs , num)          
        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                run = False
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_r :
                    run = False
                    break 
            
                elif event.key == pygame.K_p :
                    pygame.image.save(WIN , "angry_birds.png")

                elif event.key == pygame.K_w :
                    # will create the wall if w is pressed 

                    if not wall :
                        create_segments(space)
                
                elif event.key == pygame.K_g :
                    space.gravity = (0 , 10)
                
                elif event.key == pygame.K_n :
                    space.gravity = (0 , 981)
                    level.bool_space = False 
                
            if pygame.mouse.get_pressed()[0] and (100 < pos[0] < 250) and 370 < pos[1] <  550 :
                mouse_pressed = True 

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and mouse_pressed :
                # releasing new bird 

                mouse_pressed = False
                if level.number_of_birds > 0 :
                    level.number_of_birds -= 1 
                    t1 = time.time() * 1000

                    x0 , y0 = 154 , HEIGHT - 156 
                    if mouse_dist > rope_length :
                        mouse_dist = rope_length 
                    if pos[0] < SLING_X + 5 :
                        bird = Bird(mouse_dist , angle , x0 , y0 , space)
                        birds.append(bird)
                    else :
                        bird = Bird(-mouse_dist , angle , x0 , y0 , space )
                        birds.append(bird)
                    
                    if level.number_of_birds == 0 :
                        t2 = time.time()

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1 :
                if pos[0] < 60 and pos[1] < 155 and pos[1] > 90  :
                    game_state = 1
                
                if game_state == 1 :
                    if pos[0] > WIDTH // 2 -100 and pos[1] > HEIGHT//2 - 100 :
                        game_state = 0
                    
                    if pos[0] > WIDTH//2 - 100 and pos[1] > HEIGHT//2 :
                        restart(space , birds , pigs , beams , columns)
                        num = level.load_level(level.curr)
                        game_state = 0 
                        bird_path = []
                
                if game_state == 3:
                    # condition when the player has failed
                    if WIDTH // 2 - 100 < pos[0] < WIDTH//2 + 20 and pos[1] > 450 :
                        restart(space , birds , pigs , beams , columns)
                        num = level.load_level(level.curr)
                        game_state = 0 
                        bird_path = []
                        score = 0 
                
                if game_state == 4 :
                    # buidling next level
                    if WIDTH//2 + 10 < pos[0] and pos[1] > 450 :
                        restart(space , birds , pigs , beams , columns)
                        game_state = 0 
                        num = level.load_level()
                        score = 0 
                        bird_path = []
                        bonus_score_query = True 

                    if WIDTH//2 - 100 < pos[0] < WIDTH//2 + 10 and pos[1] > 450 :
                        restart(space , birds , pigs , beams , columns)
                        game_state = 0 
                        num = level.load_level(level.curr)
                        score = 0 
                        bird_path = []                        

        if mouse_pressed and level.number_of_birds > 0 :
            angle = sling_action(rope_length)
        else :
            if time.time() * 1000 - t1 > 300 and level.number_of_birds > 0 :
                WIN.blit(REDBIRD , (130 , 426))

            else :
                pygame.draw.line(WIN , BLACK , (SLING_X , SLING_Y - 8) , (SLING2_X , SLING2_Y - 7) , 5)

        counter += 1

        pygame.display.update()
   
    score = 0 
    game_state = 0 
    bird_path = []
    counter = 0 
    restart_counter = False 
                
    main()

if __name__ == "__main__":
    main()