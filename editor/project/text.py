import pygame


class Text:
    def __init__(self, text='', font='Comic Sans MS', size=30, color=(0, 0, 0),
                 background=None, antialias=True):
        self._text = text
        self._color = color
        self._background = background
        self._font = font
        self._size = size
        self._antialias = antialias

        self._dirty = True
        self._surface_cache = None

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._dirty = True
        self._text = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._dirty = True
        self._color = value

    @property
    def background(self):
        return self._background

    @background.setter
    def background(self, value):
        self._dirty = True
        self._background = value

    @property
    def font(self):
        return self._font

    @font.setter
    def font(self, value):
        self._dirty = True
        self._font = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._dirty = True
        self._size = value

    @property
    def antialias(self):
        return self._antialias

    @antialias.setter
    def antialias(self, value):
        self._dirty = True
        self._antialias = value

    @property
    def surface(self):
        if self._dirty:
            self._dirty = False
            self._surface_cache = pygame.font.SysFont(self.font, self.size) \
                .render(self.text, self.antialias, self.color, self.background)
        return self._surface_cache

    def get_surface_size(self):
        return pygame.font.SysFont(self.font, self.size).size(self.text)
