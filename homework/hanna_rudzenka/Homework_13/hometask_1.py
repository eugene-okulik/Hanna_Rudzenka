import os
from datetime import datetime, timedelta

current_file_path = os.path.dirname(__file__)
hanna_rudzenka_folder_path = os.path.dirname(current_file_path)
homework_folder_path = os.path.dirname(hanna_rudzenka_folder_path)
hw_13_file_path = os.path.join(homework_folder_path, 'eugene_okulik', 'hw_13', 'data.txt')


def create_python_date_format():
    with open(hw_13_file_path, 'r', encoding='utf-8') as hw_13:
        dates = []
        for line in hw_13.readlines():
            dates.append(datetime.strptime(line[3:29], "%Y-%m-%d %H:%M:%S.%f"))
        return dates


def format_python_dates():
    for index, date in enumerate(create_python_date_format()):
        if index == 0:
            print(f'{date}: In a week the date will be {date + timedelta(days=7)}')
        elif index == 1:
            print(f'{date}: The number of the day of the week is {date.weekday()}')
        else:
            days = datetime.now() - date
            print(f'{date}: The difference in days is {days.days}')


format_python_dates()
