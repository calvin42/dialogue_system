from log_lib import print_log
import sqlsoup
import sys

class DatabaseManager():
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
    
    