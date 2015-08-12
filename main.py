# Copyright (c) 2015 K. Gabriel Rosati
#
# This software is released under the LGPL V3 or later.
# Please see the files COPYING and COPYING.LESSER in the
# source distribution of this software for license terms.
#


import sqlite3
from initDiscoDB import initDiscoDB
from insertSampleQs import insertSampleQs
from writeDBToLatex import writeDBToLatex
from latex_constants import file_start, file_end
from Question import Question

def main():
    conn = sqlite3.connect('disco.db')

    initDiscoDB(conn)
    insertSampleQs(conn)
    writeDBToLatex(conn)

if __name__ == "__main__":
    main()
