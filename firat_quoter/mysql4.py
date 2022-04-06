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

# select news.user_id, news.body, news.created_at
# from news
# join friendship
# on news.user_id = friendship.friend_id
# join users
# on friendship.user_id = users.id
# where news.user_id = 2;

# select friend_id from friendship where user_id = 2;
# select * from news where user_id in (7, 8, 17);

# select messages.body, users.firstname, users.lastname, messages.created_at
# from messages
# join users
# on users.id = messages.to_user_id
# where messages.from_user_id = 2;

# select messages.body, users.firstname, users.lastname, messages.created_at
#   from messages
#     join users
#       on users.id = messages.from_user_id
#   where messages.to_user_id = 2;

# Считаем количество друзей
# select firstname, lastname, count(*) as total_friends
#   from users
#     join friendship
#       on users.id = friendship.user_id
#   group by friendship.user_id
#  order by total_friends desc;

# Получаем данные о медиафайлах, владельце, лайках
# select media.filename,
#   media_types.name,
#   count(*) as total_likes,
#   concat(firstname, ' ', lastname) as owner
#   from media
#     join media_types
#       on media.media_type_id = media_types.id
#     join likes
#       on media.id = likes.to_subject_id
#     join users
#       on users.id = media.user_id
#   where users.id = 2
#   group by media.id;

# Подсчет количества сообществ у пользователя
# select firstname, lastname, count(*) as total_communities
#   from users
#     join communities_users
#       on users.id = communities_users.user_id
#   group by users.id;

# Среднее количество сообществ у пользователя
# select avg(total_communities) as average_communities
#   from (
#     select firstname, lastname, count(*) as total_communities
#       from users
#         join communities_users
#           on users.id = communities_users.user_id
#   group by users.id
#   ) as list;

# select firstname, lastname, count(*) as total_likes
#   from users
#     join media
#       on users.id = media.user_id
#     join likes
#       on media.id = likes.to_subject_id
#   group by users.id
#   order by total_likes desc
#   limit 10;

# Транзакция

# start transaction;
# insert into users (firstname, lastname, email, phone)
#   values('Old', 'User', 'user@mail.com', 4567893);
#
# select @user_id := (select max(id) from users);
#
# insert into profiles (user_id, sex, birthday, hometown, photo_id)
#   values(@user_id, 'M', '1969-09-29', 'Chimki', 459);
# commit;