def return_num(string):
    return int(string[string.index(':') + 2:]) + 10


print(return_num('результат операции: 42'))
print(return_num('результат операции: 54'))
print(return_num('результат работы программы: 209'))
print(return_num('результат: 2'))
