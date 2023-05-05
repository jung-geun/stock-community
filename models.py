import json

from database import Stock
from database.Stock import Ant

if __name__ == "__main__":
    with open("db.json", "r") as db:
        db_data = json.load(db)
    db = Stock(conn_data=db_data)
    
    db.Ant()
    # stock = Stock()

    # stock.Ant("test", "test@example.com", "test", "test")

    # print(2)
