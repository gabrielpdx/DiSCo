"""import sqlite3

conn = sqlite3.connect('disco.db')

c = conn.cursor()
"""

#insert examples  
def insert_sample_qrs (cursor):        
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
