import time
import pygame

from ui import Gizmo
from uitext import UiText
from transform import Transform
from vector import Vector
from text import Text

# The title of the windows
CAPTION = 'TextAdventure'

# The size of the window
SIZE = (600, 600)
WHITE = (255, 255, 255)
LIGHT_GRAY = (250, 250, 250)
RED = (255, 0, 0)
LIGHT_RED = (255, 200, 200)

running = True
texts = []
gizmos = []

SPEED = 100
INTERVAL = 0.01667
REL_SPEED = SPEED * INTERVAL

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

font_index = 0
text_index = 0


def handle_event(event):
    global running
    global font_index
    global text_index

    # Handle quit events
    if event.type == pygame.QUIT:
        running = False

    for obj in gizmos:
        if obj.gizmo_hover:
            obj.on_gizmo_control(event)
            return

    if event.type == pygame.KEYDOWN:
        # if event.key == pygame.K_ESCAPE or event.unicode == 'q':
        #     running = False

        text = texts[text_index]

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
                font_index = (font_index + 1) % len(FONTS)
                text.text.font = FONTS[font_index]
            elif event.key == pygame.K_d:
                font_index = (font_index - 1) % len(FONTS)
                text.text.font = FONTS[font_index]
            elif event.key == pygame.K_n:
                text_index = (text_index + 1) % len(texts)

        elif event.key not in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT,
                               pygame.K_RIGHT):
            _text = text.text.text + event.unicode
            if _text != text.text.text:
                text.text.text = _text


def main():
    global running

    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption(CAPTION)

    texts.append(UiText(Transform(), Text('Hello', FONTS[font_index],
                                          background=LIGHT_GRAY)))
    gizmos.append(Gizmo(texts[-1]))
    # texts.append(UiText(Transform(), Text('World', FONTS[font_index],
    #                                       color=RED, background=LIGHT_RED)))

    try:
        # The game loop
        while running:
            mouse_pos = pygame.mouse.get_pos()
            for obj in gizmos:
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

            # Handle events
            events = pygame.event.get()
            for event in events:
                handle_event(event)


            # Gizmo update phase
            for obj in gizmos:
                obj.gizmo_update()

            # Update phase
            if pygame.key.get_pressed()[pygame.K_UP]:
                texts[0].transform.position -= Vector.up() * REL_SPEED
            if pygame.key.get_pressed()[pygame.K_DOWN]:
                texts[0].transform.position += Vector.up() * REL_SPEED
            if pygame.key.get_pressed()[pygame.K_LEFT]:
                texts[0].transform.position -= Vector.right() * REL_SPEED
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                texts[0].transform.position += Vector.right() * REL_SPEED

            x_position, _ = texts[0].text.get_surface_size()
            for text in texts[1:]:
                text.transform.position = texts[0].transform.position + \
                                          Vector.right() * x_position
                x, _ = text.text.get_surface_size()
                x_position += x

            # Draw phase
            screen.fill(WHITE)
            for text in texts:
                text.draw(screen)

            # Draw gizmo phase
            for obj in gizmos:
                obj.draw_gizmo(screen)

            pygame.display.update()
            time.sleep(INTERVAL)
    finally:
        pygame.quit()


if __name__ == '__main__':
    main()
