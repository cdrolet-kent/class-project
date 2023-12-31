import sqlite3

connection = sqlite3.connect("xmas-list.db")
connection = sqlite3.connect("task-list.db")

def get_items_xmas(id=None):
    cursor = connection.cursor()
    if id == None:
        rows = cursor.execute("select id, description, price from xmas_list")
    else:
        rows = cursor.execute(f"select id, description, price from xmas_list where id={id}")
    rows = list(rows)
    rows = [ {'id' : row[0], 'description': row[1], 'price':row[2]} for row in rows ]
    return rows

def get_items_task(id=None):
    cursor = connection.cursor()
    if id == None:
        rows = cursor.execute("select id, description from task_list")
    else:
        rows = cursor.execute(f"select id, description from task_list where id={id}")
    rows = list(rows)
    rows = [ {'id' : row[0], 'description': row[1]} for row in rows ]
    return rows

def search_list(description):
    cursor = connection.cursor()
    rows = cursor.execute(f"select description from xmas_list where description={description}")
    if description == rows:
        return description
    else:
        return "The item does not exist"

def add_item_xmas(description, price):
    cursor = connection.cursor()
    cursor.execute(f"insert into xmas_list(description, price) values ('{description}', '{price}')")
    connection.commit()

def add_item_task(description):
    cursor = connection.cursor()
    cursor.execute(f"insert into task_list(description) values ('{description}')")
    connection.commit()

def update_item_xmas(id, description, price):
    cursor = connection.cursor()
    statement = f"update xmas_list set description='{description}', price='{price}' where id={id}"
    cursor.execute(statement)
    connection.commit()

def update_item_task(id, description):
    cursor = connection.cursor()
    statement = f"update task_list set description='{description}' where id={id}"
    cursor.execute(statement)
    connection.commit()

def delete_item_xmas(id):
    cursor = connection.cursor()
    cursor.execute(f"delete from xmas_list where id={id}")
    connection.commit()

def delete_item_task(id):
    cursor = connection.cursor()
    cursor.execute(f"delete from task_list where id={id}")
    connection.commit()

def set_up_database_xmas():
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

def set_up_database_task():
    cursor = connection.cursor()
    try:
        cursor.execute("drop table task_list")
    except:
        pass
    cursor.execute("create table task_list(id integer primary key, description text)")
    for item in ['finish school projects', 'groceries', 'laundry', 'clean apartment', 'shopping with girlfriend']:
        cursor.execute(f"insert into task_list (description) values ('{item}')")
    connection.commit()

def test_set_up_database_xmas():
    print("testing set_up_database_xmas()")
    set_up_database_xmas()
    items = get_items_xmas()
    assert len(items) == 5
    descriptions = [item['description'] for item in items]
    prices = [item['price'] for item in items]
    for description in ['Nike Shoes', 'Brown Hoodie', 'Gift Card(s)', 'Coffee Machine', 'Bar Instruments']:
        assert description in descriptions
    for price in ['$150', '$45', '$25', '$1000', '$95']:
        assert price in prices

def test_set_up_database_task():
    print("testing set_up_database_task()")
    set_up_database_task()
    items_task = get_items_task()
    assert len(items_task) == 5
    descriptions = [item['description'] for item in items_task]
    for description in ['finish school projects', 'groceries', 'laundry', 'clean apartment', 'shopping with girlfriend']:
        assert description in descriptions

def test_get_items_xmas():
    print("testing get_items_xmas()")
    items = get_items_xmas()
    assert type(items) is list
    assert len(items) > 0
    for item in items:
        assert type(item) is dict
        assert 'id' in item
        assert type(item['id']) is int
        assert 'description' in item
        assert type(item['description']) is str
        assert 'price' in item
        assert type(item['price']) is str
    id = items[0]['id']
    description = items[0]['description']
    price = items[0]['price']
    items = get_items_xmas(id)
    assert type(items) is list
    assert len(items) == 1
    assert items[0]['id'] == id
    assert items[0]['description'] == description
    assert items[0]['price'] == price

def test_get_items_task():
    print("testing get_items_task()")
    items = get_items_task()
    assert type(items) is list
    assert len(items) > 0
    for item in items:
        assert type(item) is dict
        assert 'id' in item
        assert type(item['id']) is int
        assert 'description' in item
        assert type(item['description']) is str
    id = items[0]['id']
    description = items[0]['description']
    items = get_items_task(id)
    assert type(items) is list
    assert len(items) == 1
    assert items[0]['id'] == id
    assert items[0]['description'] == description

def test_add_item_xmas():
    print("testing add_item_xmas()")
    set_up_database_xmas()
    items = get_items_xmas()
    original_length = len(items)
    add_item_xmas("golf hat", "$28")
    items = get_items_xmas()
    assert len(items) == original_length + 1
    descriptions = [item['description'] for item in items]
    prices = [item['price'] for item in items]
    assert "golf hat" in descriptions
    assert "$28" in prices

def test_add_item_task():
    print("testing add_item_task()")
    set_up_database_task()
    items = get_items_task()
    original_length = len(items)
    add_item_task("dinner reservation")
    items = get_items_task()
    assert len(items) == original_length + 1
    descriptions = [item['description'] for item in items]
    assert "dinner reservation" in descriptions

def test_update_item_xmas():
    print("testing update_item_xmas()")
    set_up_database_xmas()
    items = get_items_xmas()
    id = items[1]['id']
    description = items[1]['description']
    description = items[1]['price']
    update_item_xmas(id, "coffe syrup", "$65")
    items = get_items_xmas()
    assert items[1]['description'] == "coffe syrup"
    assert items[1]['price'] == "$65"

def test_update_item_task():
    print("testing update_item_task()")
    set_up_database_task()
    items = get_items_task()
    id = items[1]['id']
    description = items[1]['description']
    update_item_task(id, "finish exams")
    items = get_items_task()
    assert items[1]['description'] == "finish exams"

def test_delete_item_xmas():
    print("testing delete_item_xmas()")
    set_up_database_xmas()
    add_item_xmas("mango", "$5")
    items = get_items_xmas()
    for item in items:
        if item['description'] == 'mango':
            delete_item_xmas(item['id'])
    items = get_items_xmas()
    for item in items:
        assert item['description'] != 'mango'

def test_delete_item_task():
    print("testing delete_item_task()")
    set_up_database_task()
    add_item_task("mango")
    items = get_items_task()
    for item in items:
        if item['description'] == 'mango':
            delete_item_task(item['id'])
    items = get_items_task()
    for item in items:
        assert item['description'] != 'mango'

if __name__ == "__main__":
    test_set_up_database_xmas()
    test_get_items_xmas()
    test_add_item_xmas()
    test_update_item_xmas()
    test_delete_item_xmas()
    test_set_up_database_task()
    test_get_items_task()
    test_add_item_task()
    test_update_item_task()
    test_delete_item_task()
    print("done.")