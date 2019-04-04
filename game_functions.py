import sys
import pygame


def check_events(ai_settings, stats, play_button, screen):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, mouse_x,
                              mouse_y)

def check_play_button(ai_settings, screen, stats, play_button, mouse_x,
                              mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        pygame.mouse.set_visible(False)
        stats.game_active = True


def update_screen(ai_settings, stats, center_line, gameText, play_button, screen):
    # Redraw the screen during each pass through the loop.

    screen.fill(ai_settings.bg_color)
    gameText.draw_text()
    center_line.draw_center_line()


    # Draw the play button if the game is inactive.
    if not stats.game_active:
        screen.fill(ai_settings.bg_color)
        play_button.draw_button()


    pygame.display.flip()

