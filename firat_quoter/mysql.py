# Вход в mysql
# mysql -u root -p
# Подключение к удаленному серверу
# mysql -u root -h 192.168.0.10 -P 3360 -p

# Создать файл настроек для входа в mysql в Dbeaver
# [mysql] или [client] вверху файла
# user=root
# password=1234
# файл сохранить в домашней папке .my.cnf для Linux
# файл сохранить в папке Windows my.cnf для Windows


# Команды
# USE (\u) - выбор базы (можно при входе выбрать базу введя mysql db_name)
# SOURCE (\.) - выполнение SQL- команд из файла
# SOURCE hello.sql - команда из файла (пример)
# SYSTEM (\!) - выполнение команд операционной системы
# STATUS (\s) - информация о состоянии сервера
# EXIT (\q) - выход
# \G - вывод в вертикальном формате
# SELECT * FROM mysql.user LIMIT 1\G

# Ctr + L - быстрая очистка экрана

# Перенос базы или создание резервной копии (выйти из mysql)!!!
# mysqldump database_name > sample.sql
# tail -10 sample.sql - вывод последних 10 строк файла
# mysql new_database_name < sample.sql - направляем содержимое в новую базу данных (разворот дампа)

# HELP DESCRIBE - help
# USE mysql (USE database_name) - выбрать базу данных
# CREATE DATABASE name; - созать базу данных
# CREATE DATABASE IF NOT EXISTS name; - создать базу данных
# SHOW DATABASES; - показать базы данных (список)
# DROP DATABASE name; - удалить базу
# DROP TABLE IF EXISTS table_name - удалить таблицу
# DROP DATABASE IF EXISTS name; - удалить базу
# CREATE TABLE name (column_name INT, column_name TEXT); -  создать таблицу
# CREATE TABLE IF NOT EXISTS name (column_name INT, column_name TXT, UNIQUE unique_name(name(10))); - создать таблицу
# UNIQUE unique_name(name(10)) - запретить вставку разделов, которые уже есть
# SHOW TABLES; - показать таблицы (список)
# SHOW TABLES FROM database_name; - показать таблицы из не выбранной базы (без команды USE)
# DESCRIBE table_name; - показать таблицу с колонками
# DESCRIBE table_name 'column_name'; - показать выбранный столбец
# DESCRIBE table_name 'm%; - - колонки, начинающиеся на 'm'


# SELECT mysql.USER.USER; - явное обращение к базе, таблице и колонке (вывод колонки) - не работает!!!
# SELECT * FROM database_name.table_name; - выбрать таблицу из другой базы
# SELECT * FROM table_name; - выбрать таблицу
# SELECT * FROM information_schema.TABLES WHERE TABLE_SCHEMA = 'shop'\G; - выбрать таблицу из списка с
# вертикальным выводом
# SHOW VARIABLES LIKE 'datadir'; - вывести каталог в базе

# Комментарии
# -- SELECT - два дефиса и пробел (однострочный комментарий)
# /* - многострочный комментарий */
# скалярные выражения - это числа и строки
# одиночную кавычку в строке экранируем \
# `create` - обратные кавычки, если имя столбца совпадает с ключевым словом

# Типы данных
# CREATE TABLE table_name (id INT(8)) - количество символов под число заполняются пробелами
# CREATE TABLE table_name (id INT UNSIGNED) - устанавливает только положительные значения
# CREATE TABLE table_name (id INT(8) ZEROFILL) - отведенные под число поля заменяются нулями
# CREATE TABLE tbl (price DECIMAL(7,4)) - для больших чисел (строковый тип), поля до запятой и после
# INSERT INTO table_name VALUES (5); - вставить значение

# Строковые типы
# (name CHAR(10)) - столбец фиксированного размера 10 байт
# (name CHAR(10) DEFAULT 'anonymous') - если строка не помещается - вывод по умолчанию
# (description VARCHAR(255)) - поле переменной длины

# Пример из текстового редактора
# DROP TABLE IF EXISTS tbl;
# CREATE TABLE tbl (
# name CHAR(10) DEFAULT 'anonymous',
# description VARCHAR(255)
# );
# INSERT INTO tbl VALUES (DEFAULT, 'New user');  - (кириллицу не воспринимает? 2-3 байта на 1 символ)
# SELECT * FROM tbl;
# - Alt + x - запуск команд

# Тип TEXT
# TINYTEXT, TEXT, MEDIUMTEXT, LONGTEXT

# Тип NULL, календарные и коллекционные типы (множества)
# NOT NULL - запрет вставлять ничейное значение

# Преобразование таблицы
# CREATE TABLE tbl (id INT UNSIGNED);
# ALTER TABLE tbl CHANGE id id INT UNSIGNED NOT NULL;

# Очитска таблицы
# TRUNCATE table_name;

# Календарные типы:
# TIME - хранит сутки  '00:00:00'
# YEAR - год  0000
# DATE - хранит дату с точностью до дня  '0000-00-00'
# DATETIME - хранит дату и время  '0000-00-00 00:00:00'
# TIMESTAMP - хранит даты от 1970 до 2038 '0000-00-00 00:00:00' (или NOW() )
# Операции с датами:
# select '2021-07-26 0:00:00' - INTERVAL 1 DAY;
# select '2021-07-26 0:00:00' + INTERVAL 1 WEEK;
# select '2021-07-26 0:00:00' + INTERVAL '1-1' YEAR_MONTH;

# ENUM и SET
# хранят числа в виде строк - first, second
# ENUM - по одному значению в ячейке (first)
# SET - по несколько - first, second

# Формат JSON
# ALTER TABLE tbl ADD collect JSON - добавили столбец
# Добавляем запись с JSON-объектом
# INSERT INTO tbl VALUES (1, '{"first": "Hello", "second": "World"}');
# Обращение к ключам JSON:
# SELECT collect->>"$.first" FROM tbl;
# Время по умолчанию
# DEFAULT CURRENT_TIMESTAMP  (можно использовать функцию NOW() - тоже, что TIMESTAMP)
# Автоматическое обновление даты по умолчанию
# DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP

# Индексы
# Объявить первичный ключ можно в скобках с указанием столбца либо в описании столбца:
# PRIMARY KEY(id)
# PRIMARY KEY(id, name(10)) - по столбцу id и первым 10 символам строки в столбце name (можно указать все 255)
# PRIMARY KEY AUTOINCREMENT - автоматическое создание уникального индекса

# Псевдотип SERIAL
# SERIAL = BIGINT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE
# id SERIAL PRIMARY KEY - делает запись короче

# Присвоение индексу имени
# KEY index_of_field_name(field_name)
# Создать индекс в существующей таблице:
# CREATE INDEX index_of_field_name ON table_name (field_name);
# Удалить индекс
# DROP INDEX index_of_field_name ON table_name;
# Явно указать путь поиска
# CREATE INDEX index_of_field_name USING BTREE ON table_name (field_name);
# CREATE INDEX index_of_field_name USING HASH ON table_name (field_name);

# CRUD - операции
# INSERT, SELECT, UPDATE, DELETE

# Однострочная вставка:
# INSERT INTO catalogs VALUES (NULL, 'Processors');
# INSERT INTO catalogs (id, name) VALUES (NULL, 'Motherboards'); # явно указываем столбцы
# INSERT INTO catalogs (name, id) VALUES (DEFAULT, 'Motherboards'); # вместо NULL
# UNIQUE unique_name(name(10)) - запретить вставку разделов, которые уже есть
# INSERT IGNORE INTO .... игнорировать ограничение вставки (не будет ошибки и вставки тоже)
# Просто пример
# CREATE TABLE tbl (name CHAR(10) DEFAULT 'anonymous', description VARCHAR(255));
# INSERT INTO tbl VALUES(DEFAULT, 'Новый пользователь');
# SELECT * FROM tbl;
# INSERT INTO tbl (description) VALUES('Еще один пользователь');
# INSERT INTO tbl VALUES('Очень длинное имя пользователя', 'Еще один пользователь');

# Многострочная:
# INSERT INTO catalogs VALUES
#  (DEFAULT, 'Processors'),
#  (DEFAULT, 'Motherboards'),
#  (DEFAULT, 'Videocards');

# Извлечение данных
# SELECT id, name FROM catalogs; # порядок столбцов можно менять
# SELECT * FROM catalogs; # вывести все столбцы

# Удаление
# DELETE FROM catalogs;
# DELETE FROM catalogs LIMIT 2; # удалить первые 2 записи
# DELETE FROM catalogs WHERE id > 1 LIMIT 2; # условие на удаление
# Очистка таблицы (в т.ч. сброс autoincrement)
# TRUNCATE catalogs;

# Обновление записи
# UPDATE catalogs SET name = 'Processors (Intel)' WHERE name = 'Processors';

# Перемещение записей из одной таблицы в другую
# INSERT INTO cat SELECT * FROM catalogs;
