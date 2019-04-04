import pygame.sysfont

class NameToJudge:
    def __init__(self, ai_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        self.leftColor = (255, 0, 0)
        self.rightColor = (0, 0, 255)
        self.vsColor = (167, 136, 168)

        self.font = pygame.font.SysFont(None, 48)

        # function to display left participant
        self.prepLeftName(msg)

        #function to display right participant
        self.prepRightName(msg)

        self.prepVS("V  S")

    def prepLeftName(self, msg):
        pass

    def prepRightName(self, msg):
        pass

    def prepVS(self, msg):
        vsStr = msg
        self.vsImage = self.font.render(vsStr, True,
                        self.vsColor, self.ai_settings.bg_color)

        self.VS_rect = self.vsImage.get_rect()
        self.VS_rect.centery = self.screen_rect.centery
        self.VS_rect.centerx = self.screen_rect.centerx

    def draw_text(self):
        self.screen.blit(self.vsImage, self.VS_rect)

        '''
        self.rect.centery = self.screen_rect.centery
        self.rect.centerx = self.screen_rect.centerx
        '''