import en_core_web_sm

nlp = en_core_web_sm.load()

def get_named_entities(lines, names=None):
    entities = []
    for line in lines:
        doc = nlp(line)
        for entity in doc.ents:
            if names==None:
                entities.append((entity.text, entity.label_))
            elif entity.label_ in names:
                entities.append((entity.text, entity.label_))

    return entities