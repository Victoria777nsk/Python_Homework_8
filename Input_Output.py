'''
Модуль ввода и вывода данных, содержащихся в базе.
'''
# Метод для записи новых данных в базу:

def write_file(data):
    with open('file.csv', 'a', encoding = 'utf-8') as file:
        file.write(data)
          
# Метод для извлечения информации из базы данных:

def read_file():
    with open('file.csv', 'r', encoding = 'utf-8') as file:
        return file.readlines()
