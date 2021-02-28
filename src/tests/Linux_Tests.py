import unittest
import sys
sys.path.insert(1, '../')
sys.path.insert(1, './src')
from Commands.scripLINUXONLY import Linux_Find_Groups, alyn


class TestUserAndGroupCommands(unittest.TestCase):
    """
    Linux Command Tests for User and Group Commands
    """

    def test_test(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_audit_w_Lynis(self):
        result = alyn()
        self.assertEqual(result, 0)

    def test_Linux_Find_Groups(self):
        result = Linux_Find_Groups(False)
        self.assertEqual(result, Linux_Find_Groups(False))


if __name__ == '__main__':
    unittest.main()
