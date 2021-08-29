import os
import pandas as pd
import numpy as np
# import openpyxl
# import warnings

path = r'C:\Users\yurikov\Desktop\test'
# file = 'example3.xlsx'
file = 'zoo.csv'
# file = 'test.xlsx'
# file = 'titanic.csv'
file_obj = os.path.join(path, file)
# with warnings.catch_warnings(record=True):
#     warnings.simplefilter("always")
#     data = pd.read_excel(file_obj, engine="openpyxl")     #names=[1, 2, 3, 4] - можно задать заголовки

# Чтение из Excel и scv
# data = pd.read_excel(file_obj)        #engine="openpyxl"
# data = pd.read_csv(file_obj, sep=',')
data = pd.read_csv(file_obj, names=['animal', 'uniq_id', 'water_need'])
df = pd.DataFrame(data)

# print(data)
# print(data.animal)  # название столбца, как атрибут (выводит список)
# print(data.head())    # вывод первых 5 строк
# print(data.head()[['animal']])    # вывод первых 5 строк с отбором колонок
# print(data.tail())    # вывод последних 5 строк
# print(data.sample(5))    # вывод случайных 5 строк
# print(data[['animal', 'water_need']])  # вывод выбранных колонок
# print(data.animal)  # вывод списка без заголовка
# print(data[data.animal == 'lion'])   # фильтр по значению в колонке

# Агрегация данных
# print(data.count())  # считает количество значений в каждой колонке
# print(data.animal.count()) # -- то же в выбранной колонке
# print(data.water_need.sum())  # сумма значений в колонке
# print(data.water_need.min())  # мин значение
# print(data.water_need.max())  # макс значение
# print(data.water_need.mean())  # среднее значение
# print(data.water_need.median())  # медиана
# print(data.groupby('animal').mean())  # группировка по колонке animal с выводом среднего значения
# print(data.groupby('animal').mean()[['water_need']])
# print(data.groupby('animal').mean().water_need)  # объект Series
# print(data.groupby('animal').count()[['water_need']])
# print(data[data.animal == 'lion'].groupby('uniq_id').min())

# print(df.head())
# print(df.iloc[0:2])  # доступ по индексу
# print(df.animal)
# print(df['animal'])
# print(df.index)
# print(df[df.water_need > 500][['animal', 'water_need']])

# df['new'] = df['water_need'] / df['uniq_id'] * 1000  # добавляем новый столбец
# print(df)
# df.drop(['new'], axis='columns')  # удаление нового столбца
# del df['new']  # удаление нового столбца
# print(df)
# df = df.rename(columns={'animal': 'ANIMALS'}) # переименование столбца
# print(df)
# df.to_csv('new.csv')  # записать в файл
# df = pd.read_csv('new.csv')  # прочитать файл
# print(df)
# print(df['animal'].describe())  # описание элементов колонки


# titanic
# print(data.head())
# print(df.head())
# print(data.groupby(['Sex', 'Survived'])['PassendgerID'].count())



# print(df.get(["Часы", "Итог"]))
# print(df.head(5))
# print(df.tail(2))
# print(df.columns)
# print(df.values)
# print(df['Часы'].describe())

# print(df[['Часы', 'Суммы', 'Итог']])
# print(df[1:3])
# print(df.iloc[:, 2])
# print(df.groupby(['Часы', 'Итог']).count())
# print(df[['Часы', 'ЗП/час']].cumprod())




# Конвертация из sqlite3 в Excel

# import sqlite3
# import pandas as pd
#
# conn = sqlite3.connect('test.db')
#
# df = pd.read_sql_query("SELECT * FROM patients", conn)
# print(df)

# sql_file = 'sql.xlsx'
# new_file = df.to_excel(os.path.join(path, sql_file)) # запись в Excel
# conn.close()

# Запись в MySQL (разные варианты)

# df.to_sql(con=engine, name='table_name', if_exists='replace') #- запись в sql

# import psycopg2
# from sqlalchemy import create_engine
# # предполагаем, что у нас есть DataFrame с названием 'date'
# # Подключаемся к базе данных PGSQL
# engine = create_engine('postgresql+psycopg2://user_name:password@host_name_or_ip/database_name')
# # Пишем в PGSQL
# data.to_sql('table_name', con=engine, schema = 'dbo', if_exists='replace')

# import pymysql
# user = 'root'
# passw = 'my-secret-pw-for-mysql-12ud'
# host =  '172.17.0.2'
# port = 3306
# database = 'data_2'
# conn = pymysql.connect(host=host,
#                        port=port,
#                        user=user,
#                        passwd=passw,
#                        db=database,
#                        charset='utf8')
#
# data.to_sql(name=database, con=conn, if_exists='replace', index=False, flavor='mysql')

# from pandas.io import sql
# from sqlalchemy import create_engine
#
# engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
#                        .format(user="root",
#                                pw="your_password",
#                                db="pandas"))
# df.to_sql(con=engine, name='table_name', if_exists='replace')