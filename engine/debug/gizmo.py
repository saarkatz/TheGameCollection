import pygame
from space2d.vector import Vector


BLUE = (0, 0, 255, 127)
TRANS_BLUE = (223, 223, 255, 223)

CONTROL_POSITIONS = [
    Vector(0, 0), Vector(.5, 0), Vector(1, 0),
    Vector(0, .5), Vector(.5, .5), Vector(1, .5),
    Vector(0, 1), Vector(.5, 1), Vector(1, 1),
]

MIRROR_X = [
    2, 1, 0,
    5, 4, 3,
    8, 7, 6,
]

MIRROR_Y = [
    6, 7, 8,
    3, 4, 5,
    0, 1, 2,
]


class Gizmo:
    def __init__(self, ui):
        self.ui = ui

        self.gizmo_hover = False
        self.gizmo_control = -1
        self.view_gizmo_control = -1
        self.control_hover = False

        self.gizmo_move = False
        self.mouse_cache = None
        self.control_cache = None

    # Gizmo functions
    def draw_gizmo(self, screen):
        # Draw the rectangle of the shape
        if self.gizmo_hover:
            pygame.draw.rect(screen, BLUE, (self.ui.transform.position,
                                            self.ui.size), 1)
        else:
            pygame.draw.rect(screen, TRANS_BLUE,
                             (self.ui.transform.position, self.ui.size), 1)

        # Draw control button
        if self.view_gizmo_control > -1:
            if self.control_hover:
                pygame.draw.rect(screen, BLUE,
                                 ((self.ui.transform.position + self.ui.size *
                                  CONTROL_POSITIONS[self.view_gizmo_control] -
                                  Vector(6, 6)).int(), (12, 12)), 0)
            else:
                pygame.draw.rect(screen, BLUE,
                                 ((self.ui.transform.position + self.ui.size *
                                  CONTROL_POSITIONS[self.view_gizmo_control] -
                                  Vector(5, 5)).int(), (10, 10)), 0)

    def on_gizmo_hover_enter(self):
        pass

    def on_gizmo_hover_exit(self):
        self.view_gizmo_control = -1

    def on_gizmo_hover(self):
        # The gizmo is clicked
        if self.gizmo_move:
            return

        # Determine which control should be used
        mouse = pygame.mouse.get_pos()
        x = int((mouse[0] - self.ui.transform.position.x + 6) /
                (self.ui.size.x + 12) * 3)
        y = int((mouse[1] - self.ui.transform.position.y + 6) /
                (self.ui.size.y + 12) * 3)
        self.gizmo_control = x + y * 3
        self.view_gizmo_control = self.gizmo_control

        # Check if the mouse if hovering over control
        control_position = self.ui.transform.position + self.ui.size * \
                           CONTROL_POSITIONS[self.gizmo_control]
        corner = control_position - Vector(6, 6)
        if pygame.Rect(corner, (12, 12)).collidepoint(mouse):
            self.control_hover = True
        else:
            self.control_hover = False

    def on_gizmo_control(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and \
                event.button == pygame.BUTTON_LEFT and \
                self.control_hover:
            self.gizmo_move_enter()
        elif event.type == pygame.MOUSEBUTTONUP and \
                event.button == pygame.BUTTON_LEFT and \
                self.control_hover:
            self.gizmo_move_exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKQUOTE:
            # Cancel move action
            if self.gizmo_move:
                self.ui.transform.position = self.control_cache[0]
                self.ui.size = self.control_cache[1]
                self.gizmo_move_exit()

    def gizmo_move_enter(self):
        self.gizmo_move = True
        self.mouse_cache = Vector(*pygame.mouse.get_pos())
        self.control_cache = (self.ui.transform.position, self.ui.size)

    def gizmo_move_exit(self):
        self.gizmo_move = False

    def gizmo_update(self):
        if self.gizmo_move:
            mouse_vector = Vector(*pygame.mouse.get_pos()) - self.mouse_cache
            position = self.control_cache[0]
            size = self.control_cache[1]
            if self.gizmo_control == 0:
                position += mouse_vector
                size -= mouse_vector
            elif self.gizmo_control == 1:
                position += Vector.up() * mouse_vector
                size -= Vector.up() * mouse_vector
            elif self.gizmo_control == 2:
                position += Vector.up() * mouse_vector
                size += Vector.second() * mouse_vector
            elif self.gizmo_control == 3:
                position += Vector.right() * mouse_vector
                size -= Vector.right() * mouse_vector
            elif self.gizmo_control == 4:
                position += mouse_vector
            elif self.gizmo_control == 5:
                size += Vector.right() * mouse_vector
            elif self.gizmo_control == 6:
                position += Vector.right() * mouse_vector
                size -= Vector.second() * mouse_vector
            elif self.gizmo_control == 7:
                size += Vector.up() * mouse_vector
            else:
                size += mouse_vector

            # Normalize negative size and change the control
            normal = Vector.zero()
            self.view_gizmo_control = self.gizmo_control
            if size.x < 0:
                normal += -Vector.right()
                self.view_gizmo_control = MIRROR_X[self.view_gizmo_control]
            if size.y < 0:
                normal += -Vector.up()
                self.view_gizmo_control = MIRROR_Y[self.view_gizmo_control]

            position -= size * normal
            size *= Vector.one() + 2 * normal

            self.ui.transform.position = position
            self.ui.size = size
