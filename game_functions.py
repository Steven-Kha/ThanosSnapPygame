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
                  chosen, avenger, newChosen, newAvenger, popCounter, clock,
                  play_button, screen):
    if stats.game_active:
        if len(chosen) > len(avenger):
            length = len(avenger)
            chosenLong = 1
        else:
            length = len(chosen)
            avengerLong = 1

        print ("length of newChosen: " + str(len(newChosen)))
        screen.fill(ai_settings.bg_color)
        leftName = ""
        rightName = ""

        # initialize first in case
        call = 0

        # randomly set it to 0 or 1
        call = random.randint(0, 1)

        nowTime = pygame.time.get_ticks()
        sTime = pygame.time.get_ticks()
        while (sTime - nowTime < 3000):
            sTime = pygame.time.get_ticks()

        if (sTime - nowTime >= 3000 and len(chosen) > 0):
            nowTime = sTime
            print("Tick tock is % by 1000: " + str(sTime))
            print
            #pop names so they don't appear again
            if call:
                leftName = chosen.pop()
                rightName = avenger.pop()
                newChosen.append(leftName)
                newAvenger.append(rightName)
                gameText.prepLeftName(leftName)
                gameText.prepRightName(rightName + ": " + str(len(newChosen)))

                #print out these two times to see why they don't appear 3 seconds later.

            else:
                rightName = chosen.pop()
                leftName = avenger.pop()
                newChosen.append(rightName)
                newAvenger.append(leftName)
                gameText.prepLeftName(leftName)
                gameText.prepRightName(rightName + ": " + str(len(newChosen)))

        gameText.draw_text()
        center_line.draw_center_line()
     
        dustStart = pygame.time.get_ticks()
        dustStop = pygame.time.get_ticks()
    
        while (dustStop - dustStart < 3000):
            if call:
                gameText.prepTitleLeft(“Dust”)
                gameText.prepTitleRight(“Avenger”)
            else: 
                gameText.prepTitleRight(“Dust”)
                gameText.prepTitleLeft(“Avenger”)
        
        gameText.draw_text()
        center_line.draw_center_line()


    if not stats.game_active:
        screen.fill(ai_settings.bg_color)
        play_button.draw_button()

    pygame.display.flip()

