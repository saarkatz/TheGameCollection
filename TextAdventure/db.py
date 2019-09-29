import sys
import sqlite3
import os
import os.path

PATH = "rooms"


def main(dbname):
    connect = sqlite3.connect(dbname)
    connect.execute("CREATE TABLE IF NOT EXISTS rooms(id INTEGER PRIMARY KEY, json TEXT NOT NULL)")
    connect.commit()

    for filename in os.listdir(PATH):
        base, extension = os.path.splitext(filename)
        if extension == ".json":
            with open("{0}//{1}".format(PATH, filename), 'r') as json_file:
                json = json_file.read()

                print("Inserting room {0}".format(int(base)))

                connect.execute("INSERT OR REPLACE INTO rooms(id, json) VALUES(?, ?);", (int(base), json))
                connect.commit()


if __name__ == "__main__":
    main("rooms.db")
