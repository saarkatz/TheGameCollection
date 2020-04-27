"""
The app module handles the main loop of the app
"""
import time
import pygame

from engine.debug import Gizmo
from engine.space2d import Vector
from uitext import UiText
from transform import Transform
from text import Text

WHITE = (255, 255, 255)
LIGHT_GRAY = (250, 250, 250)
RED = (255, 0, 0)
LIGHT_RED = (255, 200, 200)

FONTS = [
    'Ariel',
    'Helvetica',
    'Times New Roman',
    'Courier New',
    'Verdana',
    'Tahoma',
    'Comic Sans MS',
    'Avant Garde',
    'Georgia'
]


pygame.init()


class App:
    def __init__(self, caption, resolution, background):
        self.caption = caption
        self.resolution = resolution
        self.background = background

        self.gameobjects = []
        self.running = False

        # Demo
        self.texts = []
        self.gizmos = []
        self.interval = 0.01667
        self.speed = self.interval * 100
        self.font_index = 0
        self.text_index = 0

    def run(self):
        self.running = True

        screen = pygame.display.set_mode(self.resolution)
        pygame.display.set_caption(self.caption)

        # Set the texts
        self.texts.append(UiText(Transform(), Text('Hello', FONTS[
            self.font_index], background=LIGHT_GRAY)))

        # Set the gizmos
        for text in self.texts:
            self.gizmos.append(Gizmo(text))

        try:
            # The game loop
            while self.running:
                self.gizmo_focus()

                # Handle events
                events = pygame.event.get()
                for event in events:
                    self.event(event)

                # Gizmo update phase
                self.gizmo_update()

                # Update phase
                self.update()

                # Draw phase
                self.draw(screen)

                # Draw gizmo phase
                self.gizmo_draw(screen)

                pygame.display.update()
                time.sleep(self.interval)
        finally:
            pygame.quit()

    def update(self):
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.texts[0].transform.position -= Vector.up() * self.speed
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.texts[0].transform.position += Vector.up() * self.speed
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.texts[0].transform.position -= Vector.right() * self.speed
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.texts[0].transform.position += Vector.right() * self.speed

        x_position, _ = self.texts[0].text.get_surface_size()
        for text in self.texts[1:]:
            text.transform.position = \
                self.texts[0].transform.position + \
                Vector.right() * x_position
            x, _ = text.text.get_surface_size()
            x_position += x

    def draw(self, screen):
        screen.fill(self.background)
        for text in self.texts:
            text.draw(screen)

    def gizmo_focus(self):
        mouse_pos = pygame.mouse.get_pos()
        for obj in self.gizmos:
            rect = pygame.Rect(
                (obj.ui.transform.position.int() - Vector(6, 6)),
                obj.ui.size + Vector(12, 12))
            if rect.collidepoint(*mouse_pos):
                if not obj.gizmo_hover:
                    obj.gizmo_hover = True
                    obj.on_gizmo_hover_enter()
            elif obj.gizmo_hover and not obj.gizmo_move:
                obj.on_gizmo_hover_exit()
                obj.gizmo_hover = False

            if obj.gizmo_hover:
                obj.on_gizmo_hover()

    def gizmo_update(self):
        for obj in self.gizmos:
            obj.gizmo_update()

    def gizmo_draw(self, screen):
        for obj in self.gizmos:
            obj.gizmo_draw(screen)

    def event(self, event):
        # Handle quit events
        if event.type == pygame.QUIT:
            self.running = False

        for obj in self.gizmos:
            if obj.gizmo_hover:
                obj.on_gizmo_control(event)
                return

        if event.type == pygame.KEYDOWN:
            text = self.texts[self.text_index]

            if event.key == pygame.K_BACKSPACE:
                text.text.text = text.text.text[:-1]
            elif pygame.key.get_mods() & pygame.KMOD_CTRL:
                if event.key == pygame.K_a:
                    text.text.antialias = not text.text.antialias
                elif event.key == pygame.K_EQUALS:
                    text.text.size += 1
                elif event.key == pygame.K_MINUS:
                    text.text.size -= 1
                elif event.key == pygame.K_f:
                    self.font_index = (self.font_index + 1) % len(FONTS)
                    text.text.font = FONTS[self.font_index]
                elif event.key == pygame.K_d:
                    self.font_index = (self.font_index - 1) % len(FONTS)
                    text.text.font = FONTS[self.font_index]
                elif event.key == pygame.K_n:
                    self.text_index = (self.text_index + 1) % len(self.texts)

            elif event.key not in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT,
                                   pygame.K_RIGHT):
                _text = text.text.text + event.unicode
                if _text != text.text.text:
                    text.text.text = _text
