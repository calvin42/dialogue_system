from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import logging
import warnings

# from policy import RestaurantPolicy, ScriptedPolicy
from rasa_core import utils
from rasa_core.actions import Action
from rasa_core.agent import Agent
from rasa_core.channels import HttpInputChannel
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.channels.telegram import TelegramInput
from rasa_core.events import SlotSet
from rasa_core.interpreter import RasaNLUInterpreter, RegexInterpreter
from rasa_core.policies.memoization import MemoizationPolicy


from database_manager import MovieBuff

URI = "mysql://lus:lus@localhost:3306/lus"

class ActionSearchMovie(Action):
    def name(self):
        return "action_search_movie"
    
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("I'm searching for a movie")
        director = tracker.get_slot("director")
        movie = tracker.get_slot("movie")
        producer = tracker.get_slot("producer")
        movie_buff = MovieBuff(URI)
        result = movie_buff.get_movie(director=director, movie=movie, producer=producer)
        return [SlotSet("movie", "WIP")]

#############################################################################################
#                                                                                           #
#                                                                                           #
#                                   Actions for one movie                                   #
#                                                                                           #
#                                                                                           #
#############################################################################################
    
class ActionSearchYear(Action):
    def name(self):
        return "action_search_year"
    
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("I'm searching the year of production")
        movie = tracker.get_slot("movie")
        movie_buff = MovieBuff(URI)
        year = movie_buff.get_year(movie=movie)
        if year is None:
            dispatcher.utter_message("I'm sorry, I searched everywhere but I found nothing")
        else:
            return [SlotSet("year",  str(year))]


class ActionSearchDirector(Action):
    def name(self):
        return "action_search_director"
    
    def run(self, dispatcher, tracker, domain):
        pass

class ActionSearchActor(Action):
    def name(self):
        return "action_search_actor"
    
    def run(self, dispatcher, tracker, domain):
        pass

class ActionSearchCountry(Action):
    def name(self):
        return "action_search_country"
    
    def run(self, dispatcher, tracker, domain):
        pass


class ActionSearchColor(Action):
    def name(self):
        return "action_search_color"
    
    def run(self, dispatcher, tracker, domain):
        pass

class ActionSearchBudget(Action):
    def name(self):
        return "action_search_budget"
    
    def run(self, dispatcher, tracker, domain):
        pass

class ActionSearchRating(Action):
    def name(self):
        return "action_search_rating"
    
    def run(self, dispatcher, tracker, domain):
        pass

class ActionSearchRuntime(Action):
    def name(self):
        return "action_search_duration"
    
    def run(self, dispatcher, tracker, domain):
        pass

class ActionSearchLanguage(Action):
    def name(self):
        return "action_search_language"
    
    def run(self, dispatcher, tracker, domain):
        pass

class ActionSearchGross(Action):
    def name(self):
        return "action_search_gross"
    
    def run(self, dispatcher, tracker, domain):
        pass

class ActionSearchGenre(Action):
    def name(self):
        return "action_search_genres"
    
    def run(self, dispatcher, tracker, domain):
        pass

#############################################################################################
#                                                                                           #
#                                                                                           #
#                                   Actions returning a list                                #
#                                                                                           #
#                                                                                           #
#############################################################################################

class ActionSearchActorsList(Action):
    def name(self):
        return "action_search_actors_list"
    
    def run(self, dispatcher, tracker, domain):
        pass


class ActionSearchMoviesList(Action):
    def name(self):
        return "action_search_movies_list"
    
    def run(self, dispatcher, tracker, domain):
        pass



class ActionCannotDoThis(Action):
    def name(self):
        return "action_cannot_do_this"
    
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("I'm sorry, but I'm afraid that I can't do that")
        
'''
class ActionSearch(Action):
    def name(self):
        return "action_search_"
    
    def run(self, dispatcher, tracker, domain):
        pass
'''