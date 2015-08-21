# Copyright (c) 2015 K. Gabriel Rosati
#
# This software is released under the LGPL V3 or later.
# Please see the files COPYING and COPYING.LESSER in the
# source distribution of this software for license terms.
#

import os
import json
import sqlite3
from flask import (Flask, session, abort, render_template, redirect,
                    url_for, request, make_response, g, flash)

from Question import Question
from latexConstants import FILE_START, FILE_END


app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'disco.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))

DATABASE = 'disco.db'


def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.before_first_request
def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


def writeQuestionToDB(conn, question):
    writer = DBWriter(conn)
    writer.addQuestion(question)
    writer.writeToDB()


@app.route("/init/", methods=["GET"])
def oneTimeInit():
    init_db()
    response = make_response(redirect(url_for('index')))
    return response


@app.route("/clear/", methods=["GET"])
def clearDB():
    db = get_db()
    db.execute("DELETE FROM questions;")
    db.commit()
    flash("Database cleared successfully")
    response = make_response(redirect(url_for('index')))
    return response


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def insertQuestion():
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
    flash("New question written successfully")
    return response


@app.route("/latex/", methods=["GET"])
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

    quiz_to_print.insert(0,FILE_START)
    quiz_to_print.append(FILE_END)
    output = ""
    for line in quiz_to_print:
        output += line
    response = make_response(output)
    response.headers["Content-Disposition"] = "attachment; filename=disco.tex"
    return response

@app.route("/rct/", methods=["GET"])
@app.route("/rct/<hello>")
def reactTest(hello="Gabe", iterable=[]):
    iterable = [1,2,3]
    return render_template("reactTest.html", hello=hello, iterable=iterable)




if __name__ == "__main__":
    app.run(debug=True)
