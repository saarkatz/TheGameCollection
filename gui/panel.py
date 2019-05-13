from gui.gui_object import GUIObject


class Panel(GUIObject):
    """
    Simple container GUI object.
    """
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.child = None
