import pygame.sysfont

class NameToJudge:
    def __init__(self, ai_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        self.leftColor = (255, 0, 0)
        self.rightColor = (0, 0, 255)

        self.font = pygame.font.SysFont(None, 48)

        self.prepLeftName(msg)
        self.prepRightName(msg)


