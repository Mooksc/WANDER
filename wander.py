import pygame
import random

pygame.init()

black = [0, 0, 0]
white = [255, 255, 255]
blue = [0, 0, 255]
red = [255, 0, 0]
green = [0,255,0]
grey = [105, 105, 105]

x_resolution = 1200
y_resolution = 800

mouse_pos = [0, 0]

game_display = pygame.display.set_mode((x_resolution, y_resolution))
pygame.display.set_caption('class testing')
pygame.display.set_icon(pygame.image.load('tomboy_sprite.jpg'))

tomboy_sprite = pygame.image.load('tomboy_sprite.jpg')
img_width = 128

font1 = "LBRITEDI.TTF"
font2 = "ALGER.TTF"
font3 = "BAUHS93.TTF"

clock = pygame.time.Clock()
clock.tick(60)

sq_movingBLOCKSPEED_x = 8
sq_movingBLOCKSPEED_y = 8
sq_movingBLOCKSPEED = 8

pressed = False
new_pressed = False

score = 0


def text_object(font, font_size, text, color, x_pos, y_pos):
    font_choice = pygame.font.Font(font, font_size)
    font = font_choice
    words = font.render(text, True, color)
    game_display.blit(words, [x_pos, y_pos])

class Player_sprite:

    sprite_x = 0
    sprite_y = 0

    def __init__(self, sprite_x, sprite_y, sprite_img):
        Player_sprite.sprite_x = sprite_x
        Player_sprite.sprite_y = sprite_y
        Player_sprite.sprite_img = sprite_img
      
    def place_sprite(self):
        game_display.blit(Player_sprite.sprite_img, (Player_sprite.sprite_x, Player_sprite.sprite_y))

class Draw_square:

    def __init__(self, sq_x, sq_y, sq_width, sq_height, sq_color):
        self.sq_x = sq_x
        self.sq_y = sq_y
        self.sq_width = sq_width
        self.sq_height = sq_height
        self.sq_color = sq_color
        self.sq_movingBLOCKSPEED_x = 8
        self.sq_movingBLOCKSPEED_y = 8
        self.sq_movingBLOCKSPEED = 8

    def square(self):

        rect_object = ((self.sq_x, self.sq_y), (self.sq_width, self.sq_height))

        game_display.fill(self.sq_color, rect_object)
    
    def moving_square(self, speed, new_pos, direction):

        global score

        rect_object = ((self.sq_x, self.sq_y), (self.sq_width, self.sq_height))

        game_display.fill(self.sq_color, rect_object)

        if direction is 'down':
            self.sq_y += self.sq_movingBLOCKSPEED * speed
            if self.sq_y > y_resolution:
                self.sq_x = new_pos
                self.sq_y = -200

            if Player_sprite.sprite_y < self.sq_y + 35:
                if Player_sprite.sprite_x + (img_width * .65) > self.sq_x > Player_sprite.sprite_x - (img_width * .25):
                    Player_sprite.sprite_x = x_resolution * .0001
                    Player_sprite.sprite_y = y_resolution * .845
                    score = 0
                    
        if direction is 'up':
            self.sq_y -= sq_movingBLOCKSPEED * speed
            if self.sq_y < -200:
                self.sq_x = new_pos
                self.sq_y = y_resolution

        if direction is 'left':
            self.sq_x += sq_movingBLOCKSPEED * speed
            if self.sq_x > x_resolution:
                self.sq_x = -200
                self.sq_y = new_pos

        if direction is 'right':
            self.sq_x -= sq_movingBLOCKSPEED * speed
            if self.sq_x < 0:
                self.sq_x = 1400
                self.sq_y = new_pos

    def bouncing_square(self, speed, tf, tf2):
       
        rect_object = ((self.sq_x, self.sq_y), (self.sq_width, self.sq_height))

        game_display.fill(self.sq_color, rect_object)
        
        if self.sq_x < x_resolution and self.sq_y < y_resolution:

            if tf is True:    
                self.sq_x += self.sq_movingBLOCKSPEED_x * speed
                self.sq_y += self.sq_movingBLOCKSPEED_y * speed
                if self.sq_x > x_resolution - 35:                    
                    self.sq_movingBLOCKSPEED_x = -8                   
                if self.sq_x < 0:                    
                    self.sq_movingBLOCKSPEED_x = 8                    
                if self.sq_y > y_resolution - 35:                    
                    self.sq_movingBLOCKSPEED_y = -8                    
                if self.sq_y < 0:
                    self.sq_movingBLOCKSPEED_y = 8                 
            else:
                self.sq_x -= self.sq_movingBLOCKSPEED_x * speed
                self.sq_y -= self.sq_movingBLOCKSPEED_y * speed
                if self.sq_x > x_resolution - 35:
                    self.sq_movingBLOCKSPEED_x = 8                   
                if self.sq_x < 0:
                    self.sq_movingBLOCKSPEED_x = -8                   
                if self.sq_y > y_resolution - 35:
                    self.sq_movingBLOCKSPEED_y = 8                    
                if self.sq_y < 0:
                    self.sq_movingBLOCKSPEED_y = -8

class Draw_button(Draw_square):

    def button(self, inactive_color, active_color, pressed_color):
        mouse_press = pygame.mouse.get_pressed()

        global new_pressed

        if self.sq_x + self.sq_width > mouse_pos[0] > self.sq_x and self.sq_y + self.sq_height > mouse_pos[1] > self.sq_y:
            inactive_color = active_color
            new_pressed = False
            if mouse_press == (1,0,0):
                inactive_color = pressed_color
                new_pressed = True
        else:
            inactive_color = inactive_color
            new_pressed = False

        rect_object = ((self.sq_x, self.sq_y), (self.sq_width, self.sq_height))
        game_display.fill(inactive_color, rect_object)

    def text_button(self, inactive_color, active_color, pressed_color, text, text_color, font_select, font_size, mov_x, mov_y):
        mouse_press = pygame.mouse.get_pressed()

        global pressed

        font_choice = pygame.font.Font(font_select, font_size)
        font = font_choice
        words = font.render(text, True, text_color)

        if self.sq_x + self.sq_width > mouse_pos[0] > self.sq_x and self.sq_y + self.sq_height > mouse_pos[1] > self.sq_y:
            inactive_color = active_color
            if mouse_press == (1, 0, 0):
                inactive_color = pressed_color
                pressed = True
            else:
                pressed = False

        else:
            inactive_color = inactive_color
            pressed = False

        rect_object = ((self.sq_x, self.sq_y), (self.sq_width, self.sq_height))
        game_display.fill(inactive_color, rect_object)
        game_display.blit(words, [self.sq_x + mov_x, self.sq_y + mov_y])


def intro_loop():

    while True:
        
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                quit()
            if event.type is pygame.KEYDOWN:
                if event.key is pygame.K_q:
                    quit()
                if event.key is pygame.K_RETURN:
                    game_loop_func()

        game_display.fill(black)
        text_object(font1, 75, 'WANDER', white, x_resolution/2.7, y_resolution/2.4)
        text_object(font1, 25, 'Press \"Enter\" to begin', white, x_resolution * .075, y_resolution * .95)
        text_object(font1, 25, 'Press \"Q\" to exit', white, x_resolution * .75, y_resolution * .95)
        pygame.display.flip()


def pause_loop():

    paused = True

    while paused is True:

        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                quit()
            if event.type is pygame.KEYDOWN:
                if event.key is pygame.K_q:
                    intro_loop()
                if event.key is pygame.K_p:
                    paused = False

        game_display.fill(black)
        text_object(font1, 75, 'PAUSED', white, x_resolution/2.7, y_resolution/2.4)
        text_object(font1, 25, 'Press \"P\" to resume', white, x_resolution * .4, y_resolution * .6)
        text_object(font1, 25, 'Press \"Q\" to return to the Start Screen', white, x_resolution * .6, y_resolution * .01)
        pygame.display.flip()


def game_loop_func():

    global mouse_pos
    global score

    random_int0 = random.randrange(1, 255)

    player_sprite_x_change = 0
    player_sprite_y_change = 0

    game_sequence = True
    help_sequence = True
    exit_text = False
    
    quit_event = pygame.USEREVENT + 1
    pygame.time.set_timer(quit_event, 750)

    b_square0 = Draw_square(random.randrange(img_width + 50, x_resolution), 0, 35, 35, (random.randrange(1,255), random.randrange(1,255), random.randrange(1,255)))
    b_square1 = Draw_square(random.randrange(img_width + 50, x_resolution), 0, 35, 35, (random.randrange(1,255), random.randrange(1,255), random.randrange(1,255)))
    b_square2 = Draw_square(random.randrange(img_width + 50, x_resolution), 0, 35, 35, (random.randrange(1,255), random.randrange(1,255), random.randrange(1,255)))
    b_square3 = Draw_square(random.randrange(img_width + 50, x_resolution), 0, 35, 35, (random.randrange(1,255), random.randrange(1,255), random.randrange(1,255)))
    b_square4 = Draw_square(random.randrange(img_width + 50, x_resolution), 0, 35, 35, (random.randrange(1,255), random.randrange(1,255), random.randrange(1,255)))

    b_button0 = Draw_button(x_resolution/2, y_resolution/2, 50, 50, white)

    player_sprite = Player_sprite(x_resolution * 0, y_resolution * .845, tomboy_sprite)

    while game_sequence is True:

        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                quit()

            if event.type is pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()

            if event.type is pygame.KEYDOWN:
                if event.key is pygame.K_d:
                    player_sprite_x_change = 5
                if event.key is pygame.K_a:
                    if player_sprite.sprite_x > img_width * -.5:
                        player_sprite_x_change = -5
                if event.key is pygame.K_SPACE:
                    if Player_sprite.sprite_y > y_resolution - (img_width - 1):
                        player_sprite_y_change = -125
                if event.key is pygame.K_r:
                    Player_sprite.sprite_x = x_resolution * 0
                    Player_sprite.sprite_y = y_resolution * .845
                    score = 0
                if event.key is pygame.K_h:
                    if help_sequence is True:
                        help_sequence = False
                    else:
                        help_sequence = True
                if event.key is pygame.K_p:                                                               
                    pause_loop()
                if event.key is pygame.K_q:
                    exit_text = True
                    score = 0
            if exit_text is True:
                if event.type is quit_event:
                    game_sequence = False

            if event.type is pygame.KEYUP:
                if event.key is pygame.K_d:
                    player_sprite_x_change = 0
                if event.key is pygame.K_a:
                    player_sprite_x_change = 0

        Player_sprite.sprite_x += player_sprite_x_change
        Player_sprite.sprite_y += player_sprite_y_change

        if Player_sprite.sprite_y < y_resolution:
            player_sprite_y_change = 5
        if Player_sprite.sprite_y > y_resolution - (img_width - 1) or Player_sprite.sprite_y < 0:
            player_sprite_y_change = 0
        if Player_sprite.sprite_x < img_width * -.5:
            player_sprite_x_change = 0
        if Player_sprite.sprite_x > x_resolution - (img_width * .5):
            Player_sprite.sprite_x = x_resolution * -.03
            Player_sprite.sprite_y = (y_resolution * .845)
            score += 1

            if score > 0:
                help_sequence = False
            if score >= random.randrange(5,9):
                random_int0 = random.randrange(1, 255)
            if score >= 9:
                random_int1 = random.randrange(1, 255)
                random_int2 = random.randrange(1, 255)
                random_int3 = random.randrange(1, 255)

        game_display.fill(black)

        b_button0.button(green, red, grey)

        rain_square = Draw_square(random.randrange(1, x_resolution), random.randrange(1, y_resolution), 10, 15, grey)
        rain_square.square()
        if score >= 0:
            b_square0.moving_square(1, random.randrange(img_width + 50, x_resolution), 'down')
            if b_square0.sq_y == -200 or 0:
                b_square0.sq_color = (random.randrange(1,255), random.randrange(1,255), random.randrange(1,255))
        if score >= 3:
            b_square1.moving_square(1.15, random.randrange(img_width + 50, x_resolution), 'down')
            if b_square1.sq_y == -200:
                b_square1.sq_color = (random.randrange(1,255), random.randrange(1,255), random.randrange(1,255))
        if score >= 5:
            b_square2.moving_square(1.35, random.randrange(img_width + 50, x_resolution), 'down')
            if b_square2.sq_y == -200:
                b_square2.sq_color = (random.randrange(1,255), random.randrange(1,255), random.randrange(1,255))
        if score >= 7:
            b_square3.moving_square(1.55, random.randrange(img_width + 50, x_resolution), 'down')
            if b_square3.sq_y == -200:
                b_square3.sq_color = (random.randrange(1,255), random.randrange(1,255), random.randrange(1,255))
        if score >= 10:
            b_square4.moving_square(1.75, random.randrange(img_width + 50, x_resolution), 'down')
            if b_square4.sq_y == -200:
                b_square4.sq_color = (random.randrange(1,255), random.randrange(1,255), random.randrange(1,255))

        player_sprite.place_sprite()

        text_object(font3, int(float(x_resolution * .02)), str(score), green, x_resolution *.98, y_resolution/80)
        text_object(font3, int(float(x_resolution * .02)), 'Press \"Q\" to EXIT', red, x_resolution/50, y_resolution/75)
        if help_sequence is True:
            text_object(font3, int(float(x_resolution * .02)), 'Use \"A\" and \"D\" to move!', white, x_resolution/35, y_resolution/10)    
            text_object(font3, int(float(x_resolution * .02)), 'Press \"SPACE\" to jump!', white, x_resolution/35, y_resolution/7.5)
            text_object(font3, int(float(x_resolution * .017)), 'Use \"R\" to return to the start', white, x_resolution/35, y_resolution/6)
            text_object(font3, int(float(x_resolution * .017)), 'Use \"P\" to pause the game!', white, x_resolution/35, y_resolution/4.5)
            text_object(font3, int(float(x_resolution * .017)), 'BEWARE!', red, x_resolution/35, y_resolution/5.2)
            text_object(font3, int(float(x_resolution * .017)), 'Score will reset as well!', green, x_resolution/10, y_resolution/5.2)
        if Player_sprite.sprite_x < x_resolution/3 and score == 0:
            text_object(font3, int(float(x_resolution * .025)), 'Why is it always raining...', blue, x_resolution/20, y_resolution * .75)
        if exit_text is True:
            text_object(font3, int(float(x_resolution * .02)), 'Exiting...', red, x_resolution/50, y_resolution/25)
        if score < 2:
            text_object(font3, int(float(x_resolution * .018)), 'Press \"H\" to view controls', white, x_resolution/2, y_resolution/75)
        if player_sprite.sprite_x < x_resolution * -.05:
            text_object(font3, int(float(x_resolution * .02)), 'You can\'t escape...', red, x_resolution/75, y_resolution/4)
        if 10 > score >= 5:
            text_object(font3, int(float(x_resolution * .03)), 'Why are you still here...', [random_int0, 0, 0], x_resolution*.3, y_resolution/2)
        if score >= 10:
            text_object(font3, int(float(x_resolution * .04)), 'I WANT TO BE ALONE', [random_int1, random_int2, random_int3], x_resolution*.3, y_resolution/2)

        if new_pressed is True:
            b_square0.sq_movingBLOCKSPEED = 0
            b_square1.sq_movingBLOCKSPEED = 0
            b_square2.sq_movingBLOCKSPEED = 0
            b_square3.sq_movingBLOCKSPEED = 0
            b_square4.sq_movingBLOCKSPEED = 0
        else:
            b_square0.sq_movingBLOCKSPEED = 8
            b_square1.sq_movingBLOCKSPEED = 8
            b_square2.sq_movingBLOCKSPEED = 8
            b_square3.sq_movingBLOCKSPEED = 8
            b_square4.sq_movingBLOCKSPEED = 8

        clock.tick(60)
        pygame.display.flip()

intro_loop()
