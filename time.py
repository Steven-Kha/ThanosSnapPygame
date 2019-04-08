import pygame
clock = pygame.time.Clock()

startTime = pygame.time.get_ticks()
print("startTime: " + str(startTime))
stopTime = pygame.time.get_ticks()
print("stopTIme: " + str(stopTime))

print("while stopTime - startTime < 3: ")
print("-"*40)
while stopTime - startTime < 3:
    stopTime = pygame.time.get_ticks()
    print("startTime: " + str(startTime))
    print("stopTIme: " + str(stopTime))
print("-"*40)

if stopTime - startTime > 2:
    print( (str(startTime)) + " - " + str(stopTime) + " >= 3" )

#----------

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