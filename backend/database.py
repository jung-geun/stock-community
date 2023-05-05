import datetime
import urllib.parse
from sqlalchemy import create_engine
from sqlalchemy import Column, TEXT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class Stock:
    def __init__(self, conn_data):

        conn_dialect = conn_data["dialect"]
        conn_driver = conn_data["driver"]
        conn_user = conn_data["user"]
        conn_passwd = urllib.parse.quote_plus(conn_data["password"])
        host = conn_data["host"]
        port = conn_data["port"]
        db_name = conn_data["database"]

        SQLALCHEMY_DATABASE_URL = f"{conn_dialect}+{conn_driver}://{conn_user}:{conn_passwd}@{host}:{port}/{db_name}?charset=utf8"
        self.engine = create_engine(
            SQLALCHEMY_DATABASE_URL, encoding="utf-8", echo=True
        )

    def connect(self):
        self.conn = self.engine.connect()
        return self.conn

    class Ant:
        def __init__(self, id, mail, name, passwd):
            self.id = id
            self.mail = mail
            self.name = name
            self.passwd = passwd
            self._INSERT_ANT = f"INSERT INTO ANT('id','mail','name','passwd') values({id},{mail},{name},{passwd})"
            self._UPDATE_ANT = f"UPDATE ANT SET mail={mail}, name={name}, passwd={passwd} WHERE id={id}"

        def __repr__(self):
            return f"Ant(id={self.id}, mail={self.mail}, name={self.name}, passwd={self.passwd})"

        def insert(self):
            conn = super.connect()
            sql = self._INSERT_ant
            conn.execute(sql)