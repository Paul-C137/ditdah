#!usr/bin/env python3

# import necessary modules
import pygame

pygame.init()

BLUE = (0, 0, 255)
BLACK = (255, 255, 255)
WHITE = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
SURFACE_COLOR = (0, 0, 0)

width = round(pygame.display.get_desktop_sizes()[0][0])
height = round(pygame.display.get_desktop_sizes()[0][1])
size = width, height
screen = pygame.display.set_mode(size)

all_sprites_list= pygame.sprite.Group()

pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

# Object class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
  
        self.image = pygame.Surface([width, height])
        #self.image.fill(SURFACE_COLOR)
  
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
  
        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels
 
    def moveLeft(self, pixels):
        self.rect.x -= pixels
 
    def moveForward(self, pixels):
        self.rect.y += pixels
 
    def moveBack(self, pixels):
        self.rect.y -= pixels


class Bomb(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
  
        self.image = pygame.Surface([width, height])
  
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
  
        self.rect = self.image.get_rect()

    def fall(self, xpixels, ypixels):
        self.rect.x -= xpixels
        self.rect.y += ypixels

    def update(self):
        self.rect.centery += 5
        if self.rect.y > 850:
            self.kill()

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        screen.fill(WHITE)
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("Dit Dah!", largeText)
        TextRect.center = ((width/2),(height/2))
        screen.blit(TextSurf, TextRect)

        button("Start", width/3-50, (height/3)*2, 100, 50, GREEN, RED, game_loop)
        button("Quit", (width/3)*2-50, (height/3)*2, 100, 50, RED, RED, quitgame)

        pygame.display.update()
        clock.tick(15)

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def quitgame():
    pygame.quit()
    quit()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x , y, w, h))
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))
    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)   

def game_loop():
    # create plane_ instance and give it a location
    plane_ = Sprite(RED, 20, 50)
    plane_.rect.x = width 
    plane_.rect.y = 100

    # create bomb_ instance of Sprite class
    a_bomb = Bomb(GREEN, 15, 10)

    all_sprites_list.add(plane_)

    exit = True
    clock = pygame.time.Clock()

    while exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = False

        plane_.moveLeft(5)
        if plane_.rect.x < 0:
            plane_.rect.x = width
        if plane_.rect.x < width/2 and plane_.rect.x > width/2-15:
            all_sprites_list.add(a_bomb)
            a_bomb.rect.x = plane_.rect.x + 20
            a_bomb.rect.y = 110
        a_bomb.fall(5, 1)
        if a_bomb.rect.x < 0:
            a_bomb.rect.x = width
        if 780 < a_bomb.rect.y < 795:
            explosion = Sprite(BLUE, 100,100)
            all_sprites_list.add(explosion)
            explosion.rect.x = a_bomb.rect.x - 75
            explosion.rect.y = height - 75
            explosion.update()

        all_sprites_list.update()
        screen.fill(SURFACE_COLOR)
        all_sprites_list.draw(screen)
        pygame.display.flip()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
