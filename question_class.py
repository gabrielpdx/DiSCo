# Copyright (c) 2015 K. Gabriel Rosati
#
# This software is released under the LGPL V3 or later.
# Please see the files COPYING and COPYING.LESSER in the
# source distribution of this software for license terms.
#

class MetaFoo(type):
    def __iter__(self):
        for attr in dir(Foo):
            if not attr.startswith("__"):
                yield attr

class Foo(metaclass=MetaFoo):
    bar = "bar"
    baz = 1

class MetaQuestion(type):
    def __iter__(self):
        for attribute in dir(Question):
            if not attr.startswith("__"):
                yield attribute


class Question(metaclass=MetaQuestion):
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

"""
    def stringRepresentation (self):
        listOut = [
            self.primarySubject,
            self.secondarySubject,
            self.family,
            str(self.difficulty),
            self.question,
            str(self.correctResponseIndex),
            str("\n".join(self.responses))
        ]
        return ("\n" .join(listOut))
        """
def printQuestion(question):
    output = ""
    for attribute in question:
        output += attribute
    return output
    
lotus = Question()
printQuestion(lotus)
