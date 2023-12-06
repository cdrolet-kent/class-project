from bottle import route, post, run, template, redirect, request
import database

@route("/")
def get_index():
    redirect("/home")

@route("/home")
def get_home():
    return template("home.tpl")

@route("/list")
def get_list():
    items = database.get_items_xmas()
    return template("list.tpl", xmas_list=items)

@route("/list/search")
def get_search():
    return template("search.tpl")

@post("/list/search")
def post_search():
    description = request.forms.get("description")
    print("description = ", [description])
    database.search_list()

@route("/task")
def get_task():
    items = database.get_items_task()
    return template("task.tpl", task_list=items)

@route("/list/add")
def get_add():
    return template("add_list.tpl")

@post("/list/add")
def post_add():
    description = request.forms.get("description")
    price = request.forms.get("price")
    database.add_item_xmas(description, price)
    redirect("/list")

@route("/task/add")
def get_add():
    return template("add_task.tpl")

@post("/task/add")
def post_add():
    description = request.forms.get("description")
    print("description = ", [description])
    database.add_item_task(description)
    redirect("/task")

@route("/list/update/<id>")
def get_update(id):
    items = database.get_items_xmas(id)
    return template("update_list.tpl", item=items[0])

@post("/list/update")
def post_update():
    description = request.forms.get("description")
    price = request.forms.get("price")
    id = request.forms.get("id")
    database.update_item_xmas(id, description, price)
    redirect("/list")

@route("/task/update/<id>")
def get_update(id):
    items = database.get_items_task(id)
    return template("update_task.tpl", item=items[0])

@post("/task/update")
def post_update():
    description = request.forms.get("description")
    id = request.forms.get("id")
    print("/task/update",[id,description])
    database.update_item_task(id, description)
    redirect("/task")

@route("/list/delete/<id>")
def get_delete(id):
    database.delete_item_xmas(id)
    redirect("/list")

@route("/task/delete/<id>")
def get_delete(id):
    database.delete_item_task(id)
    redirect("/task")

run(host='localhost', port=8080)

