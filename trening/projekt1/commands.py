import click
from database import Database
from os import getenv 
from repositories.urls import save_command, fetch_categories, fetch_urls

@click.group()
def cli():
    pass



@click.command(name='setup')
def setup_command():

    print('tworze  tabele w bazie danych')
    db = Database(getenv('DB-NAME')) 
    db.create_table('''CREATE TABLE urls (id INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT, url TEXT)''')        #tworzenie tabeli w d
    #                              nazwa ( kolumna 1                          , kolumna 2    , kolumna 3   )




@click.command(name='add')
@click.argument('category')
@click.argument('url')
def add_command(category: str, url: str):
    print('dodaje nowy url')
    save_command(category, url)
    



@click.command(name='index')
@click.argument('category')
def index_command(category: str):
    print(f'lista linkow z kategorii: {category}')
    for link in fetch_urls(category):
        print(link[2])




@click.command(name='categories')
def list_command():
    print('lista kategorii: ')

    for name in fetch_categories():
        print(name)
