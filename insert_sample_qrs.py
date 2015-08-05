# Copyright (c) 2015 K. Gabriel Rosati
#
# This software is released under the LGPL V3 or later.
# Please see the files COPYING and COPYING.LESSER in the
# source distribution of this software for license terms.
#

from question_class import Question



#insert examples  
def insert_sample_qrs (cursor, question):        
    cursor.execute('''INSERT INTO questions VALUES(
                "example",
                "sub-example",
                "exfam",
                5,
                "Let $n$ be any integer, $X$ the statement ``$n+3>0$'' and $Y$ the statement ``$n>0$''.",
                1,
                "{\emph{if $X$ then $Y$}}",
                "{\emph{if $Y$ then $X$}}",
                "{\emph{$X$ if and only if $Y$}}",
                "{\emph{$Y$ if and only if $X$}}")
                ''')
