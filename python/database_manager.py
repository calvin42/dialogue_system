from log_lib import print_log
from sqlalchemy import or_, and_
import sqlsoup
import sys


class MovieBuff:
    def __init__(self, uri):
        self.db = sqlsoup.SQLSoup(uri)
        self.movie = self.db.Movie
        self.movies = self.db.Movies
        self.actor = ""
        self.budget = 0
        self.country = ""
        self.runtime = 0
        self.rate = float(0)
        self.year = 0
        self.gross = 0
        self.languate = ""
        self.movie_name = ""

    def commit(self):
        self.db.commit()
        print_log("Committed to db")

    def rollback(self):
        self.db.rollback
        print_log("Rolled back")

    def build_select_filter_movie(self, **kwargs):
        at_least_one = False
        select = and_()
        for k, v in kwargs:
            if v is not None:
                if k == "title":
                    select = and_(select, self.movie.title==v)
                    if not at_least_one:
                        at_least_one = not at_least_one
                elif k == "director":
                    select = and_(select, self.movie.director==v)
                    if not at_least_one:
                        at_least_one = not at_least_one
                elif k == "budget":
                    select = and_(select, self.movie.budget==v)
                    if not at_least_one:
                        at_least_one = not at_least_one
                elif k == "language":
                    select = and_(select, self.movie.language==v)
                    if not at_least_one:
                        at_least_one = not at_least_one
                elif k == "year":
                    select = and_(select, self.movie.year==v)
                    if not at_least_one:
                        at_least_one = not at_least_one
                elif k == "runtime":
                    select = and_(select, self.movie.duration==v)
                    if not at_least_one:
                        at_least_one = not at_least_one
                elif k == "score":
                    select = and_(select, self.movie.rating==v)
                    if not at_least_one:
                        at_least_one = not at_least_one
                elif k == "actor":
                    select = and_(select, self.movie.actors.like("%"+v+"%"))
                    if not at_least_one:
                        at_least_one = not at_least_one
                elif k == "genre":
                    select = and_(select, self.movie.genres==v)
                    if not at_least_one:
                        at_least_one = not at_least_one
                elif k == "country":
                    select = and_(select, self.movie.country)
                    if not at_least_one:
                        at_least_one = not at_least_one
                elif k == "gross":
                    select = and_(select, self.movie.gross==v)
                    if not at_least_one:
                        at_least_one = not at_least_one
        if at_least_one:
            return select
        return None

##############################################################################
##############################################################################
##############################################################################

##############################################################################
##############################################################################
##############################################################################


    def get_movie(self, **kwargs):
        result = None
        select = self.build_select_filter_movie(**kwargs)
        if select is not None:
            result = self.movie.filter(select)
            if result is not None:
                return result.all()
            else:
                return None
    
    def get_director(self, movie):
        result = None
        select = self.build_select_filter_movie(title=movie)
        if select is not None:
            result = self.movie.filter(select)
            if result is not None:
                return result.first().director
        return None
    
    
    def get_year(self, **kwargs):
        result = None
        select = self.build_select_filter_movie(**kwargs)
        if select is not None:
            result = self.movie.filter(select)
            if result is not None:
                return result.first().year
        return None
    def get_country(self, movie):
        result = None
        select = self.build_select_filter_movie(title=movie)
        if select is not None:
            result = self.movie.filter(select)
            if result is not None:
                return result.first().country
        return None
            

#TODO implementare la ricerca nel db dei film, dei registi etc
 
# class MovieBuff:
#     def __init__(self, uri):
#         self.dbm = DatabaseManager(uri)
#         self.dbm.movie
    