import datetime
import urllib.parse

from dataclasses import dataclass

import pymysql
from sqlalchemy import create_engine
from sqlalchemy import Column, TEXT, VARCHAR
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os
import json

class Stock:
    def __init__(self, conn_data: dict):
        conn_dialect = conn_data["dialect"]
        conn_driver = conn_data["driver"]
        conn_user = conn_data["user"]
        conn_passwd = urllib.parse.quote_plus(conn_data["password"])
        host = conn_data["host"]
        port = conn_data["port"]
        db_name = conn_data["database"]
        try:
            SQLALCHEMY_DATABASE_URL = f"{conn_dialect}+{conn_driver}://{conn_user}:{conn_passwd}@{host}:{port}/{db_name}?charset=utf8mb4"
            self.__engine = create_engine(
                SQLALCHEMY_DATABASE_URL, echo=True
            )
            # self.conn = pymysql.connect(
            #     host=host,
            #     port=port,
            #     user=conn_user,
            #     password=conn_passwd,
            #     charset="utf8mb4",
            # )
            print("DB connected")
        except Exception as e:
            print(e)
            raise e

    def _connect(self):
        try:
            conn = self.__engine.connect()
        except Exception as e:
            print(e)
            conn = None
            raise e
        finally:
            return conn

@dataclass
class Ant_Data:
    seq_id:int = None
    id :str= None
    mail:str = ''
    name:str = ''
    passwd:str = ''
    regdate:datetime = None
    moddate:datetime = None
class Ant(Stock):
    def __init__(self, conn_data:dict,seq_id:int=None, id:str=None, mail:str=None, name:str=None, passwd:str=None, regdate:datetime=None, moddate:datetime=None):
        self.vo = Ant_Data()
        self.seq_id = seq_id
        self.vo.id = id
        self.vo.mail = mail
        self.vo.name = name
        self.vo.passwd = passwd
        self.vo.regdate = regdate
        self.vo.moddate = moddate
        
        super().__init__(conn_data)
        
        self.__SELECT_ANT = f"SELECT * FROM ant"
        self.__INSERT_ANT = f"INSERT INTO ant('id','mail','name','passwd') values('{id}','{mail}','{name}','{passwd}')"
        self.__UPDATE_ANT = f"UPDATE ant SET mail='{mail}', name='{name}', passwd='{passwd}' WHERE id='{id}'"
        self.__DELETE_ANT = f"DELETE FROM ant WHERE id='{id}'"
        

    def __repr__(self):
        return f"Ant(id={self.vo.id}, mail={self.vo.mail}, name={self.vo.name}, passwd={self.vo.passwd})"
    
    # 전체 출력
    def select(self, id:str = None):
        print("select")
        conn = super()._connect()
        sql = self.__SELECT_ANT
        if id:
            insert_sql += f" WHERE id='{id}'"
        if conn:
            try:
                result = conn.execute(sql).fetchall()
            except Exception as e:
                print(e)
                result = None
                raise e
            finally:
                conn.close()
        else :
            result = None
        return result                      
    
    def insert(self, id:str, mail:str, name:str, passwd:str):
        print("insert")
        conn = super()._connect()
        sql = self.__INSERT_ANT
        if conn:
            try:
                result = conn.execute(sql)
            except Exception as e:
                print(e)
                result = None
                raise e
            finally:
                conn.close()
        else :
            result = None
        return result
    
                                      
if __name__ == "__main__":
    # dir_path = os.getcwd()
    # file_list = os.listdir(dir_path)
    # print(file_list)
    with open("./backend/db.json", "r") as f:
        conn_data = json.load(f)
        
    stock = Ant(conn_data)
    # print(stock.__repr__())
    result = stock.select(id="test")
    print(result)