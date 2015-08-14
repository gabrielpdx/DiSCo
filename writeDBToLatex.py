# Copyright (c) 2015 K. Gabriel Rosati
#
# This software is released under the LGPL V3 or later.
# Please see the files COPYING and COPYING.LESSER in the
# source distribution of this software for license terms.
#


import sqlite3
from latexConstants import FILE_START, FILE_END
from Question import Question


fileName = "generatedQuiz.tex"


def fileW(quizList):
    file = ""
    while not file:
        file = open(fileName,"w")
    quizList.insert(0,FILE_START)
    quizList.append(FILE_END)
    file.writelines(quizList)
    file.close()

'''
conn = sqlite3.connect('disco.db')
c = conn.cursor()
'''

def writeDBToLatex(conn):
    #db = get_db()
    cur = conn.execute('select * from questions')
    quiz = cur.fetchall()

    # cursor = conn.cursor()
    # cursor.execute("SELECT * FROM questions")
    # quiz = cursor.fetchall()

    #conn.close()

    quiz_to_print = []
    print("writeDB2Latex Iterating through rows")
    for row in quiz:
        print(row)
        quiz_to_print.append('\n')
        questionLatex = Question(row).latexLines()
        for line in questionLatex:
            quiz_to_print.append(line + '\n')

    #import pdb; pdb.set_trace()
    print(quiz)
    print(quiz_to_print)

    fileW(quiz_to_print)
