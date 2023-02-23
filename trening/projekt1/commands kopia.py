from database import Database
import click
from os import getenv 


@click.group()
def cli():
    pass

@click.command()
def setup():

    print('tworze  tabele w bazie danych')
    db = Database(getenv('DB-NAME')) 
    db.create_table('''CREATE TABLE urls (id INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT, url TEXT)''')        #tworzenie tabeli w d
    #                              nazwa ( kolumna 1                          , kolumna 2    , kolumna 3   )



@click.command()
@click.argument('category')
@click.argument('url')
def add(category: str, url: str):
    
    print('dodaje nowy url')
    db = Database(getenv('DB-NAME'))
    db.insert('urls', None, category, url)



@click.command()
@click.argument('category')
def index(category: str):

    print(f'lista linkow z kategorii: {category}')
    db = Database(getenv('DB-NAME'))
    links = db.fetch_all('urls', category=category)

    for link in links:
        print(link[2])



@click.command()
def fetch_catergories():

    print('lista kategorii: ')
    db = Database(getenv('DB-NAME'))
    catergories = db.fetch_distinct('urls', 'category')

    for name in catergories:
        print(name)
