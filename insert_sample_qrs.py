# Copyright (c) 2015 K. Gabriel Rosati
#
# This software is released under the LGPL V3 or later.
# Please see the files COPYING and COPYING.LESSER in the
# source distribution of this software for license terms.
#


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
                "Let $A=false$ and $B=true$. \\
Let $X=A~and~(not~B)$ and $Y=not(A\ or\ (not~B))$.",
                1,
                "{$X=false$ and $Y=false$}",
                "{$X=false$ and $Y=true$}",
                "{$X=true$ and $Y=false$}",
                "{$X=true$ and $Y=true$}")
                ''')
    cursor.execute('''INSERT INTO questions VALUES(
                "example",
                "sub-example",
                "exfam",
                5,
                "Let $X$ be the statement: \emph{if\ A\ then\ B}. \\
Let $Y$ be the statement: \emph{if\ B\ then\ A}.",
                0,
                "{$X$ is the converse of $Y$}",
                "{$X$ is the consequent of $Y$}",
                "{$X$ is the antecendent of $Y$}",
                "{$X$ is the contrapositive of $Y$}")
                ''')
    cursor.execute('''INSERT INTO questions VALUES(
                "example",
                "sub-example",
                "exfam",
                5,
                "Let $f : \naturals \to \naturals $ be the function that computes 
the number of digits of the usual decimal representation of a
natural number.",
                3,
                "{$f$ is injective}",
                "{$f$ is surjective}",
                "{$f$ is bijective}",
                "{none of the above}")
                ''')
    cursor.execute('''INSERT INTO questions VALUES(
                "example",
                "sub-example",
                "exfam",
                5,
                "A function is injective if and only if:",
                2,
                "{Each element of the domain is mapped to each element of the codomain}",
                "{Equal elements of the domain are mapped to equal elements of the codomain}",
                "{Different elements of the domain are mapped to different elements of the codomain}",
                "{The size of the codomain is not smaller than the size of the range}")
                ''')
    cursor.execute('''INSERT INTO questions VALUES(
                "example",
                "sub-example",
                "exfam",
                5,
                "Let $R$ be the relation on $\naturals \times \naturals$ defined by
$x\,R\,y$ iff $x < 3\,y$.",
                0,
                "{$10\,R\,4$ and $4\,R\,10$}}",
                "{$10\,R\,4$ and not $4\,R\,10$}",
                "{not $10\,R\,4$ and $4\,R\,10$}",
                "{not $10\,R\,4$ and not $4\,R\,10$}}")
                ''')
"""

\begin{ex}
Let $A=\{2,3,5,7\}$ and $B=\{1,2,6,8\}$.
Let $X=(A \cap B) \oplus B$.
\choice[4]
    {$X=\varnothing$}
    {$X=\{2\}$}
    {$X=\{6,8\}$}
    {$X=\{1,6,8\}$}  % <---
\end{ex}

\begin{ex}
Let $X$ and $Y$ be sets such that $X \oplus Y = \varnothing$.
Choose the most accurate.
\choice[1]
    {$X = Y$}   % <---
    {$X \subseteq Y$}
    {$X \subsetneq Y$}
    {None of the above}
\end{ex}

\begin{ex}
Let $B$ and $P$ be the multisets (bags) made with the
letters of the words ``banana'' and ``panama'', respectively.
The number of elements of $B \cup P$ is:
\choice[3] {0} {4} {8} {12}
\end{ex}

\begin{ex}
The closed form of $\displaystyle \sum_{i=2}^n (2i)$ is:
\choice[1] 
    {$n^2+n-2$}  % <---
    {$n^2-n+2$}
    {$n(n+1)$}
    {$n^2+2n+1$}
\end{ex}

\begin{ex}
Consider the grammar $G$ defined (with usual conventions) by:\\[.5ex]
\phantom{XXX} $S \to Sa \mid bS \mid c$ \\[.5ex]
Which of the following strings belongs to the language of $G$:
\choice[3]
    {$abc$}
    {$cba$}
    {$bca$}   % <---
    {$cab$}
\end{ex}

\begin{ex}
Let $f : \naturals \to \naturals$ be recursively defined by 
$f(0)=2$ and for $n>0$, $f(n)=f(n-1)$ if $n$ is odd and
$f(n)=2\,f(n-1)+1$  if $n$ is even.
The value of $f(4)$ is:
\choice[3]
    {2}
    {5}
    {11}   % <---
    {23}
\end{ex}
"""
