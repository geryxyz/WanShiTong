# Adatbázis kapcsoló modul
import os
import sqlite3


class Database:

    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def __init__(self, *args):
        # print(os.getcwd())
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "wst-db.sqlite")
        print(db_path)
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = self.dict_factory
        # self.testconn()

    def query(self, sqlc, params):
        cur = self.conn.cursor()
        cur.execute(sqlc, params)
        output = cur.fetchall()
        return output

    def query_and_return_in_dict(self, sqlc, params):
        cur = self.conn.cursor()
        cur.execute(sqlc, params)
        output = cur.fetchall()
        return output

    def queryandcommit(self, sqlc, params):
        cur = self.conn.cursor()
        cur.execute(sqlc, params)
        self.conn.commit()
        output = cur.fetchall()

    def testconn(self):
        print("Adatbázis kapcsolat tesztelése...")
        cur = self.conn.cursor()
        cur.execute("select sqlite_version()")
        output = cur.fetchall()
        print(output)

