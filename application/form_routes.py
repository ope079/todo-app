from application import app, db
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, DecimalField, SelectField, SubmitField
from application.models import Todo

@app.route('/',methods=['GET', 'POST'])
@app.route('/home',methods=['GET', 'POST'])
def home_page():
    
    return render_template('home.html', todos = Todo.query.all())

@app.route('/add', methods=['POST'])
def include():
    form = BasicForm()

    item = form.name_field.data
    new_todo = Todo(name=item)
    db.session.add(new_todo)
    db.session.commit()
    return render_template('home.html', todos = Todo.query.all())

@app.route('/completed', methods=['GET'])
def view_completed():
    form = BasicForm()
    completed_field = form.completed_field.data

    if completed_field == 'Yes':
        return render_template('completed.html',form=form, todos = Todo.query.all())

@app.route('/edit', methods=['PUT'])
def edit():
    first_todo = Todo.query.get(id)
    first_todo.name = name_update
    db.session.commit()
    return render_template('edit.html')

@app.route('/delete', methods=['DELETE'])
def delete_task():
    return render_template('completed.html',form=form, todos = Todo.query.all())
        