from ast import parse
from snips_nlu import SnipsNLUEngine
# from db import LibraryDatabase
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, TrigramSimilarity
from django.db.models.functions import Cast
from enum import Enum
from .models import *

from .views import *
class Status(Enum):
    SUCCESSFULL = 1
    INTENT_NOT_FOUND = 2
    SLOT_NOT_FOUND = 3


class NLUEngine():
    def __init__(self):
        self.engine = SnipsNLUEngine.from_path('./model')
        self.intents = {
            'searchBook': {'slots_required': True, 'function': self.search_book},
            'searchByAuthor': {'slots_required': True, 'function': self.search_books_by_author},
            'summarizeBook': {'slots_required': True, 'function': self.search_book},
            'searchByGenre': {'slots_required': True, 'function': self.search_books_by_genre}
        }
       

    def parse(self, text):
        return self.engine.parse(text)

    def get_results(self, text):
        parsed_text = self.parse(text)
        print("PARSED TEXT",parsed_text)
        if parsed_text['intent']['intentName']:
            intent = parsed_text['intent']['intentName']
            if self.intents[intent]['slots_required']:
                if parsed_text['slots']:
                    intent_func = self.intents[intent]['function']
                    value = parsed_text['slots'][0]['value']['value']
                    
                    return {
                        'intent': intent,
                        'result': intent_func(value),
                        'value': value,
                        'status': Status.SUCCESSFULL
                    }
                else:
                    return {
                        'intent': intent,
                        'result': None,
                        'status': Status.SLOT_NOT_FOUND
                    }
            else:
                intent_func = self.intents[intent]
                return {
                    'intent': intent,
                    'result': intent_func(),
                    'status': Status.SUCCESSFULL
                }

        else:
            return {"intent": None, 'data': None, 'status': Status.INTENT_NOT_FOUND}

    def search_book(self,book_name):
        #Write all functions here.
        print("Book Name",book_name)
        book = Book.objects.filter(title= 'Vanished')
        print("Books",book)
        book_serialize = BookSerializer(book,many=True)
        print("Result:",book_serialize)
        return book_serialize.data

    def search_books_by_author(self, author_name, count=10):
     
       books_by_author = Book.objects.filter(author__name__search=author_name) # This is full text search, but it won't account for spelling mistakes
       book_serialize = BookSerializer(books_by_author,many=True)
       print("Result:",book_serialize)
       return book_serialize.data
        

    def search_books_by_genre(self, genre, count=10):
      
        books_by_genre = Book.objects.filter(category__category__search=genre)
        book_serialize = BookSerializer(books_by_genre,many=True)
        print("Result:",book_serialize)
        return book_serialize.data
        



# print(NLUEngine().get_results('abra cadabra'))
