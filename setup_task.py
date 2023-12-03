import sqlite3

connection = sqlite3.connect("task-list.db")

cursor = connection.cursor()

try:
    cursor.execute("drop table task_list")
except:
    pass

cursor.execute("create table task_list(id integer primary key, description text)")

for item in ['finish school projects', 'groceries', 'laundry', 'clean apartment', 'shopping with girlfriend']:
    cursor.execute(f"insert into task_list (description) values ('{item}')")

connection.commit()
connection.close()
print("done.")

