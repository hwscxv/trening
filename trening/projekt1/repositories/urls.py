from database import Database
from os import getenv            #getenv 


def save_command(category: str, url: str):
    db = Database(getenv('DB-NAME'))
    db.insert('urls', None, category, url)

def fetch_categories():
    db = Database(getenv('DB-NAME'))
    return db.fetch_distinct('urls', 'category')

def fetch_urls(category):
    db = Database(getenv('DB-NAME'))
    return  db.fetch_all('urls', category=category)