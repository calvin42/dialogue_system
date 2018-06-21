#python -m rasa_nlu.evaluate --data data/final.json --model project/default/model_20180530-140957
#python -m rasa_nlu.evaluate --verbose --data data/final.json --config data/config_spacy.yml --mode crossvalidation
python -m rasa_nlu.evaluate -d models/nlu/default/current/training_data.json -m models/nlu/default/current/
