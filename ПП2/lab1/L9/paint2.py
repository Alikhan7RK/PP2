import pygame

pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Drawing Program")
screen.fill(WHITE)

# Tool constants
DRAW_RECT = 1
DRAW_CIRCLE = 2
ERASER = 3
DRAW_SQUARE = 4
DRAW_RIGHT_TRIANGLE = 5
DRAW_EQ_TRIANGLE = 6
DRAW_RHOMBUS = 7

# Current settings
current_tool = DRAW_RECT
color = BLACK
drawing = False
start_pos = None

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Choose tools and colors
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                current_tool = DRAW_RECT
            elif event.key == pygame.K_c:
                current_tool = DRAW_CIRCLE
            elif event.key == pygame.K_e:
                current_tool = ERASER
            elif event.key == pygame.K_s:
                current_tool = DRAW_SQUARE
            elif event.key == pygame.K_t:
                current_tool = DRAW_RIGHT_TRIANGLE
            elif event.key == pygame.K_y:
                current_tool = DRAW_EQ_TRIANGLE
            elif event.key == pygame.K_h:
                current_tool = DRAW_RHOMBUS

            # Color selection
            elif event.key == pygame.K_1:
                color = BLACK
            elif event.key == pygame.K_2:
                color = RED
            elif event.key == pygame.K_3:
                color = GREEN
            elif event.key == pygame.K_4:
                color = BLUE

        # Start drawing
        elif event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos
            drawing = True

        # Finish drawing
        elif event.type == pygame.MOUSEBUTTONUP:
            if drawing:
                end_pos = event.pos
                x1, y1 = start_pos
                x2, y2 = end_pos

                # Rectangle
                if current_tool == DRAW_RECT:
                    rect = pygame.Rect(start_pos, (x2 - x1, y2 - y1))
                    pygame.draw.rect(screen, color, rect, 2)

                # Circle
                elif current_tool == DRAW_CIRCLE:
                    radius = int(((x2 - x1)**2 + (y2 - y1)**2)**0.5)
                    pygame.draw.circle(screen, color, start_pos, radius, 2)

                # Eraser (dot)
                elif current_tool == ERASER:
                    pygame.draw.circle(screen, WHITE, end_pos, 10)

                # Square
                elif current_tool == DRAW_SQUARE:
                    side = min(abs(x2 - x1), abs(y2 - y1))
                    rect = pygame.Rect(x1, y1, side, side)
                    pygame.draw.rect(screen, color, rect, 2)

                # Right triangle
                elif current_tool == DRAW_RIGHT_TRIANGLE:
                    points = [(x1, y1), (x2, y2), (x1, y2)]
                    pygame.draw.polygon(screen, color, points, 2)

                # Equilateral triangle
                elif current_tool == DRAW_EQ_TRIANGLE:
                    side = abs(x2 - x1)
                    height = (3 ** 0.5 / 2) * side
                    points = [
                        (x1, y1),
                        (x1 - side // 2, y1 + height),
                        (x1 + side // 2, y1 + height)
                    ]
                    pygame.draw.polygon(screen, color, points, 2)

                # Rhombus
                elif current_tool == DRAW_RHOMBUS:
                    dx = abs(x2 - x1)
                    dy = abs(y2 - y1)
                    center_x = (x1 + x2) // 2
                    center_y = (y1 + y2) // 2
                    points = [
                        (center_x, y1),        # top
                        (x2, center_y),        # right
                        (center_x, y2),        # bottom
                        (x1, center_y)         # left
                    ]
                    pygame.draw.polygon(screen, color, points, 2)

                drawing = False

        # Eraser drag
        elif event.type == pygame.MOUSEMOTION and drawing and current_tool == ERASER:
            pygame.draw.circle(screen, WHITE, event.pos, 10)

    pygame.display.flip()

pygame.quit()