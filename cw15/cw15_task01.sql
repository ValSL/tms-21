-- Создание таблицы
CREATE TABLE user (
   id integer primary key autoincrement,
   firstname varchar(255),
   lastname varchar(255),
   age integer
);
-- Добавление пользователей
INSERT INTO user(firstname, lastname, age)
VALUES('Andrey', 'Andreev', 25), ('Ivan', 'Ivanov', 33), ('Igor', 'Igorev', 46);

SELECT * FROM user
WHERE firstname = 'Valid';

SELECT * FROM user
WHERE age < 25;

UPDATE user
SET age = 16
WHERE age > 40;

SELECT * FROM user
WHERE age > 15 and age < 18;

