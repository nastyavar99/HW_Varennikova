"""
1. Вам необходимо написать скрипт solution.py, в котором реализован класс FileReader.

Конструктор этого класса принимает один параметр: путь до файла на диске.

В классе FileReader должен быть реализован метод read, возвращающий строку - содержимое файла, путь к которому был
 указан при создании экземпляра класса, а так же метод write, который записывает некоторое содержимое в файл.

Python модуль должен быть написан таким образом, чтобы импорт класса FileReader из него не вызвал ошибок. Например,
при написании реализации метода read, вам нужно учитывать случай, когда при инициализации был передан путь к
несуществующему файлу. Требуется обработать возникающее при этом исключение FileNotFoundError и вернуть из метода read
пустую строку.

Также в классе должен реализован метод count, который возвращает количество строк и слов в файле
 (для токенизации используйте NLTK), а также записывает информацию в соответствующие атрибуты line_count и word_count.

Кроме того в классе необходимо переопределять следующие магические методы:
a) add: склеивает содержимое двух файлов, записывает в текущую директорию, возвращает объект класса FileReader
b) str: выводит путь до файла

Базовый пример:
# >>> from solution import FileReader
# >>> reader = FileReader('not_exist_file.txt')
# >>> text = reader.read()
# >>> text
# ''
# >>> with open('some_file.txt', 'w') as file:
# ...     file.write('some text')
# ...
# 9
# >>> reader = FileReader('some_file.txt')
# >>> text = reader.read()
# >>> text
# 'some text'
# >>> type(reader)
<class 'solution.FileReader'>
"""


class FileReader:
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        try:
            with open(self.file_name, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return ''

    def write(self, text):
        with open(self.file_name, 'w') as file:
            return file.write(text)


reader = FileReader('not_exist_file.txt')
text = reader.read()
print(text)
