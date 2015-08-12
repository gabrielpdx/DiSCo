# Copyright (c) 2015 K. Gabriel Rosati
#
# This software is released under the LGPL V3 or later.
# Please see the files COPYING and COPYING.LESSER in the
# source distribution of this software for license terms.
#

import sqlite3

from insertSampleQs import insertSampleQs


conn = sqlite3.connect('disco.db')
c = conn.cursor()

#insert
cursor.execute(r'''INSERT INTO questions VALUES(
                "example",
                "sub-example",
                "exfam",
                5,
                "Let $A=false$ and $B=true$. \\
Let $X=A~and~(not~B)$ and $Y=not(A\ or\ (not~B))$.",
                1,
                "$X=false$ and $Y=false$",
                "$X=false$ and $Y=true$",
                "$X=true$ and $Y=false$",
                "$X=true$ and $Y=true$")
                ''')



insertSampleQs(c)

conn.commit()

conn.close()