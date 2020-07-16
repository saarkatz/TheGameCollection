import sys
import sqlite3
import os
import os.path

FOLDER = "Words"
CREATE_TABLE_QUERY = "CREATE TABLE IF NOT EXISTS {table}(word INTEGER PRIMARY KEY, json TEXT NOT NULL)"


def commit_to_db(dbname, query):
    """

    :param dbname:
    :param query:
    :return:
    """
    connect = sqlite3.connect(dbname)
    connect.execute(query)
    connect.commit()


def add_words_to_db(dbname, table, filename):
    with open(filename, 'r') as words_file:
        words_list = words_file.read().split("\r\n")


def main(dbname):
    for filename in os.listdir(FOLDER):
        base, extension = os.path.splitext(filename)
        if extension == ".json":
            with open("{0}//{1}".format(FOLDER, filename), 'r') as json_file:
                json = json_file.read()

                print("{0}".format(int(base)))

                connect.execute("INSERT OR REPLACE INTO rooms(id, json) VALUES(?, ?);", (int(base), json))
                connect.commit()


if __name__ == "__main__":
    main("hangman.db")
