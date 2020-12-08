from application import app, db
from application.models import Todo
from application.forms import BasicForm
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, DecimalField, SelectField, SubmitField



@app.route('/add/<item>', methods=['POST'])
def add(item):

    new_todo = Todo(name=item)
    db.session.add(new_todo)
    db.session.commit()
    return render_template('home.html', todos = Todo.query.all())


@app.route('/read')
def read():
    all_todos = Todo.query.all()
    todo_string = ""
    for todo in all_todos:
        todo_string +=  str(todo.id) + ". " + str(todo.date) + " "  + todo.name + "<br>"
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
        todo_string +=  str(todo.id) + ". " + str(todo.date) + " " + todo.name + "<br>"
    return todo_string

@app.route('/count')
def count():
    all_todos = Todo.query.all()
    todo_count = 0
    for i in range(len(all_todos)+1):
        todo_count =+ i
    return str(todo_count)