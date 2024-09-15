import datetime

date = "Jan 15, 2023 - 12:05:33"
python_date_format = datetime.datetime.strptime(date, '%b %d, %Y - %H:%M:%S')
print(python_date_format)
print(python_date_format.strftime('%B'))
print(datetime.datetime.strftime(python_date_format, "%d.%m.%Y, %H:%M"))
