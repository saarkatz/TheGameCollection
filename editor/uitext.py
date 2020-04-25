import pygame
from ui import UiBase

BLACK = (0, 0, 0)


class UiText(UiBase):
    def __init__(self, transform, text):
        super().__init__(transform)
        self.text = text

        self.size *= 80

    def draw(self, screen):
        if self.text:
            screen.blit(self.text.surface, self.transform.position,
                        area=pygame.Rect(0, 0, *self.size))
