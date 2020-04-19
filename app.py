from flask import Flask, render_template, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://tyler.lanigan@localhost:5432/todoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Needed to run flask db init


class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'


# db.create_all(), not needed if using migrations

# Add some error handling.
@app.route('/todos/create', methods=['POST'])
def create_todo():
    error = False
    body = {}
    try:
        description = request.json['description']
        todo = Todo(description=description)
        db.session.add(todo)
        db.session.commit()
        # Instead of putting this in jsonify like it was before,
        # we make a body here before we close in finally. This way
        # we don't access the todo object after the session is closed
        # and cuase an error.
        body['description'] = todo.description
    except:
        error = True
        db.session.rollback()
        app.logger.info(sys.exc_info())
    finally:
        db.session.close()
    if error:
        # Always return an intentional error
        abort(400)
    if not error:
        return jsonify(body)


@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.all())
