import os
from corus import load_corpora
from tqdm import tqdm
from collections import defaultdict
from sklearn.model_selection import train_test_split
import pickle
from sklearn.metrics import precision_score


class UnigramMorphAnalyzer:
    def __init__(self):
        self.x_test, self.y_test, self.ending_stat = self.train()

    def train(self):
        path = os.path.abspath('annot.opcorpora.xml.byfile.zip')
        records = load_corpora(path)

        rec_pairs = []
        for rec in tqdm(records):
            for par in rec.pars:
                for sent in par.sents:
                    for token in sent.tokens:
                        rec_pairs.append((token.text, token.forms[0].grams[0]))

        x, y = [], []
        for word, pos in rec_pairs:
            x.append(word)
            y.append(pos)
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

        endings_stat = defaultdict(lambda: defaultdict(int))
        for w, p in zip(x_train, y_train):
            for i in range(1, 5):
                endings_stat[str(w[-i:])][p] += 1

        return x_test, y_test, endings_stat

    def predict(self, token):
        stop_pronouns = {'я', 'мы', 'ты', 'вы', 'он', 'она', 'оно', 'они'}
        stop_prepositions = {'без', 'в', 'к', 'у', 'до', 'для', 'за', 'перед', 'об', 'от', 'из-за', 'из-под', 'около',
                             'с', 'про', 'между', 'под', 'по', 'о', 'на'}
        stop_conjunctions = {'и', 'а', 'или', 'либо', 'но'}

        token = token.lower()
        if token in stop_pronouns:
            return {'NPRO': 100}
        elif token in stop_prepositions:
            return {'PREP': 100}
        elif token in stop_conjunctions:
            return {'CONJ': 100}
        else:
            pos = (
                    self.ending_stat.get(token[-4:])
                    or self.ending_stat.get(token[-3:])
                    or self.ending_stat.get(token[-2:])
                    or self.ending_stat.get(token[-1:])
            )
            if pos is None:
                return

        percent_100 = sum(pos.values())
        percentage = {}
        for name, amount in pos.items():
            percentage[name] = amount * 100 / percent_100

        return percentage

    def save(self):
        with open(f'{self.__class__.__name__}.pickle', 'wb') as file:
            pickle.dump(self, file)

    def load(self):
        with open(f'{self.__class__.__name__}.pickle', 'rb') as file:
            data = pickle.load(file)
            return data

    def __getitem__(self, key):
        return dict(self.ending_stat[key])

    def eval(self):
        y_pred = []

        for token in self.x_test:
            variants = self.predict(token)
            if variants is None:
                y_pred.append('UNKN')
            else:
                y_pred.append(max(variants.items(), key=lambda x: x[1])[0])

        return f'precision: {precision_score(self.y_test, y_pred, average="micro")}'
