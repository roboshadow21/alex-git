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

# select filename from media where user_id = 3
#   and media_type_id = (
#   select id from media_types where name like 'photo'
#   );

# select count(*) from media where user_id = 3
#   and media_type_id = (
#   select id from media_types where name like 'photo'
#   );

# select * from friendship where user_id = 1 and status is true;
# select * from friendship where user_id = 1 and status;

# select * from news where user_id in (
#   select friend_id from friendship where user_id = 1 and status
# );

# select * from news where user_id = 1
# UNION
# select * from news where user_id in (
#   select friend_id from friendship where user_id = 1 and status
#   ) order by created_at desc limit 10;

# select to_subject_id from news where user_id = 1
# union
# select to_subject_id from news where user_id in (
#   select friend_id from friendship where user_id = 1 and status
# );

# select to_subject_id, count(*) from likes where to_subject_id in(
#   select to_subject_id from news where user_id = 1
#     union
#   select to_subject_id from news where user_id in (
#   select friend_id from friendship where user_id = 1 and status)
# )
# group by to_subject_id;

# select count(id) as news, monthname(created_at) as month
#   from news
#   group by month
#   order by field(month, 'January', 'February') desc;

# select user_id,
#        case (sex)
#        when 'm' then 'man'
#        when 'f' then 'woman'
#        end as sex,
#        'age'
#  from profiles
#  where user_id in (
#   select friend_id
#    from friendship
#    where user_id = 1
#     and confirmed_at is not null
#  );
