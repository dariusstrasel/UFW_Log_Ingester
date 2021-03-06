from flask import Flask, redirect, url_for, jsonify
from controllers import api_controller
from config import DATABASE_NAME
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./%s.db' % DATABASE_NAME
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def index():
    """Redirect the user to the api endpoint."""
    return redirect(url_for('log_events'))


@app.route('/api/v1/log_events')
def log_events():
    """Query all the log_events in the database and if None returned, insert a log_file."""
    print("Getting log events from database...")
    response_message = api_controller.get_all_log_events()
    return jsonify(response_message)


if __name__ == "__main__":
    app.debug = True
    app.run()
