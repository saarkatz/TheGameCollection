import os
import json
import jsonschema
import munch

from engine.game_object import GameObject
from engine.utils.path import normalize


def load_json(jsonfile):
    with open(jsonfile.schema, 'r') as schemafile:
        schema = json.load(schemafile)
    with open(jsonfile.file, 'r') as file:
        content = json.load(file)

    jsonschema.validate(content, schema)
    return munch.munchify(content)


def main():
    # search for the meta.json and meta.schema in data and schema respectively
    meta = load_json(munch.munchify({
        'schema': 'schema/meta.schema',
        'file': 'meta.json'
    }))

    # Add the project root to the system path
    import sys
    sys.path.append(normalize(meta.projectroot))

    # Load data
    config = load_json(meta.config)
    objects = GameObject.objectify(load_json(meta.objects))

    # Import the app
    from app import App

    # Initiate the app
    app = App(**config)
    app.gameobjects.extend(objects)
    app.run()


if __name__ == '__main__':
    main()
