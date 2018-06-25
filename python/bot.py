# encoding=utf8  
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core import utils
from rasa_core.actions import Action
from rasa_core.agent import Agent
from rasa_core.events import SlotSet
from rasa_nlu.training_data import load_data
from rasa_core.channels import HttpInputChannel
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.channels.telegram import TelegramInput
# from rasa_core.featurizers import MaxHistoryTrackerFeaturizer, BinarySingleStateFeaturizer
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.interpreter import RasaNLUInterpreter, RegexInterpreter




import argparse
import logging
import sys

logger = logging.getLogger(__name__)
reload(sys)  
sys.setdefaultencoding('utf8')

TRAINING_DATA = "exact.json"
NLU_CONFIG = "data/config_nlu.yml"

MODEL_DIRECTORY = "model/nlu/default/current"
MODEL_DIRECTORY_TENSORFLOW = "model/tensorflow_nlu/default/current"
DOMAIN = "domain.yml"
MODEL_DIALOGUE = "model/dialogue"
MODEL_DIALOGUE_TENSORFLOW = "model/tensorflow_dialogue"


STORIES = "stupid_stories.md"


def train_nlu():
    from rasa_nlu.training_data import load_data
    from rasa_nlu import config
    from rasa_nlu.model import Trainer

    training_data = load_data(TRAINING_DATA)
    trainer = Trainer(config.load(NLU_CONFIG))
    trainer.train(training_data)
    model_directory = trainer.persist("model/nlu/", fixed_model_name="current")
    # model_directory = trainer.persist("model/tensorflow_nlu/", fixed_model_name="current")
    
    return model_directory

def train_dialogue():
    interpreter = RasaNLUInterpreter(MODEL_DIRECTORY)
    # interpreter = RasaNLUInterpreter(MODEL_DIRECTORY_TENSORFLOW)
    agent = Agent(DOMAIN, policies=[MemoizationPolicy(max_history=3), KerasPolicy()], interpreter=interpreter)
    # training_data = agent.load_data(STORIES)    
    training_data = STORIES    
    agent.train(training_data, epochs=100, batch_size=100, validation_split=0.2)
    agent.persist(MODEL_DIALOGUE)
    # agent.persist(MODEL_DIALOGUE_TENSORFLOW)

    # input_channel = get_input_channel()
    # agent.train_online(
    #             training_data,
    #             input_channel=input_channel,
    #             epochs=100,
    #             batch_size=100
    #     )
    return agent


def get_input_channel(ip=None):
    if ip is not None:
        input_channel = TelegramInput(
            access_token="583835183:AAF9oo9QpLzWS7I_IQ4f_j0Um-HzH6TK9n4", # you get this when setting up a bot
            verify="KerovAssistantBot", # this is your bots username
            webhook_url="https://"+ ip +".ngrok.io/webhook" # the url your bot should listen for messages
        )
    else:
        input_channel = ConsoleInputChannel()
    return input_channel


def run(serve_forever=True):
    # training_data_file = "data/stories.md"
    interpreter = RasaNLUInterpreter("model/nlu/default/current")
    # training_data = agent.load_data(STORIES)   

    agent = Agent.load(MODEL_DIALOGUE, interpreter=interpreter)
    # agent = Agent.load(MODEL_DIALOGUE_TENSORFLOW)#, interpreter=interpreter)
     
    # input_channel = get_input_channel()
    # agent.handle_channel(input_channel)
    
    input_channel = get_input_channel("dda3ac6e")
    agent.handle_channel(HttpInputChannel(5004,"/", input_channel))

    return agent

# utils.configure_colored_logging(loglevel="INFO")

# train_nlu()
# train_dialogue()
# run()

if __name__ == '__main__':
    utils.configure_colored_logging(loglevel="INFO")

    parser = argparse.ArgumentParser(
            description='starts the bot')

    parser.add_argument(
            'task',
            choices=["train-nlu", "train-dialogue", "run"],
            help="what the bot should do - e.g. run or train?")
    task = parser.parse_args().task

    # decide what to do based on first parameter of the script
    if task == "train-nlu":
        train_nlu()
    elif task == "train-dialogue":
        train_dialogue()
    elif task == "run":
        run()
    else:
        warnings.warn("Need to pass either 'train-nlu', 'train-dialogue' or "
                      "'run' to use the script.")
        exit(1)