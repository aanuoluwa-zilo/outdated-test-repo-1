import unittest
from src.main import main, get_version

class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertTrue(main())
    
    def test_get_version(self):
        self.assertEqual(get_version(), '1.0.0')

if __name__ == '__main__':
    unittest.main()