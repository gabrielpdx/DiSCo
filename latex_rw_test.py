# Copyright (c) 2015 K. Gabriel Rosati
#
# This software is released under the LGPL V3 or later.
# Please see the files COPYING and COPYING.LESSER in the
# source distribution of this software for license terms.
#


import unittest
reference_filename = "dbsample.tex"
output_filename = "dup.tex"

with open (reference_filename, 'r') as reference_file:
    reference_string = reference_file.read()

with open (output_filename, 'r') as output_file:
    output_string = output_file.read()

class TestLatexString(unittest.TestCase):

    def test_equality (self):
        self.assertEqual(reference_string, output_string)

if __name__ == "__main__":
    unittest.main()
