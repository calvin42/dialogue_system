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

    