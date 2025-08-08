from src.api import APIClient, DataProcessor
from src.utils import calculate_average, find_max, find_min

def main():
    print('Hello from outdated test repo 1 - UPDATED VERSION')
    print('This is a new feature added to simulate outdated state')
    
    # Test new API functionality
    api_client = APIClient("https://api.example.com")
    data_processor = DataProcessor()
    
    # Test utility functions
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Average: {calculate_average(numbers)}")
    print(f"Max: {find_max(numbers)}")
    print(f"Min: {find_min(numbers)}")
    
    return True

def get_version():
    return '3.0.0'  # Updated version

def new_function():
    print('This is a new function added to trigger outdated detection')
    return 'new_feature'

def process_data(data):
    # New function to process data
    return [item * 2 for item in data]

def api_integration_test():
    # Test API integration
    client = APIClient("https://test.api.com")
    result = client.get_data("/test")
    return result

if __name__ == '__main__':
    main()
    new_function()
    api_integration_test()
