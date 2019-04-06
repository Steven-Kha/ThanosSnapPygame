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
        self.prepLeftName("")

        #add avenger title below
        self.prepAvengerLeft("")

        #add fallen title below
        self.prepChosenLeft("")

        #function to display right participant
        self.prepRightName("")

        # add avenger title below
        self.prepAvengerRight("")

        # add fallen title below
        self.prepChosenRight("")

        self.prepVS("V  S")

    def prepLeftName(self, msg):
        leftName = msg
        self.leftNameImage = self.font.render(leftName, True,
                          self.leftColor, self.ai_settings.bg_color)
        self.leftName_rect = self.leftNameImage.get_rect()
        self.leftName_rect.centery = self.screen_rect.centery
        self.leftName_rect.centerx = self.ai_settings.screen_width / 4

    def prepRightName(self, msg):
        rightName = msg
        self.rightNameImage = self.font.render(rightName, True,
                                              self.rightColor, self.ai_settings.bg_color)
        self.rightName_rect = self.rightNameImage.get_rect()
        self.rightName_rect.centery = self.screen_rect.centery
        self.rightName_rect.centerx = (self.ai_settings.screen_width * 3) / 4

    def prepVS(self, msg):
        vsStr = msg
        self.vsImage = self.font.render(vsStr, True,
                        self.vsColor, self.ai_settings.bg_color)

        self.VS_rect = self.vsImage.get_rect()
        self.VS_rect.centery = self.screen_rect.centery
        self.VS_rect.centerx = self.screen_rect.centerx

    def prepAvengerLeft(self, msg):
        pass

    def prepAvengerRight(self, msg):
        pass

    def prepChosenLeft(self, msg):
        pass

    def prepChosenRight(self, msg):
        pass


    def draw_text(self):
        self.screen.blit(self.vsImage, self.VS_rect)
        self.screen.blit(self.leftNameImage, self.leftName_rect)
        self.screen.blit(self.rightNameImage, self.rightName_rect)
        '''
        self.rect.centery = self.screen_rect.centery
        self.rect.centerx = self.screen_rect.centerx
        '''