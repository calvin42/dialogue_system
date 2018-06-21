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
from rasa_core.events import SlotSet, AllSlotsReset, Restarted
from rasa_core.interpreter import RasaNLUInterpreter, RegexInterpreter
from rasa_core.policies.memoization import MemoizationPolicy


from database_manager import MovieBuff
from gtts import gTTS
import random
import time

logger = logging.getLogger(__name__)

URI = "mysql://lus:lus@localhost:3306/lus"
slots = ["title", "actor_name", "actors_names", "director", 
        "year", "budget", "runtime", "genre", "country", 
        "language", "gross", "color", "score"
]

audio_folder = "/Users/claudio/CloudDrive/com~apple~CloudDocs/Magistrale/LUS/Part2/python/audio"


def didnt_get_title():
    sentences = [
        "I'm afraid I didn't understand the movie title",
        "I didn't understand the title of the movie",
        "Sorry, I didn't get the title"
    ]
    return random.choice(sentences)


class ActionRestarted(Action):
    def name(self):
        return "action_restarted"
    
    def run(self, dispatcher, tracker, domain):
        return [Restarted()]

class ActionAllSlotReset(Action):
    def name(self):
        return "action_slot_reset"

    def run(self, dispatcher, tracker, domain):
        return [AllSlotsReset()]


class ActionAskIfRightTitle(Action):
    def name(self):
        return "action_is_title_right"
    
    def run(self, dispatcher, tracker, domain):
        if tracker.get_slot("movie.name") is not None:
            dispatcher.utter_button_message("Is "+tracker.get_slot("movie.name")+" the movie you want me to search?", [{"yes": "Yes", "no": "No"}])
        else:
            dispatcher.utter_message(didnt_get_title())
        return []



#############################################################################################
#                                                                                           #
#                                                                                           #
#                                   Actions for one movie                                   #
#                                                                                           #
#                                                                                           #
#############################################################################################

class ActionSearchMovie(Action):
    def name(self):
        return "action_search_movie"
    
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("I'm searching for a movie")
        # director = tracker.get_slot("director")
        # movie = tracker.get_slot("movie")
        # producer = tracker.get_slot("producer")
        current_slots = {}
        for slot in slots:
            current_slots[slot] = tracker.get_slot(slot)
        movie_buff = MovieBuff(URI)

        # result = movie_buff.get_movie(director=director, movie=movie, producer=producer)
        result = movie_buff.get_titles(**current_slots)
        if result is None:
            dispatcher.utter_message("No movie found")
        else:
            dispatcher.utter_message("I found this: "+result[0])
        return [SlotSet("movie", result[0])]

class ActionSearchDirector(Action):
    def name(self):
        return "action_search_director"

    def resets_topic(self):
        return True

    def run(self, dispatcher, tracker, domain):
        # from telegram import Voice
        # from mutagen.mp3 import MP3
        movie = tracker.get_slot("movie.name")
        if movie is None:
            dispatcher.utter_message(didnt_get_title())
        else:
            movie_buff = MovieBuff(URI)
            logger.debug("movie: "+movie)
            result = movie_buff.get_director(movie)
            logger.debug("Result: "+str(result))
            if result is None:
                dispatcher.utter_message("I'm sorry, I searched everywhere but I found nothing")
            else:
                answer = "The director of "+movie+" is "+result
                # tts = gTTS(answer, lang='en')
                # tts.save(audio_folder+"/message.mp3")

                # audio = open(audio_folder+"/message.mp3", "rb")
                # audio_len = MP3(audio_folder+"/message.mp3").info.length
                # voice = Voice(audio, audio_len)
                # dispatcher.utter_audio(audio, answer)
                dispatcher.utter_message(answer)

                return [SlotSet("director.name", result)]
        

class ActionSearchYear(Action):
    def name(self):
        return "action_search_year"
    
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("I'm searching for the year of production")
        movie = tracker.get_slot("movie.name")
        if movie is None:
            dispatcher.utter_message(didnt_get_title())
        else:
            movie_buff = MovieBuff(URI)
            result = movie_buff.get_year(movie)
            if result is None:
                dispatcher.utter_message("I'm sorry, I searched everywhere but I found nothing")
            else:
                year = str(result)
                answer = "This movie was made in "+year
                dispatcher.utter_message(answer)
                return [SlotSet("movie.release_date",  str(result))]


class ActionSearchActor(Action):
    def name(self):
        return "action_search_actor"
    
    def run(self, dispatcher, tracker, domain):
        movie = tracker.get_slot("movie.name")
        if movie is None:
            dispatcher.utter_message(didnt_get_title())
        else:
            movie_buff = MovieBuff(URI)
            result = movie_buff.get_actors(movie)
            if result is None:
                dispatcher.utter_message("Either this is a movie without actors or I got nothing in my database")
            else:
                if "|" in result:
                    actor = result.split("|")[0]
                else:
                    actor = result
                dispatcher.utter_message("Maybe "+actor+" is the actor you are looking for")
                return [SlotSet("actor.name", actor)]

class ActionSearchCountry(Action):
    def name(self):
        return "action_search_country"
    
    def run(self, dispatcher, tracker, domain):
        movie = tracker.get_slot("movie.name")
        if movie is None:
            dispatcher.utter_message(didnt_get_title())
        else:
            movie_buff = MovieBuff(URI)
            result = movie_buff.get_country(movie)
            if result is None:
                dispatcher.utter_message("I guess it comes from nowhere, because I found nothing")
            else:
                dispatcher.utter_message(movie+" was made in "+result)
                return [SlotSet("movie.location", result)]

# class ActionSearchColor(Action):
    # def name(self):
    #     return "action_search_color"
    
    # def run(self, dispatcher, tracker, domain):
    #     movie = tracker.get_slot("movie.name")
    #     if movie is None:
    #         dispatcher.utter_message("Sorry, what was the name?")
    #     else:
    #         movie_buff = MovieBuff(URI)
    #         result = movie_buff.get_color(movie)
    #         if result is None:
    #             dispatcher.utter_message("I'm sorry, but I don't know :(")
    #         else:
    #             dispatcher.utter_message()

class ActionSearchBudget(Action):
    def name(self):
        return "action_search_budget"
    
    def run(self, dispatcher, tracker, domain):
        movie = tracker.get_slot("movie.name")
        if movie is None:
            dispatcher.utter_message("I'm afraid I didn't understand the movie title")
        else:
            movie_buff = MovieBuff(URI)
            result = movie_buff.get_budget(movie)
            if result is None:
                dispatcher.utter_message("I'm sorry, but I don't know :(")
            else:
                dispatcher.utter_message("The budget for this movie was "+str(result)+"$")
                return [SlotSet("movie.budget", result)]

class ActionSearchRating(Action):
    def name(self):
        return "action_search_rating"
    
    def run(self, dispatcher, tracker, domain):
        movie = tracker.get_slot("movie.name")
        if movie is None:
            dispatcher.utter_message(didnt_get_title())
        else:
            movie_buff = MovieBuff(URI)
            result = movie_buff.get_rating(movie)
            if result is None:
                dispatcher.utter_message("I'm sorry, but I don't know :(")
            else:
                dispatcher.utter_message("WIP")
                return []

class ActionSearchRuntime(Action):
    def name(self):
        return "action_search_duration"
    
    def run(self, dispatcher, tracker, domain):
        movie = tracker.get_slot("movie.name")
        if movie is None:
            dispatcher.utter_message(didnt_get_title())
        else:
            movie_buff = MovieBuff(URI)
            result = movie_buff.get_runtime(movie)
            if result is None:
                dispatcher.utter_message("I'm sorry, but I don't know :(")
            else:
                dispatcher.utter_message(movie+" last "+str(result)+" minutes")
                return [SlotSet("movie.runtime", result)]

class ActionSearchLanguage(Action):
    def name(self):
        return "action_search_language"
    
    def run(self, dispatcher, tracker, domain):
        movie = tracker.get_slot("movie.name")
        if movie is None:
            dispatcher.utter_message(didnt_get_title())
        else:
            movie_buff = MovieBuff(URI)
            result = movie_buff.get_language(movie)
            if result is None:
                dispatcher.utter_message("I'm sorry, but I don't know :(")
            else:
                dispatcher.utter_message(movie+" was filmed in "+result.lower())
                result [SlotSet("movie.language", result)]

class ActionSearchGross(Action):
    def name(self):
        return "action_search_gross"
    
    def run(self, dispatcher, tracker, domain):
        movie = tracker.get_slot("movie.name")
        if movie is None:
            dispatcher.utter_message(didnt_get_title())
        else:
            movie_buff = MovieBuff(URI)
            result = movie_buff.get_gross(movie)
            if result is None:
                dispatcher.utter_message("I'm sorry, but I don't know :(")
            else:
                dispatcher.utter_message("This movie earned "+str(result)+"$")
                return [SlotSet("movie.gross_revenue", result)]

class ActionSearchGenre(Action):
    def name(self):
        return "action_search_genre"
    
    def run(self, dispatcher, tracker, domain):
        vowels = ["a", "e", "i", "o", "u"]
        movie = tracker.get_slot("movie.name")
        if movie is None:
            dispatcher.utter_message(didnt_get_title())
        else:
            movie_buff = MovieBuff(URI)
            result = movie_buff.get_genre(movie)
            if result is None:
                dispatcher.utter_message("I'm sorry, but I don't know :(")
            else:
                genre = result.split("|")[0]
                if genre[0].lower() in vowels:
                    article = "an"
                else: 
                    article = "a"
                dispatcher.utter_message(movie+" is "+article+" movie")
                return [SlotSet("movie.genre", genre)]

class ActionCannotDoThis(Action):
    def name(self):
        return "action_cannot_do_this"
    
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("I'm sorry, but I'm afraid that I can't do that")

# class ActionAskMovieTitle(Action):
#     def name(self):
#         return "action_ask_movie_title"
        
#     def run(self, dispatcher, tracker, domain:
#         movie = tracker.get_slot("movie.name")

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
        movie = tracker.get_slot("movie.name")
        if movie is None:
            dispatcher.utter_message(didnt_get_title())
        else:
            movie_buff = MovieBuff(URI)
            result = movie_buff.get_actors(movie)
            if result is None:
                dispatcher.utter_message("Either this is a movie without actors or I got nothing in my database")
            else:
                results = []
                for el in result.split("|"):
                    if el != "":
                        results.append(el)
                
                if len(results) > 0:
                    dispatcher.utter_message("I got these actors: ")
                    for el in results:
                        dispatcher.utter_message("- "+el)
                return []


class ActionSearchMoviesList(Action):
    def name(self):
        return "action_search_movies_list"
    
    def run(self, dispatcher, tracker, domain):
        infos = {}
        for slot in slots:
            if tracker.get_slot(slot) is not None:
                infos[slot] = tracker.get_slot(slot)
        if len(infos.keys()) > 0:


class ActionShowActionsList(Action):
    def name(self):
        return "action_show_actions_list"
    
    def run(self, dispatcher, tracker, domain):
        actions_list = ''' I can search many things about a specific movie:
        \t- director
        \t- production year
        \t- three main actors
        \t- gross
        \t- production country
        \t- budget
        \t- duration
        \t- language spoken
        \t- genre
        \t- IMDb rating
        Or I can show you a list of everything that I listed before, plus movies.
        '''
        dispatcher.utter_messagge(actions_list)



'''
class ActionSearch(Action):
    def name(self):
        return "action_search_"
    
    def run(self, dispatcher, tracker, domain):
        pass
'''