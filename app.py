from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import redirect
from flask import url_for


# Creates an app that is named after our file.
app = Flask(__name__)

# Configs
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://tyler.lanigan@localhost:5432/todoapp'
# Discussed here: https://stackoverflow.com/questions/33738467/how-do-i-know-if-i-can-disable-sqlalchemy-track-modifications/33790196#33790196
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Todo Table
class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer(), primary_key=True)
    description = db.Column(db.String(), nullable=False)

    # Dundar repr method for printing
    def __repr__(self):
        return f'<Todo: {self.id} {self.description}>'


# Creates all the tables if they haven't been created
db.create_all()


@app.route('/todos/create', methods=['POST'])
def create_todo():
    description = request.form.get('description', '')
    todo = Todo(description=description)
    db.session.add(todo)
    db.session.commit()
    # Redirect to the index url to display the todolist.
    return redirect(url_for('index'))


@app.route('/')
def index():
    return render_template(
        'index.html',
        data=Todo.query.all()
    )
