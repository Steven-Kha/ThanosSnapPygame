import pygame
from pygame.sprite import Group
from settings import Settings
from center_line import Center_Line
from game_stats import GameStats
import game_functions as gf
from button import Button

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    stats = GameStats(ai_settings)

    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Super Pong 64")

    start_game = False

    center_line = Center_Line(ai_settings, screen)

    play_button = Button(ai_settings, screen, "Play")

    # Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen)

        gf.update_screen(ai_settings, stats, center_line, play_button, screen)


run_game()