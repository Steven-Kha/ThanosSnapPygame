import pygame.sysfont

class NameToJudge:
    def __init__(self, ai_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        self.leftColor = (255, 0, 0)
        self.rightColor = (0, 0, 255)
        self.vsColor = (167, 136, 168)
        self.fallenColor = (102, 102, 102)

        self.font = pygame.font.SysFont(None, 48)

        # function to display left participant
        self.prepLeftName("")

        self.prepRightName("")

        #add avenger title below
        self.prepTitleLeft("")

        #add fallen title below
        self.prepNumNames("")

        #function to display right participant
        self.prepNamesRemain("")

        # add avenger title below
        self.prepTitleRight("")

        # add fallen title below
        #self.prepChosenRight("")

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
        self.rightName_rect.centerx = ((self.ai_settings.screen_width * 3) / 4)

    def prepVS(self, msg):
        vsStr = msg
        self.vsImage = self.font.render(vsStr, True,
                        self.vsColor, self.ai_settings.bg_color)

        self.VS_rect = self.vsImage.get_rect()
        self.VS_rect.centery = self.screen_rect.centery
        self.VS_rect.centerx = self.screen_rect.centerx

    def prepTitleLeft(self, msg):
        leftName = msg
        self.leftTitleNameImage = self.font.render(leftName, True,
                            self.leftColor, self.ai_settings.bg_color)
        self.leftTitleName_rect = self.leftNameImage.get_rect()
        self.leftTitleName_rect.centery = self.screen_rect.centery + 40
        self.leftTitleName_rect.centerx = self.ai_settings.screen_width / 4
        pass

    def prepTitleRight(self, msg):
        rightName = msg
        self.rightTitleNameImage = self.font.render(rightName, True,
                            self.rightColor, self.ai_settings.bg_color)
        self.rightTitleName_rect = self.rightNameImage.get_rect()
        self.rightTitleName_rect.centery = self.screen_rect.centery + 40
        self.rightTitleName_rect.centerx = (self.ai_settings.screen_width * 3) / 4
        pass

    def prepNumNames(self, msg):
        leftName = msg
        self.leftFallenNameImage = self.font.render(leftName, True,
                            self.fallenColor, self.ai_settings.bg_color)
        self.leftFallenName_rect = self.leftNameImage.get_rect()
        self.leftFallenName_rect.centery = self.screen_rect.centery + 80
        self.leftFallenName_rect.centerx = self.ai_settings.screen_width / 4
        pass

    def prepNamesRemain(self, msg):
        rightName = msg
        self.rightFallenNameImage = self.font.render(rightName, True,
                             self.fallenColor, self.ai_settings.bg_color)
        self.rightFallenName_rect = self.rightNameImage.get_rect()
        self.rightFallenName_rect.centery = self.screen_rect.centery + 80
        self.rightFallenName_rect.centerx = (self.ai_settings.screen_width * 3) / 4
        pass


    def draw_text(self):
        self.screen.blit(self.vsImage, self.VS_rect)
        self.screen.blit(self.leftNameImage, self.leftName_rect)
        self.screen.blit(self.rightNameImage, self.rightName_rect)

        self.screen.blit(self.leftTitleNameImage, self.leftTitleName_rect)
        self.screen.blit(self.rightTitleNameImage, self.rightTitleName_rect)

        self.screen.blit(self.leftFallenNameImage, self.leftFallenName_rect)
        self.screen.blit(self.rightFallenNameImage, self.rightFallenName_rect)

        # self.screen.blit(self.leftFallenNameImage, self.leftFallenName_rect)
        # self.screen.blit(self.rightFallenNameImage, self.rightFallenName_rect)

        '''
        self.rect.centery = self.screen_rect.centery
        self.rect.centerx = self.screen_rect.centerx
        '''