import os
import random
import msvcrt
import time

# Define constants
WIDTH = 20
HEIGHT = 10
SNAKE_HEAD = '@'
SNAKE_BODY = 'o'
FOOD = '*'
EMPTY = ' '

# Define game state variables
snake = [(HEIGHT // 2, WIDTH // 2)]
food = (random.randint(0, HEIGHT - 1), random.randint(0, WIDTH - 1))
direction = (0, 1)
score = 0

# Function to print the game board
def print_board():
    os.system('cls' if os.name == 'nt' else 'clear')
    board = [[EMPTY] * WIDTH for _ in range(HEIGHT)]
    for y, x in snake:
        board[y][x] = SNAKE_BODY
    board[snake[0][0]][snake[0][1]] = SNAKE_HEAD
    board[food[0]][food[1]] = FOOD

    for row in board:
        print(''.join(row))

# Function to handle user input
def get_key():
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key in [b'w', b'a', b's', b'd']:
                return key

# Function to move the snake
def move_snake():
    global snake, direction, score
    y, x = snake[0]
    dy, dx = direction
    new_head = (y + dy, x + dx)
    if (
        new_head in snake or
        new_head[0] < 0 or new_head[0] >= HEIGHT or
        new_head[1] < 0 or new_head[1] >= WIDTH
    ):
        print("Game Over!")
        print("Your Score:", score)
        exit()
    snake.insert(0, new_head)
    if new_head == food:
        score += 1
        food = (random.randint(0, HEIGHT - 1), random.randint(0, WIDTH - 1))
    else:
        snake.pop()

# Main game loop
while True:
    print_board()
    key = get_key()
    if key == b'w':
        direction = (-1, 0)
    elif key == b'a':
        direction = (0, -1)
    elif key == b's':
        direction = (1, 0)
    elif key == b'd':
        direction = (0, 1)
    move_snake()
    time.sleep(0.2)
