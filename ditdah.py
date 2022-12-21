#!usr/bin/env python3

# import necessary modules
import pygame, sys

pygame.init()

BLACK = (255, 255, 255)
WHITE = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
SURFACE_COLOR = (0, 0, 0)
COLOR = (255, 100, 98)


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
        self.image.fill(SURFACE_COLOR)
        self.image.set_colorkey(COLOR)
  
        pygame.draw.rect(self.image,color,pygame.Rect(0, 0, width, height))
  
        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels
 
    def moveLeft(self, pixels):
        self.rect.x -= pixels
 
    def moveForward(self, speed):
        self.rect.y += speed * speed/10
 
    def moveBack(self, speed):
        self.rect.y -= speed * speed/10

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
        pygame.draw.rect(screen, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))
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
    bomb_ = Sprite(GREEN, 15, 10)

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
            all_sprites_list.add(bomb_)
            bomb_.rect.x = plane_.rect.x + 20
            bomb_.rect.y = 110
        bomb_.moveForward(5)
        bomb_.moveLeft(5)
        if bomb_.rect.x < 0:
            bomb_.rect.x = width

        all_sprites_list.update()
        screen.fill(SURFACE_COLOR)
        all_sprites_list.draw(screen)
        pygame.display.flip()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
