# Copyright (c) 2015 K. Gabriel Rosati
#
# This software is released under the LGPL V3 or later.
# Please see the files COPYING and COPYING.LESSER in the
# source distribution of this software for license terms.
#

import sqlite3

from question_class import *


TABLE_HEADINGS = ("primary subject: ", "secondary subject: ",
        "family: ", "difficulty: ", "question: ",
        "correct index: ", "response 1: ", "response 2: ",
        "response 3: ", "response 4: ")


conn = sqlite3.connect('disco.db')
c = conn.cursor()

#print the contents of a row
def row_pretty_print (row_to_print) :
    for i in range(10):
        print(TABLE_HEADINGS[i] + str(row[i]))

def row_to_string (row) :
    output = []
    for i in range(9):
        output.append(str(row[i]))
    return output


c.execute("SELECT * FROM questions")

rows = c.fetchall()

for row in rows:
    row_pretty_print(row)

testQ = Question(rows[0])
print(testQ.stringRepresentation())

conn.close()
