import sqlite3
import os
from datetime import date
from dateutil import parser
from tkinter import *
from tkinter import scrolledtext, messagebox
from tkinter.ttk import Checkbutton
dir_names = r'C:\Users\Анна\PycharmProjects\pythonProject2\database'
# dir_names = r'\\dc\ADRRBASE\base'
file = 'pml.db'
path = os.path.join(dir_names, file)
conn = sqlite3.connect(path)
cursor = conn.cursor()


def check_box1():
    data = 'Согласие на обработку персональных данных'
    if chk_state1.get():
        return data
    else:
        return ''


def check_box2():
    data = 'ИДС первичные виды помощи'
    if chk_state2.get():
        return data
    else:
        return ''


def check_box3():
    data = 'Согласие с общим планом'
    if chk_state3.get():
        return data
    else:
        return ''


def check_box4():
    data = 'ИДС на медицинское вмешательство'
    if chk_state4.get():
        return data
    else:
        return ''


def check_box5():
    data = 'Отказ от госпитализации'
    if chk_state5.get():
        return data
    else:
        return ''


def check_box6():
    data = 'Согласие на отправку анализов по e-mail'
    if chk_state6.get():
        return data
    else:
        return ''


def add_some_docs():
    """Adding other documents"""
    data = text6.get()
    if text6.get():
        return data
    else:
        return ''


def auto_complete():
    """Auto complete fields card number and patients name"""
    card_number = text1.get()
    card_number = [card_number]
    cursor.execute("select name from patients where patient_id=?", card_number)
    data = cursor.fetchone()
    res = str(data).strip(',()\'')
    text2.insert(0, card_number)
    text4.insert(0, res)


def auto_insert_date():          # автозаполнение даты
    current_date = date.today()
    text5.insert(0, current_date)


def del_text():
    txt.delete(1.0, END)


def del_entry():
    text1.delete(0, END)
    text2.delete(0, END)
    text3.delete(0, END)
    text4.delete(0, END)
    text5.delete(0, END)
    text6.delete(0, END)
    text7.delete(0, END)
    chk_state1.set(0)
    chk_state2.set(0)
    chk_state3.set(0)
    chk_state4.set(0)
    chk_state5.set(0)
    chk_state6.set(0)


def find_patient():
    """Search patient using card number"""
    card_number = text1.get()
    card_number = [card_number]
    cursor.execute("select * from patients where patient_id=?", card_number)
    data = cursor.fetchall()
    txt.insert(INSERT, data)
    file_to_print = r'\\dc\ADRRBASE\base\patient.txt'
    # file_to_print = r'C:\Users\yurikov\Desktop\patient.txt'
    with open(file_to_print, 'w', encoding='utf-8') as f:
        f.writelines(str(data))


def find_name():                                   # Добавлен поиск по ФИО
    """"Search patient by name"""
    patient_name = text7.get()
    patient_name = [patient_name]
    cursor.execute("select * from patients where name=?", patient_name)
    data = cursor.fetchall()
    txt.insert(INSERT, data)
    file_to_print = r'C:\Users\yurikov\Desktop\patient.txt'
    with open(file_to_print, 'w', encoding='utf-8') as f:
        f.writelines(str(data))


def add_patient_full_info():
    """Adding patients info to database"""
    if text2.get() == '':
        messagebox.showwarning('Ошибка ввода!', 'Не заполнено поле "№ медицинской карты"!')
    elif text2.get().isalpha():
        messagebox.showwarning('Ошибка ввода!', 'Номер карты должен содержать только цифры!')
    elif text3.get() == '':
        messagebox.showwarning('Ошибка ввода!', 'Не заполнено поле "№ коробки"!')
    elif text4.get() == '':
        messagebox.showwarning('Ошибка ввода!', 'Не заполнено поле "ФИО пациента"!')
    elif text5.get() == '':
        messagebox.showwarning('Ошибка ввода!', 'Не заполнено поле "Дата посещения"!')
    try:
        parser.parse(text5.get())
    except Exception as exc:
        messagebox.showwarning('Неверный формат даты!', exc)
    else:
        card_number = text2.get()
        box_number = text3.get()
        name = str(text4.get()).lower()
        date = text5.get()
        some_docs = add_some_docs()
        docs = check_box1() + ' ' + check_box2() + ' ' + check_box3() + ' ' + check_box4() + \
                              ' ' + check_box5() + ' ' + check_box6() + ' ' + some_docs
        value = [card_number, box_number, name, date, docs]
        sql = "INSERT INTO patients VALUES(?,?,?,?,?)"
        cursor.execute(sql, value)
        conn.commit()
        cursor.execute("select * from patients where patient_id=?", [card_number])
        data = cursor.fetchall()
        txt.insert(INSERT, data)


window = Tk()
window.geometry('600x450')
window.title('База пациентов ООО "ПМЛ СМП   version 1.1"')

lbl1 = Label(window, text="Введите номер карты для поиска пациента", font=("Arial Bold", 12))
lbl1.grid(column=4, row=0)
lbl2 = Label(window, text="Введите номер медицинской карты", font=("Arial Bold", 9))
lbl2.grid(column=0, row=2)
lbl3 = Label(window, text="Введите № коробки", font=("Arial Bold", 9))
lbl3.grid(column=0, row=3)
lbl4 = Label(window, text="Введите ФИО пациента", font=("Arial Bold", 9))
lbl4.grid(column=0, row=4)
lbl5 = Label(window, text="Ведите дату посещения (дд.мм.гггг)", font=("Arial Bold", 9))
lbl5.grid(column=0, row=5)
lbl6 = Label(window, text="Заполните поля для создания новой записи", font=("Times New Roman", 15))
lbl6.grid(column=0, row=0)
lbl7 = Label(window, text="Введите ФИО для поиска пациента", font=("Arial Bold", 12))  # добавлен поиск по ФИО
lbl7.grid(column=4, row=1)


# Ввод пользователя
text1 = Entry(window, width=20, bg="linen")    # state="disabled" - отключить виджет ввода
text2 = Entry(window, width=20, bg="linen")
text3 = Entry(window, width=20, bg="linen")
text4 = Entry(window, width=40, bg="linen")
text5 = Entry(window, width=20, bg="linen")
text6 = Entry(window, width=60, bg="DarkSeaGreen3")
text7 = Entry(window, width=30, bg="Linen")    # добавлено поле поиска по ФИО

text1.focus()   # установка курсора в окне ввода

text1.grid(column=5, row=0)
text2.grid(column=1, row=2)
text3.grid(column=1, row=3)
text4.grid(column=1, row=4)
text5.grid(column=1, row=5)
text6.grid(column=1, row=20)
text7.grid(column=5, row=1)         # добавлено поле поиска по ФИО


# Кнопка
btn1 = Button(window, text="Поиск", bg="lavender", fg="Black", command=find_patient)
btn2 = Button(window, text="Записать", bg="turquoise", fg="Black", command=add_patient_full_info)
btn3 = Button(window, text="Очистить текстовое поле", bg="sienna1", fg="Black", command=del_text)
btn4 = Button(window, text="Очистить поля ввода", bg="sienna1", fg="Black", command=del_entry)
btn5 = Button(window, text="Другие документы", bg="aquamarine4", fg="Black", command=add_some_docs)
btn6 = Button(window, text="Поиск ФИО", bg="Lavender", fg="Black", command=find_name)   # Поиск ФИО
btn7 = Button(window, text="Автозаполнение", bg="Lavender", fg="Black", command=auto_complete)   # Автозаполнение
btn8 = Button(window, text="Текущая дата", bg="Lavender", fg="Black", command=auto_insert_date)   # Автозаполнение дата
btn1.grid(column=6, row=0)
btn2.grid(column=2, row=2)
btn3.grid(column=6, row=4)
btn4.grid(column=6, row=5)
btn5.grid(column=2, row=20)
btn6.grid(column=6, row=1)   # Поиск ФИО
btn7.grid(column=2, row=4)   # Автозаполнение
btn8.grid(column=2, row=5)   # Автозаполнение дата


# Чек-бокс
chk_state1 = IntVar()
chk_state1.set(0)  # 0- False, 1 - True
chk_state2 = IntVar()
chk_state2.set(0)
chk_state3 = IntVar()
chk_state3.set(0)
chk_state4 = IntVar()
chk_state4.set(0)
chk_state5 = IntVar()
chk_state5.set(0)
chk_state6 = IntVar()
chk_state6.set(0)

chk1 = Checkbutton(window, text="Согласие на обработку перс. данных", var=chk_state1, command=check_box1)
chk1.grid(column=0, row=15)
chk2 = Checkbutton(window, text="ИДС первичные виды помощи", var=chk_state2, command=check_box2)
chk2.grid(column=1, row=15)
chk3 = Checkbutton(window, text="Согласие с общим планом", var=chk_state3, command=check_box3)
chk3.grid(column=2, row=15)
chk4 = Checkbutton(window, text="ИДС на мед. вмешательство", var=chk_state4, command=check_box4)
chk4.grid(column=0, row=16)
chk5 = Checkbutton(window, text="Отказ от госпитализации", var=chk_state5, command=check_box5)
chk5.grid(column=1, row=16)
chk6 = Checkbutton(window, text="Согласие на отправку анализов по e-mail", var=chk_state6, command=check_box6)
chk6.grid(column=2, row=16)

# Окно с прокруткой
txt = scrolledtext.ScrolledText(window, width=70, height=35, bg="linen")
txt.grid(column=4, row=5)


# window.mainloop()

# cursor.close()
# conn.close()
