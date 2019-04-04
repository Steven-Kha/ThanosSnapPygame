import pygame.sysfont

class NameToJudge:
    def __init__(self, ai_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        self.leftColor = (255, 0, 0)
        self.rightColor = (0, 0, 255)

        self.font = pygame.font.SysFont(None, 48)

        # function to display left participant
        self.prepLeftName(msg)

        #function to display right participant
        self.prepRightName(msg)

    def prepLeftName(self, msg):
        pass

    def prepRightName(self, msg):
        pass