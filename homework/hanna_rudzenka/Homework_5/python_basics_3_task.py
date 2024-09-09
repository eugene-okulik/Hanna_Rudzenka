person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person

res_1 = 'результат операции: 42'
res_2 = 'результат операции: 514'
res_3 = 'результат работы программы: 9'

res_1 = int(res_1[res_1.index('42'):])
res_2 = int(res_2[res_2.index('514'):])
res_3 = int(res_3[res_3.index('9'):])

print(res_1 + 10)
print(res_2 + 10)
print(res_3 + 10)

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

students = ', '.join(students)
subjects = ', '.join(subjects)
print(f'Students {students} study these subjects: {subjects}')


