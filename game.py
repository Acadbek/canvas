import curses
import random
import time

stdscr = curses.initscr()
curses.curs_set(0)  # Hide the cursor
sh, sw = stdscr.getmaxyx()  # Get the screen dimensions

snake = [[sh//2, sw//2 + i] for i in range(-1, 2)]
food = [sh//4, sw//4]

def move_snake(key):
    head = snake[0]
    new_head = [head[0], head[1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    elif key == curses.KEY_UP:
        new_head[0] -= 1
    elif key == curses.KEY_LEFT:
        new_head[1] -= 1
    elif key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)
    if snake[0] == food:
        food[0] = random.randint(1, sh-2)
        food[1] = random.randint(1, sw-2)
    else:
        snake.pop()

def check_collision():
    if (
        snake[0][0] in [0, sh-1] or
        snake[0][1] in [0, sw-1] or
        snake[0] in snake[1:]
    ):
        return True
    return False

def draw():
    stdscr.clear()
    stdscr.addch(food[0], food[1], curses.ACS_PI)
    for i, (y, x) in enumerate(snake):
        if i == 0:
            stdscr.addch(y, x, curses.ACS_CKBOARD)
        else:
            stdscr.addch(y, x, curses.ACS_BLOCK)
    stdscr.refresh()

def main(stdscr):
    stdscr.timeout(100)
    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break

        move_snake(key)
        if check_collision():
            break

        draw()
        time.sleep(0.1)

curses.wrapper(main)
