import pygame
from snapAlgorithmMain import infinitySnap

from center_line import Center_Line

from settings import Settings
from game_stats import GameStats
from button import Button
from nameToJudge import NameToJudge

import game_functions as gf

chosen = []
avenger = []
infinitySnap(chosen, avenger)
def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Super Pong 64")

    start_game = False

    stats = GameStats(ai_settings)

    #participant names, the VS string and more
    gameText = NameToJudge(ai_settings, screen, "")

    #make the game objects
    center_line = Center_Line(ai_settings, screen)


    play_button = Button(ai_settings, screen, "Play")

    # Start the main loop for the game
    while True:
        gf.check_events(ai_settings, stats, play_button, screen)

        if stats.game_active:
            pass

        gf.update_screen(ai_settings, stats, center_line, gameText, play_button, screen)


run_game()