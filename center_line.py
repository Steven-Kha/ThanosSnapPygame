# # By Steven Kha 2018

import pygame
pygame.init()
from pygame.sprite import Sprite

class Center_Line(Sprite):

    def __init__(self, ai_settings, screen):
        """Create the left_paddle and set its starting position."""
        super(Center_Line, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.rect = pygame.Rect(0, 0, ai_settings.center_line_width,
                                ai_settings.center_line_height)

        self.screen_rect = screen.get_rect()

        self.color = ai_settings.center_line_color

        self.rect.centery = self.screen_rect.centery
        self.rect.centerx = self.screen_rect.centerx


    def draw_center_line(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

# By Steven Kha 2018