import random

salary = int(input('Введите сумму вашей зарплаты'))
bonus_bool = random.choice([True, False])
bonus_numb = int(random.random() * 100)

if bonus_bool:
    print(f"{salary}, {bonus_bool} - '${salary + bonus_numb}'")
else:
    print(f"{salary}, {bonus_bool} - '${salary}'")
