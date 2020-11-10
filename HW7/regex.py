import re


def change_pattern(string):
    words = re.findall('(\S+)', string)
    return f'{words[1]}, {words[0]}'


print(change_pattern('А.С. Пушкин'))
