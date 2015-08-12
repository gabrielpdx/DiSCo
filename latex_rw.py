# Copyright (c) 2015 K. Gabriel Rosati
#
# This software is released under the LGPL V3 or later.
# Please see the files COPYING and COPYING.LESSER in the
# source distribution of this software for license terms.
#


import sqlite3
from latex_constants import file_start, file_end


fileName = "dup.tex"


def fileW(quizList):
    file = ""
    while not file:
        file = open(fileName,"w")
    quizList.insert(0,file_start)
    quizList.append(file_end)
    file.writelines(quizList)
    file.close()
    
'''
conn = sqlite3.connect('disco.db')
c = conn.cursor()

c.execute("SELECT * FROM questions")
quiz = c.fetchall()

conn.close()

quiz_to_print = []

for row in quiz:
    row_pretty_print(row)
    quiz_to_print.append(row_to_string(row))
'''
quiz_to_print = []

fileW(quiz_to_print)
