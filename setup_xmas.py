import sqlite3

connection = sqlite3.connect("xmas-list.db")

cursor = connection.cursor()

try:
    cursor.execute("drop table xmas_list")
except:
    pass

cursor.execute("create table xmas_list(id integer primary key, description text, price text)")

cursor.execute("INSERT INTO xmas_list (description,price) VALUES ('Nike Shoes', '$150')")
cursor.execute("INSERT INTO xmas_list (description,price) VALUES ('Brown Hoodie', '$45')")
cursor.execute("INSERT INTO xmas_list (description,price) VALUES ('Gift Card(s)', '$25')")
cursor.execute("INSERT INTO xmas_list (description,price) VALUES ('Coffee Machine', '$1000')")
cursor.execute("INSERT INTO xmas_list (description,price) VALUES ('Bar Instruments', '$95')")

connection.commit()
connection.close()
print("done.")

