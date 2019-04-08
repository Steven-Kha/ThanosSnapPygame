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

        pygame.mixer.init()
        pygame.mixer.music.load('Music\Giants Theme - The Legend of Zelda- Majoras Mask.mp3')
        pygame.mixer.music.play(-1)


def update_screen(ai_settings, stats, center_line, gameText,
                  chosen, avenger, newChosen, newAvenger, length, clock,
                  play_button, screen):
    if stats.game_active:

        screen.fill(ai_settings.bg_color)



        #print ("length of newChosen: " + str(len(newChosen)))

        leftName = ""
        rightName = ""

        # initialize first in case
        call = 0

        # randomly set it to 0 or 1
        call = random.randint(0, 1)
        #print("-" * 40)
        nowTime = pygame.time.get_ticks()
        #print("nowTime: " + str(nowTime))
        sTime = pygame.time.get_ticks()
        #print("sTime: " + str(sTime))
        #print("-" * 40)
        #print("while sTime - nowTime < 3000: ")
        while (sTime - nowTime < 2081):
            sTime = pygame.time.get_ticks()
            # print("nowTime: " + str(nowTime))
            # print("sTime: " + str(sTime))
        #print("-" * 40)

        if (sTime - nowTime >= 2081 and len(chosen) > 0):
            #print(str(sTime) + " - " + str(nowTime) + ">= 3000")
            nowTime = sTime

            #pop names so they don't appear again
            if call:
                #print ("call is 1")
                leftName = chosen.pop()
                rightName = avenger.pop()
                newChosen.append(leftName)
                newAvenger.append(rightName)
                gameText.prepLeftName(leftName)
                gameText.prepRightName(rightName)
                gameText.prepTitleLeft('Dust')
                gameText.prepTitleRight('Avenger')
                gameText.prepNumNames(str(len(chosen)))
                gameText.prepNamesRemain("left")

                #print out these two times to see why they don't appear 3 seconds later.

            else:
                print ("call is 0")
                rightName = chosen.pop()
                leftName = avenger.pop()
                newChosen.append(rightName)
                newAvenger.append(leftName)
                gameText.prepLeftName(leftName)
                gameText.prepRightName(rightName)
                gameText.prepTitleRight('Dust')
                gameText.prepTitleLeft('Avenger')
                gameText.prepNumNames(str(len(chosen)))
                gameText.prepNamesRemain("left")

        gameText.draw_text()
        center_line.draw_center_line()

        # print("-" * 40)
        # print("printing subtitles now...")
        # print("-" * 40)
        #
        # nowTime = pygame.time.get_ticks()
        # sTime = pygame.time.get_ticks()
        # print("nowTime: " + str(nowTime))
        # print("sTime: " + str(sTime))
        #
        # print("-" * 40)
        # print("while sTime - nowTime < 3000")
        # print("-" * 40)
        #
        # while sTime - nowTime < 3000:
        #     gameText.draw_text()
        #     center_line.draw_center_line()
        #     sTime = pygame.time.get_ticks()
        #     # print("nowTime: " + str(nowTime))
        #     # print("sTime: " + str(sTime))
        #
        # if sTime - nowTime >= 3000:
        #     print(str(sTime) + "-" + str(nowTime) + ">=3000")
        #     if call:
        #         nowTime = sTime
        #         gameText.prepTitleLeft('Dust')
        #         gameText.prepTitleRight('Avenger')
        #     else:
        #         nowTime = sTime
        #         gameText.prepTitleRight('Dust')
        #         gameText.prepTitleLeft('Avenger')
        #
        # gameText.draw_text()
        # center_line.draw_center_line()

        gameText.prepTitleLeft('')
        gameText.prepTitleRight('')

        if len(chosen) < 1:
            gameText.prepLeftName("THE")
            gameText.prepRightName("END")
            gameText.prepNamesRemain("")
            gameText.prepNumNames("")


    if not stats.game_active:
        screen.fill(ai_settings.bg_color)
        play_button.draw_button()

    pygame.display.flip()

