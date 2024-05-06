# Тестовое задание
## Задание 1
Ваша задача - создать API для управления заметками пользователей с использованием FastAPI, PostgreSQL для хранения данных, SQLAlchemy для взаимодействия с базой данных, Alembic для миграций и JWT для аутентификации пользователей.

## Задание 2
Ваша задача написать SQL-запрос, который вернет список студентов (student_name) и названия курсов (course_name), включая тех студентов, которые не зарегистрированы на какие-либо курсы.

### Исходные таблицы:
courses:

![image](https://github.com/Lapuskin/test_task/assets/93324745/2df13a48-6a35-4267-85fd-5555d95da57a)

students:

![image](https://github.com/Lapuskin/test_task/assets/93324745/0b7c556d-0633-47d3-a064-16aadd8e4787)

enrollments:

![image](https://github.com/Lapuskin/test_task/assets/93324745/9c28eada-f551-4b76-92ba-e4583122d2f4)


Для выполнения задания был написан запрос, выделяющий student_name и course_name, путем последовательного джоина трех таблиц.

`
SELECT students.student_name, COALESCE(courses.course_name, 'Not enrolled') as course_name
FROM students LEFT JOIN enrollments ON students.student_id = enrollments.student_id LEFT JOIN courses ON enrollments.course_id = courses.course_id; `

Результат: ![image](https://github.com/Lapuskin/test_task/assets/93324745/5e266727-f6d5-4473-95f6-cc84c6992e50)

