from log_lib import print_log
import sqlsoup
import sys


class MovieBuff:
    def __init__(self, uri):
        self.db = sqlsoup.SQLSoup(uri)
        self.movie = self.db.Movie
        self.movies = self.db.Movies

    def commit(self):
        self.db.commit()
        print_log("Committed to db")

    def rollback(self):
        self.db.rollback
        print_log("Rolled back")

    def select_blueprint(self, select_query):
        try:
            select = select_query()
        except:
            e = sys.exc_info()
            print_log(e)
        if select is not None:
            return True
        return False

    def get_movie(self, **kwargs):
        movie = ""
        director = ""
        producer = ""
        year = ""
        for k, v in kwargs:
            if v is not None:
                key = k.lowercase()
                if key == "director":
                    director = v
                elif key == "movie":
                    movie = v
                elif key == "producer":
                    producer = v
                elif key == "year":
                    year = v
        self.movie.filter()
        return "movie"
    
    def get_director(self):
        return "director"
    
    def get_producer(self):
        return "producer"
    
    def get_year(self, **kwargs):
        movie = ""
        for k, v in kwargs:
            if v is not None:
                key = k.lowercase()
                if key == "movie":
                    movie = v
                    something_found = True
        if something_found:
            m1 = self.movie.filter(self.movie.title==movie).one()
            m2 = self.movies.filter(self.movies.movie_title==movie).one()
            if m1 is not None:
                return m1.year
            elif m2 is not None:
                return m2.title_year
            else:
                return None
            

#TODO implementare la ricerca nel db dei film, dei registi etc
 
# class MovieBuff:
#     def __init__(self, uri):
#         self.dbm = DatabaseManager(uri)
#         self.dbm.movie
    