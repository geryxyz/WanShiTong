# Adatbázis kapcsoló modul
import sqlite3


class Database():
    def __init__(self, *args):
        self.conn = pymysql.connect(*args)
        self.testconn()

    def query(self, sqlc, params):
        cur = self.conn.cursor(pymysql.cursors.DictCursor)
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
        cur.execute("select @@version")
        output = cur.fetchall()
        print(output)
