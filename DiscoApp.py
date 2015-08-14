import os
import json
import sqlite3
from flask import (Flask, session, abort, render_template, redirect,
                    url_for, request, make_response, g, flash)

from initDiscoDB import initDiscoDB
from Question import Question
from DBWriter import DBWriter
from latexConstants import FILE_START, FILE_END
from writeDBToLatex import writeDBToLatex


app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'disco.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

DATABASE = 'disco.db'

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

# @app.cli.command('initdb')
# def initdb_command():
#     """Initializes the database."""
#     init_db()
#     print ('Initialized the database.')

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

FILENAME = "generatedQuiz.tex"

def fileW(quizList):
    file = ""
    while not file:
        file = open(FILENAME,"w")
    quizList.insert(0,FILE_START)
    quizList.append(FILE_END)
    file.writelines(quizList)
    file.close()

# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = connect_to_database()
#     return db
#
# @app.teardown_appcontext
# def close_connection(exception):
#     db = getattr(g, '_database', None)
#     if db is not None:
#         db.close()

def writeQuestionToDB(conn, question):
    writer = DBWriter(conn)
    writer.addQuestion(question)
    writer.writeToDB()



# def get_saved_data():
#     try:
#         data = json.loads(request.cookies.get('question')) #loads loads a string
#     except TypeError:
#         data = {}
#     return data

@app.route("/init/", methods=["GET"])
def oneTimeInit():
    init_db()
    response = make_response(redirect(url_for('index')))
    return response


@app.route("/", methods=["GET"])
def index():
    # init_db()
    #initDiscoDB(conn)
    #data = get_saved_data()
    return render_template("mockup.html")#, saves=data)

@app.route("/", methods=["POST"])
def save():
    response = make_response(redirect(url_for('index')))
    question = Question()
    question.setQuestion(dict(request.form.items()))
    db = get_db()
    db.execute('insert into questions (\
        primarySubject, secondarySubject, family,\
        difficulty, question, correctIndex,\
        response1, response2, response3, response4) values\
        (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', question.asRow)
    db.commit()
    flash('New question written successfully')

    # data = get_saved_data()
    # data.update(dict(request.form.items()))
    #import pdb; pdb.set_trace()
    #writeQuestionToDB(conn, question)
    #import pdb; pdb.set_trace()

    ## the name of the cookie, and the dict
    #response.set_cookie('question', json.dumps(data)) #dumps creates a string!
    return response

@app.route("/latex/")
def writeLatex():
    db = get_db()
    cur = db.execute('select * from questions')
    quiz = cur.fetchall()

    quiz_to_print = []
    for row in quiz:
        quiz_to_print.append('\n')
        questionLatex = Question(row).latexLines()
        for line in questionLatex:
            quiz_to_print.append(line + '\n')

    fileW(quiz_to_print)
    return 'Successfullly wrote "generatedQuiz.tex"'


if __name__ == "__main__":
    app.run(debug=True)
