import unittest
import sys
sys.path.insert(1, "../")
from Commands.scripWINONLY import Find_Names

class TestUserAndGroupCommands(unittest.TestCase):

    def test_test(self):
        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()
