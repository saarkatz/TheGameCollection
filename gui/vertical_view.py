from linalg import Vector2
from gui.gui_object import GUIObject
from gui import Panel


class VerticalView(GUIObject):
    """
    Vertical view for GUI objects.
    Organizes an object list in a vertical fashion bounded within the view rectangle.
    """
    def __init__(self, position, size, alignment=Vector2.zeros(), parent=None):
        super().__init__(parent=parent)
        self.rect.position = position
        self.rect.size = size
        self.alignment = alignment
        self.objects_list = []

    def _update_positions(self):
        if len(self.objects_list) == 0:
            return
        height = self.rect.size[1] / len(self.objects_list)
        for i, obj in enumerate(self.objects_list):
            obj.parent.position = (self.position[0], self.position[1] + i * height)
            obj.parent.rect.size = (self.rect.size[0], height)

    def _wrap_with_panel(self, obj):
        panel = Panel(self)
        obj.anchor = self.alignment
        obj.rect.pivot = self.alignment
        obj.parent = panel

    def append_object(self, obj):
        self._wrap_with_panel(obj)
        self.objects_list.append(obj)
        self._update_positions()

    def insert(self, index, obj):
        self._wrap_with_panel(obj)
        self.objects_list.insert(index, obj)
        self._update_positions()

    def clear(self):
        self.objects_list.clear()

    def remove(self, obj):
        self.objects_list.remove(obj)
        self._update_positions()

    def sort(self, key=None, reverse=False):
        self.objects_list.sort()
        self._update_positions()

