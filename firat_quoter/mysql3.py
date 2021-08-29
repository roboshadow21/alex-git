# Запросы

# select * from users where id = 1;
# select
#   firstname,
#   lastname,
#   'main_photo',
#   'city'
#   from users
#   where id = 1;

# Выбираем фото
# select
#   firstname,
#   lastname,
#   (select photo_id from profiles where user_id = 1),
#   'city'
#   from users
#   where id = 1;
# Находим путь к фото
# select
#   firstname,
#   lastname,
#   (select filename from media where id =
#     (select photo_id from profiles where user_id = 1)
#     ) as main_photo,
#   'city'
#   from users
#   where id = 1;

# Находим город
# select
#   firstname,
#   lastname,
#   (select filename from media where id =
#     (select photo_id from profiles where user_id = 1)
#     ) as main_photo,
#   (select hometown from profiles where user_id = 1) as city
#   from users
#   where id = 1;

# select * from media_types where name like 'photo';

# select filename from media
#   where user_id = 3
#     and media_type_id = (
#       select id from media_types where name like 'photo'
#     );

# select body,
#   (select filename from media where subject_type_id = (
#   select id from subject_types where name like 'photo'
#   )) as filename,
#   created_at
#   from news
#   where user_id = 1;