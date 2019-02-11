# Course: TC4002 Analysis, Design and Construction of Software Systems
# Enrollment: A00354776
# Author: Alex Garcia
# Excercise: L3
# File name: comparison_test.py
# Description: filecmp.cmp function using unittest
# Date created: 02/01/2019
# Date last modified: 02/01/2019
# Python Version:  3.7.2

# Begin code
import unittest
import filecmp

#TODO: create functions to manipulate files

def compareFiles():
    if filecmp.cmp('C:\\Users\\jorgagar\\PycharmProjects\\ITESM\\SameFile1.txt',
                   'C:\\Users\\jorgagar\\PycharmProjects\\ITESM\\SameFile2.txt'):
        return "The files are the same"
    else:
        return "The files are not the same"

class TestComparison(unittest.TestCase):

    def test_PositiveComparison(self):
        self.assertEqual(compareFiles(), "The files are the same")

    def test_NegativeComparison(self):
        self.assertNotEqual(compareFiles(), "The files are not the same")

if __name__ == '__main__':
    unittest.main()