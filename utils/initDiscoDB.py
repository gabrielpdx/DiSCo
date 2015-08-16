# Copyright (c) 2015 K. Gabriel Rosati
#
# This software is released under the LGPL V3 or later.
# Please see the files COPYING and COPYING.LESSER in the
# source distribution of this software for license terms.
#

import sqlite3

def initDiscoDB (conn):
    cursor = conn.cursor()

    #drop current
    cursor.execute("DROP TABLE IF EXISTS questions")

    #create the table
    cursor.execute('''CREATE TABLE questions(
                primary_subject text,
                secondary_subject text,
                family text,
                difficulty real,
                question text,
                correct_index real,
                response1 text,
                response2 text,
                response3 text,
                response4 text)''')

    conn.commit()

    #conn.close()
