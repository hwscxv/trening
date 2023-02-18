from sys import argv
from  database import Database                               
from os import getenv            #getenv 
from dotenv import load_dotenv   #getenv                 
load_dotenv()           #getenv

if len(argv) > 1 and argv[1] == "setup":
    '''
    initialize database 
    usage python main.py setup
    '''
    #jezeli argv zwraca wiecej niz 1 i druga pozycja to setup
    print('tworze  tabele w bazie danych')
    db = Database(getenv('DB-NAME')) 
    db.create_table('''CREATE TABLE urls (id INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT, url TEXT)''')        #tworzenie tabeli w d
    #                              nazwa ( kolumna 1                          , kolumna 2    , kolumna 3   )
if len(argv) == 4 and argv[1] == 'add':
    '''
        adding new resource with category
        usage: python yt_01.py add przyklady http//przyklad.pl
                            1    2         3                 4 
    '''
    print('dodaje nowy url')
    category = argv[2]
    url = argv[3]
    db = Database(getenv('DB-NAME'))
    db.insert('urls', None, category, url)

if len(argv) == 3  and argv[1] == 'list':
    '''
        usage: python main.py list category_name
    '''

    print('lista linkow z kategorii: ')
    category = argv[1]
    db = Database(getenv('DB-NAME'))
    links = db.fetch_all('urls', category=category)
#                 nazwa tabeli  
 
    for link in links:
        print(links)
