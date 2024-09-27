INSERT INTO students (name, second_name) VALUES ('Hanna', 'R')
INSERT INTO books (title, taken_by_student_id) VALUES ('Python for beginners', 2165)
INSERT INTO books (title, taken_by_student_id) VALUES ('Python from scratch', 2165)
INSERT INTO `groups` (title, start_date, end_date) VALUES ('self-group', 'sep 2024', 'nov 2024')
UPDATE students SET group_id = 1954 WHERE students.id = 2165
INSERT INTO subjets (title) VALUES ('Python Automation Course')
INSERT INTO subjets (title) VALUES ('Python Course for beginners')
INSERT INTO lessons (title, subject_id) VALUES ('classes', 2782)
INSERT INTO lessons (title, subject_id) VALUES ('objects', 2782)
INSERT INTO lessons (title, subject_id) VALUES ('data types', 2783)
INSERT INTO lessons (title, subject_id) VALUES ('variables', 2783)
INSERT INTO marks (value, lesson_id, student_id) VALUES (10, 5778, 2165 )
INSERT INTO marks (value, lesson_id, student_id) VALUES (9, 5777, 2165 )
INSERT INTO marks (value, lesson_id, student_id) VALUES (8, 5776, 2165 )
INSERT INTO marks (value, lesson_id, student_id) VALUES (7, 5775, 2165 )

SELECT * FROM marks m WHERE student_id = 2165
SELECT * FROM books b WHERE taken_by_student_id = 2165
SELECT s.name, s.second_name, s.group_id,books.title as book_title,  g.title as group_title,
g.start_date, g.end_date, subjets.title as subject_title, l.title as lesson_title, m2.value
FROM books
join students s on books.taken_by_student_id = s.id
join marks m2 on m2.student_id = s.id
join `groups` g on s.group_id = g.id
join lessons l on m2.lesson_id = l.id
join subjets on l.subject_id = subjets.id
WHERE s.id = 2165