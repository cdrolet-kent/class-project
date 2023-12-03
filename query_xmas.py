import sqlite3

connection = sqlite3.connect("xmas-list.db")

cursor = connection.cursor()

rows = cursor.execute("select id, description from xmas_list")
rows = list(rows)

rows = [ {'id' : row[0], 'description': row[1]} for row in rows ]

print(rows)