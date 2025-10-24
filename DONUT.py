import pygame
import math


pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

WIDTH = 1920
HEIGHT = 1080

x_start, y_start = 0, 0

x_seperator =10
y_seperator = 20

rows = HEIGHT // y_seperator
collums = WIDTH // x_seperator
screen_size = rows * collums

x_offset = collums / 2
y_offset = rows / 2

A,B = 0,0 # rotating animation

theta_spacing = 10
phi_spacing = 1

chars = ".,-~:;=!*#$@" #Lumanance Index

screen = pygame.display.set_mode((WIDTH, HEIGHT))

display_surface = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Donut")
font = pygame.font.SysFont ("Arial", 18, bold=True) 


def text_display(letter, x_start, y_start):
    text = font.render(str(letter), True, white)
    display_surface.blit(text, (x_start, y_start))




run = True
while run:
    
    screen.fill(black)

    z = [0] * screen_size #Donut. Fills donut space
    b = [" "] * screen_size # Background. fills empty space

    for j in range(0, 628, theta_spacing):
        for i in range(0, 628, phi_spacing):
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(A)
            f = math.sin(j)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            I = math.cos(i)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e 
            x = int(x_offset + 40 * D * (I * h * m - t * n)) # 3D  x cordinate after rotation
            y = int(y_offset + 20 * D * (I * h * n + t * m)) # 3D y cordinate after rotation
            o = int(x + collums * y) # 3D z cordinate after rotation
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - I * d * n)) # Lumanance Index
            if 0 <= o < screen_size and rows > y > 0 and 0 < x < collums and D > z[o]:
                z[o]= D
                b[o] = chars[N if N > 0 else 0]
        

        if y_start == rows * y_seperator - y_seperator:
           y_start = 0

 
    for i in range(len(b)):
        A+=0.000002
        B+=0.000001
        if i == 0 or i % collums:
            text_display(b[i], x_start, y_start)
            x_start += x_seperator
        else:
            y_start += y_seperator
            x_start = 0
            text_display(b[i], x_start, y_start)
            x_start += x_seperator

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False