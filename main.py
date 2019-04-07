import pygame
from snapAlgorithmMain import infinitySnap

from center_line import Center_Line

from settings import Settings
from game_stats import GameStats
from button import Button
from nameToJudge import NameToJudge

import game_functions as gf
clock = pygame.time.Clock()
chosen = []
avenger = []
newChosen = []
newAvenger = []
popCounter = 0
chosenLong = 0
length = 0

infinitySnap(chosen, avenger)
if len(chosen) > len(avenger):
    length = len(avenger)
    chosenLong = 1
else:
    length = len(chosen)
    avengerLong = 1

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Avenger's: EndGame")

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

        gf.update_screen(ai_settings, stats, center_line, gameText,
                  chosen, avenger, newChosen, newAvenger, popCounter, clock,
                  play_button, screen)


run_game()