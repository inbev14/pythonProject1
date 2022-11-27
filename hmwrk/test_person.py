import unittest


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
    
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('foo'.isupper())
    
    def test_split(self):
        welcome = 'Hello, World!'
        self.assertEqual(welcome.split(' '), ['Hello,', 'World!'])
        
        with self.assertRaises(TypeError):
            welcome.split(0)


if __name__ == '__main__':
    unittest.main()