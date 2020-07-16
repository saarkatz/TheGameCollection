"""
The view of the board
"""
import pygame
from os import listdir
from string import ascii_letters

RESOLUTION = (600, 600)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (128, 0, 0)
COLORS = {"black": (0, 0, 0), "darkgray": (70, 70, 70), "gray": (128, 128, 128), "lightgray": (200, 200, 200),
          "white": (255, 255, 255), "red": (255, 0, 0),
          "darkred": (128, 0, 0), "green": (0, 255, 0), "darkgreen": (0, 128, 0), "blue": (0, 0, 255),
          "navy": (0, 0, 128), "darkblue": (0, 0, 128),
          "yellow": (255, 255, 0), "gold": (255, 215, 0), "orange": (255, 165, 0), "lilac": (229, 204, 255),
          "lightblue": (135, 206, 250), "teal": (0, 128, 128),
          "cyan": (0, 255, 255), "purple": (150, 0, 150), "pink": (238, 130, 238), "brown": (139, 69, 19),
          "lightbrown": (222, 184, 135), "lightgreen": (144, 238, 144),
          "turquoise": (64, 224, 208), "beige": (245, 245, 220), "honeydew": (240, 255, 240),
          "lavender": (230, 230, 250), "crimson": (220, 20, 60)}

BOARD_SIZE = (400, 400)
BORDER_SIZE = (10, 10)


class BoardView:
    def __init__(self, secret_word, screen, pic_dir, sound_dir):
        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.screen = screen
        self.secret_word = secret_word
        self.buttons_list = []
        j = 0
        for number, letter in enumerate(ascii_letters):
            if number > 12:  # TO ALIGN THE LETTERS ON THE SCREEN ( HORIZONTALLY )
                number = number - 13
                j = 1
            self.buttons_list.append(Button(COLORS["gray"], (70 + number * 90, 140 + j * 60), 50, 50, letter,
                                       pygame.font.SysFont(None, 50)))

        # initiate images
        self.images = {}
        for image in listdir(pic_dir):
            if ".png" in image:
                image_path = "{dir}/{filename}".format(dir=pic_dir, filename=image)
                self.images[image] = pygame.image.load(image_path)

        # initiate sounds
        self.sounds = {}
        for sound in listdir(sound_dir):
            if ".wav" in sound:
                sound_path = "{dir}/{filename}".format(dir=sound_dir, filename=sound)
                self.sounds[sound] = pygame.mixer.Sound(sound_path)

    def update(self):
        for letter in self.buttons_list:  # DRAWING
            letter.draw(self.screen)  # THE BUTTONS


class Button(object):  # A GENERAL CLASS FOR ALL THE BUTTONS ON THE SCREEN (LETTERS & LANGUAGE BUTTONS)
    def __init__(self, color, pos, width, height, text, font, size=40):
        self.clicked = False  # A VARIABLE ONLY FOR TYPE 1
        self.rollOver = False  # A VARIABLE ONLY FOR TYPE 1
        self.size = size
        self.font = font
        self.color = color
        self.text = text
        self.pos = pos
        self.width = width
        self.height = height
        self.subsurface = pygame.Surface((self.width, self.height))  # CREATING A SUBSURFACE
        self.subsurface.fill(self.color)  # GET A RECT (FOR COLLISION)
        self.text = self.font.render(self.text, True, COLORS["white"])

    def draw(self, surface):
        if self.rollOver:  # IF A TYPE 1 BUTTON IS UNDER
            self.subsurface.set_alpha(200)  # THE MOUSE, MAKE IT LESS VIBRANT
        else:
            self.subsurface.set_alpha(255)
        if not self.clicked:
            surface.blit(self.subsurface, self.pos)
            self.subsurface.blit(self.text, (self.width / 4, self.height / 5))
