import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Combobox 


def update_data_in_all_contact():
    all_contact(listbox_all_contact)
    cursor.execute('''SELECT name FROM contacts''')
    sql_combo_contact = cursor.fetchall()
    combo_contact['values'] = [x for x in sql_combo_contact]
    combo_contact.current(0)


def all_contact(lsbox):
    lsbox.delete(0,tk.END)
    count = 1
    cursor.execute('''SELECT name, phone_number, city, comment
                        FROM contacts, phone 
                   WHERE contacts_id = whose_phone''')
    all_cont = cursor.fetchall()
    for i in all_cont:
        count = print_contact(lsbox, i, count)


def print_contact(lsbx: tk.Listbox, i, count: int) -> int:
    lsbx.insert(count, f'Контакт: {i[0]}')
    lsbx.insert(count+1, f'Номер телефона: {i[1]} ')
    lsbx.insert(count+2, f'Город: {i[2]}')
    lsbx.insert(count+3, f'Примечание: {i[3]}')
    lsbx.insert(count+4, '')
    count += 5
    return count


def add_new_contact():
    user_name_new = txt_name.get()
    user_telephone_new = txt_telephone.get()
    user_city_new = txt_city.get()
    user_note_new = txt_note.get()
    if user_name_new != '' and user_telephone_new != '':
        user_list_new = [txt_name.get(), user_city_new, user_note_new]
        sqlite_add_contact = ('''INSERT INTO contacts 
                       (name, city, comment)
                       VALUES(?,?,?)''')
        cursor.execute(sqlite_add_contact, user_list_new)

        name_id = cursor.lastrowid

        telephone_new_list = user_telephone_new.split(',')
        for i in telephone_new_list:
            sqlite_add_phone = ('''INSERT INTO phone 
                       (whose_phone, phone_number)
                       VALUES(?,?)''')
            cursor.execute(sqlite_add_phone, (name_id, i))

        connection.commit()
        lbl_notification.configure(text='Контакт успешно сохранён', fg='green')
        lbl_notification.place(x=10, y=305)
        update_data_in_all_contact()
    else:
        lbl_notification.configure(text='Ошибка. Не заполнены обязательные поля', fg='red')
        lbl_notification.place(x=10, y=305)
    txt_name.delete(0, tk.END)
    txt_telephone.delete(0, tk.END)
    txt_city.delete(0, tk.END)
    txt_note.delete(0, tk.END)


def btn_choose():
    user_choose = combo_contact.get()

    sql_contact_temp = ('''SELECT name, city, comment
                FROM contacts
                WHERE name = ?''')
    cursor.execute(sql_contact_temp, (user_choose,))
    sql_contact_user = cursor.fetchone()

    sql_phone_temp = ('''SELECT phone_number
                FROM phone
                WHERE whose_phone = ?''')
    
    sql_temp = ('''SELECT contacts_id
                FROM contacts
                WHERE name = ?''')
    cursor.execute(sql_temp, (user_choose,))
    temp = cursor.fetchone()
    cursor.execute(sql_phone_temp, (temp))
    sql_qwerty = cursor.fetchall()

    lbl_fact_name.place(x=7, y=75)
    txt_fact_name.delete(0, tk.END)
    txt_fact_name.insert(0, user_choose)
    txt_fact_name.place(x=10, y=105)

    lbl_fact_telephone.place(x=10, y=140)
    txt_fact_telephone.delete(0, tk.END)
    txt_fact_telephone.insert(0, [x for x in sql_qwerty])
    txt_fact_telephone.place(x=10, y=170)

    lbl_fact_city.place(x=10, y=210)
    txt_fact_city.delete(0, tk.END)
    txt_fact_city.insert(0, sql_contact_user[1])
    txt_fact_city.place(x=10, y=240)

    lbl_fact_note.place(x=10, y=280)
    txt_fact_note.delete(0, tk.END)
    txt_fact_note.insert(0, sql_contact_user[2])
    txt_fact_note.place(x=10, y=310)

    btn_save_changes.place(x=50, y=390)
    btn_delete.place(x=320, y=390)

    lbl_fact_inform.place(x=10, y=440)


def save_changes():
    user_old_name = combo_contact.get()
    user_fact_name = txt_fact_name.get()
    user_fact_telephone = txt_fact_telephone.get()
    user_fact_city = txt_fact_city.get()
    user_fact_note = txt_fact_note.get()
    if user_fact_name != '' and user_fact_telephone != '':
        if user_fact_name == user_old_name:
            sql_temp = ('''SELECT contacts_id
                        FROM contacts
                        WHERE name = ?''')
            cursor.execute(sql_temp, (user_old_name,))
            temp = cursor.fetchone()
            sql_change_contact = ('''UPDATE contacts
                                  SET name = ?, city = ?, comment = ?
                                  WHERE contacts_id = ?''')
            cursor.execute(sql_change_contact, (user_fact_name, user_fact_city, user_fact_note, temp[0]))
            sql_change_phone = ('''UPDATE phone
                                SET phone_number = ?
                                WHERE whose_phone = ?''')
            cursor.execute(sql_change_phone, (user_fact_telephone, temp[0]))
            connection.commit()
        update_data_in_all_contact()
        lbl_fact_notification.configure(text='Изменение успешно сохранено', fg='green')
        lbl_fact_notification.place(x=10, y=350)
        txt_fact_name.delete(0, tk.END)
        txt_fact_telephone.delete(0, tk.END)
        txt_fact_city.delete(0, tk.END)
        txt_fact_note.delete(0, tk.END)
    else:
        lbl_fact_notification.configure(text='Ошибка. Не заполнены обязательные поля', fg='red')


def delete_contact():
    user_contact = combo_contact.get()
    sql_delete = ('''DELETE FROM contacts
                   WHERE name = ? ''')
    cursor.execute(sql_delete, (user_contact,))
    connection.commit()
    update_data_in_all_contact()
    txt_fact_name.delete(0, tk.END)
    txt_fact_telephone.delete(0, tk.END)
    txt_fact_city.delete(0, tk.END)
    txt_fact_note.delete(0, tk.END)
    lbl_fact_notification.configure(text='Контакт успешно удален', fg='green')
    lbl_fact_notification.place(x=10, y=350)


def search_by_parametr():
    listbox_parametr.delete(0,tk.END)
    listbox_parametr.place(x=0, y=135)
    user_text_parametr = txt_parametr.get()
    if user_text_parametr == '':
        all_contact(listbox_parametr)
    else:
        count = 1
        cursor.execute('''SELECT name, phone_number, city, comment
                    FROM contacts, phone 
                    WHERE contacts_id = whose_phone''')
        all_cont = cursor.fetchall()
        for item in all_cont:
            for j in item:
                if user_text_parametr in j:
                    count = print_contact(listbox_parametr, item, count)




connection = sqlite3.connect('tel_guide.db')
cursor = connection.cursor()

contacts_table = '''CREATE TABLE IF NOT EXISTS contacts (
                        contacts_id INTEGER PRIMARY KEY AUTOINCREMENT,                        
                        name TEXT NOT NULL,
                        city TEXT,
                        comment TEXT);'''

cursor.execute(contacts_table)

phone_numbers_table = '''CREATE TABLE IF NOT EXISTS phone (
                        phone_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        whose_phone INTEGER NOT NULL,
                        phone_number TEXT NOT NULL,
                        FOREIGN KEY (whose_phone)
                        REFERENCES contacts (contacts_id) ON DELETE CASCADE);'''

cursor.execute(phone_numbers_table)

window = tk.Tk()  
window.title("Телефонный справочник")
window.geometry('500x500')
window.resizable(width=False, height=False)
window.configure(background='black')

tab_control = ttk.Notebook(window)
tab_all_contact = tk.Frame(tab_control, background='beige')
tab_control.add(tab_all_contact, text='Все контакты')
listbox_all_contact = tk.Listbox(tab_all_contact, font=("Arial", 12), bg='beige')
listbox_all_contact.yview()
listbox_all_contact.xview()
all_contact(listbox_all_contact)
listbox_all_contact.pack(fill=tk.BOTH, expand=True)


tab_add_contact = tk.Frame(tab_control, background='#87CEEB')   
tab_control.add(tab_add_contact, text='Добавление нового контакта')

lbl_name = tk.Label(tab_add_contact, text='*Введите имя контакта:', font=("Arial", 12), bg='#87CEEB')
lbl_name.place(x=7, y=5)
txt_name = tk.Entry(tab_add_contact, width=52, font =("Arial", 12))
txt_name.place(x=10, y=35)

lbl_telephone = tk.Label(tab_add_contact, text='*Введите номер телефона', font=("Arial", 12), bg='#87CEEB')
lbl_telephone.place(x=7, y=75)
lbl_telephone_1 = tk.Label(tab_add_contact, text='Если номеров больше одного, тогда запишите их через запятую', font=("Arial", 12), bg='#87CEEB')
lbl_telephone_1.place(x=10, y=95)
txt_telephone = tk.Entry(tab_add_contact, width=52, font =("Arial", 12))
txt_telephone.place(x=10, y=125)

lbl_city = tk.Label(tab_add_contact, text='Введите город', font=("Arial", 12), bg='#87CEEB')
lbl_city.place(x=10, y=165)
txt_city = tk.Entry(tab_add_contact, width=52, font =("Arial", 12))
txt_city.place(x=10, y=195)

lbl_note = tk.Label(tab_add_contact, text='Введите дополнительную информацию', font=("Arial", 12), bg='#87CEEB')
lbl_note.place(x=10, y=235)
txt_note = tk.Entry(tab_add_contact, width=52, font =("Arial", 12))
txt_note.place(x=10, y=265)

lbl_notification = tk.Label(tab_add_contact, font=("Arial", 12), bg='#87CEEB')

btn_save_new = tk.Button(tab_add_contact, text="Сохранить контакт", font=("Arial", 12), bg='#20B2AA', command=add_new_contact)
btn_save_new.place(x=165, y=360)
lbl_inform = tk.Label(tab_add_contact, text='* - Обязательные поля для ввода', font=("Arial", 12), bg='#87CEEB')
lbl_inform.place(x=10, y=440)


tab_change_contact = tk.Frame(tab_control, background='#87CEEB')
tab_control.add(tab_change_contact, text='Изменение контакта')

lbl_select_contact = tk.Label(tab_change_contact, text='Выберите контакт', font=("Arial", 12), bg='#87CEEB')
lbl_select_contact.place(x=7, y=5)
combo_contact = Combobox(tab_change_contact, state="readonly", font=("Arial", 12), width= 30)
cursor.execute('''SELECT name FROM contacts''')
sql_combo_contact = cursor.fetchall()
combo_contact['values'] = [x for x in sql_combo_contact]
combo_contact.current(0)
combo_contact.place(x=10, y=35)

btn_choosing_contact = tk.Button(tab_change_contact, text="Выбрать", font=("Arial", 12), bg='#20B2AA', command=btn_choose)
btn_choosing_contact.place(x=315, y=30)

lbl_fact_name = tk.Label(tab_change_contact, text='*Имя контакта', font=("Arial", 12), bg='#87CEEB')
txt_fact_name = tk.Entry(tab_change_contact, width=52, font=("Arial", 12))

lbl_fact_telephone = tk.Label(tab_change_contact, text='*Номер телефона', font=("Arial", 12), bg='#87CEEB')
txt_fact_telephone = tk.Entry(tab_change_contact, width=52, font=("Arial", 12))

lbl_fact_city = tk.Label(tab_change_contact, text='Город', font=("Arial", 12), bg='#87CEEB')
txt_fact_city = tk.Entry(tab_change_contact, width=52, font=("Arial", 12))

lbl_fact_note = tk.Label(tab_change_contact, text='Примечание', font=("Arial", 12), bg='#87CEEB')
txt_fact_note = tk.Entry(tab_change_contact, width=52, font=("Arial", 12))

lbl_fact_notification = tk.Label(tab_change_contact, font=("Arial", 12), bg='#87CEEB')
btn_save_changes = tk.Button(tab_change_contact, text="Сохранить изменения", font=("Arial", 12), bg='#20B2AA', command=save_changes)
btn_delete = tk.Button(tab_change_contact, text="Удалить контакт", font=("Arial", 12), bg='#20B2AA', command=delete_contact)
lbl_fact_inform = tk.Label(tab_change_contact, text='* - Обязательные поля для ввода', font=("Arial", 12), bg='#87CEEB')


tab_search_by = tk.Frame(tab_control, background='#87CEEB')
tab_control.add(tab_search_by, text='Поиск по параметру')

lbl_parametr = tk.Label(tab_search_by, text='Выберите параметр', font=("Arial", 12), bg='#87CEEB')
lbl_parametr.place(x=10,y=5)
combo_parametr = Combobox(tab_search_by, state="readonly",  width=30, font=("Arial", 12))
combo_parametr['values'] = ['Имя контакта', 'Номер телефона', 'Город', 'Примечание']
combo_parametr.current(0)
combo_parametr.place(x=10, y=35)
btn_parametr = tk.Button(tab_search_by, text="Поиск", font=("Arial", 12), bg='#20B2AA', command=search_by_parametr)
btn_parametr.place(x=320, y=100)
lbl_parametr_1 = tk.Label(tab_search_by, text='Введите, что искать', font=("Arial", 12), bg='#87CEEB')
lbl_parametr_1.place(x=10, y=75)
txt_parametr = tk.Entry(tab_search_by, width=32, font=("Arial", 12))
txt_parametr.place(x=10, y=105)

listbox_parametr = tk.Listbox(tab_search_by, font=("Arial", 12), width=55, height=18, bg='beige')
listbox_all_contact.yview()
tab_control.pack(expand=1, fill='both') 


window.mainloop()
