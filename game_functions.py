import sys
import pygame


def check_events(ai_settings, screen):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, stats, center_line, play_button, screen):
    # Redraw the screen during each pass through the loop.

    # Draw the play button if the game is inactive.
    if not stats.game_active:
        screen.fill(ai_settings.bg_color)
        play_button.draw_button()
        center_line.draw_center_line()

    pygame.display.flip()

