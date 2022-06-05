import argparse
from database import Database
import hashlib
import datetime


if __name__ == '__main__':
    my_parser = argparse.ArgumentParser(description="Details of the user")
    my_parser.add_argument('Username', metavar='username', type=str, help="The username")
    my_parser.add_argument('Password', metavar='password', type=str, help="The password")
    args = my_parser.parse_args()

    username = args.Username
    password = args.Password

    db = Database("wst-db.sqlite")
    password_hashed = hashlib.md5(password.encode('utf-8')).hexdigest()

    sqlc = '''INSERT INTO users (username, password, regdate) VALUES (?, ?, ?)'''
    db.queryandcommit(sqlc, (username, password_hashed, datetime.datetime.now()))
    print("User succesfully registered. Username: "+username+", password: "+password)
