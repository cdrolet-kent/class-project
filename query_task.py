import sqlite3

connection = sqlite3.connect("task-list.db")

cursor = connection.cursor()

rows2 = cursor.execute("select id, description from task_list")
rows2 = list(rows2)

rows2 = [ {'id' : row[0], 'description': row[1]} for row in rows2 ]

print(rows2)

