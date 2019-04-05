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

    def update(self, chosen, avenger, center_line):
        if len(chosen) > len(avenger):
            length = len(avenger)
        else:
            length = len(chosen)

        # a vector that goes up to length of chosen/avenger whatever is largets
        #lenVector = [0] * length-1

        # for i in range(len(lenVector)):
        #     lenVector[i] = i
        #
        #call = 0

        #call = random.randint(0, 1)

        #lenVector index counter iterator
        j = 0

        print("pygame running the for loop in range(length) \n")
        while j < length:

            print ("j counter: " + str(j))
            self.screen.fill(self.ai_settings.bg_color)

            #if stime % 5 == 0:
            self.prepLeftName(chosen[j])
            self.prepRightName(str(avenger[j]) + " stop number: " + str(j))

                #j += 1
                # if call:
                #     self.prepLeftName(chosen[i])
                #     self.prepRightName(str(avenger[i]) + " stop number: " + str(stop))
                # else:
                #     self.prepLeftName(avenger[i])
                #     self.prepRightName(str(chosen[i]) + " stop number: " + str(stop))
            # elif stime % 1111 == 1 and j == i:
            #     self.prepLeftName(chosen[i])
            #     self.prepRightName(str(avenger[i]) + " stop number: " + str(i))
            #     #j += 1
            center_line.draw_center_line()
            stime = pygame.time.get_ticks()
            if stime % 1000 == 0:
                self.draw_text()
            j += 1





    def draw_text(self):
        self.screen.blit(self.vsImage, self.VS_rect)
        self.screen.blit(self.leftNameImage, self.leftName_rect)
        self.screen.blit(self.rightNameImage, self.rightName_rect)
        '''
        self.rect.centery = self.screen_rect.centery
        self.rect.centerx = self.screen_rect.centerx
        '''