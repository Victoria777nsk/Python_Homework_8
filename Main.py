'''
Основной модуль работы с базой данных:
'''
def sort_data(number, read, write, sor, da, data):
    while True: 
        n = number()
        if n == '1':
            print(*sor(input('Должность: '), read()), sep = '')   
        elif n == '2':
            print(*read(), sep = '')
        elif n == '3':
            print(*sor(input('Введите фамилию сотрудника:'), read()), sep = '')    
        elif n == '4':
            write(data())
        elif n == '5':
            print('До свидания!')        
            break
