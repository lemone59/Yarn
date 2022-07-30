from .words import *
import random


def genesent(sent):
    if sent == 1: # TYPE 1 // I + AM + VERB
        return f"{random.choice(talking)} {random.choice(verbs2)} {random.choice(verbs)}"

    elif sent == 2: # TYPE 2 // I + AM + VERB + VERB
        return f"{random.choice(talking)} {random.choice(verbs2)} {random.choice(verbs)}"

    elif sent == 3: # TYPE 3 // I + AM + ADJECTIVE
        return f"{random.choice(talking)} {random.choice(state)} {random.choice(adjectives)}"

    elif sent == 4: # TYPE 4 // CONJUNCTION + I + AM + VERB
        return f"{random.choice(conjunctions)} {random.choice(talking)} {random.choice(verbs2)} {random.choice(verbs)}"

    elif sent == 5: # TYPE 5 // CONJUNCTION + I + AM + VERB + NOUN
        return f"{random.choice(conjunctions)} {random.choice(talking)} {random.choice(verbs2)} {random.choice(verbs)} {random.choice(nouns)}"

    elif sent == 6: # TYPE 6 // I + AM + VERB + CONJUNCTION + I + AM + ADJECTIVE
        return f"{random.choice(talking)} {random.choice(verbs2)} {random.choice(verbs)} {random.choice(conjunctions)} I {random.choice(verbs2)} {random.choice(adjectives)}"


def fusesent(sent1, sent2):
    newsent1 = sent1.split(' ')
    newsent1.append(random.choice(simconjunctions))
    new = newsent1 + sent2.split(' ')
    return ' '.join(new)

def writeparagraph(sentences=[]):
    paragraph = []
    for i in range(len(sentences)):
        paragraph.append(fusesent(sentences[i], sentences[i - i]))
    return ''.join(paragraph)


