import pygame
from pygame.locals import *
import game
import leaderboard_screen
import sys
from subprocess import call

import leaderboard_screen

# Initialize pygame
pygame.init()

# Set up the window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game')

# Set up the colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up the font
font = pygame.font.Font(None, 32)

# Function to display the main screen
def main_screen():
    username = ''
    class_name = ''
    username_input_active = False
    class_input_active = False

    cursor_blink_timer = 0
    cursor_visible = True

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    if username_input_active and len(username) > 0:
                        username = username[:-1]
                    elif class_input_active and len(class_name) > 0:
                        class_name = class_name[:-1]
                elif event.key == K_TAB:
                    if username_input_active and len(username) > 0:
                        username += '\t'
                    elif class_input_active and len(class_name) > 0:
                        class_name += '\t'
                elif event.key == K_RETURN:
                    if len(username) > 0:
                        return username, class_name
                else:
                    if username_input_active:
                        username += event.unicode
                    elif class_input_active:
                        class_name += event.unicode
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    username_input_active = pygame.Rect(window_width // 2 + 5, window_height // 2 - 95, 200, 30).collidepoint(event.pos)
                    class_input_active = pygame.Rect(window_width // 2 + 5, window_height // 2 + 5, 200, 30).collidepoint(event.pos)
                    start_button = pygame.Rect(window_width // 2 - 75, window_height // 2 + 150, 150, 50)
                    if start_button.collidepoint(event.pos):
                        start_game()
                else:
                    username_input_active = False
                    class_input_active = False

        draw_main_screen(username, class_name, username_input_active, class_input_active, cursor_visible)

        # Toggle cursor visibility every 0.5 seconds
        cursor_blink_timer += 1
        if cursor_blink_timer >= 700:
            cursor_visible = not cursor_visible
            cursor_blink_timer = 0

# Function to draw the main screen
def draw_main_screen(username, class_name, username_input_active, class_input_active, cursor_visible):
    window.fill(black)

    # Render the text
    username_text = font.render('Username:', True, white)
    class_text = font.render('Class:', True, white)
    username_input = font.render(username, True, white)
    class_input = font.render(class_name, True, white)
    prompt_text = font.render('Press Enter to Start', True, white)

    # Display the text on the screen
    window.blit(username_text, (window_width // 2 - 100, window_height // 2 - 100))
    window.blit(class_text, (window_width // 2 - 100, window_height // 2))
    pygame.draw.rect(window, white, (window_width // 2 + 100, window_height // 2 - 100, 200, 30), 2)
    pygame.draw.rect(window, white, (window_width // 2 + 100, window_height // 2 + 5, 200, 30), 2)
    window.blit(username_input, (window_width // 2 + 105, window_height // 2 - 95))
    window.blit(class_input, (window_width // 2 + 105, window_height // 2 + 5))
    window.blit(prompt_text, (window_width // 2 - 150, window_height // 2 + 100))

    # Draw the cursor in the active input box
    if username_input_active and cursor_visible:
        cursor_pos_x = window_width // 2 + 105 + username_input.get_width()
        pygame.draw.line(window, white, (cursor_pos_x, window_height // 2 - 95), (cursor_pos_x, window_height // 2 - 75), 2)
    elif class_input_active and cursor_visible:
        cursor_pos_x = window_width // 2 + 105 + class_input.get_width()
        pygame.draw.line(window, white, (cursor_pos_x, window_height // 2 + 5), (cursor_pos_x, window_height // 2 + 30), 2)

    # Draw the start game button
    start_button = pygame.Rect(window_width // 2 - 75, window_height // 2 + 150, 150, 50)
    pygame.draw.rect(window, white, start_button)
    start_text = font.render('Start Game', True, black)
    window.blit(start_text, (window_width // 2 - 60, window_height // 2 + 165))

    pygame.display.update()

# Function to start the game
def start_game():
    game.game_loop()

# Example usage
username, class_name = main_screen()
print('Username:', username)
print('Class:', class_name)