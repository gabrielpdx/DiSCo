# Copyright (c) 2015 K. Gabriel Rosati
#
# This software is released under the LGPL V3 or later.
# Please see the files COPYING and COPYING.LESSER in the
# source distribution of this software for license terms.
#

import sqlite3
from Question import Question

from insertSampleQs import insertSampleQs

TABLE_HEADINGS = ("Primary subject: ", "Secondary subject: ",
                  "Family: ", "Difficulty: ", "Question: ",
                  "Correct index: ", "Response 1: ", "Response 2: ",
                  "Response 3: ", "Response 4: ")


class DBWriter():
    """Writes user input to the database"""
    def __init__(self, conn):
        self.cursor = conn.cursor()
        self.questions = []

    def getQuestion(self):
        row = []
        for heading in TABLE_HEADINGS:
            row.append(input(heading))
        self.questions.append(Question(row))

    def writeToDB(self):
        for question in self.questions:
            self.cursor.execute
            ("INSERT INTO questions VALUES({})").format(question.asRow)
            print("INSERT INTO questions VALUES({})".format(question.asRow))


    def getUserInput(self):
        session = 'Y'
        while (session == 'Y'):
            self.getQuestion()
            session = input("Insert another question? (y/n) > ")
            session = session[0].upper()
        self.writeToDB()