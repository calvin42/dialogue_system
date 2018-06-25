# Language Understanding Systems --- Final project - Dialog System within Rasa framework in movie domai

## Requirements
This project requires the installation of the following libraries for python 2.7:
<!-- 1. [OpenGRM](http://www.opengrm.org/twiki/bin/view/GRM/WebHome) and [OpenFST](http://www.openfst.org/twiki/bin/view/FST/WebHome) for command line. -->
1. mysqldb
2. sqlsoup
3. rasa_core 0.9.0a3
4. rasa_nlu 12.3

## Dataset conversion
To convert the dataset simply write ```python converter.py``` and the script will convert the dataset in the json format.

## Training and execution of the bot
The bot is called with one of the following parameters: "train-nlu", "train-dialogue or "run".
### train-nlu
With this parameter the script will train the NLU. This is the first step to be done to train the bot.
### train-dialogue
The script will train the dialogue maneger loading the NLU created before.
### run
The script will run the bot, which will listen in the console prompt.

