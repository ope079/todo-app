from application import app, db
from application.models import Todo

@app.route('/add/<item>')
def add(item):
    new_todo = Todo(name=item)
    db.session.add(new_todo)
    db.session.commit()
    return item 

@app.route('/read')
def read():
    all_todos = Todo.query.all()
    todo_string = ""
    for todo in all_todos:
        todo_string += str(todo.id) + ". " + todo.name + "<br>"
    return todo_string

@app.route('/update/<int:id>/<name_update>')
def update(id, name_update):
    first_todo = Todo.query.get(id)
    first_todo.name = name_update
    db.session.commit()
    return first_todo.name

@app.route('/delete/<int:id>')
def delete(id):
    first_todo = Todo.query.get(id)
    db.session.delete(first_todo)
    db.session.commit()
    all_todos = Todo.query.all()
    todo_string = ""
    for todo in all_todos:
        todo_string += str(todo.id) + ". " + todo.name + "<br>"
    return todo_string

@app.route('/count')
def count():
    all_todos = Todo.query.all()
    todo_count = 0
    for i in range(len(all_todos)+1):
        todo_count =+ i
    return str(todo_count)