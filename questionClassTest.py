# Copyright (c) 2015 K. Gabriel Rosati
#
# This software is released under the LGPL V3 or later.
# Please see the files COPYING and COPYING.LESSER in the
# source distribution of this software for license terms.
#

from question_class import Question

import unittest
referenceQuestion = r'''\begin{ex}
Let $A=false$ and $B=true$. \\
Let $X=A~and~(not~B)$ and $Y=not(A\ or\ (not~B))$.
\choice[2]
  {$X=false$ and $Y=false$}
  {$X=false$ and $Y=true$}  % <---
  {$X=true$ and $Y=false$}
  {$X=true$ and $Y=true$}
\end{ex}
'''

questionInstance = Question()
questionInstance.difficulty = 2
questionInstance.question = r'''Let $A=false$ and $B=true$. \\
Let $X=A~and~(not~B)$ and $Y=not(A\ or\ (not~B))$.'''
questionInstance.responses = [
    "{$X=false$ and $Y=false$}",
    "{$X=false$ and $Y=true$}",
    "{$X=true$ and $Y=false$}",
    "{$X=true$ and $Y=true$}"
    ]

questionInstanceLatex = r""
for line in questionInstance.latexLines():
    questionInstanceLatex += str(line)

class TestQuestionClassLatex(unittest.TestCase):

    def test_equality (self):
        self.assertEqual(referenceQuestion, questionInstanceLatex)

if __name__ == "__main__":
    unittest.main()
