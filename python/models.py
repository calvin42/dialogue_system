'''
    Scorro
    creo entity
    tag O = controllo se entity ha un tag: si-> entity aggiunta alla lista | no -> niente
    tag B = controllo se entity ha un tag: si-> entity aggiunta alla lista e creo nuova entity | no -> aggiungo tag all'entity
    tag I = controllo blabla: si -> se e' lo stesso tag aggiungo value 
'''

class Entity():
    def __init__(self, start, end, value, entity):
        self.start = start
        self.end = end
        self.value = value
        self.entity = entity
        self.to_add = False

    def get_json(self):
        return {
            "start": self.start,
            "end": self.end,
            "value": self.value,
            "entity": self.entity
        }
    
    def find_start_end(self, text):
        try:
            i = text.index(self.value)
            j = i + len(self.value)
            self.start = i
            self.end = j    
        except:# Exception as err:
            print (text)
            print (self.value)
            print(text.index(self.value))

class Example():
    def __init__(self, text, intent, entities):
        self.text = text
        self.intent = intent
        self.entities = entities
    
    def get_json(self):
        return {
            "text": self.text,
            "intent": self.intent,
            "entities": [entity.get_json() for entity in self.entities]
        }

