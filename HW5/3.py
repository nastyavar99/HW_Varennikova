from collections import Counter


def sort_str(string: str) -> str:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    string_dict = Counter(string)

    result = ''
    for letter in alphabet:
        if letter in string_dict:
            result += (letter * string_dict[letter])

    return result


print(sort_str('acabcd'))
