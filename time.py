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
    print( (str(stopTime)) + " - " + str(stopTime) + " >= 3" )