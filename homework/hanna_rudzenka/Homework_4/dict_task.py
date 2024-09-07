my_dict = {
    'tuple': (1, True, [1, 6, 2], 'cat', {9, 5, 2}),
    'list': [2, 4, 5, 7, 9],
    'dict': {'name': 'Hanna', 'surname': 'Rudenka', 'age': 30, 'country': 'Poland', 'city': 'Wroclaw'},
    'set': {4, False, 3.5, 'time', 987}
}
print(my_dict['tuple'][-1])
my_dict['list'].append(8)
my_dict['list'].pop(1)
my_dict['i am a tuple'] = (8, 7, 6, 5)
my_dict['dict'].pop('city')
my_dict['set'].add(8888)
my_dict['set'].pop()
print(my_dict)
