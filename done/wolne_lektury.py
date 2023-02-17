from requests import get


def get_authors(search:str=None):
    authors = []
    query = get('https://wolnelektury.pl/api/authors/')  #przypisuje api do query
    for author_id, author in enumerate(query.json(), start=1):                               #przez kazdego autora w query typu json wypisz imie autora i href
        if search is not None or search in author['name']:
            # @TODO: convert author to object
            authors.append({
                "author_id": author_id,
                "name": author.get('name'),
                "api_books_url": author.get('href') + 'books'
            })
    return authors


authors = get_authors('Adam')
for author in authors:
    print(f'{author.get("author_id")}. {author.get("name")}')

# print(authors)
search_author_id = int(input('ktorego autora chcesz zobaczyc? '))

found_author = filter(lambda x: x.get('author_id') == search_author_id, authors)

print(next(found_author))