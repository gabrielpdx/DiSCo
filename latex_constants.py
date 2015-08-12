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
"""

file_end = r"""
\end{enumerate}

\end{document}
"""
