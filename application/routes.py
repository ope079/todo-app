from application import app, db
from application.models import Todo
from application.forms import TaskForm
from flask import render_template, request, redirect, url_for
 

@app.route('/')
@app.route('/home')
def home():
    all_todos = Todo.query.all()
    todo_string = ""
    return render_template("index.html", title="Home", all_todos=all_todos)


@app.route('/complete/<int:id>', methods=['GET','POST'])
def complete(id):
    todo = Todo.query.filter_by(id=id).first()
    todo.completed = True
    db.session.commit()
    return redirect(url_for("home"))

@app.route('/incomplete/<int:id>', methods=['GET','POST'])
def incomplete(id):
    todo = Todo.query.filter_by(id=id).first()
    todo.completed = False
    db.session.commit()
    return redirect(url_for("home"))


@app.route('/add', methods=['GET','POST'])   
def add():
    form = TaskForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_todo = Todo(description=form.description.data)
            db.session.add(new_todo)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template("add.html", title="Add a task", form=form)

@app.route('/update/<int:id>',  methods=['GET','POST'])
def update(id):
    form = TaskForm()
    todo = Todo.query.filter_by(id=id).first()
    if request.method =="POST":
        todo.description = form.description.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("update.html", form=form, title="Update Todo", todo=todo)

@app.route('/delete/<int:id>')
def delete(id):
    todo = Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))

