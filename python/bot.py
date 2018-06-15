from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core import utils
from rasa_core.actions import Action
from rasa_core.agent import Agent
from rasa_core.events import SlotSet
from rasa_core.channels import HttpInputChannel
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.channels.telegram import TelegramInput
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.interpreter import RasaNLUInterpreter, RegexInterpreter




import argparse
import logging

logger = logging.getLogger(__name__)


def train_dialogue():
    domain_file = "domain.yml"
    model_path="model/dialogue"
    training_data = "data/stories.md"
    agent = Agent(domain_file, policies=[KerasPolicy()])

    agent.train(training_data, max_history=3, epochs=1000, batch_size=100, validation_split=0.2)

    agent.persist(model_path)
    
    return agent


def train_nlu():
    from rasa_nlu.training_data import load_data
    from rasa_nlu import config
    from rasa_nlu.model import Trainer

    training_data = load_data("data/final.json")
    trainer = Trainer(config.load("data/congif_spacy.yml"))
    trainer.train(training_data)
    model_directory = trainer.persist("models/nlu/", fixed_model_name="current")

    return model_directory

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

    training_data_file = "data/stories.md"

    interpreter = RasaNLUInterpreter("models/nlu/default/current")

    agent = Agent.load("model/dialogue", interpreter=interpreter)
    
    # input_channel = get_input_channel("22af799c")
    input_channel = get_input_channel()
    
    agent.train_online(
                training_data_file,
                max_history=3,
                epochs=1000,
                batch_size=100
        )

    # agent.train(
    #         training_data_file,
    #         max_history=3,
    #         epochs=100,
    #         batch_size=100
    # )

    # agent.handle_channel(HttpInputChannel(5004,"/", input_channel))
    agent.handle_channel(input_channel)

    return agent

utils.configure_colored_logging(loglevel="INFO")

# train_nlu()
# train_dialogue()
run()