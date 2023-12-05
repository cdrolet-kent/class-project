import sqlite3

connection = sqlite3.connect("xmas-list.db")

cursor = connection.cursor()

rows = cursor.execute("select id, description, price from xmas_list")
rows = list(rows)

rows = [ {'id' : row[0], 'description': row[1], 'price':row[2]} for row in rows ]

print(rows)

