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
    def __init__(self):
        #self.cursor = conn.cursor()
        self.questions = []

    def getQuestion(self):
        row = []
        for heading in TABLE_HEADINGS:
            row.append(input(heading))
        self.questions.append(Question(row))

    def writeToDB(self, conn):
        cursor = conn.cursor()
        for question in self.questions:
            CSVString = ""
            for column in question.asRow:
                CSVString += ('"'+column+'"')
                if (column != question.asRow[-1]):
                    CSVString += ','
            cursor.execute('''INSERT INTO questions VALUES('''
            + CSVString + ''')''')
            print(r'''INSERT INTO questions VALUES({})'''.format(CSVString))
        conn.commit()


    def getUserInput(self, conn):
        session = 'Y'
        while (session == 'Y'):
            self.getQuestion()
            print("Added question. All row content:")
            for question in self.questions:
                print(question.question)
            session = input("Insert another question? (y/n) > ")
            session = session[0].upper()
        self.writeToDB(conn)
