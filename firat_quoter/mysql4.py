# Lesson 5 - 6 UNION, сложные запросы с использованием JOIN

# create table rubrics (
#   id serial primary key,
#   name varchar(255) comment 'Название раздела'
#   ) comment = 'Разделы интернет-магазина';

# insert into rubrics values
# (null, 'Видеокарты'),
# (null, 'Память');

# Union - данные в таблицахб характеристики столбцов должны быть идентичны
# в результат попадают только не повторяющиеся строки

# select name from catalogs
# union
# select name from rubrics order by name;

# Union All
# В результат попадают все записи

# select name from catalogs
# union all
# select name from rubrics order by name;

# ALL и DISTINCT - взаимозаменяемы, но distinct выводит только уникальные значения, без дублей
# select name from catalogs
# union distinct
# select name from rubrics;

# Уравниваем количество столбцов в таблицах

# select * from catalogs
#   union
# select id, name from products;

# select * from catalogs
#   union
# select id, name from products
#   union
# select id, name from users;

# (select name from catalogs
#  order by name desc limit 2)
# union all
# (select name from rubrics
#  order by name desc limit 2);

# Сложные запросы с использованием JOIN

# select * from users, orders;

# select users.id, users.name, users.birthday_at, orders.id, orders.user_id
#   from users, orders;

# select users.id, users.name, users.birthday_at, orders.id, orders.user_id
#   from users, orders
#   where users.id = orders.user_id;

# JOIN - означает INNER JOIN (пересечение)
# select users.id, users.name, users.birthday_at, orders.id, orders.user_id
# from users
# join orders
# on users.id = orders.user_id;

# select users.id, users.name, users.birthday_at, orders.id, orders.user_id
# from users
# inner join orders
# on users.id = orders.user_id;

# select users.name, count(orders.user_id) as total_orders
# from users
# inner join orders
# on users.id = orders.user_id
# group by orders.user_id
# order by total_orders;

# Сокращения

# select u.name, count(o.user_id) as total_orders
# from users u
# inner join orders o
# on u.id = o.user_id
# group by o.user_id
# order by total_orders;

# LEFT and RIGHT JOIN

# select users.id, users.name, users.birthday_at, orders.id, orders.user_id
# from users
# left join orders
# on users.id = orders.user_id;

# select users.id, users.name, users.birthday_at, orders.id, orders.user_id
# from users
# left join orders
# on users.id = orders.user_id
# where orders.id is null;

# USE vk

# select firstname, lastname, email, phone, sex, birthday, hometown
# from users
# join profiles
# on users.id = profiles.user_id
# where users.id = 2;