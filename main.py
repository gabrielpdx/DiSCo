# Copyright (c) 2015 K. Gabriel Rosati
#
# This software is released under the LGPL V3 or later.
# Please see the files COPYING and COPYING.LESSER in the
# source distribution of this software for license terms.
#


import sqlite3
from initDiscoDB import initDiscoDB
from insertSampleQs import insertSampleQs
#from DBWriter import DBWriter
from writeDBToLatex import writeDBToLatex

def main():
    conn = sqlite3.connect('disco.db')

    initDiscoDB(conn)
    insertSampleQs(conn)
    #UI = DBWriter(conn)
    #UI.getUserInput()
    writeDBToLatex(conn)

    conn.close()

if __name__ == "__main__":
    main()
