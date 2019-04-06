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
                  chosen, avenger, newChosen, newAvenger, popCounter, length,
                  play_button, screen):
    # if stats.game_active:
    if len(chosen) > len(avenger):
        length = len(avenger)
        chosenLong = 1
    else:
        length = len(chosen)
        avengerLong = 1

    screen.fill(ai_settings.bg_color)
    leftName = ""
    rightName = ""


    #print("am I running again?")
    for i in range(length):
        print(i)
        sTime = pygame.time.get_ticks()
        if sTime % 2 == 0:
            #pop names so they don't appear again
            leftName = chosen.pop()
            rightName = avenger.pop()
            newChosen.append(leftName)
            newAvenger.append(rightName)
            gameText.prepLeftName(leftName)
            gameText.prepRightName(rightName + ": " + str(i))

            #trying to display the odd name but it didnt' work maybe just add one more false name?
            if (len(chosen) > 0 ) and len(avenger) == 0:
                leftName = chosen.pop()
                gameText.prepLeftName(leftName)
            if (len(avenger) > 0 ) and len(chosen) == 0:
                rightName = avenger.pop()
                gameText.prepRightName(rightName)
        gameText.draw_text()
        center_line.draw_center_line()


    print("we've displayed these many names: " + str(popCounter) + " x2!")
    print("newChosen length: " + str(len(newChosen)))
    print("newAvenger length: " + str(len(newAvenger)))

    #stops names from appearing
    if len(chosen) == 0 or len(avenger) == 0:
        print("ALL NAMES HAVE BEEN POPPPED!!")
        for i in range(len(newAvenger)):
            print("new chosen: " + str(i) + ": " + str(newChosen[i]))
            print("new avenger: " + str(i) + ": " + str(newAvenger[i]))

    if not stats.game_active:
        screen.fill(ai_settings.bg_color)
        play_button.draw_button()

    pygame.display.flip()

