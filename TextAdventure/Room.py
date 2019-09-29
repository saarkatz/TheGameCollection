import json
import sqlite3

ROOM_DB = "rooms.db"


def get_room(room_id):
    ret_room = None

    connect = sqlite3.connect(ROOM_DB)

    for row in connect.execute("select json from rooms where id=?", (room_id,)):
        json_text = row[0]
        dictionary = json.loads(json_text)
        dictionary['room_id'] = room_id
        ret_room = Room(**dictionary)
        break
    return ret_room


class Room:
    def __init__(self, room_id=0, name="A Room", description="An empty room", neighbors={}):
        self.room_id = room_id
        self.name = name
        self.description = description
        self.neighbors = neighbors

    def _neighbor(self, direction):
        if direction in self.neighbors:
            return self.neighbors[direction]
        else:
            return None

    def north(self):
        return self._neighbor('n')

    def south(self):
        return self._neighbor('s')

    def east(self):
        return self._neighbor('e')

    def west(self):
        return self._neighbor('w')
