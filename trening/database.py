import sqlite3
class Database:
    def __init__(self, database_name):                             #self robi ze zmiennej wlasciwosc klasy czyli dostepna w calej klasie, nie tylko w init
        self.connection = sqlite3.connect(database_name)          #polaczenie z baza danych przez modul sqlite3
        self.cursor = self.connection.cursor()                    # kursor z sqlite3 
    
    def __del__(self):                      #destruktor roozlacza polaczenie z db
        self.connection.close()
    
    def create_table(self, sql: str):
        self.cursor.execute(sql)
        self.connection.commit()

    def insert(self, table, *values):
        self.cursor.execute(f"INSERT INTO {table} VALUES ({','.join(['?' for _ in values])})", values)
        self.connection.commit()
    def fetch_all(self, table, **conditions):
        self.cursor.execute(f"SELECT * FROM {table} WHERE {' and '.join([f'{condition}=?' for condition in conditions])}")
