import test_connect
from models import Author, Quote

list_quotes = []

def search_quote_by_tag(tag):
    quotes = Quote.objects(tags = tag)
    for qu in quotes:
        list_quotes.append(qu.quote)
    return list_quotes

def search_quote_by_tags(tags):
    tags.split(',')
    quotes = Quote.objects(tags__in = tags)
    for qu in quotes:
        list_quotes.append(qu.quote)
    return list_quotes

def search_quote_by_name(word):
    author_id = Author.objects(fullname = word).first().id
    if author_id:
        quotes = Quote.objects(author = author_id)
        for qu in quotes:
            list_quotes.append(qu.quote)
        return list_quotes
    else:
        print('No such author')
  
if __name__ == "__main__":

    test_connect

    while True:

        user_command = input('Please, input your command: ')
        command, *args = user_command.split(':')
        command.strip()

        if command == 'name':
            name = str(*args).strip()
            print(search_quote_by_name(name))

        elif command == 'tag':
            tag = str(*args).strip()
            print(search_quote_by_tag(tag))

        elif command == 'tags':  
            print(search_quote_by_tags(*args))

        elif command == 'exit':
            break

        else:
            print('unknown command')




