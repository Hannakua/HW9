import json
import test_connect
from models import Author, Quote


def load_save_data_from_json():

    with open('authors.json', 'r', encoding='utf-8') as au:
        authors_ = json.load(au)


    with open('quotes.json', 'r', encoding='utf-8') as qu:
        quotes_ = json.load(qu)

    for author_ in authors_:
        author_db_note = Author(**author_)
        author_db_note.save()

    
    for quote_ in quotes_:

        author_name = quote_.get('author')
        
        authors_all = Author.objects()

        for auth in authors_all:
            if auth.fullname == author_name:
                quote_['author'] = auth.id
                quote_db_note = Quote(**quote_)
                quote_db_note.save()



if __name__ == "__main__":
    test_connect
    load_save_data_from_json()