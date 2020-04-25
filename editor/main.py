import json
import jsonschema
import munch

import app


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
        'file': 'data/meta.json'
    }))

    config = load_json(meta.config)
    app.main(**config)


if __name__ == '__main__':
    main()
