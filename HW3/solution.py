import nltk
import os


class FileReader:
    def __init__(self, file_name):
        self.file_name = file_name
        self.line_count = 0
        self.word_count = 0

    def __add__(self, other, encoding='utf-8'):
        with open(self.file_name, 'r', encoding=encoding) as f1, open(other.file_name, 'r', encoding=encoding) as f2:
            with open('merged_file.txt', 'w', encoding=encoding) as file:
                for l in f1:
                    file.write(l)
                file.write('\n')
                for l in f2:
                    file.write(l)

        return FileReader('merged_file.txt')

    def __str__(self):
        return os.path.abspath(self.file_name)

    def read(self, encoding='utf-8'):
        try:
            with open(self.file_name, 'r', encoding=encoding) as file:
                return file.read()
        except FileNotFoundError:
            return ''

    def write(self, text, encoding='utf-8', mode='a'):
        with open(self.file_name, encoding=encoding, mode=mode) as file:
            file.write('\n' + text)

    def count(self):
        try:
            with open(self.file_name, 'r') as file:
                lines_result = 0
                words_result = 0

                for line in file:
                    lines_result += 1
                    words = nltk.word_tokenize(line, language="russian")
                    words_result += len(words)

                self.line_count = lines_result
                self.word_count = words_result

                return self.line_count, self.word_count
        except FileNotFoundError:
            return ''



