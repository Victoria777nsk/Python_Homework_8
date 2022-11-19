'''
Модуль сортировки данных, содержащихся в базе.
'''
def get_da(n,f):
    my_list = []
    for i in f:
        my_list.append(i.split()[n])
    return my_list

def sort(n,f):
    my_list = []
    for i in f:
        if n in i:
            my_list.append(i)
    return my_list
