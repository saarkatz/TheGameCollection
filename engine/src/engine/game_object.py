import json


class GameObject:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.components = []

    def __str__(self):
        return json.dumps(self.as_dict())

    def __repr__(self):
        str(self)

    def as_dict(self):
        return {
            "name": self.name,
            "children": [child.as_dict() for child in self.children],
            "components": [component.as_dict() for component in self.components]
        }

    @staticmethod
    def objectify(object):
        if isinstance(object, (list, tuple)):
            return [GameObject.objectify(o) for o in object]
        elif isinstance(object, dict):
            obj = GameObject(object['name'])
            obj.children.extend(
                GameObject.objectify(object.get('children', []))
            )
            # TODO: Components not implemented
            obj.components.extend(object.get('components', []))
            return obj
        else:
            raise NotImplementedError("Can't objectify instance of '{}'"
                                      .format(object.__class__))
