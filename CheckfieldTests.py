import unittest
from main import CheckField
import json

with open('CheckFieldExamples.json', 'r') as filehandle:
    test_examples = json.load(filehandle)


class Test_check_field(unittest.TestCase):
    def test1(self):
        self.assertTrue(CheckField(test_examples['example1']).check)

    def test2(self):
        self.assertFalse(CheckField(test_examples['example2']).check)

    def test3(self):
        self.assertTrue(CheckField(test_examples['example3']).check)

    def test4(self):
        self.assertFalse(CheckField(test_examples['example4']).check_square())

    def test5(self):
        self.assertTrue(CheckField(test_examples['example5']).check_square())

    def test6(self):
        self.assertFalse(CheckField(test_examples['example5']).check_line())

    def test7(self):
        self.assertFalse(CheckField(test_examples['example6']).check)


if __name__ == "__main__":
    unittest.main()
