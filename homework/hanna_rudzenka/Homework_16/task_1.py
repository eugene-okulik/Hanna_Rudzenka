import os
import csv
import mysql.connector as mysql
import dotenv

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)
cursor = db.cursor(dictionary=True, buffered=True)

homework_folder_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
lesson_16_hw_data_file_path = os.path.join(homework_folder_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

with open(lesson_16_hw_data_file_path, newline='') as csv_file:
    file_data = csv.reader(csv_file)
    data = []
    for row in file_data:
        data.append(row)
    csv_students_data = data[1:]

    for row in csv_students_data:
        name, second_name, group_title, book_title, subject_title, lesson_title, mark_value = row
        cursor.execute(f"""SELECT *
        FROM books
        join students s on books.taken_by_student_id = s.id
        join marks m2 on m2.student_id = s.id
        join `groups` g on s.group_id = g.id
        join lessons l on m2.lesson_id = l.id
        join subjets on l.subject_id = subjets.id
        WHERE s.name = '{name}' AND s.second_name = '{second_name}' AND g.title = '{group_title}' AND
        books.title = '{book_title}' AND subjets.title = '{subject_title}' AND l.title = '{lesson_title}'
        AND m2.value = '{mark_value}'""")

        response = cursor.fetchone()
        if response is None:
            print(f'This data is missing in database: {row}')
