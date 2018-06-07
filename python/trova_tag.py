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

# train()
label()
with open("tags.txt", "w") as f:
    f.writelines(seen)