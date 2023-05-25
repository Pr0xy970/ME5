import pygame
import random
import sys

# 游戏初始化
pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

# 定义颜色
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 定义方向
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# 贪吃蛇类
class Snake:
    def __init__(self):
        self.body = [(200, 200), (200, 210), (200, 220)]
        self.direction = UP

    def move(self):
        head = self.body[0]
        x = head[0] + self.direction[0] * 10
        y = head[1] + self.direction[1] * 10
        self.body.insert(0, (x, y))
        self.body.pop()

    def change_direction(self, direction):
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], 10, 10))

    def check_collision(self):
        head = self.body[0]
        if (
            head[0] < 0
            or head[0] >= 400
            or head[1] < 0
            or head[1] >= 400
            or head in self.body[1:]
        ):
            return True
        return False

    def check_eat_food(self, food):
        if self.body[0] == food.position:
            self.body.append((0, 0))
            food.generate_position()

# 食物类
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.generate_position()

    def generate_position(self):
        x = random.randint(0, 39) * 10
        y = random.randint(0, 39) * 10
        self.position = (x, y)

    def draw(self):
        pygame.draw.rect(screen, RED, (self.position[0], self.position[1], 10, 10))

# 主循环
running = True
snake = Snake()
food = Food()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction(UP)
            elif event.key == pygame.K_DOWN:
                snake.change_direction(DOWN)
            elif event.key == pygame.K_LEFT:
                snake.change_direction(LEFT)
            elif event.key == pygame.K_RIGHT:
                snake.change_direction(RIGHT)

    snake.move()
    snake.check_eat_food(food)
    if snake.check_collision():
        running = False

    screen.fill(BLACK)
    snake.draw()
    food.draw()
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
sys.exit()
