import pygame
from board import boards
import math
import random

pygame.init()

WIDTH = 900
HEIGHT = 950
screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
pygame.display.set_caption("Pacman")
fps = 60
color = 'blue'
PI = math.pi
font = pygame.font.Font('freesansbold.ttf', 20)
level = boards
counter = 0
flicker = False

player_images = []
for i in range(1, 5):
    player_images.append(pygame.transform.scale(pygame.image.load(f'player_images/{i}.png'), (45, 45)))

class Orange_ghost:
    def __init__(self):
        num1 = ((HEIGHT - 50) // 32)
        num2 = (WIDTH // 30)
        self.image = pygame.image.load('ghost_images/orange.png' )
        self.image = pygame.transform.scale(self.image, (45, 45))

        while True:
            self.x = random.randint(0, 29)  
            self.y = random.randint(0, 31)  
            
            if level[self.y][self.x] == 1 or level[self.y][self.x] == 2:
                self.x = self.x * num2 + (0.5 * num2) - 22
                self.y = self.y * num1 + (0.5 * num1) - 22
                break

    def draw_ghost(self):
        screen.blit(self.image, (self.x, self.y))

class Player:
    def __init__(self):
        num1 = ((HEIGHT - 50) // 32)
        num2 = (WIDTH // 30)
        
        while True:
            self.x = random.randint(0, 29)  
            self.y = random.randint(0, 31)  
            
            if level[self.y][self.x] == 1 or level[self.y][self.x] == 2:
                self.x = self.x * num2 + (0.5 * num2) - 22
                self.y = self.y * num1 + (0.5 * num1) - 22
                break

    def draw_player(self):
        screen.blit(player_images[counter // 5], (self.x, self.y))

player = Player()
orange = Orange_ghost()

    

def draw_board():
    num1 = ((HEIGHT - 50) // 32)
    num2 = (WIDTH // 30)
    for i in range(len(level)): 
        for j in range(len(level[i])):
            # if level[i][j] == 1:
            #     pygame.draw.circle(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 4)
            # if level[i][j] == 2 and not flicker:
            #     pygame.draw.circle(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 10)
            if level[i][j] == 3:
                pygame.draw.line(screen, color, (j * num2 + (0.5 * num2), i * num1),
                                 (j * num2 + (0.5 * num2), i * num1 + num1), 3)
            if level[i][j] == 4:
                pygame.draw.line(screen, color, (j * num2, i * num1 + (0.5 * num1)),
                                 (j * num2 + num2, i * num1 + (0.5 * num1)), 3)
            if level[i][j] == 5:
                pygame.draw.arc(screen, color, [(j * num2 - (num2 * 0.4)) - 2, (i * num1 + (0.5 * num1)), num2, num1],
                                0, PI / 2, 3)
            if level[i][j] == 6:
                pygame.draw.arc(screen, color,
                                [(j * num2 + (num2 * 0.5)), (i * num1 + (0.5 * num1)), num2, num1], PI / 2, PI, 3)
            if level[i][j] == 7:
                pygame.draw.arc(screen, color, [(j * num2 + (num2 * 0.5)), (i * num1 - (0.4 * num1)), num2, num1], PI,
                                3 * PI / 2, 3)
            if level[i][j] == 8:
                pygame.draw.arc(screen, color,
                                [(j * num2 - (num2 * 0.4)) - 2, (i * num1 - (0.4 * num1)), num2, num1], 3 * PI / 2,
                                2 * PI, 3)
            if level[i][j] == 9:
                pygame.draw.line(screen, 'white', (j * num2, i * num1 + (0.5 * num1)),
                                 (j * num2 + num2, i * num1 + (0.5 * num1)), 3)

run = True
while run:
    timer.tick(fps)
    if counter < 19:
        counter += 1
        if counter > 3:
            flicker = False
    else:
        counter = 0
        flicker = True
    screen.fill('black')    
    draw_board()
    player.draw_player()
    orange.draw_ghost()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()
pygame.quit() 