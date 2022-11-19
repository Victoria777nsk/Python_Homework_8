'''
Модуль контроллера (отвечает за обработку данных в базе):
'''
from Sort import sort, get_da
from View import get_number_operation, get_data
from Input_Output import read_file, write_file
from Main import sort_data

def start():
    return sort_data(get_number_operation, read_file, write_file, sort, get_da, get_data)
