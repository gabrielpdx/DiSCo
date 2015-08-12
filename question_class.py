# Copyright (c) 2015 K. Gabriel Rosati
#
# This software is released under the LGPL V3 or later.
# Please see the files COPYING and COPYING.LESSER in the
# source distribution of this software for license terms.
#

class Question():
    """A question, its responses, and metadata"""
    def __init__(self, rowList = None):
        if (rowList is None):
            self.primarySubject = ""
            self.secondarySubject = ""
            self.family = ""
            self.difficulty = -1
            self.question = ""
            self.correctResponseIndex = -1
            self.responses = []
        else:
            self.primarySubject = rowList[0]
            self.secondarySubject = rowList[1]
            self.family = rowList[2]
            self.difficulty = rowList[3]
            self.question = rowList[4]
            self.correctResponseIndex = rowList[5]
            self.responses = rowList[6:]
        self.asRow = rowList

    def latexLines (self):
        begin = r"\begin{ex}"
        choice = r"\choice[{}]".format(int(self.difficulty))
        end = r"\end{ex}"
        output = [
            begin,
            self.question,
            choice,
        ]
        for response in self.responses:
            output.append("  " + response)
        output.append(end)
        return output

    def printQuestion (self):
        output = []
        if (self.asRow):
            for attribute in self.asRow:
                output.append(str(attribute))
        return output
