# from database_manager import DatabaseManager
# import rasa
from models import Entity, Example
import log_lib
import json
import sys
folder = "../intents_db/"
# SQLALCHEMY_DATABASE_URI = "mysql://lus:lus@password@localhost:3306/lus"
train_data = "NLSPARQL.train.data"
train_labels = "NLSPARQL.train.utt.labels.txt"

test_data = "NLSPARQL.test.data"
test_labels = "NLSPARQL.test.utt.labels.txt"


# dbm = DatabaseManager(SQLALCHEMY_DATABASE_URI)

cant = [
    "other",
    "media",
    "info",
    "birth_date",
    "character",
    "composer",
    "producer_count",
    "organization",
    "person",
    "person_name",
    "producer",
    "rating ",
    "subjects",
    "writer",
    "movie_other",
    "award",
    "picture",
    "review",
    "synopsis",
    "theater",
    "trailer",
    "award_count",
    "award_category_count"
]

def transform_intent(intent):
    if intent == "director":
        return "director_name"
    if intent == "actor":
        return "actor_name"
    if " " in intent:
        intent = intent.replace(" ", "_and_")
    elif intent in cant:
        return "other"
    return intent


# devo:
# creare la frase per text
# mettere l'intent (dal file delle label)
# usare i tag per capire le entities
# dentro le entities trovare la posizione che corrisponde in text (indexOf penso vada bene)
# quindi parso il dataset fino al prossimo \n
# quando trovo un tag B-qualcosa quello è un pezzo di una entity, quindi continuando a leggere, 
#       se c'eè il tag I-qualcosa continuo ad aggiungere a quello che poi sarà "value" della entity
examples = []
ex = Example(None, None, [])
cur_entity = Entity(0,0,None, None)
text = ""
entities = []
with open(folder+train_data, "r") as tr:
    with open(folder+train_labels, "r") as lb:
        for line in tr.readlines():
            if line == "\n":
                if cur_entity.to_add:
                    entities.append(cur_entity)

                cur_label = lb.readline()
                ex.text = text
                ex.intent = transform_intent(cur_label.split("\n")[0])
                for ent in entities:
                    ent.find_start_end(ex.text)
                    ex.entities.append(ent)
                examples.append(ex)
                ex = Example(None, None, [])  
                text = ""
                entities = []
                cur_entity = Entity(0,0,None, None)

            else:
                word, tag = line.split("\t")
                if text == "":
                    text = word
                else:
                    text = text + " " + word
                tag = tag.split("\n")[0]
                if tag == "O":
                    if cur_entity.entity is not None:

                        entities.append(cur_entity)
                        cur_entity = Entity(0,0,None,None)
                elif tag.startswith("B"):
                    if cur_entity.entity is not None:

                        entities.append(cur_entity)
                        cur_entity = Entity(0,0,word, tag[2:])
                    else:
                        cur_entity.entity = tag[2:]
                        cur_entity.value = word
                        cur_entity.to_add = True
                elif tag.startswith("I"):
                    if cur_entity is not None:
                        if cur_entity.entity == tag[2:]:
                            cur_entity.value = cur_entity.value + " " + word
                            cur_entity.to_add = True





final_json = {
        "rasa_nlu_data": {
            "common_examples": [example.get_json() for example in examples],
            "entity_examples": [],
            "intent_examples": []
        }
    }
with open("basic_intents.json") as f:
    data = json.load(f)
    for el in data:
        final_json["rasa_nlu_data"]["common_examples"].append(el)


with open("exact.json", "w") as j:
    json.dump(final_json, j)