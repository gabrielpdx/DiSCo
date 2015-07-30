# Copyright (c) 2015 K. Gabriel Rosati
#
# This software is released under the LGPL V3 or later.
# Please see the files COPYING and COPYING.LESSER in the
# source distribution of this software for license terms.
#


r'''file_start = \documentclass[11pt,fleqn]{article}

% \usepackage{times}
\usepackage[normalem]{ulem}
\usepackage[all]{xy}
\usepackage{pstricks}
\usepackage{ifthen}
\usepackage{lastpage}

\usepackage{fancyhdr}
\renewcommand{\headrulewidth}{0pt}
\fancyfoot[R]{\small Db devel.~sample, page \thepage/\pageref{LastPage}}
\fancyfoot[C]{}
\fancyhead{}

\parindent=0pt
\parskip=1ex

\oddsidemargin=0in
\evensidemargin=0in
\textwidth=6.5in
\topmargin=-.5in
\textheight=9in

\newcounter{nextcounter}
\newenvironment{ex}{%
\begin{minipage}{.9\textwidth}%
\addtocounter{nextcounter}{1}%
\hspace*{-.8ex}\leavevmode\llap{\arabic{nextcounter}.\hspace*{.90em}}%
}{\end{minipage}}

\newcommand{\markx}[2]{%
%%% COMMENT NEXT
% \ifthenelse{#1=#2}{\rlap{\colorbox{gray}{\phantom{\vrule height1.2ex .....}}}}{}%
}
\newcommand{\choice}[5][0]{%
  \removelastskip
  \vspace*{-1.5ex}%
  \begin{tabbing}
    \quad\markx{#1}{1}[-A-]~~ \= #2 \\
    \quad\markx{#1}{2}[-B\kern.04em-] \> #3 \\
    \quad\markx{#1}{3}[-C\kern.04em-] \> #4 \\
    \quad\markx{#1}{4}[-D-] \> #5
  \end{tabbing}
  \vspace*{-1.5ex}%
}

\renewcommand{\arraystretch}{1.5}
\usepackage{amssymb}

\newcommand{\naturals}{{\mathbb N}}
\newcommand{\integers}{{\mathbb Z}}
\newcommand{\evens}{{\mathbb E}}

\newcommand{\myl}[1]{\langle #1 \rangle}
\newcommand{\branch}[3]{\myl{#1,#2,#3}}
\newcommand{\leaf}[0]{\myl{}}
\newcommand{\rel}[0]{\,{\cal R}\,}

\begin{document}
% \thispagestyle{empty}
\pagestyle{fancy}

\vspace*{-1in}
\begin{flushright}
Name: \uline{\mbox{\hspace*{2in}}} \\[2ex]
Date: \uline{\mbox{\hspace*{2in}}} \\[2ex]
Grade: \uline{\mbox{\hspace*{2in}}}
\end{flushright}

\vspace*{2ex}

If a question is wrong, or has no acceptable answer,
choose [-E-].
\\
If a question has several correct answers, choose the most
accurate.
\\
You will get one point for each correct answer.

\begin{enumerate}
\item[]\par'''

file_start = r"""\documentclass[11pt,fleqn]{article}

% \usepackage{times}
\usepackage[normalem]{ulem}
\usepackage[all]{xy}
\usepackage{pstricks}
\usepackage{ifthen}
\usepackage{lastpage}

\usepackage{fancyhdr}
\renewcommand{\headrulewidth}{0pt}
\fancyfoot[R]{\small Db devel.~sample, page \thepage/\pageref{LastPage}}
\fancyfoot[C]{}
\fancyhead{}

\parindent=0pt
\parskip=1ex

\oddsidemargin=0in
\evensidemargin=0in
\textwidth=6.5in
\topmargin=-.5in
\textheight=9in

\newcounter{nextcounter}
\newenvironment{ex}{%
\begin{minipage}{.9\textwidth}%
\addtocounter{nextcounter}{1}%
\hspace*{-.8ex}\leavevmode\llap{\arabic{nextcounter}.\hspace*{.90em}}%
}{\end{minipage}}

\newcommand{\markx}[2]{%
%%% COMMENT NEXT
% \ifthenelse{#1=#2}{\rlap{\colorbox{gray}{\phantom{\vrule height1.2ex .....}}}}{}%
}
\newcommand{\choice}[5][0]{%
  \removelastskip
  \vspace*{-1.5ex}%
  \begin{tabbing}
    \quad\markx{#1}{1}[-A-]~~ \= #2 \\
    \quad\markx{#1}{2}[-B\kern.04em-] \> #3 \\
    \quad\markx{#1}{3}[-C\kern.04em-] \> #4 \\
    \quad\markx{#1}{4}[-D-] \> #5
  \end{tabbing}
  \vspace*{-1.5ex}%
}

\renewcommand{\arraystretch}{1.5}
\usepackage{amssymb}

\newcommand{\naturals}{{\mathbb N}}
\newcommand{\integers}{{\mathbb Z}}
\newcommand{\evens}{{\mathbb E}}

\newcommand{\myl}[1]{\langle #1 \rangle}
\newcommand{\branch}[3]{\myl{#1,#2,#3}}
\newcommand{\leaf}[0]{\myl{}}
\newcommand{\rel}[0]{\,{\cal R}\,}

\begin{document}
% \thispagestyle{empty}
\pagestyle{fancy}

\vspace*{-1in}
\begin{flushright}
Name: \uline{\mbox{\hspace*{2in}}} \\[2ex]
Date: \uline{\mbox{\hspace*{2in}}} \\[2ex]
Grade: \uline{\mbox{\hspace*{2in}}}
\end{flushright}

\vspace*{2ex}

If a question is wrong, or has no acceptable answer,
choose [-E-].
\\
If a question has several correct answers, choose the most
accurate.
\\
You will get one point for each correct answer.

\begin{enumerate}
\item[]\par

\begin{ex}
Let $A=false$ and $B=true$. \\
Let $X=A~and~(not~B)$ and $Y=not(A\ or\ (not~B))$.
\choice[2]
  {$X=false$ and $Y=false$}
  {$X=false$ and $Y=true$}  % <---
  {$X=true$ and $Y=false$}
  {$X=true$ and $Y=true$}
\end{ex}

\begin{ex}
Let $X$ be the statement: \emph{if\ A\ then\ B}. \\
Let $Y$ be the statement: \emph{if\ B\ then\ A}.

\choice[3]
    {$X$ is the converse of $Y$}   % <---
    {$X$ is the consequent of $Y$}
    {$X$ is the antecendent of $Y$}
    {$X$ is the contrapositive of $Y$}
\end{ex}

\begin{ex}
Let $f : \naturals \to \naturals $ be the function that computes 
the number of digits of the usual decimal representation of a
natural number.
\choice[4]
    {$f$ is injective}
    {$f$ is surjective}
    {$f$ is bijective}
    {none of the above}  % <---
\end{ex}

\begin{ex}
A function is injective if and only if:
\choice[3]
   {Each element of the domain is mapped to each element of the codomain}
   {Equal elements of the domain are mapped to equal elements of the codomain}
   {Different elements of the domain are mapped to different elements of the codomain}  % <---
   {The size of the codomain is not smaller than the size of the range}
\end{ex}

\begin{ex}
Let $R$ be the relation on $\naturals \times \naturals$ defined by
$x\,R\,y$ iff $x < 3\,y$.
\choice[1]
    {$10\,R\,4$ and $4\,R\,10$}   % <---
    {$10\,R\,4$ and not $4\,R\,10$}
    {not $10\,R\,4$ and $4\,R\,10$}
    {not $10\,R\,4$ and not $4\,R\,10$}
\end{ex}

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

file_end = r"""
\end{enumerate}

\end{document}
"""
