import unittest
import json
from SolveField import SolveField

with open('SolveFieldTests.json', 'r') as filehandle:
    tests = json.load(filehandle)

with open('SolveFieldAnswers.json', 'r') as filehandle:
    answers = json.load(filehandle)


class SolveFieldTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(SolveField(tests['example1']).field, answers['example1'])

    def test2(self):
        self.assertEqual(SolveField(tests['example2']).field, answers['example2'])


if __name__ == "__main__":
    unittest.main()
