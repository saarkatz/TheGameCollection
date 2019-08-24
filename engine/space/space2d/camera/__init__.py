"""
The Camera package is responsible for facilitating the casting of a
view of the environment to a 2D surface.
"""
from engine.backend import Surface
from engine.space.space2d.transform import Transform
from engine.space.space2d.vector import Vector
from engine.space.space2d.base_member2d import BaseMember2D
from engine.space.space2d.primitives.rectangle import Rectangle


class Camera(BaseMember2D):
    def __init__(self, space):
        super().__init__(space)
        transform = Transform()
        size = Vector.one()

    def view(self, surface: Surface):
        members = self.space.members[:]
        members.remove(self)
        for m in members:
            backend.draw.rect(
                surface, (0, 0, 128),
                (m.transform.position[0], m.transform.position[0],
                 m.size[0], m.size[1]))
        return surface


if __name__ == '__main__':
    from engine.space.space2d import Space2D
    import engine.backend as backend
    backend.init()
    t_screen = backend.display.set_mode((500, 500))
    t_surface = backend.Surface((300, 300))

    t_space = Space2D()
    t_camera = Camera(t_space)
    t_rectangle = Rectangle(t_space)
    t_rectangle.size = 50 * Vector.one()
    t_rectangle.transform.position = 150 * Vector.one()
    t_rectangle2 = Rectangle(t_space)
    t_rectangle2.size = 50 * Vector.one()
    t_rectangle2.transform.position = 100 * Vector.one()

    t_camera.view(t_surface)
    for i in range(4):
        t_surface = backend.transform.rotate(t_surface, 45)
        t_screen.blit(t_surface, t_surface.get_bounding_rect())
        backend.display.update()
    input('Press to continue...')

    backend.quit()
