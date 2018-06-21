from log_lib import print_log
from sqlalchemy import or_, and_
import logging
import difflib
import sqlsoup
import sys

logger = logging.getLogger(__name__)

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
        # logger.debug("kwargs: "+kwargs)
        for k in kwargs:
            v = kwargs[k]
            if v is not None:
                if k == "title":
                    if v[-1] == "?" or v[-1]== "!":
                        v = v[:-1]
                    select = and_(select, self.movie.title.ilike("%"+v+"%"))
                    if not at_least_one:
                        at_least_one = not at_least_one
                elif k == "director":
                    select = and_(select, self.movie.director.ilike("%"+v+"%"))
                    if not at_least_one:
                        at_least_one = not at_least_one
                elif k == "budget":
                    select = and_(select, self.movie.budget.ilike("%"+v+"%"))
                    if not at_least_one:
                        at_least_one = not at_least_one
                elif k == "language":
                    select = and_(select, self.movie.language.ilike("%"+v+"%"))
                    if not at_least_one:
                        at_least_one = not at_least_one
                elif k == "year":
                    select = and_(select, self.movie.year.ilike("%"+v+"%"))
                    if not at_least_one:
                        at_least_one = not at_least_one
                elif k == "runtime":
                    select = and_(select, self.movie.duration.ilike("%"+v+"%"))
                    if not at_least_one:
                        at_least_one = not at_least_one
                elif k == "score":
                    select = and_(select, self.movie.rating.ilike("%"+v+"%"))
                    if not at_least_one:
                        at_least_one = not at_least_one
                elif k == "actor":
                    select = and_(select, self.movie.actors.ilike("%"+v+"%"))
                    if not at_least_one:
                        at_least_one = not at_least_one
                elif k == "genre":
                    select = and_(select, self.movie.genres.ilike("%"+v+"%"))
                    if not at_least_one:
                        at_least_one = not at_least_one
                elif k == "country":
                    select = and_(select, self.movie.country.ilike("%"+v+"%"))
                    if not at_least_one:
                        at_least_one = not at_least_one
                elif k == "gross":
                    select = and_(select, self.movie.gross.ilike("%"+v+"%"))
                    if not at_least_one:
                        at_least_one = not at_least_one
        if at_least_one:
            return select
        return None


    def get_movie(self, **kwargs):
        # Type (**kwargs) -> List
        select = self.build_select_filter_movie(**kwargs)
        if select is not None:
            result = self.movie.filter(select).all()
            return result
        else:
            return None


    def check_list(self, results, title):
        # Type(List, Text) -> Text
        match = {}
        for result in results:
            match[result.title] = result

        res = difflib.get_close_matches(title, match.keys())
        if len(res) > 0:
            best = res[0]
            return match[best]
        else:
            return None



 
##############################################################################
##############################################################################
##############################################################################

##############################################################################
##############################################################################
##############################################################################

    #############################
    #           TITLES          #
    #############################
    def get_titles(self, **kwargs):
        result = None
        select = self.build_select_filter_movie(**kwargs)
        if select is not None:
            result = self.movie.filter(select)
            if result is not None:
                return result.all()
            else:
                return None
    #############################
    #          DIRECTOR         #
    #############################
    def get_director(self, title):
        result = self.get_movie(title=title)
        if result is not None:
            check = self.check_list(result, title)
            if check is not None:
                return check.director
        return None
    #############################
    #            YEAR           #
    #############################
    def get_year(self, title):
        result = self.get_movie(title=title)
        if result is not None:
            check = self.check_list(result, title)
            if check is not None:
                return check.year
        return None
    #############################
    #           ACTORS          #
    #############################
    def get_actors(self, title):
        result = self.get_movie(title=title)
        if result is not None:
            check = self.check_list(result, title)
            if check is not None:
                return check.actors
        return None
    #############################
    #          COUNTRY          #
    #############################
    def get_country(self, title):
        result = self.get_movie(title=title)
        if result is not None:
            check = self.check_list(result, title)
            if check is not None:
                return check.country
        return None
    #############################
    #           COLOR           #
    #############################
    def get_color(self, title):
        result = self.get_movie(title=title)
        if result is not None:
            check = self.check_list(result, title)
            if check is not None:
                return check.color
        return None
    #############################
    #           BUDGET          #
    #############################
    def get_budget(self, title):
        result = self.get_movie(title=title)
        if result is not None:
            check = self.check_list(result, title)
            if check is not None:
                return check.budget
        return None
    #############################
    #           RATING          #
    #############################
    def get_rating(self, title):
        result = self.get_movie(title=title)
        if result is not None:
            check = self.check_list(result, title)
            if check is not None:
                return check.rating
        return None
    #############################
    #          RUNTIME          #
    #############################
    def get_runtime(self, title):
        result = self.get_movie(title=title)
        if result is not None:
            check = self.check_list(result, title)
            if check is not None:
                return check.duration
        return None
    #############################
    #           LANGUAGE           #
    #############################
    def get_language(self, title):
        result = self.get_movie(title=title)
        if result is not None:
            check = self.check_list(result, title)
            if check is not None:
                return check.language
        return None
    #############################
    #           GROSS           #
    #############################
    def get_gross(self, title):
        result = self.get_movie(title=title)
        if result is not None:
            check = self.check_list(result, title)
            if check is not None:
                return check.gross
        return None
    #############################
    #           GENRE           #
    #############################
    def get_genre(self, title):
        result = self.get_movie(title=title)
        if result is not None:
            check = self.check_list(result, title)
            if check is not None:
                return check.genres
        return None


#TODO implementare la ricerca nel db dei film, dei registi etc
 
# class MovieBuff:
#     def __init__(self, uri):
#         self.dbm = DatabaseManager(uri)
#         self.dbm.movie


