import sqlite3

connection = sqlite3.connect("xmas-list.db")

cursor = connection.cursor()

try:
    cursor.execute("drop table xmas_list")
except:
    pass

cursor.execute("create table xmas_list(id integer primary key, description text)")

for item in ['shoes', 'brown hoodie', 'gift cards', 'coffee machine', 'bar instruments']:
    cursor.execute(f"insert into xmas_list (description) values ('{item}')")

connection.commit()
connection.close()
print("done.")

