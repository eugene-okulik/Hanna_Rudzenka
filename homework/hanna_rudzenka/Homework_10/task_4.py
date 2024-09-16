PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

res_list = PRICE_LIST.split('\n')
name_list = [name.split()[0] for name in res_list]
price_list = [int(price.split()[1][:-1]) for price in res_list]
res_dct = dict(zip(name_list, price_list))
