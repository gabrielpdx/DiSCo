# Copyright (c) 2015 K. Gabriel Rosati
#
# This software is released under the LGPL V3 or later.
# Please see the files COPYING and COPYING.LESSER in the
# source distribution of this software for license terms.
#

#from question_class import Question



#insert examples
def insertSampleQs (conn):
    cursor = conn.cursor()
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
    cursor.execute(r'''INSERT INTO questions VALUES(
                "example",
                "sub-example",
                "exfam",
                5,
                "Let $X$ be the statement: \emph{if\ A\ then\ B}. \\
Let $Y$ be the statement: \emph{if\ B\ then\ A}.",
                0,
                "$X$ is the converse of $Y$",
                "$X$ is the consequent of $Y$",
                "$X$ is the antecendent of $Y$",
                "$X$ is the contrapositive of $Y$")
                ''')
    cursor.execute(r'''INSERT INTO questions VALUES(
                "example",
                "sub-example",
                "exfam",
                5,
                "Let $f : \naturals \to \naturals $ be the function that computes
the number of digits of the usual decimal representation of a
natural number.",
                3,
                "$f$ is injective",
                "$f$ is surjective",
                "$f$ is bijective",
                "none of the above")
                ''')
    cursor.execute(r'''INSERT INTO questions VALUES(
                "example",
                "sub-example",
                "exfam",
                5,
                "A function is injective if and only if:",
                2,
                "Each element of the domain is mapped to each element of the codomain",
                "Equal elements of the domain are mapped to equal elements of the codomain",
                "Different elements of the domain are mapped to different elements of the codomain",
                "The size of the codomain is not smaller than the size of the range")
                ''')
    cursor.execute(r'''INSERT INTO questions VALUES(
                "example",
                "sub-example",
                "exfam",
                5,
                "Let $R$ be the relation on $\naturals \times \naturals$ defined by
$x\,R\,y$ iff $x < 3\,y$.",
                0,
                "$10\,R\,4$ and $4\,R\,10$",
                "$10\,R\,4$ and not $4\,R\,10$",
                "not $10\,R\,4$ and $4\,R\,10$",
                "not $10\,R\,4$ and not $4\,R\,10$")
                ''')
    conn.commit()