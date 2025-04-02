import pygame
import time
import random

# Initial snake speed
snake_speed = 10

# Window size
window_x = 1000
window_y = 500

# Defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialize pygame
pygame.init()

# Set game window
pygame.display.set_caption('Snake Game with Levels')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS controller
fps = pygame.time.Clock()

# Snake initial position
snake_position = [100, 50]

# Initial snake body
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

# Generate food position ensuring it doesn't spawn on the snake

def generate_food():
    while True:
        food = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
        if food not in snake_body:
            return food

fruit_position = generate_food()
fruit_spawn = True

# Default direction of movement
direction = 'RIGHT'
change_to = direction

# Initial score and level
score = 0
level = 1

# Display score and level
def show_info():
    font = pygame.font.SysFont('times new roman', 25)
    score_surface = font.render(f'Score: {score}  Level: {level}', True, blue)
    game_window.blit(score_surface, (10, 10))

# Game over function
def game_over():
    font = pygame.font.SysFont('times new roman', 50)
    message = font.render(f'Game Over! Your Score: {score}', True, red)
    game_window.blit(message, (window_x//4, window_y//3))
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            if event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'

    # Move in the changed direction
    direction = change_to
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Snake body growing
    snake_body.insert(0, list(snake_position))
    if snake_position == fruit_position:
        score += 10
        fruit_spawn = False
        
        # Increase level every 30 points
        if score % 30 == 0:
            level += 1
            snake_speed += 2  # Increase speed
    else:
        snake_body.pop()

    # Generate new food if needed
    if not fruit_spawn:
        fruit_position = generate_food()
    fruit_spawn = True

    # Fill background and draw snake & food
    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    # Check for collisions with walls
    if snake_position[0] < 0 or snake_position[0] >= window_x or snake_position[1] < 0 or snake_position[1] >= window_y:
        game_over()
    
    # Check for collisions with itself
    if snake_position in snake_body[1:]:
        game_over()
    
    # Display score and level
    show_info()

    # Update screen
    pygame.display.update()

    # Control game speed
    fps.tick(snake_speed)