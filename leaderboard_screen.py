import pygame
import csv
import sys

# Initialize pygame
pygame.init()

# Set up the window
window_width = 640
window_height = 480
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Leaderboard')

# Set up the colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up the font
font = pygame.font.Font(None, 28)

# Load leaderboard data from CSV file
def load_leaderboard():
    leaderboard_data = []
    with open('leaderboard.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        for row in reader:
            leaderboard_data.append(row)
    return leaderboard_data

# Function to display the leaderboard screen
def leaderboard_screen():
    leaderboard_data = load_leaderboard()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_leaderboard(leaderboard_data)
        pygame.display.update()

# Function to draw the leaderboard
def draw_leaderboard(leaderboard_data):
    window.fill(black)

    # Render the table headers
    rank_header = font.render('Rank', True, white)
    username_header = font.render('Username', True, white)
    class_header = font.render('Class', True, white)
    score_header = font.render('Score', True, white)

    # Display the table headers on the screen
    window.blit(rank_header, (40, 50))
    window.blit(username_header, (180, 50))
    window.blit(class_header, (300, 50))
    window.blit(score_header, (500, 50))

    # Render and display the leaderboard data
    y = 100
    for row in leaderboard_data:
        rank = font.render(row[0], True, white)
        username = font.render(row[1], True, white)
        class_name = font.render(row[2], True, white)
        score = font.render(row[3], True, white)

        window.blit(rank, (40, y))
        window.blit(username, (180, y))
        window.blit(class_name, (300, y))
        window.blit(score, (500, y))

        y += 30

# Call the function to display the leaderboard screen
def leader():
    leaderboard_screen()
