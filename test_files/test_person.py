import unittest
from test_files.person import Person


class TestStringMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.person = Person()
    
    def tearDown(self):
        del self.person


if __name__ == '__main__':
    unittest.main()