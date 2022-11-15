from flask import Flask, redirect, request, url_for, render_template
from model_pylist import model
import sqlite3 as sql

app = Flask(__name__)
model = model('entries.db')


def initiate_database():
    comments = '0'  # it isn't working otherwise
    try:
        sqlite_create_table_query = '''create table if not exists messages(
                                        name text,
                                        email text,
                                        date datetime,
                                        entry text);'''
        comments = sql.connect('entries.db')
        cursor = comments.cursor()
        cursor.execute(sqlite_create_table_query)
        comments.commit()
        cursor.close()
    except sql.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (comments):
            comments.close()
            print("Соединение с SQLite закрыто")


@app.route("/")
def mainPage():
    return render_template('bio.html')


@app.route('/guestbook')
def index():
    entries = [dict(name=row[0], email=row[1], signed_on=row[2], message=row[3]) for row in model.select()]
    return render_template('index.html', entries=entries)


@app.route('/sign', methods=['POST'])
def sign():
    """
    Accepts POST requests, and processes the form;
    Redirect to index when completed.
    """
    model.insert(request.form['name'], request.form['email'], request.form['message'])
    return redirect(url_for('index'))


if __name__ == '__main__':
    initiate_database()

    app.run(host='0.0.0.0', debug=True)
