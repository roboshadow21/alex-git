# Оператор SELECT
# SELECT 3 + 5;
# SELECT 3 + 5 AS summ;
# UPDATE catalogs SET id = id + 10; #увеличили значение столбца id
# SELECT '3' + '5'; # сложение числовых строк приводится к числам
# SELECT 'ab' + 'cd'; # сложение символов строк приводится к 0
# SELECT -7;  # меняет знак операнда
# SELECT 8 / 0; - NULL
# SELECT 8 / 3; - вещественное число
# SELECT 8 DIV 3; - целочисленное деление
# SELECT 5 % 2, 5 MOD 2; - остаток от деления
# SELECT TRUE, FALSE; или SELECT ! TRUE, ! FALSE;
# SELECT NOT TRUE, NOT FALSE;
# != и <> - одно и тоже
# <=> - безопасное сравнение с NULL
# SELECT 2 IS NULL, IS NOT NULL;
# CREATE TABLE tbl (
#   x INT,
#   y INT,
#   summ INT AS (x + y) STORED   # STORED - для сохранения на жесткий диск
# );
# SELECT * FROM catalogs WHERE id > 2;
# SELECT * FROM catalogs WHERE id > 2 AND id <= 4;
# SELECT * FROM catalogs WHERE id BETWEEN 2 and 4;
# SELECT * FROM catalogs WHERE id NOT BETWEEN 2 and 4;
# SELECT 2 BETWEEN 2 AND 4;
# SELECT * FROM catalogs WHERE id IN (1, 2, 5);
# SELECT * FROM catalogs WHERE id NOT IN (1, 2, 5);
# SELECT * FROM catalogs WHERE name = "Процессоры";
# SELECT * FROM catalogs WHERE name LIKE "Процессоры";
# SELECT * FROM catalogs WHERE name NOT LIKE "Процессоры";
# SELECT * FROM catalogs WHERE name LIKE "Процесс%"; % - заменяет любой символ или все символы
# SELECT * FROM catalogs WHERE name LIKE "_"; _ - заменяет ОДИН любой символ
# \%, \_ - экранирует спецсимволы
# SELECT * FROM users WHERE birthday_at >= "1990-01-01" AND birthday_at < "2000-01-01";
# SELECT * FROM users WHERE birthday_at BETWEEN "1990-01-01" AND "2000-01-01";
# SELECT * FROM users WHERE birthday_at LIKE "199%";
# Регулярные выражения:
# REGEX, RLIKE
# SELECT 'программирование' RLIKE 'грам';
# SELECT 'программирование' RLIKE '^грам'; (^ - начало строки, $ - конец)
# SELECT 'a' RLIKE '[abc]' AS 'a';
# SELECT 'f' RLIKE '[a-z]';
# Классы
# SELECT 7 RLIKE '[[:digit:]]'; - ('[[:digit:]]' - класс для цифр, '[[:alpha:]]') для строк
# Квантификаторы ?, *, + - то же, что в re
# SELECT '342.34' RLIKE '^[0-9]*\\.[0-9]{2}$' AS '342.34';
# Сортировка и ограничения
# SELECT * FROM catalogs ORDER BY name;
# SELECT * FROM catalogs ORDER BY name DESC; - обратный порядок сортировки
# SELECT id, catalog_id, price, name FROM products ORDER BY catalog_id, price; - сортировка по нескольким полям
# SELECT id, catalog_id, price, name FROM products ORDER BY catalog_id DESC, price DESC;
# SELECT id, catalog_id, price, name FROM products LIMIT 2; -поиск и выдача по частям
# SELECT id, catalog_id, price, name FROM products LIMIT 2, 2; - следующая запись
# SELECT id, catalog_id, price, name FROM products LIMIT 2 OFFSET 4; - OFFSET указывает позицию следующей выдачи
# SELECT DISTINCT catalog_id FROM products ORDER BY catalog_id; - вывод только уникальных значений
# SELECT id, catalog_id, price, name FROM products WHERE catalog_id = 2 AND price > 5000;
# Меняем цену в выбранных позициях:
# UPDATE products SET price = price * 0.9 WHERE catalog_id = 2 AND price > 5000;
# Удаляем 2 самые дорогие позиции:
# DELETE FROM products ORDER BY price DESC LIMIT 2;

# Предопределенные функции
# SELECT NOW() - возвращает текущую дату и время
# INSERT INTO users VALUES (NULL, 'Александр', '1986-01-20', NOW(), NOW());
# SELECT name, DATE(created_at), DATE(updated_at) FROM USERS; - оставляем в выводе только дату
# SELECT name, DATE(created_at) AS created_at, DATE(updated_at) AS updated_at FROM USERS;
# Функция форматирования
# SELECT DATE_FORMAT('2021-09-07 21:53:00', 'На дворе %Y год');
# SELECT name, DATE_FORMAT(birthday_at, '%d.%m.%Y') AS birthday_at FROM users;
# UNIX_TIMESTAMP, FROM_UNIXTIME
# Посчитать возраст:
# SELECT name, (TO_DAYS(NOW()) - TO_DAYS(birthday_at)) / 365.25 AS age FROM users;
# SELECT name, FLOOR((TO_DAYS(NOW()) - TO_DAYS(birthday_at)) / 365.25) AS age FROM users;
# SELECT * FROM users ORDER BY RAND();
# SELECT VERSION()
# SELECT LAST_INSERT_ID(); - последнее значение автоинкремента
# SELECT DATABASE();
# SELECT USER();

# Математические функции
# SELECT RAND();
# SELECT SQRT();

# DROP TABLE IF EXISTS distances;
# CREATE TABLE distances (
#   id SERIAL PRIMARY KEY,
#   x1 INT NOT NULL,
#   y1 INT NOT NULL,
#   x2 INT NOT NULL,
#   y2 INT NOT NULL,
#   distance DOUBLE AS (SQRT(POW(x1 - x2, 2) + POW(y1 - y2, 2)))
# ) COMMENT = 'Расстояние между двумя точками';

# DROP TABLE IF EXISTS distances;
# CREATE TABLE distances (
#   id SERIAL PRIMARY KEY,
#   a JSON NOT NULL,
#   b JSON NOT NULL,
#   distance DOUBLE AS (SQRT(POW(a->>'$.x' - b->>'$.x', 2) + POW(a->>'$.y' - b->>'$.y', 2)))
# ) COMMENT = 'Расстояние между двумя точками';
#
# INSERT INTO distances
#   (a, b)
# VALUES
#   ('{"x": 1, "y": 1}', '{"x": 4, "y": 5}'),
#   ('{"x": 4, "y": -1}', '{"x": 3, "y": 2}'),
#   ('{"x": -2, "y": 5}', '{"x": 1, "y": 3}');

# DROP TABLE IF EXISTS triangles;
# CREATE TABLE triangles (
#   id SERIAL PRIMARY KEY,
#   a DOUBLE NOT NULL COMMENT 'Сторона треугольника',
#   b DOUBLE NOT NULL COMMENT 'Сторона треугольника',
#   angle INT NOT NULL COMMENT 'Угол треугольника в градусах',
#   square DOUBLE AS (a * b * SIN(RADIANS(angle)) / 2.0)
# ) COMMENT = 'Площадь треугольника';

# INSERT INTO
#   triangles (a, b, angle)
# VALUES
#   (1.414, 1, 45),
#   (2.707, 2.104, 60),
#   (2.088, 2.112, 56),
#   (5.014, 2.304, 23),
#   (3.482, 4.708, 38);
# Функция ROUND(), SEILING(), FLOOR()
# ALTER TABLE triangles CHANGE square square DOUBLE AS (ROUND(a * b * SIN(RADIANS(angle)) / 2.0, 4));

# Функции строк
# SELECT id, SUBSTRING(name, 1, 5) as name FROM users;
# Объединение строк
# SELECT id, CONCAT(name, ' ', TIMESTAMPDIFF(YEAR, birthday_at, NOW())) AS name FROM users;

# Логические функции
# SELECT IF(TRUE, 'истина', 'ложь'), SELECT IF(FALSE, 'истина', 'ложь')
# SELECT name, IF(TIMESTAMPDIFF(YEAR, birthday_at, NOW()) >= 18, 'legal age', 'not legal age') AS status FROM users;

# DROP TABLE IF EXISTS rainbow;
# CREATE TABLE rainbow (
#   id SERIAL PRIMARY KEY,
#   color VARCHAR(255)
# ) COMMENT = 'Цвета радуги';

# INSERT INTO
#   rainbow (color)
# VALUES
#   ('red'),
#   ('orange'),
#   ('yellow'),
#   ('green'),
#   ('blue'),
#   ('indigo'),
#   ('violet');

# Изменить английские названия на русские
# SELECT
#   CASE
#     WHEN color = 'red' THEN 'красный'
#     WHEN color = 'orange' THEN 'оранжевый'
#     WHEN color = 'yellow' THEN 'желтый'
#     WHEN color = 'green' THEN 'зеленый'
#     WHEN color = 'blue' THEN 'голубой'
#     WHEN color = 'indigo' THEN 'синий'
#     ELSE 'фиолетовый'
#   END AS russian
# FROM
#   rainbow;

# SELECT INET_ATON('127.0.0.1');
# SELECT INET_NTOA(2130706433);
# SELECT UUID();

# Группировка данных
# SELECT DISTINCT catalog_id FROM products;
# SELECT catalog_id FROM products GROUP BY catalog_id;
# SELECT id, name, id % 3 FROM products ORDER BY id % 3;
# SELECT id, name, SUBSTRING(birthday_at, 1, 3) AS decade FROM users;
# SELECT id, name, SUBSTRING(birthday_at, 1, 3) AS decade FROM users ORDER BY decade;
# SELECT id, name, SUBSTRING(birthday_at, 1, 3) AS decade FROM users GROUP BY decade;
# SELECT COUNT(*), SUBSTRING(birthday_at, 1, 3) AS decade FROM users GROUP BY decade;
# SELECT COUNT(*), SUBSTRING(birthday_at, 1, 3) AS decade FROM users GROUP BY decade ORDER BY decade DESC;
# SELECT COUNT(*) AS total, SUBSTRING(birthday_at, 1, 3) AS decade FROM users GROUP BY decade ORDER BY total DESC;
# SELECT COUNT(*) FROM users;
# SELECT GROUP_CONCAT(name), SUBSTRING(birthday_at, 1, 3) AS decade FROM users GROUP BY decade;
# SELECT GROUP_CONCAT(name SEPARATOR ' '), SUBSTRING(birthday_at, 1, 3) AS decade FROM users GROUP BY decade;
# SELECT GROUP_CONCAT(name ORDER BY name DESC SEPARATOR ' '), SUBSTRING(birthday_at, 1, 3) AS decade FROM users GROUP BY decade;

# SELECT COUNT(id) FROM catalogs; # - строки. где нет NULL
# SELECT COUNT(*) FROM catalogs; # - все строки
# SELECT catalog_id, COUNT(*) AS total FROM products GROUP BY catalog_id;
# CREATE TABLE test (id INT NOT NULL, value INT DEFAULT NULL);

# INSERT INTO test VALUES (1, 230),
# (2, NULL),
# (3, 405),
# (4, NULL);


# SELECT COUNT(id), COUNT(value) FROM test;
# SELECT COUNT(*) FROM test;
# SELECT COUNT(id) AS total_ids, COUNT(catalog_id) AS catalog_total_ids FROM products;
# Подсчитываем только уникальные значения
# SELECT COUNT(DISTINCT id) AS total_ids, COUNT(DISTINCT catalog_id) AS catalog_total_ids FROM products;

# SELECT MIN(price) AS min, MAX(price) AS max FROM products;
# SELECT MIN(price) AS min, MAX(price) AS max FROM products GROUP BY catalog_id;
# SELECT id, name, price FROM products ORDER BY price DESC LIMIT 1;
# SELECT AVG(price) FROM products;  - среднее
# SELECT ROUND(AVG(price), 2) FROM products;
# SELECT ROUND(AVG(price), 2) FROM products GROUP BY catalog_id;
# SELECT ROUND(AVG(price * 1.2), 2) AS price FROM products GROUP BY catalog_id; - увеличили цену на 20%
# SELECT SUM(price) FROM products;
# SELECT catalog_id, SUM(price) FROM products GROUP BY catalog_id;

# Специальные возможности GROUP BY

# SELECT GROUP_CONCAT(name), SUBSTRING(birthday_at, 1, 3) AS decade FROM users GROUP BY decade;
# SELECT COUNT(*) AS total, SUBSTRING(birthday_at, 1, 3) AS decade FROM users GROUP BY decade;
# SELECT COUNT(*) AS total, SUBSTRING(birthday_at, 1, 3) AS decade FROM users GROUP BY decade HAVING total >= 2;
# SELECT * FROM users HAVING birthday_at >= '1990-01-01';
# SELECT name, description, price, catalog_id FROM products GROUP BY name, description, price, catalog_id;
# Переносим из таблицы в таблицу
# INSERT INTO products_new SELECT NULL, name, description, price, catalog_id, NOW(), NOW()
# FROM products GROUP BY name, description, price, catalog_id;

# ALTER TABLE products_new RENAME products;
# INSERT INTO users (name, birthday_at) VALUES ('Светлана', '1988-02-04'),
# ('Олег', '1988-03-20'), ('Юлия', '2006-07-12');
# SELECT name, birthday_at FROM users ORDER BY birthday_at;
# SELECT YEAR(birthday_at) FROM users ORDER BY birthday_at;
# SELECT MAX(name), YEAR(birthday_at) AS birthday_year FROM users GROUP BY birthday_year ORDER BY birthday_year;
# Или:
# SELECT ANY_VALUE(name), YEAR(birthday_at) AS birthday_year FROM users GROUP BY birthday_year ORDER BY birthday_year;
# SELECT SUBSTRING(birthday_at, 1, 3) AS decade, COUNT(*) FROM users GROUP BY decade WITH ROLLUP;