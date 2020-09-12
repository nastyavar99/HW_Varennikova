import re
import collections
import csv
from pymystem3 import Mystem

import requests as req
from bs4 import BeautifulSoup
import json

words = []
PATTERN = r'[…!,\\.?*/«»:–()“”";:\.]'  # для удаления знаков препинания по шаблону

with open('dom.txt', 'r', encoding='utf-8-sig') as file:  # открываем файл и подготавливаем слова для частотного словаря
    for line in file:
        string = line.lower().strip()
        if not string:
            continue
        strings = re.sub(PATTERN, '', string).split()
        words.extend(strings)

    frequency_dict = collections.Counter(words)
    del frequency_dict['-']  # данный сивол иногда встречался в словах, поэтому его нельзя удалить с помощью re
    frequency_dict['1964'] = frequency_dict.pop('-1964')  # исправление маленьких недочетов
    frequency_dict['1996'] = frequency_dict.pop('-1996')

    with open('dom.csv', 'w') as f:  # записываем чачтотный словарь в csv файл
        writer = csv.DictWriter(f, fieldnames=['Слово', 'Количество'])
        writer.writeheader()
        for word, amount in frequency_dict.items():
            writer.writerow({'Слово': word, 'Количество': amount})

    word_lemmas = []
    lemmatizer = Mystem()
    keys = frequency_dict.keys()
    for word in keys:  # лемматизируем слова, но отбираем только те, у которых ровно 2 "о"
        word_lemmas.extend(w for w in lemmatizer.lemmatize(word) if w.count('о') == 2)

r = req.get('http://lib.ru/POEZIQ/PESSOA/lirika.txt')  # запрос на сайт
soup = BeautifulSoup(r.content, features='html.parser')
text = []
for tag in soup.find_all('ul'):
    # тег ul - сосед безъямянного тег, под которым хранится текст стихотворения, поэтому будем использовать атрибут next_sibling
    title = re.sub(r'[xIV]', '', tag.find('h2').text).lower().strip()  # извлекаем название стихотворения
    sentence = re.sub(PATTERN, '', str(tag.next_sibling)).lower().strip()  # текст самого стихотворения
    if title:
        text.append(title)
    if sentence:
        text.append(sentence)

lemmas = []
for sentence in text:  # лемматизирует слова из предложений + удаляет пробелы
    lemmas.extend(s for s in lemmatizer.lemmatize(sentence) if s != ' ')

freq_dict = collections.Counter(lemmas)
del freq_dict['-']

with open('frequency_dictionary.json', 'w', encoding='utf-8') as f2:
    json.dump(frequency_dict, f2)
