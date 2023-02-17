from sys import argv
import sqlite3
from os import getenv
from dotenv import load_dotenv
load_dotenv()


class Database:
    def __init__(self, database_name):
        self.connection = sqlite3.connect(database_name)          #polaczenie z baza danych przez modul sqlite3
        self.cursor = self.connection.cursor()                    # kurson
    
    def __del__(self):
        self.connection.close()
    
    def create_table(self, sql: str):
        self.cursor.execute(sql)
        self.connection.commit()




if len(argv) > 1 and argv[1] == "setup":    #jezeli argv zwraca wiecej niz 1 i druga pozycja to setup
    print('tworze baze danych')
    db = Database(getenv('DB-NAME')) 
    db.create_table('''CREATE TABLE urls (id INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT, url TEXT)''')        #tworzenie tabeli w db

if len(argv) == 4 and argv[2] == 'add':
    print('dodaje nowy url')


