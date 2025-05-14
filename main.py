import pygame
import time
import random
import sys

pygame.init()

WIDTH, HEIGHT = 400, 400
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

font = pygame.font.SysFont('Arial', 36)

def draw_grid():
    """Отрисовка сетки (опционально)"""
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, (50, 50, 50), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, (50, 50, 50), (0, y), (WIDTH, y))

def game_over():
    """Вывод 'Game Over' и завершение игры"""
    text = font.render('GAME OVER', True, WHITE)
    screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2 - 18))
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    sys.exit()

def main():
    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
    direction = RIGHT
    food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != DOWN:
                    direction = UP
                elif event.key == pygame.K_DOWN and direction != UP:
                    direction = DOWN
                elif event.key == pygame.K_LEFT and direction != RIGHT:
                    direction = LEFT
                elif event.key == pygame.K_RIGHT and direction != LEFT:
                    direction = RIGHT

        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

        if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or
            new_head[1] < 0 or new_head[1] >= GRID_HEIGHT):
            game_over()

        if new_head in snake:
            game_over()

        snake.insert(0, new_head)

        if snake[0] == food:
            food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        else:
            snake.pop()

        screen.fill(BLACK)
        draw_grid()
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, RED, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        pygame.display.update()
        clock.tick(10)

if __name__ == "__main__":
    main()