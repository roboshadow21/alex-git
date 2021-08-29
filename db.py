import pandas as pd
import os
import sqlite3

# conn = sqlite3.connect('pml.db')
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
# cursor.execute("""CREATE TABLE IF NOT EXISTS patients
#               (patient_id text, box_number text, name text, date text, docs text)""")

# conn.commit()
# path = r'C:\Users\yurikov\Desktop'
# file = 'example.xlsx'
# file_obj = os.path.join(path, file)
# content = pd.read_excel(file_obj)
# df = pd.DataFrame(content)
# res = list(df.values)
# Lower symbols in patients names
# for el in range(len(res)):
#     res[el][2] = res[el][2].lower()


# cursor.executemany("INSERT INTO patients VALUES (?,?,?,?,?)", res)
# conn.commit()


def add_patient_full_info():
    """Merge name and surname"""
    # add input for docs l[5] + l[6] visit date
    print('Введите данные пациента через пробел: № карты, № коробки, ФИО (Иванов_Иван_Иванович), дату визита')

    data = input('Введите данные пациента: ').lower().split()
    docs = input('Введите названия документов: ')
    docs = [docs]
    li2 = [data[2] + ' ' + data[3] + ' ' + data[4]]  # ФИО
    li3 = data[0:2] + li2 + data[5:] + docs
    sql = "INSERT INTO patients VALUES(?,?,?,?,?)"
    cursor.execute(sql, li3)
    conn.commit()


# add_patient_full_info()


# def find_patient_full_info():
#     card_number = input('Введите номер медицинской карты: ')
#     card_number = [card_number]
#     cursor.execute("select * from patients where patient_id=?", card_number)
#     print(cursor.fetchall())

# find_patient_full_info()


# def update_box_number():
#     card_number = input('Введите номер медицинской карты: ')
#     box_number = input('Введите новый номер коробки: ')
#     value = [box_number, card_number]
#     cursor.execute("update patients set box_number=? where patient_id=?", value)
#     conn.commit()
#     print(f'Номер коробки изменен на: ', box_number)
#     cursor.execute("select * from patients where patient_id=?", [card_number])
#     print(cursor.fetchall())

# update_box_number()


# sql = "INSERT INTO patients VALUES('5', '555555', 'Киргуду Болтабек', 'ИДС, ', '18/18/1818')"
# cursor.execute(sql)
# conn.commit()

# sql = "DELETE FROM patients WHERE name='Шуравин Алексей'"
# cursor.execute(sql)
# conn.commit()

# sql = "SELECT * FROM patients WHERE name=?"
# cursor.execute(sql, [('ЗИНЧУК Алиса Владимировна')])

sql = "SELECT name FROM patients WHERE patient_id='26661'"
cursor.execute((sql))

# sql = "SELECT * FROM patients WHERE name LIKE 'Кир%'"
# cursor.execute(sql)

# update
# lst = [('Матпомощь, отказ, согласие'), ('01/01/2021')]
# # lst2 = ['01/01/2021']
# cursor.execute("UPDATE patients SET docs=?, date=? WHERE patient_id=1374313", lst)
# conn.commit()

# partial input
# temp = ['юр%']
# cursor.execute("select * from patients where name like ?", temp)

# cursor.execute("SELECT name, docs FROM patients")
# cursor.execute("""SELECT * FROM patients WHERE date='01/07/2021'""")
# cursor.execute("""SELECT * FROM patients WHERE name='ЗИНЧУК Алиса Владимировна'""")
# cursor.execute("""SELECT * FROM patients WHERE name='Киргуду Болтабек'""")
# cursor.execute("""SELECT * FROM patients WHERE name='Алтын'""")
# cursor.execute("""SELECT * FROM patients WHERE box_number=5""")
# cursor.execute("SELECT * FROM patients WHERE name='Юриков Алексей'")
# cursor.execute("SELECT * FROM patients WHERE patient_id=1668967")
# cursor.execute("SELECT * FROM patients WHERE patient_id=777777")
# print('--№ ЭМК, -№ коробки, ФИО пациента, -------дата визита, --документы')
# cursor.execute("SELECT * FROM patients WHERE patient_id=1374313")  # Товара
# cursor.execute("""SELECT * FROM patients WHERE docs='ИДС, '""")
# cursor.execute("SELECT * FROM patients WHERE name LIKE 'Шур%'")

# rec = cursor.execute("select * from patients")
# for el in rec:
#     print(el)

# for row in cursor.execute("SELECT rowid, * FROM patients ORDER BY box_number"):
#     print(row)

print(cursor.fetchall())
cursor.close()
conn.close()


