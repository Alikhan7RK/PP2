import pygame
import datetime
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1000,750))
pygame.display.set_caption("Clock")
clock = pygame.time.Clock()

clock_surface = pygame.image.load("C:/Users/uzzer/Downloads/clock.png")
left_hand_surface = pygame.image.load("C:/Users/uzzer/Downloads/righthand.png").convert_alpha()
left_hand_origin = (400, 300) 

right_hand_surface = pygame.image.load("C:/Users/uzzer/Downloads/lefthand.png").convert_alpha()
right_hand_origin = (400, 300)

def rotate(image, angle, center):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=center)
    return rotated_image, new_rect

while True:
    for event in pygame.event.get():
        if pygame.QUIT == event.type:
            pygame.quit()
            exit()

    now = datetime.datetime.now() + datetime.timedelta(minutes=9, seconds=-9)
    second_angle = -now.second * 6 
    minute_angle = -now.minute * 6 + 90 
    rotated_left_hand, left_hand_rect = rotate(left_hand_surface, second_angle, left_hand_origin)
    rotated_right_hand, right_hand_rect = rotate(right_hand_surface, minute_angle, right_hand_origin)

    screen.fill((255, 255, 255))
    screen.blit(clock_surface, (0, 0))
    screen.blit(rotated_left_hand, left_hand_rect)
    screen.blit(rotated_right_hand, right_hand_rect)
    
    pygame.display.update()
    clock.tick(60)