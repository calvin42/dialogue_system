seen = []
def train():
    with open("../intents_db/NLSPARQL.train.data", "r") as f:
        for line in f.readlines():
            if line != "\n":
                splitted = line.split("\t")[1]
                if splitted not in seen and "-" in splitted:
                    seen.append(splitted)

def label():
    with open("../intents_db/NLSPARQL.train.utt.labels.txt", "r") as  f:
        for line in f.readlines():
            if line not in seen:
                seen.append(line)


def prepare_intents():
    
    intents = []
    for s in seen:
        if " " in s:
            splitted = s.split(" ")
            for tag in splitted:
                if "\n" in tag:
                    tag = tag[:-1]
                if tag not in intents:
                    intents.append(tag)
        else:
            s = s[:-1]
            if s not in intents:
                intents.append(s)
    print(intents)    
    with open("intents.txt", "w") as f:
        for el in intents:
            f.write("search_"+el+"\n")
        

# train()
label()
prepare_intents()
# with open("tags.txt", "w") as f:
    # f.writelines(seen)