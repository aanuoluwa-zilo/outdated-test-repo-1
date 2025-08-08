import unittest
from src.new_module import process_data, validate_input, calculate_average

class TestNewModule(unittest.TestCase):
    def test_process_data(self):
        data = [1, 2, 3, 4, 5]
        result = process_data(data)
        self.assertEqual(result, [2, 4, 6, 8, 10])
    
    def test_validate_input(self):
        self.assertTrue(validate_input(42))
        self.assertTrue(validate_input(3.14))
        self.assertFalse(validate_input("string"))
    
    def test_calculate_average(self):
        self.assertEqual(calculate_average([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(calculate_average([]), 0)

if __name__ == '__main__':
    unittest.main()
