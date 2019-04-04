import sys
import pygame
import random
import time


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


def update_screen(ai_settings, stats, center_line, gameText,
                  chosen, avenger, stop, play_button, screen):
    if stats.game_active:
        length = 0

        if len(chosen) > len(avenger):
            length = len(avenger)
        else:
            length = len(chosen)

        #call = 0

        #call = random.randint(0, 1)

        print("pygame running the for loop in range(length) \n")
        while stop < length:
            print ("stop number: " + str(stop))
            screen.fill(ai_settings.bg_color)
            stime = pygame.time.get_ticks()
            if stime % 1000 == 0:
                gameText.prepLeftName(chosen[stop])
                gameText.prepRightName(str(avenger[stop]) + " stop number: " + str(stop))
                # if call:
                #     gameText.prepLeftName(chosen[i])
                #     gameText.prepRightName(str(avenger[i]) + " stop number: " + str(stop))
                # else:
                #     gameText.prepLeftName(avenger[i])
                #     gameText.prepRightName(str(chosen[i]) + " stop number: " + str(stop))
            gameText.draw_text()
            center_line.draw_center_line()
            stop += 1


            #time = pygame.time.get_ticks()
            #if time % 3500 == 0:
                #if call:
                    # add fall title under left name
                    # add avenger title under right name
                    # gray out the left name too?
                 #   pass
                #else:
                    # add fall title under right name
                    # add avenger title under left name
                    # gray out the right name too?
                   # pass


            # if stop == length-1:
            #     stats.game_active = False
                # Draw the play button if the game is inactive.
    if not stats.game_active:
        screen.fill(ai_settings.bg_color)
        play_button.draw_button()


    pygame.display.flip()

