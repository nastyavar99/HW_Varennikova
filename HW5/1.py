from itertools import product
import pymorphy2
import random


def generator():
    morph = pymorphy2.MorphAnalyzer()
    nouns = []
    adjectives = []
    with open('rus_shuffled.txt', 'r', encoding='utf-8') as f:
        lines = [line.rstrip() for line in f]
        for line in lines[:10]:
            p = morph.parse(line)[0]
            if 'NOUN' in p.tag:
                nouns.append(p)
            elif 'ADJF' in p.tag:
                adjectives.append(p)

    pairs = list(product(adjectives, nouns))
    random.shuffle(pairs)
    for pair in pairs:
        adj, noun = pair
        adj = adj.inflect({'nomn'})
        noun = noun.inflect({'nomn'})
        if noun.tag.number != adj.tag.number:
            adj = adj.inflect({noun.tag.number})
        if noun.tag.gender != adj.tag.gender and adj.tag.number != 'plur':
            adj = adj.inflect({noun.tag.gender})

        yield f'{adj.word} {noun.word}'


for i in generator():
    print(i)
