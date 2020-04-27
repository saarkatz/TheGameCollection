"""
The main module bootstraps the application
"""
import sys
import json
import jsonschema
import munch

from engine.game_object import GameObject
from engine.utils.path import specify


class JsonLoader:
    def __init__(self, schema_root):
        self.resolver = jsonschema.RefResolver(
            'file:///{}/'.format(specify(schema_root)), None
        )

    def load(self, json_object):
        with open(json_object.schema, 'r') as schemafile:
            schema = json.load(schemafile)
        with open(json_object.file, 'r') as file:
            content = json.load(file)

        jsonschema.validate(content, schema, resolver=self.resolver)
        return munch.munchify(content)


def main():
    # Bootstrap the configuration from meta.json/schema_root
    with open('meta.json', 'r') as metafile:
        meta = json.load(metafile)
        jsonschema.validate(
            meta,
            {
                "type": "object",
                "properties": {"schema_root": {"type": "string"}},
                "required": ["schema_root"]
            }
        )

    # Initialize the loader with the schema directory
    loader = JsonLoader(meta.get('schema_root'))

    # Reload the meta.json for everything else
    meta = loader.load(munch.munchify({
        'schema': 'schema/meta.json',
        'file': 'meta.json'
    }))

    # Add the project root to the system path
    sys.path.append(specify(meta.project_root))

    # Load data
    config = loader.load(meta.config)
    objects = GameObject.objectify(loader.load(meta.objects))

    # Import the app
    from app import App

    # Initiate and run the app
    app = App(**config)
    app.gameobjects.extend(objects)
    app.run()


if __name__ == '__main__':
    main()
