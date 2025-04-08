import pygame
import time
import random

# Initial snake speed
snake_speed = 10

# Window size
window_x = 1000
window_y = 500

# Define colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
yellow = pygame.Color(255, 255, 0)

# Initialize pygame
pygame.init()

# Game window
pygame.display.set_caption('Snake Game with Levels & Timed Food')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS controller
fps = pygame.time.Clock()

# Snake starting position and body
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

# Function to generate random food (position and weight)
def generate_food():
    while True:
        pos = [random.randrange(1, (window_x // 10)) * 10,
               random.randrange(1, (window_y // 10)) * 10]
        if pos not in snake_body:
            weight = random.choice([10, 20, 30])  # Random weight (score points)
            return pos, weight

# Food setup
fruit_position, fruit_value = generate_food()
fruit_spawn = True
fruit_timer = time.time()  # Start timing the food

# Movement directions
direction = 'RIGHT'
change_to = direction

# Game variables
score = 0
level = 1

# Function to show score and level
def show_info():
    font = pygame.font.SysFont('times new roman', 25)
    text = font.render(f'Score: {score}  Level: {level}  Food: +{fruit_value}', True, yellow)
    game_window.blit(text, (10, 10))

# Game over screen
def game_over():
    font = pygame.font.SysFont('times new roman', 50)
    message = font.render(f'Game Over! Your Score: {score}', True, red)
    game_window.blit(message, (window_x // 4, window_y // 3))
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Main game loop
while True:
    # Handle key events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            if event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'

    # Update direction
    direction = change_to
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Update snake body
    snake_body.insert(0, list(snake_position))

    # Check if snake eats the food
    if snake_position == fruit_position:
        score += fruit_value
        fruit_spawn = False

        # Increase level every 30 points
        if score % 30 == 0:
            level += 1
            snake_speed += 2
    else:
        snake_body.pop()

    # Time check: If food exists too long, replace it
    if time.time() - fruit_timer > 10:
        fruit_spawn = False

    # Generate new food
    if not fruit_spawn:
        fruit_position, fruit_value = generate_food()
        fruit_timer = time.time()  # Reset food timer
    fruit_spawn = True

    # Fill background
    game_window.fill(black)

    # Draw the snake
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

    # Draw the food
    pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    # Check for wall collision
    if (snake_position[0] < 0 or snake_position[0] >= window_x or
        snake_position[1] < 0 or snake_position[1] >= window_y):
        game_over()

    # Check for self-collision
    if snake_position in snake_body[1:]:
        game_over()

    # Show score and level
    show_info()

    # Update the screen
    pygame.display.update()

    # Control speed
    fps.tick(snake_speed)