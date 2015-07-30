# Copyright (c) 2015 K. Gabriel Rosati
#
# This software is released under the LGPL V3 or later.
# Please see the files COPYING and COPYING.LESSER in the
# source distribution of this software for license terms.
#

import sqlite3

from insert_sample_qrs import insert_sample_qrs



conn = sqlite3.connect('disco.db')
c = conn.cursor()

#drop current
c.execute("DROP TABLE IF EXISTS questions")

#create the table
c.execute('''CREATE TABLE questions(
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

#insert the example            
insert_sample_qrs(c)

conn.commit()

conn.close()
